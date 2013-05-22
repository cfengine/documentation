---
layout: default
title: cf-key
categories: [Reference, Components, cf-key]
published: true
alias: reference-components-cfkey.html
tags: [Components, cf-key]
---


# `cf-key`

Key generation tool - run once on every host to create public/private key pairs for secure communication (in CFEngine 2 the key generation tool was called `cfkey`). `cf-key` does not keep any promises. 

## Command reference

        '--help'
           (-h) - Print the help message
        '--debug'
           (-d value) - Set debugging level 0,1,2,3
        '--verbose'
           (-v) - Output verbose information about the behaviour of the agent
        '--version'
           (-V) - Output the version of the software
        '--output-file'
           (-f value) - Specify an alternative output file than the default (localhost.*)
        '--show-hosts'
           (-s) - Show lastseen hostnames and IP addresses
        '--remove-keys'
           (-r value) - Remove keys for specified hostname/IP from lastseen database 
        '--install-license'
           (-l value) - Install license without boostrapping (CFEngine Enterprise only)
