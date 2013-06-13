---
layout: default
title: cf-key
categories: [Reference, Components, cf-key]
published: true
alias: reference-components-cfkey.html
tags: [Components, cf-key]
---

The CFEngine key generator makes key pairs for [remote 
authentication][Networking].

## Command reference

    --help, -h
        Print the help message

    --debug, -d
        Enable debugging output

    --verbose, -v
        Output verbose information about the behaviour of the agent

    --version, -V
        Output the version of the software

    --output-file, -f
        Specify an alternative output file than the default (localhost)

    --show-hosts, -s
        Show lastseen hostnames and IP addresses

    --remove-keys, -r
        Remove keys for specified hostname/IP

    --install-license, -l
        Install license without boostrapping (CFEngine Enterprise only)

    --print-digest, -p
        Print digest of the specified public key

    --trust-key, -t
        Make cf-serverd/cf-agent trust the specified public key

    --color, -C
        Enable colorized output. Possible values: 'always', 'auto', 'never'. Default is 'never'
