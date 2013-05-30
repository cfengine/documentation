---
layout: default
title: cf-monitord
categories: [Reference, Components, cf-monitord]
published: true
alias: reference-components-cfmonitord.html
tags: [Components, cf-monitord]
---

Passive monitoring agent - responsible for collecting information about the 
status of your system, which can be reported upon or used to enforce promises 
or influence when promises are enforced.

`cf-monitord` keeps the promises made in `common`and `monitor` bundles, and is 
affected by  `common` and `monitor` control bodies.

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
       (-T) - Interface with tcpdump if available to collect data about 
       network

Debug levels: 1=parsing, 2=running, 3=summary,

## Control Promises


Settings describing the details of the fixed behavioral promises
made by `cf-monitord`. The system defaults will be sufficient for
most users. This configurability potential, however, will be a key
to developing the integrated monitoring capabilities of CFEngine.


```cf3         
    body monitor control()
    {
        #version => "1.2.3.4";

        forgetrate => "0.7";
        tcpdump => "false";
        tcpdumpcommand => "/usr/sbin/tcpdump -i eth1 -n -t -v";
    }
```


### forgetrate

**Type**: real

**Allowed input range**: `0,1`

**Default value:** 0.6

**Synopsis**: Decimal fraction [0,1] weighting of new values over
old in 2d-average computation

    body monitor control
    {
    forgetrate => "0.7";
    }

**Notes**:

Configurable settings for the machine-learning algorithm that
tracks system behavior. This is only for expert users. This
parameter effectively determines (together with the monitoring
rate) how quickly CFEngine forgets its previous history.


### histograms

**Type**: (menu option)

**Allowed input range**:

    true
    false
    yes
    no
    on
    off

**Default value:** true

**Synopsis**: Ignored, kept for backward compatibility

    body monitor control
    {
    histograms => "true";
    }

**Notes**:

`cf-monitord` now always keeps histograms information, so this
option is a no-op kept for backward compatibility. It used to cause
CFEngine to learn the conformally transformed distributions of
fluctuations about the mean.


### monitorfacility

**Type**: (menu option)

**Allowed input range**:

    LOG_USER
    LOG_DAEMON
    LOG_LOCAL0
    LOG_LOCAL1
    LOG_LOCAL2
    LOG_LOCAL3
    LOG_LOCAL4
    LOG_LOCAL5
    LOG_LOCAL6
    LOG_LOCAL7

**Default value:** LOG\_USER

**Synopsis**: Menu option for syslog facility

    body monitor control
    {
    monitorfacility => "LOG_USER";
    }

**Notes**:

See notes for syslog.


### tcpdump

**Type**: (menu option)

**Allowed input range**:

    true
    false
    yes
    no
    on
    off

**Default value:** false

**Synopsis**: true/false use tcpdump if found

    body monitor control
    {
    tcpdump => "true";
    }

**Notes**:

Interface with TCP stream if possible.


### tcpdumpcommand

**Type**: string

**Allowed input range**: `"?(/.*)`

**Synopsis**: Path to the tcpdump command on this system

    body monitor control
    {
    tcpdumpcommand => "/usr/sbin/tcpdump -i eth1";
    }

**Notes**:

If this is defined, the monitor will try to interface with the TCP
stream and monitor generic package categories for anomalies.

