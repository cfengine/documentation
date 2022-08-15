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
55. microsoft\_ds\_out: Samba/MS\_ds name sessions (out)
56. www\_alt\_in: Alternative web service connections (in)
57. www\_alt\_out: Alternative web client connections (out)
58. imaps\_in: encrypted imap mail service sessions (in)
59. imaps\_out: encrypted imap mail client sessions (out)
60. ldap\_in: LDAP directory service service sessions (in)
61. ldap\_out: LDAP directory service client sessions (out)
62. ldaps\_in: LDAP directory service service sessions (in)
63. ldaps\_out: LDAP directory service client sessions (out)
64. mongo\_in: Mongo database service sessions (in)
65. mongo\_out: Mongo database client sessions (out)
66. mysql\_in: MySQL database service sessions (in)
67. mysql\_out: MySQL database client sessions (out)
68. postgres\_in: PostgreSQL database service sessions (in)
69. postgres\_out: PostgreSQL database client sessions (out)
70. ipp\_in: Internet Printer Protocol (in)
71. ipp\_out: Internet Printer Protocol (out)
72. io\_reads: Number of I/O reads
73. io\_writes: Number of I/O writes
74. io\_readdata: Aggregate mount of data read across all devices
75. io\_writtendata: Aggregate amount of data written across all devices
76. mem\_total: Total system memory
77. mem\_free: Free system memory
78. mem\_cached: Size of disk cache
79. mem\_swap: Total swap size
80. mem\_freeswap: Free swap size

Slots with a higher number are used for custom measurement promises in
CFEngine Enterprise.

These values collected and analyzed by `cf-monitord` are transformed
into agent variables in the `$(mon.`name`)` context.

Note: There is no way for force a refresh of the monitored data.

## Data storage ##

`cf-monitord` records data in `$(sys.statedir)` (typically `/var/cfengine/state`).

* `cf_observations.lmdb`
* `nova_measures.lmdb`
* `ts_key`
* `env_data`
* `cf_incoming.<service id>`
* `cf_outgoing.<service id>`
* `cf_state.lmdb`
* `history.lmdb`

## Statistical Classes

`cf-monitord` automatically defines classes based on the observation of the data
is has collected. Classes defined are named for the measurement id (the promise
handle in the case of custom measurement promises) with prefixes and or suffixes
depending on the measurement.

The following suffixes may be used when defining classes:

* `_high` :: The last measurement seemed high. It was greater than the average of all time and also greater than the recent average. This could indicate that the measured value is experiencing a "spike" or trending in a positive direction.
* `_low` :: The last measurement was low. It was lower than the average of all time and also lower than the recent average. This could indicate that the measured value is experiencing a "dip" or trending in a negative direction.
* `_normal` :: The value was neither high nor low, (as per how those are described above).
* `_ldt` :: A leap (step) detected, meaning a distinct (significant) change in the average.
* `_dev1` :: The last measurement was at least 1 standard deviation higher/lower than the average.
* `_dev2` :: The last measurement was at least 2 standard deviations higher/lower than the average. These classes are persistently defined for a number of minutes.
* `_anomaly` :: The last measurement was at least 3 standard deviations than the average. These classes are persistently defined for a number of minutes.
* `_microanomaly` :: The last measurement was at least 2 standard deviations higher than the average.

The following prefixes may be used when defining classes:

* `entropy_` ::

Note: These suffixes and prefixes may be combined, resulting in a class like `rootprocs_high`, `loadavg_high_ldt`, `cpu1_high_dev3`, and `entropy_postgresql_out_low`.

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
