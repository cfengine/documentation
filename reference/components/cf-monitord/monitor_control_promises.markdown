---
layout: default
title: monitor control promises
categories: [Reference, Components, cf-monitord, monitor control promises]
published: true
alias: reference-components-cfmonitord-control-promises.html
tags: [Components, cf-monitord, control promises]
---

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

