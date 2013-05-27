---
layout: default
title: cf-monitord
categories: [Reference, Components, cf-monitord]
published: true
alias: reference-components-cfmonitord.html
tags: [Components, cf-monitord]
---

# `cf-monitord`

Passive monitoring agent - responsible for collecting information
about the status of your system (which can be reported upon or used
to enforce promises or influence when promises are enforced). In
CFEngine 2 the passive monitoring agent was known as `cfenvd`.

`cf-monitord` keeps the promises made in
`common`and `monitor` bundles, and is affected by 
`common` and `monitor` control bodies.


## Command reference

        '--help'
           (-h) - Print the help message
        '--debug'
           (-d value) - Set debugging level 0,1,2,3
        '--verbose'
           (-v) - Output verbose information about the behaviour of the agent
        '--dry-run'
           (-n) - All talk and no action mode - make no changes, only
            inform of promises not kept
        '--version'
           (-V) - Output the version of the software
        '--no-lock'
           (-K) - Ignore system lock
        '--file'
           (-f value) - Specify an alternative input file than the default
        '--inform'
           (-I) - Print basic information about changes made to the
            system, i.e. promises repaired
        '--diagnostic'
           (-x) - Activate internal diagnostics (developers only)
        '--no-fork'
           (-F) - Run process in foreground, not as a daemon
        '--histograms'
           (-H) - Store informatino about histograms / distributions
        '--tcpdump'
           (-T) - Interface with tcpdump if available to collect data about network

Debug levels: 1=parsing, 2=running, 3=summary,

