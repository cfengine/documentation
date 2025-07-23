#!/bin/bash

# process revisions

# replace numeric revisions by pull/REVISION/merge
CORE_REV=$(echo ${CORE_REV}|sed -r 's|^([0-9]+)$|pull/\1/merge|')
ENTERPRISE_REV=$(echo ${ENTERPRISE_REV}|sed -r 's|^([0-9]+)$|pull/\1/merge|')
NOVA_REV=$(echo ${NOVA_REV}|sed -r 's|^([0-9]+)$|pull/\1/merge|')
MASTERFILES_REV=$(echo ${MASTERFILES_REV}|sed -r 's|^([0-9]+)$|pull/\1/merge|')
DOCS_REV=$(echo ${DOCS_REV}|sed -r 's|^([0-9]+)$|pull/\1/merge|')
NT_DOCS_REV=$(echo ${NT_DOCS_REV}|sed -r 's|^([0-9]+)$|pull/\1/merge|')
#DOCUMENTATION_REV=$(echo ${DOCUMENTATION_REV}|sed -r 's|^([0-9]+)$|pull/\1/merge|')

# do nothing if empty, remove 'tag:' if found, add 'origin/' otherwise
          CORE_REV=$(echo ${CORE_REV}          |awk 'BEGIN {FS = ":"} /^$/ {next} /^tag:.*/ {print $2} !/^tag:/ {print "origin/"$1}')
    ENTERPRISE_REV=$(echo ${ENTERPRISE_REV}    |awk 'BEGIN {FS = ":"} /^$/ {next} /^tag:.*/ {print $2} !/^tag:/ {print "origin/"$1}')
          NOVA_REV=$(echo ${NOVA_REV}          |awk 'BEGIN {FS = ":"} /^$/ {next} /^tag:.*/ {print $2} !/^tag:/ {print "origin/"$1}')
   MASTERFILES_REV=$(echo ${MASTERFILES_REV}   |awk 'BEGIN {FS = ":"} /^$/ {next} /^tag:.*/ {print $2} !/^tag:/ {print "origin/"$1}')
          DOCS_REV=$(echo ${DOCS_REV}          |awk 'BEGIN {FS = ":"} /^$/ {next} /^tag:.*/ {print $2} !/^tag:/ {print "origin/"$1}')
       NT_DOCS_REV=$(echo ${NT_DOCS_REV}       |awk 'BEGIN {FS = ":"} /^$/ {next} /^tag:.*/ {print $2} !/^tag:/ {print "origin/"$1}')
#DOCUMENTATION_REV=$(echo ${DOCUMENTATION_REV} |awk 'BEGIN {FS = ":"} /^$/ {next} /^tag:.*/ {print $2} !/^tag:/ {print "origin/"$1}')

#echo "CORE_REV: ${CORE_REV:-$BASE_BRANCH}" >> revisions.props
#echo "ENTERPRISE_REV: ${ENTERPRISE_REV:-$BASE_BRANCH}" >> revisions.props
#echo "NOVA_REV: ${NOVA_REV:-$BASE_BRANCH}" >> revisions.props
#echo "MASTERFILES_REV: ${MASTERFILES_REV:-$BASE_BRANCH}" >> revisions.props
#echo "DOCS_REV: ${DOCS_REV}" >> revisions.props
#echo "NT_DOCS_REV: ${NT_DOCS_REV}" >> revisions.props
##echo "DOCUMENTATION_REV: ${DOCUMENTATION_REV}" >> revisions.props


# fetch repos

wget https://gitlab.com/Northern.tech/OpenSource/GODS/-/raw/master/parallel_git_rev_fetch.sh
chmod u+x ./parallel_git_rev_fetch.sh

for repo in core enterprise nova masterfiles documentation; do
  rev_param_name="$(echo $repo | tr '[:lower:]-' '[:upper:]_' | sed 's/DOCUMENTATION/DOCS/;s/GENERATOR/GEN/')_REV"
  revision="${!rev_param_name}"   # dereference

  # remove "origin/" (if any) and add "refs/" if necessary
  revision="${revision##origin/}"
  if expr "$revision" : "pull/" >/dev/null; then
    revision="refs/$revision"
  fi

  echo "$repo git@github.com:cfengine/$repo $revision" >> revisions
done

# fetch nt-docs
nt_docs_revision="${NT_DOCS_REV##origin/}"
echo "nt-docs git@github.com:NorthernTechHQ/nt-docs $nt_docs_revision" >> revisions

./parallel_git_rev_fetch.sh revisions

# figure out PACKAGE_UPLOAD_DIRECTORY based on 

PACKAGE_UPLOAD_DIRECTORY="$(documentation/generator/build/latest_nightly.sh "http://buildcache.cfengine.com/packages/$PACKAGE_JOB/" "jenkins-$USE_NIGHTLIES_FOR-nightly-pipeline")"

# test: see what cloned
ls -la documentation
( cd documentation; git log --oneline | head -n1 )

export BRANCH=$DOCS_BRANCH
bash -x documentation/generator/build/run.sh
