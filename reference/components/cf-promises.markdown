---
layout: default
title: cf-promises
categories: [Reference, Components, cf-promises]
published: true
alias: reference-components-cfpromises.html
tags: [Components, cf-promises]
---

`cf-promises` is a  tool for checking CFEngine policy code. It operates by first parsing policy code checing for syntax errors. Second, it validates the integrity of policy consisting of multiple files. Third, it checks for semantic errors, e.g. specific attribute set rules. Finally, `cf-promises` attempts to expose errors by partially evaluating the policy, resolving as many variable and classes promise statements as possible. At no point does `cf-promises` make any changes to the system.

## Command reference

    --help, -h
        Print the help message

    --bundlesequence, -b
        Use the specified bundlesequence for verification

    --debug, -d
        Enable debugging output

    --verbose, -v
        Output verbose information about the behaviour of the agent

    --dry-run, -n
        All talk and no action mode - make no changes, only inform of promises not kept

    --version, -V
        Output the version of the software

    --file, -f
        Specify an alternative input file than the default

    --define, -D
        Define a list of comma separated classes to be defined at the start of execution

    --negate, -N
        Define a list of comma separated classes to be undefined at the start of execution

    --inform, -I
        Print basic information about changes made to the system, i.e. promises repaired

    --diagnostic, -x
        Activate internal diagnostics (developers only)

    --reports, -r
        Generate reports about configuration and insert into CFDB

    --policy-output-format, -p
        Output the parsed policy. Possible values: 'none', 'cf', 'json'. Default is 'none'. (experimental)

    --syntax-description, -s
        Output a document describing the available syntax elements of CFEngine. Possible values: 'none', 'json'. Default is 'none'.

    --full-check, -c
        Ensure full policy integrity checks

    --warn, -W
        Pass comma-separated <warnings>|all to enable non-default warnings, or error=<warnings>|all

    --legacy-output, -l
        Use legacy output format

    --color, -C
        Enable colorized output. Possible values: 'always', 'auto', 'never'. Default is 'never'
