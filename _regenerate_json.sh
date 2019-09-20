#!/bin/bash

# This script is responsible for generating data which is used by the rest of
# the documentation system for providing the correct and up to date syntax
# descriptions, agent help, and policy documentation.

if [ -z "${WRKDIR}" ]
then
    echo Environment WRKDIR is not set, setting it to current working directory
    WRKDIR=`pwd`
    export WRKDIR
fi

# The generated files will be placed in this directory and processed by separate
# tooling.

OUTDIR=${WRKDIR}/documentation-generator/_generated/

# This is the root directory for the policy we want to generate data. Each
# policy file found under this tree will have the policy converted into JSON
# format which can more easily be parsed and used by the rest of the
# documentation system.
POLICYROOT=${WRKDIR}/masterfiles/

# Here we generate the syntax map. This is used to ensure information about
# function prototypes, return types, and default values are up to date.

${WRKDIR}/core/cf-promises/cf-promises --syntax-description json > ${OUTDIR}/syntax_map.json

# We generate a JSON representation of each .cf file that is not in the tests
# directory

for policy in $(find "${POLICYROOT}" -name "*.cf" -not -path "*/tests/*")
do
    # Here we set the output file by replacing the POLICYROOT part of the path
    # to the policy file with OUTDIR. I had issues doing this naively in bash
    # so it was switched to sed.

    out=$(echo "${policy}" | sed "s|${POLICYROOT}|${OUTDIR}|")
    out="${out/%.cf/.json}"
    if [ ! -d "$(dirname ${out})" ]; then
        mkdir -p $(dirname ${out})
    fi

    # We strip error lines because of CFE-2370 and CFE-2696
    ${WRKDIR}/core/cf-promises/cf-promises --eval-functions --policy-output-format=json ${policy} | sed '/   error\:.*/d' >  ${out}
    echo "Writing '${out}'"
done

# We extract the --help output from each component for inclusion in the component specific documentation page under reference/components/
(
    echo cf-agent
    echo cf-promises
    echo cf-runagent
    echo cf-serverd
    echo cf-execd
    echo cf-key
    echo cf-monitord
    echo cf-net
    echo cf-check
    echo cf-hub
) | while read agent
do
    if [ -x "${WRKDIR}/core/${agent}/${agent}" ]; then
        ${WRKDIR}/core/${agent}/${agent} --help > ${OUTDIR}/${agent}.help && echo "Extracted --help output from ${agent}"
    elif [ -x "${WRKDIR}/nova/${agent}/${agent}" ]; then
        ${WRKDIR}/nova/${agent}/${agent} --help > ${OUTDIR}/${agent}.help && echo "Extracted --help output from ${agent}"
    else
        echo "WARNING: No executable agent found at ${WRKDIR}/core/${agent}/${agent}"
        echo "WARNING: No executable agent found at ${WRKDIR}/nova/${agent}/${agent}"
    fi
done
