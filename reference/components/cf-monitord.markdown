---
layout: default
title: cf-monitord
published: true
sorting: 50
tags: [Components, cf-monitord]
keywords: [monitor]
---

`cf-monitord` is the monitoring daemon for CFEngine. It samples probes defined
in policy using `measurements` type promises and attempts to learn the normal
system state based on current and past observations. Current estimates are made
available as [special variables][special variables] (e.g.
[`$(mon.av_cpu)`][mon#mon.av_cpu]) to `cf-agent`, which may use them to inform
policy decisions.

`cf-monitord` keeps the promises made in `common`and `monitor` bundles, and is
affected by  `common` and `monitor` control bodies.

**Notes:**

* `cf-monitord` always considers the class ```monitor``` to be defined.

## Command reference ##

[%CFEngine_include_snippet(cf-monitord.help, [\s]*--[a-z], ^$)%]

## Standard measurements:

The `cf-monitord` service monitors a number of variables as standard on Unix
and Windows systems. Windows is fundamentally different from Unix and
currently has less support for out-of-the-box probes.

1.  users: Users logged in
2.  rootprocs: Privileged system processes
3.  otherprocs: Non-privileged process
4.  diskfree: Free disk on / partition
5.  loadavg: % kernel load utilization
6.  netbiosns\_in: netbios name lookups (in)
7.  netbiosns\_out: netbios name lookups (out)
8.  netbiosdgm\_in: netbios name datagrams (in)
9.  netbiosdgm\_out: netbios name datagrams (out)
10. netbiosssn\_in: netbios name sessions (in)
11. netbiosssn\_out: netbios name sessions (out)
12. irc\_in: IRC connections (in)
13. irc\_out: IRC connections (out)
14. cfengine\_in: CFEngine connections (in)
15. cfengine\_out: CFEngine connections (out)
16. nfsd\_in: nfs connections (in)
17. nfsd\_out: nfs connections (out)
18. smtp\_in: smtp connections (in)
19. smtp\_out: smtp connections (out)
20. www\_in: www connections (in)
21. www\_out: www connections (out)
22. ftp\_in: ftp connections (in)
23. ftp\_out: ftp connections (out)
24. ssh\_in: ssh connections (in)
25. ssh\_out: ssh connections (out)
26. wwws\_in: wwws connections (in)
27. wwws\_out: wwws connections (out)
28. icmp\_in: ICMP packets (in)
29. icmp\_out: ICMP packets (out)
30. udp\_in: UDP dgrams (in)
31. udp\_out: UDP dgrams (out)
32. dns\_in: DNS requests (in)
33. dns\_out: DNS requests (out)
34. tcpsyn\_in: TCP sessions (in)
35. tcpsyn\_out: TCP sessions (out)
36. tcpack\_in: TCP acks (in)
37. tcpack\_out: TCP acks (out)
38. tcpfin\_in: TCP finish (in)
39. tcpfin\_out: TCP finish (out)
40. tcpmisc\_in: TCP misc (in)
41. tcpmisc\_out: TCP misc (out)
42. webaccess: Webserver hits
43. weberrors: Webserver errors
44. syslog: New log entries (Syslog)
45. messages: New log entries (messages)
46. temp0: CPU Temperature core 0
47. temp1: CPU Temperature core 1
48. temp2: CPU Temperature core 2
49. temp3: CPU Temperature core 3
50. cpu: %CPU utilization (all)
51. cpu0: %CPU utilization core 0
52. cpu1: %CPU utilization core 1
53. cpu2: %CPU utilization core 2
54. cpu3: %CPU utilization core 3

Slots with a higher number are used for custom measurement promises in
CFEngine Enterprise.

These values collected and analyzed by `cf-monitord` are transformed
into agent variables in the `$(mon.`name`)` context.

Note: There is no way for force a refresh of the monitored data.

## Control Promises

Settings describing the details of the fixed behavioral promises
made by `cf-monitord`. The system defaults will be sufficient for
most users. This configurability potential, however, will be a key
to developing the integrated monitoring capabilities of CFEngine.


```cf3
    body monitor control
    {
        #version => "1.2.3.4";

        forgetrate => "0.7";
        tcpdump => "false";
        tcpdumpcommand => "/usr/sbin/tcpdump -i eth1 -n -t -v";
    }
```


### forgetrate

**Description:** Decimal fraction [0,1] weighting of new values over
old in 2d-average computation

Configurable settings for the machine-learning algorithm that
tracks system behavior. This is only for expert users. This
parameter effectively determines (together with the monitoring
rate) how quickly CFEngine forgets its previous history.

**Type:** `real`

**Allowed input range:** `0,1`

**Default value:** 0.6

**Example:**

```cf3
    body monitor control
    {
    forgetrate => "0.7";
    }
```

### histograms

**Deprecated:** Ignored, kept for backward compatibility

`cf-monitord` now always keeps histograms information, so this
option is a no-op kept for backward compatibility. It used to cause
CFEngine to learn the conformally transformed distributions of
fluctuations about the mean.


**Type:** [`boolean`][boolean]

**Default value:** true

**Example:**

```cf3
    body monitor control
    {
    histograms => "true";
    }
```

### monitorfacility

**Description:** Menu option for syslog facility

**Type:** (menu option)

**Allowed input range:**

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

**Default value:** `LOG_USER`

**Example:**

    body monitor control
    {
    monitorfacility => "LOG_USER";
    }

### tcpdump

**Description:** true/false use tcpdump if found

Interface with TCP stream if possible.

**Type:** [`boolean`][boolean]

**Default value:** false

    body monitor control
    {
    tcpdump => "true";
    }

### tcpdumpcommand

**Description:** Path to the tcpdump command on this system

If this is defined, the monitor will try to interface with the TCP
stream and monitor generic package categories for anomalies.

**Type:** `string`

**Allowed input range:** `"?(/.*)`

**Example:**

```cf3
    body monitor control
    {
    tcpdumpcommand => "/usr/sbin/tcpdump -i eth1";
    }
```
