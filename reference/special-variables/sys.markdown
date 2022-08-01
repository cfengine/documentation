---
layout: default
title: sys
published: true
tags: [reference, variables, sys, discovery, system, inventory]
---

System variables are derived from CFEngine's automated discovery of system
values. They are provided as variables in order to make automatically adaptive
rules for configuration.

```cf3
    files:

      "$(sys.resolv)"

          create        => "true",
          edit_line     => doresolv("@(this.list1)","@(this.list2)"),
          edit_defaults => reconstruct;
```

### sys.arch

The variable gives the kernel's short architecture description.

```cf3
    # arch = x86_64
```

### sys.bindir

The name of the directory where CFEngine looks for its binaries..

```cf3
    # bindir = /var/cfengine/bin
```

**History:** Introduced in CFEngine 3.6

### sys.cdate

The date of the system in canonical form, i.e. in the form of a class, from when the agent initialized.

```cf3
    # cdate = Sun_Dec__7_10_39_53_2008_
```

### sys.cf_promises

A variable containing the path to the CFEngine syntax analyzer
`cf-promises` on the platform you are using.

```cf3
    classes:

      "syntax_ok" expression => returnszero("$(sys.cf_promises)");
```

### sys.cf_version

The variable gives the version of the running CFEngine Core.

```cf3
    # cf_version = 3.0.5
```

### sys.cf_version_major

The variable gives the major version of the running CFEngine Core.

```cf3
    # cf_version = 3.0.5
    # cf_version_major = 3
```

**History:** Was introduced in 3.5.1, Enterprise 3.5.1.

### sys.cf_version_minor

The variable gives the minor version of the running CFEngine Core.

```cf3
    # cf_version = 3.0.5
    # cf_version_minor = 0
```

**History:** Was introduced in 3.5.1, Enterprise 3.5.1.

### sys.cf_version_patch

The variable gives the patch version of the running CFEngine Core.

```cf3
    # cf_version = 3.0.5
    # cf_version_patch = 5
```

**History:** Was introduced in 3.5.1, Enterprise 3.5.1.

### sys.cf_version_release

The variable gives the release number of the running CFEngine Core.

```cf3
    # cf_version_release = 1
```

**History:** Was introduced in 3.16.0.

### sys.class

This variable contains the name of the hard-class category for this host
(i.e. its top level operating system type classification).

```cf3
    # class = linux
```

**See also:** [`sys.os`][sys#sys.os]

### sys.cpus

A variable containing the number of CPU cores detected. On systems which
provide virtual cores, it is set to the total number of virtual, not
physical, cores. In addition, on a single-core system the class `1_cpu`
is set, and on multi-core systems the class *n*`_cpus` is set, where
*n* is the number of cores identified.

```cf3
    reports:

     "Number of CPUS = $(sys.cpus)";
     8_cpus::
       "This system has 8 processors.";
```

**History:** Was introduced in 3.3.0, Enterprise 2.2.0 (2012)

### sys.crontab

The variable gives the location of the current users's master crontab
directory.

```cf3
    # crontab = /var/spool/crontab/root
```

### sys.date

The date of the system as a text string, from when the agent initialized.

```cf3
    # date = Sun Dec  7 10:39:53 2008
```

### sys.doc_root

A scalar variable containing the default path for the document root of
the standard web server package.

**History:** Was introduced in 3.1.0, Enterprise 2.0.

### sys.domain

The domain name as discovered by CFEngine. If the DNS is in use, it could
be possible to derive the domain name from its DNS registration, but in
general there is no way to discover this value automatically. The
`common control` body permits the ultimate specification of this value.

```cf3
    # domain = example.org

```

### sys.enterprise_version

The variable gives the version of the running CFEngine Enterprise
Edition.

```cf3
    # enterprise_version = 3.0.0
```

**History:** Was introduced in 3.5.0, Enterprise 3.0.0.

### sys.expires

**History:**

- Removed 3.5.0
- Introduced in version 3.1.4, Enterprise 2.0.2 (2011).

### sys.exports

The location of the system NFS exports file.

```cf3
    # exports = /etc/exports
    # exports = /etc/dfs/dfstab
```

### sys.failsafe_policy_path

The name of the failsafe policy file.

```cf3
    # failsafe_policy_path = /var/cfengine/inputs/failsafe.cf
```

**History:** Introduced in CFEngine 3.6

### sys.flavor, sys.flavour

A variable containing an operating system identification string that is
used to determine the current release of the operating system in a form
that can be used as a label in naming. This is used, for instance, to
detect which package name to choose when updating software binaries for
CFEngine.

These two variables are synonyms for each other.

**History:** Was introduced in 3.2.0, Enterprise 2.0

**See also:** [`sys.ostype`][sys#sys.ostype]

### sys.fqhost

The fully qualified name of the host. In order to compute this value
properly, the domain name must be defined.

```cf3
    # fqhost = host.example.org
```

**See also:** [`sys.uqhost`][sys.uqhost]

### sys.fstab

The location of the system filesystem (mount) table.

```cf3
    # fstab = /etc/fstab
```

### sys.hardware_addresses

This is a list variable containing a list of all known MAC addresses for
system interfaces.

**History:** Was introduced in 3.3.0, Enterprise 2.2.0 (2011)

### sys.hardware_mac[interface_name]

This contains the MAC address of the named interface. For example:

```cf3
    reports:
        "Tell me $(sys.hardware_mac[eth0])";
```

**Note:** The *keys* in this array are [canonified][canonify]. For example, the entry for `wlan0.1` would be found under the `wlan0_1` key. Ref: [CFE-3224](https://tracker.mender.io/browse/CFE-3224).

**History:** Was introduced in 3.3.0, Enterprise 2.2.0 (2011)

### sys.host

The name of the current host, according to the kernel. It is undefined
whether this is qualified or unqualified with a domain name.

```cf3
    # host = myhost
```

### sys.inet

The available information about the IPv4 network stack, from when the agent initialized. This is currently available only on Linux systems with the special `/proc/net/*` information files.

From the route table, the `default_gateway` is extracted. From the list of routes in `routes`, the `default_route` is copied to the top level for convenience.

Each route's flags are extracted in a convenient list format.

The `stats` key contains all the TCP and IP counters provided by the system in `/proc/net/netstat`.

**History:** Was introduced in 3.9.0.

**See also:** `sys.inet6`, `sys.interfaces_data`

```

    % cat /proc/net/route
Iface	Destination	Gateway 	Flags	RefCnt	Use	Metric	Mask		MTU	Window	IRTT
enp4s0	00000000	0102A8C0	0003	0	0	100	00000000	0	0	0
enp4s0	0000FEA9	00000000	0001	0	0	1000	0000FFFF	0	0	0
enp4s0	0002A8C0	00000000	0001	0	0	100	00FFFFFF	0	0	0

    % cat /proc/net/netstat
TcpExt: SyncookiesSent SyncookiesRecv SyncookiesFailed EmbryonicRsts PruneCalled RcvPruned OfoPruned OutOfWindowIcmps LockDroppedIcmps ArpFilter TW TWRecycled TWKilled PAWSPassive PAWSActive PAWSEstab DelayedACKs DelayedACKLocked DelayedACKLost ListenOverflows ListenDrops TCPPrequeued TCPDirectCopyFromBacklog TCPDirectCopyFromPrequeue TCPPrequeueDropped TCPHPHits TCPHPHitsToUser TCPPureAcks TCPHPAcks TCPRenoRecovery TCPSackRecovery TCPSACKReneging TCPFACKReorder TCPSACKReorder TCPRenoReorder TCPTSReorder TCPFullUndo TCPPartialUndo TCPDSACKUndo TCPLossUndo TCPLostRetransmit TCPRenoFailures TCPSackFailures TCPLossFailures TCPFastRetrans TCPForwardRetrans TCPSlowStartRetrans TCPTimeouts TCPLossProbes TCPLossProbeRecovery TCPRenoRecoveryFail TCPSackRecoveryFail TCPSchedulerFailed TCPRcvCollapsed TCPDSACKOldSent TCPDSACKOfoSent TCPDSACKRecv TCPDSACKOfoRecv TCPAbortOnData TCPAbortOnClose TCPAbortOnMemory TCPAbortOnTimeout TCPAbortOnLinger TCPAbortFailed TCPMemoryPressures TCPSACKDiscard TCPDSACKIgnoredOld TCPDSACKIgnoredNoUndo TCPSpuriousRTOs TCPMD5NotFound TCPMD5Unexpected TCPSackShifted TCPSackMerged TCPSackShiftFallback TCPBacklogDrop TCPMinTTLDrop TCPDeferAcceptDrop IPReversePathFilter TCPTimeWaitOverflow TCPReqQFullDoCookies TCPReqQFullDrop TCPRetransFail TCPRcvCoalesce TCPOFOQueue TCPOFODrop TCPOFOMerge TCPChallengeACK TCPSYNChallenge TCPFastOpenActive TCPFastOpenActiveFail TCPFastOpenPassive TCPFastOpenPassiveFail TCPFastOpenListenOverflow TCPFastOpenCookieReqd TCPSpuriousRtxHostQueues BusyPollRxPackets TCPAutoCorking TCPFromZeroWindowAdv TCPToZeroWindowAdv TCPWantZeroWindowAdv TCPSynRetrans TCPOrigDataSent TCPHystartTrainDetect TCPHystartTrainCwnd TCPHystartDelayDetect TCPHystartDelayCwnd TCPACKSkippedSynRecv TCPACKSkippedPAWS TCPACKSkippedSeq TCPACKSkippedFinWait2 TCPACKSkippedTimeWait TCPACKSkippedChallenge TCPWinProbe TCPKeepAlive
TcpExt: 0 0 0 19896 7 0 0 9 0 0 560727 0 0 0 0 3575 2049614 302 313016 0 0 17283401 130554 186252521 0 126381259 21978 34307113 42386136 481 386568 7 175 316 11 822 2028 483 20959 148926 16709 267 271328 38869 512579 72057 281202 375133 561590 150370 23 59420 0 106 391776 9062 174837 4389 211213 13931 0 14556 0 0 0 585 594 65103 100117 0 0 0 0 2199955 0 0 0 0 0 0 0 15 36402752 5236349 0 7020 7132 4057 0 0 0 0 0 0 70 0 17925237 24 30 71 693624 275201738 33 992 2253 49843 136 484 21848 0 25 218 10478 503111
IpExt: InNoRoutes InTruncatedPkts InMcastPkts OutMcastPkts InBcastPkts OutBcastPkts InOctets OutOctets InMcastOctets OutMcastOctets InBcastOctets OutBcastOctets InCsumErrors InNoECTPkts InECT1Pkts InECT0Pkts InCEPkts
IpExt: 0 0 1304886 130589 3784495 6 437612883789 422416538003 334973818 8189234 817859007 284 1 487495405 18258 4804476 543340

    # sys.inet = {
    "default_gateway": "192.168.2.1",
    "default_route": {
      "active_default_gateway": true,
      "dest": "0.0.0.0",
      "flags": [
        "up",
        "net",
        "default",
        "gateway"
      ],
      "gateway": "192.168.2.1",
      "interface": "enp4s0",
      "irtt": 0,
      "mask": "0.0.0.0",
      "metric": 100,
      "mtu": 0,
      "refcnt": 0,
      "use": 0,
      "window": 0
    },
    "routes": [
      {
        "active_default_gateway": true,
        "dest": "0.0.0.0",
        "flags": [
          "up",
          "net",
          "default",
          "gateway"
        ],
        "gateway": "192.168.2.1",
        "interface": "enp4s0",
        "irtt": 0,
        "mask": "0.0.0.0",
        "metric": 100,
        "mtu": 0,
        "refcnt": 0,
        "use": 0,
        "window": 0
      },
      {
        "active_default_gateway": false,
        "dest": "169.254.0.0",
        "flags": [
          "up",
          "net",
          "not_default",
          "local"
        ],
        "gateway": "0.0.0.0",
        "interface": "enp4s0",
        "irtt": 0,
        "mask": "255.255.0.0",
        "metric": 1000,
        "mtu": 0,
        "refcnt": 0,
        "use": 0,
        "window": 0
      },
      {
        "active_default_gateway": false,
        "dest": "192.168.2.0",
        "flags": [
          "up",
          "net",
          "not_default",
          "local"
        ],
        "gateway": "0.0.0.0",
        "interface": "enp4s0",
        "irtt": 0,
        "mask": "255.255.255.0",
        "metric": 100,
        "mtu": 0,
        "refcnt": 0,
        "use": 0,
        "window": 0
      }
    ],
    "stats": {
      "IpExt": {
        "InBcastOctets": "817859007",
        "InBcastPkts": "3784495",
        "InCEPkts": "543340",
        "InCsumErrors": "1",
        "InECT0Pkts": "4804476",
        "InECT1Pkts": "18258",
        "InMcastOctets": "334973818",
        "InMcastPkts": "1304886",
        "InNoECTPkts": "487495405",
        "InNoRoutes": "0",
        "InOctets": "437612883789",
        "InTruncatedPkts": "0",
        "OutBcastOctets": "284",
        "OutBcastPkts": "6",
        "OutMcastOctets": "8189234",
        "OutMcastPkts": "130589",
        "OutOctets": "422416538003"
      },
      "TcpExt": {
        "ArpFilter": "0",
        "BusyPollRxPackets": "0",
        "DelayedACKLocked": "302",
        "DelayedACKLost": "313016",
        "DelayedACKs": "2049614",
        "EmbryonicRsts": "19896",
        "IPReversePathFilter": "0",
        "ListenDrops": "0",
        "ListenOverflows": "0",
        "LockDroppedIcmps": "0",
        "OfoPruned": "0",
        "OutOfWindowIcmps": "9",
        "PAWSActive": "0",
        "PAWSEstab": "3575",
        "PAWSPassive": "0",
        "PruneCalled": "7",
        "RcvPruned": "0",
        "SyncookiesFailed": "0",
        "SyncookiesRecv": "0",
        "SyncookiesSent": "0",
        "TCPACKSkippedChallenge": "218",
        "TCPACKSkippedFinWait2": "0",
        "TCPACKSkippedPAWS": "484",
        "TCPACKSkippedSeq": "21848",
        "TCPACKSkippedSynRecv": "136",
        "TCPACKSkippedTimeWait": "25",
        "TCPAbortFailed": "0",
        "TCPAbortOnClose": "13931",
        "TCPAbortOnData": "211213",
        "TCPAbortOnLinger": "0",
        "TCPAbortOnMemory": "0",
        "TCPAbortOnTimeout": "14556",
        "TCPAutoCorking": "17925237",
        "TCPBacklogDrop": "0",
        "TCPChallengeACK": "7132",
        "TCPDSACKIgnoredNoUndo": "65103",
        "TCPDSACKIgnoredOld": "594",
        "TCPDSACKOfoRecv": "4389",
        "TCPDSACKOfoSent": "9062",
        "TCPDSACKOldSent": "391776",
        "TCPDSACKRecv": "174837",
        "TCPDSACKUndo": "20959",
        "TCPDeferAcceptDrop": "0",
        "TCPDirectCopyFromBacklog": "130554",
        "TCPDirectCopyFromPrequeue": "186252521",
        "TCPFACKReorder": "175",
        "TCPFastOpenActive": "0",
        "TCPFastOpenActiveFail": "0",
        "TCPFastOpenCookieReqd": "0",
        "TCPFastOpenListenOverflow": "0",
        "TCPFastOpenPassive": "0",
        "TCPFastOpenPassiveFail": "0",
        "TCPFastRetrans": "512579",
        "TCPForwardRetrans": "72057",
        "TCPFromZeroWindowAdv": "24",
        "TCPFullUndo": "2028",
        "TCPHPAcks": "42386136",
        "TCPHPHits": "126381259",
        "TCPHPHitsToUser": "21978",
        "TCPHystartDelayCwnd": "49843",
        "TCPHystartDelayDetect": "2253",
        "TCPHystartTrainCwnd": "992",
        "TCPHystartTrainDetect": "33",
        "TCPKeepAlive": "503111",
        "TCPLossFailures": "38869",
        "TCPLossProbeRecovery": "150370",
        "TCPLossProbes": "561590",
        "TCPLossUndo": "148926",
        "TCPLostRetransmit": "16709",
        "TCPMD5NotFound": "0",
        "TCPMD5Unexpected": "0",
        "TCPMemoryPressures": "0",
        "TCPMinTTLDrop": "0",
        "TCPOFODrop": "0",
        "TCPOFOMerge": "7020",
        "TCPOFOQueue": "5236349",
        "TCPOrigDataSent": "275201738",
        "TCPPartialUndo": "483",
        "TCPPrequeueDropped": "0",
        "TCPPrequeued": "17283401",
        "TCPPureAcks": "34307113",
        "TCPRcvCoalesce": "36402752",
        "TCPRcvCollapsed": "106",
        "TCPRenoFailures": "267",
        "TCPRenoRecovery": "481",
        "TCPRenoRecoveryFail": "23",
        "TCPRenoReorder": "11",
        "TCPReqQFullDoCookies": "0",
        "TCPReqQFullDrop": "0",
        "TCPRetransFail": "15",
        "TCPSACKDiscard": "585",
        "TCPSACKReneging": "7",
        "TCPSACKReorder": "316",
        "TCPSYNChallenge": "4057",
        "TCPSackFailures": "271328",
        "TCPSackMerged": "0",
        "TCPSackRecovery": "386568",
        "TCPSackRecoveryFail": "59420",
        "TCPSackShiftFallback": "2199955",
        "TCPSackShifted": "0",
        "TCPSchedulerFailed": "0",
        "TCPSlowStartRetrans": "281202",
        "TCPSpuriousRTOs": "100117",
        "TCPSpuriousRtxHostQueues": "70",
        "TCPSynRetrans": "693624",
        "TCPTSReorder": "822",
        "TCPTimeWaitOverflow": "0",
        "TCPTimeouts": "375133",
        "TCPToZeroWindowAdv": "30",
        "TCPWantZeroWindowAdv": "71",
        "TCPWinProbe": "10478",
        "TW": "560727",
        "TWKilled": "0",
        "TWRecycled": "0"
      }
    }
  }

```

### sys.inet6

The available information about the IPv6 network stack, from when the agent initialized. This is currently available only on Linux systems with the special `/proc/net/*` information files.

The configured devices with IPv6 addresses from `/proc/net/if_inet6` are collected under `addresses`.

The routes from `/proc/net/ipv6_route` are collected but not analyzed for default route etc. as with IPv4 routes in `sys.inet`.

The network statistics from `/proc/net/snmp6` are converted to a convenient key-value format under `stats`.

**History:** Was introduced in 3.9.0.

**See also:** `sys.inet`, `sys.interfaces_data`

```

    % cat /proc/net/if_inet6
00000000000000000000000000000001 01 80 10 80       lo
fe80000000000000004249fffebdd7b4 04 40 20 80  docker0
fe80000000000000c27cd1fffe3eada6 02 40 20 80   enp4s0

    % cat /proc/net/ipv6_route
fe800000000000000000000000000000 40 00000000000000000000000000000000 00 00000000000000000000000000000000 00000100 00000001 00000004 00000001   enp4s0
00000000000000000000000000000000 00 00000000000000000000000000000000 00 00000000000000000000000000000000 ffffffff 00000001 0007e26c 00200200       lo
00000000000000000000000000000001 80 00000000000000000000000000000000 00 00000000000000000000000000000000 00000000 00000009 0000020b 80200001       lo
fe80000000000000c27cd1fffe3eada6 80 00000000000000000000000000000000 00 00000000000000000000000000000000 00000000 00000002 00000004 80200001       lo
ff000000000000000000000000000000 08 00000000000000000000000000000000 00 00000000000000000000000000000000 00000100 00000008 0003ffc5 00000001   enp4s0
00000000000000000000000000000000 00 00000000000000000000000000000000 00 00000000000000000000000000000000 ffffffff 00000001 0007e26c 00200200       lo

    % cat /proc/net/snmp6
Ip6InReceives                   	492189
Ip6InHdrErrors                  	0
Ip6InTooBigErrors               	0
Ip6InNoRoutes                   	0
Ip6InAddrErrors                 	0
Ip6InUnknownProtos              	0
Ip6InTruncatedPkts              	0
Ip6InDiscards                   	0
Ip6InDelivers                   	490145
Ip6OutForwDatagrams             	0
Ip6OutRequests                  	12145
Ip6OutDiscards                  	6
Ip6OutNoRoutes                  	249070
Ip6ReasmTimeout                 	0
Ip6ReasmReqds                   	0
Ip6ReasmOKs                     	0
Ip6ReasmFails                   	0
Ip6FragOKs                      	0
Ip6FragFails                    	0
Ip6FragCreates                  	0
Ip6InMcastPkts                  	488766
Ip6OutMcastPkts                 	10304
Ip6InOctets                     	132343220
Ip6OutOctets                    	1522724
Ip6InMcastOctets                	131896014
Ip6OutMcastOctets               	1076616
Ip6InBcastOctets                	0
Ip6OutBcastOctets               	0
Ip6InNoECTPkts                  	492196
Ip6InECT1Pkts                   	0
Ip6InECT0Pkts                   	0
Ip6InCEPkts                     	0
Icmp6InMsgs                     	275
Icmp6InErrors                   	0
Icmp6OutMsgs                    	1815
Icmp6OutErrors                  	0
Icmp6InCsumErrors               	0
Icmp6InDestUnreachs             	0
Icmp6InPktTooBigs               	0
Icmp6InTimeExcds                	0
Icmp6InParmProblems             	0
Icmp6InEchos                    	0
Icmp6InEchoReplies              	0
Icmp6InGroupMembQueries         	0
Icmp6InGroupMembResponses       	1
Icmp6InGroupMembReductions      	1
Icmp6InRouterSolicits           	0
Icmp6InRouterAdvertisements     	0
Icmp6InNeighborSolicits         	5
Icmp6InNeighborAdvertisements   	268
Icmp6InRedirects                	0
Icmp6InMLDv2Reports             	0
Icmp6OutDestUnreachs            	0
Icmp6OutPktTooBigs              	0
Icmp6OutTimeExcds               	0
Icmp6OutParmProblems            	0
Icmp6OutEchos                   	0
Icmp6OutEchoReplies             	0
Icmp6OutGroupMembQueries        	0
Icmp6OutGroupMembResponses      	0
Icmp6OutGroupMembReductions     	0
Icmp6OutRouterSolicits          	396
Icmp6OutRouterAdvertisements    	0
Icmp6OutNeighborSolicits        	206
Icmp6OutNeighborAdvertisements  	5
Icmp6OutRedirects               	0
Icmp6OutMLDv2Reports            	1208
Icmp6InType131                  	1
Icmp6InType132                  	1
Icmp6InType135                  	5
Icmp6InType136                  	268
Icmp6OutType133                 	396
Icmp6OutType135                 	206
Icmp6OutType136                 	5
Icmp6OutType143                 	1208
Udp6InDatagrams                 	486201
Udp6NoPorts                     	0
Udp6InErrors                    	0
Udp6OutDatagrams                	7273
Udp6RcvbufErrors                	0
Udp6SndbufErrors                	0
Udp6InCsumErrors                	0
Udp6IgnoredMulti                	0
UdpLite6InDatagrams             	0
UdpLite6NoPorts                 	0
UdpLite6InErrors                	0
UdpLite6OutDatagrams            	0
UdpLite6RcvbufErrors            	0
UdpLite6SndbufErrors            	0
UdpLite6InCsumErrors            	0

    # sys.inet6 = {
    "addresses": {
      "docker0": {
        "address": "d7b4:febd:49ff:42:0:0:0:fe80",
        "device_number": 4,
        "interface": "docker0",
        "prefix_length": 64,
        "raw_flags": "80",
        "scope": 32
      },
      "enp4s0": {
        "address": "ada6:fe3e:d1ff:c27c:0:0:0:fe80",
        "device_number": 2,
        "interface": "enp4s0",
        "prefix_length": 64,
        "raw_flags": "80",
        "scope": 32
      },
      "lo": {
        "address": "1:0:0:0:0:0:0:0",
        "device_number": 1,
        "interface": "lo",
        "prefix_length": 128,
        "raw_flags": "80",
        "scope": 16
      }
    },
    "routes": [
      {
        "dest": "0:0:0:0:0:0:0:0",
        "dest_prefix": "40",
        "flags": [
          "up",
          "net",
          "local"
        ],
        "interface": "enp4s0",
        "metric": 256,
        "next_hop": "0:0:0:0:0:0:0:0",
        "refcnt": 1,
        "source_prefix": "00",
        "use": 4
      },
      {
        "dest": "0:0:0:0:0:0:0:0",
        "dest_prefix": "80",
        "flags": [
          "up",
          "net",
          "local"
        ],
        "interface": "lo",
        "metric": 0,
        "next_hop": "0:0:0:0:0:0:0:0",
        "refcnt": 2,
        "source_prefix": "00",
        "use": 4
      }
    ],
    "stats": {
      "Icmp6InCsumErrors": 0,
      "Icmp6InDestUnreachs": 0,
      "Icmp6InEchoReplies": 0,
      "Icmp6InEchos": 0,
      "Icmp6InErrors": 0,
      "Icmp6InGroupMembQueries": 0,
      "Icmp6InGroupMembReductions": 1,
      "Icmp6InGroupMembResponses": 1,
      "Icmp6InMLDv2Reports": 0,
      "Icmp6InMsgs": 275,
      "Icmp6InNeighborAdvertisements": 268,
      "Icmp6InNeighborSolicits": 5,
      "Icmp6InParmProblems": 0,
      "Icmp6InPktTooBigs": 0,
      "Icmp6InRedirects": 0,
      "Icmp6InRouterAdvertisements": 0,
      "Icmp6InRouterSolicits": 0,
      "Icmp6InTimeExcds": 0,
      "Icmp6InType131": 1,
      "Icmp6InType132": 1,
      "Icmp6InType135": 5,
      "Icmp6InType136": 268,
      "Icmp6OutDestUnreachs": 0,
      "Icmp6OutEchoReplies": 0,
      "Icmp6OutEchos": 0,
      "Icmp6OutErrors": 0,
      "Icmp6OutGroupMembQueries": 0,
      "Icmp6OutGroupMembReductions": 0,
      "Icmp6OutGroupMembResponses": 0,
      "Icmp6OutMLDv2Reports": 1208,
      "Icmp6OutMsgs": 1815,
      "Icmp6OutNeighborAdvertisements": 5,
      "Icmp6OutNeighborSolicits": 206,
      "Icmp6OutParmProblems": 0,
      "Icmp6OutPktTooBigs": 0,
      "Icmp6OutRedirects": 0,
      "Icmp6OutRouterAdvertisements": 0,
      "Icmp6OutRouterSolicits": 396,
      "Icmp6OutTimeExcds": 0,
      "Icmp6OutType133": 396,
      "Icmp6OutType135": 206,
      "Icmp6OutType136": 5,
      "Icmp6OutType143": 1208,
      "Ip6FragCreates": 0,
      "Ip6FragFails": 0,
      "Ip6FragOKs": 0,
      "Ip6InAddrErrors": 0,
      "Ip6InBcastOctets": 0,
      "Ip6InCEPkts": 0,
      "Ip6InDelivers": 490145,
      "Ip6InDiscards": 0,
      "Ip6InECT0Pkts": 0,
      "Ip6InECT1Pkts": 0,
      "Ip6InHdrErrors": 0,
      "Ip6InMcastOctets": 131896014,
      "Ip6InMcastPkts": 488766,
      "Ip6InNoECTPkts": 492196,
      "Ip6InNoRoutes": 0,
      "Ip6InOctets": 132343220,
      "Ip6InReceives": 492189,
      "Ip6InTooBigErrors": 0,
      "Ip6InTruncatedPkts": 0,
      "Ip6InUnknownProtos": 0,
      "Ip6OutBcastOctets": 0,
      "Ip6OutDiscards": 6,
      "Ip6OutForwDatagrams": 0,
      "Ip6OutMcastOctets": 1076616,
      "Ip6OutMcastPkts": 10304,
      "Ip6OutNoRoutes": 249070,
      "Ip6OutOctets": 1522724,
      "Ip6OutRequests": 12145,
      "Ip6ReasmFails": 0,
      "Ip6ReasmOKs": 0,
      "Ip6ReasmReqds": 0,
      "Ip6ReasmTimeout": 0,
      "Udp6IgnoredMulti": 0,
      "Udp6InCsumErrors": 0,
      "Udp6InDatagrams": 486201,
      "Udp6InErrors": 0,
      "Udp6NoPorts": 0,
      "Udp6OutDatagrams": 7273,
      "Udp6RcvbufErrors": 0,
      "Udp6SndbufErrors": 0,
      "UdpLite6InCsumErrors": 0,
      "UdpLite6InDatagrams": 0,
      "UdpLite6InErrors": 0,
      "UdpLite6NoPorts": 0,
      "UdpLite6OutDatagrams": 0,
      "UdpLite6RcvbufErrors": 0,
      "UdpLite6SndbufErrors": 0
    }
  }

```

### sys.inputdir

The name of the inputs directory where CFEngine looks for its policy files.

```cf3
    # inputdir = /var/cfengine/inputs
```

**History:** Introduced in CFEngine 3.6

### sys.interface

The assumed (default) name of the main system interface on this host.

```cf3
    # interface = eth0
```

### sys.interfaces

Displays a system list of configured interfaces currently active in use
by the system. This list is detected at runtime and it passed in the
variables report to the CFEngine Enterprise Database.

**Example:**

[%CFEngine_include_snippet(sys_interfaces_ip_addresses_ipv4.cf, #\+begin_src\s+cfengine3\s*, .*end_src)%]

**Example Output:**

[%CFEngine_include_snippet(sys_interfaces_ip_addresses_ipv4.cf, #\+begin_src\s+static_example_output\s*, .*end_src)%]


**History:** Was introduced in 3.3.0, Enterprise 2.2.0 (2011)

### sys.interfaces_data

The network statistics of the system interfaces, from when the agent initialized. This is currently available only on Linux systems with the special `/proc/net/dev` file.

**History:** Was introduced in 3.9.0.

**See also:** `sys.inet6`, `sys.inet`

```
    % cat /proc/net/dev
Inter-|   Receive                                                |  Transmit
 face |bytes    packets errs drop fifo frame compressed multicast|bytes    packets errs drop fifo colls carrier compressed
enp4s0: 446377831179 492136556    0    0    0     0          0         0 428200856331 499195545    0    0    0     0       0          0
    lo: 1210580426 1049790    0    0    0     0          0         0 1210580426 1049790    0    0    0     0       0          0
wlp3s0:       0       0    0    0    0     0          0         0        0       0    0    0    0     0       0          0

    # sys.interfaces_data = {
    "enp4s0": {
      "device": "enp4s0",
      "receive_bytes": "446377831179",
      "receive_compressed": "0",
      "receive_drop": "0",
      "receive_errors": "0",
      "receive_fifo": "0",
      "receive_frame": "0",
      "receive_multicast": "0",
      "receive_packets": "492136556",
      "transmit_bytes": "428200856331",
      "transmit_compressed": "0",
      "transmit_drop": "0",
      "transmit_errors": "0",
      "transmit_fifo": "0",
      "transmit_frame": "0",
      "transmit_multicast": "0",
      "transmit_packets": "499195545"
    },
    "lo": {
      "device": "lo",
      "receive_bytes": "1210580426",
      "receive_compressed": "0",
      "receive_drop": "0",
      "receive_errors": "0",
      "receive_fifo": "0",
      "receive_frame": "0",
      "receive_multicast": "0",
      "receive_packets": "1049790",
      "transmit_bytes": "1210580426",
      "transmit_compressed": "0",
      "transmit_drop": "0",
      "transmit_errors": "0",
      "transmit_fifo": "0",
      "transmit_frame": "0",
      "transmit_multicast": "0",
      "transmit_packets": "1049790"
    },
    "wlp3s0": {
      "device": "wlp3s0",
      "receive_bytes": "0",
      "receive_compressed": "0",
      "receive_drop": "0",
      "receive_errors": "0",
      "receive_fifo": "0",
      "receive_frame": "0",
      "receive_multicast": "0",
      "receive_packets": "0",
      "transmit_bytes": "0",
      "transmit_compressed": "0",
      "transmit_drop": "0",
      "transmit_errors": "0",
      "transmit_fifo": "0",
      "transmit_frame": "0",
      "transmit_multicast": "0",
      "transmit_packets": "0"
    }
  }
```

### sys.interface_flags

Contains a space separated list of the flags of the named interface. e.g.

```cf3
    reports:
        "eth0 flags: $(sys.interface_flags[eth0])";
```

Outputs:

    R: eth0 flags: up broadcast running multicast


The following device flags are supported:

* up
* broadcast
* debug
* loopback
* pointopoint
* notrailers
* running
* noarp
* promisc
* allmulti
* multicast

**History:** Was introduced in 3.5.0 (2013)

### sys.ip_addresses

Displays a system list of IP addresses currently in use by the system.
This list is detected at runtime and passed in the variables report to the
CFEngine Enterprise Database.

To use this list in a policy, you will need a local copy since only
local variables can be iterated.

```cf3
    bundle agent test
    {
    vars:

     # To iterate, we need a local copy

     "i1" slist => { @(sys.ip_addresses)} ;
     "i2" slist => { @(sys.interfaces)} ;

    reports:

        "Addresses: $(i1)";
        "Interfaces: $(i2)";
        "Addresses of the interfaces: $(sys.ipv4[$(i2)])";
    }
```

**History:** Was introduced in 3.3.0, Enterprise 2.2.0 (2011)

### sys.ip2iface

A map of full IPv4 addresses (key) to the system interface (value),
e.g. `$(sys.ip2iface[1.2.3.4])`.

```cf3
    # If the IPv4 address on the interfaces are
    #    le0 = 192.168.1.101
    #    xr1 = 10.12.7.254
    #
    # Then you will have
    # sys.ip2iface[192.168.1.101] = le0
    # sys.ip2iface[10.12.7.254] = xr1
```

**Notes:**

- The list of addresses may be acquired with `getindices("sys.ip2iface")` (or
from any of the other associative arrays). Only those interfaces which are
marked as "up" and have an IP address will have entries.

- The *values* in this array are [canonified][canonify]. For example, the entry for `wlan0.1` would be `wlan0_1`. Ref: [CFE-3224](https://tracker.mender.io/browse/CFE-3224).

**History:** Was introduced in 3.9.

### sys.ipv4

All four octets of the IPv4 address of the first system interface.

**Note**:

If your system has a single ethernet interface, `$(sys.ipv4)` will contain
your IPv4 address. However, if your system has multiple interfaces, then
`$(sys.ipv4)` will simply be the IPv4 address of the first interface in the
list that has an assigned address, Use `$(sys.ipv4[interface_name])` for
details on obtaining the IPv4 addresses of all interfaces on a system.

### sys.ipv4[interface_name]

The full IPv4 address of the system interface named as the associative
array index, e.g. `$(sys.ipv4[le0])` or `$(sys.ipv4[xr1])`.

```cf3
    # If the IPv4 address on the interfaces are
    #    le0 = 192.168.1.101
    #    xr1 = 10.12.7.254
    #
    # Then the octets of all interfaces are accessible as an associative array
    # sys.ipv4_1[le0] = 192
    # sys.ipv4_2[le0] = 192.168
    # sys.ipv4_3[le0] = 192.168.1
    #   sys.ipv4[le0] = 192.168.1.101
    # sys.ipv4_1[xr1] = 10
    # sys.ipv4_2[xr1] = 10.12
    # sys.ipv4_3[xr1] = 10.12.7
    #   sys.ipv4[xr1] = 10.12.7.254
```

**Note**:

The list of interfaces may be acquired with `getindices("sys.ipv4")` (or
from any of the other associative arrays). Only those interfaces which
are marked as "up" and have an IP address will be listed.

### sys.ipv4_1[interface_name]


The first octet of the IPv4 address of the system interface named as the
associative array index, e.g. `$(ipv4_1[le0])` or `$(ipv4_1[xr1])`.

**Note:** The *keys* in this array are [canonified][canonify]. For example, the entry for `wlan0.1` would be found under the `wlan0_1` key. Ref: [CFE-3224](https://tracker.mender.io/browse/CFE-3224).

### sys.ipv4_2[interface_name]

The first two octets of the IPv4 address of the system interface named as the associative array index, e.g. `$(ipv4_2[le0])` or `$(ipv4_2[xr1])`.

**Note:** The *keys* in this array are [canonified][canonify]. For example, the entry for `wlan0.1` would be found under the `wlan0_1` key. Ref: [CFE-3224](https://tracker.mender.io/browse/CFE-3224).

### sys.ipv4_3[interface_name]

The first three octets of the IPv4 address of the system interface named as the associative array index, e.g. `$(ipv4_3[le0])` or `$(ipv4_3[xr1])`.

**Note:** The *keys* in this array are [canonified][canonify]. For example, the entry for `wlan0.1` would be found under the `wlan0_1` key. Ref: [CFE-3224](https://tracker.mender.io/browse/CFE-3224).

### sys.key_digest

The digest of the host's cryptographic public key.

```cf3
    # sys.key_digest = MD5=bc230448c9bec14b9123443e1608ac07
```

### sys.last_policy_update

Timestamp when last policy change was seen by host

### sys.libdir

The name of the directory where CFEngine looks for its libraries.

```cf3
    # libdir = /var/cfengine/inputs/lib
```

**History:** Introduced in CFEngine 3.6, version based sub directory removed in
CFEngine 3.8.

### sys.local_libdir

The name of the directory where CFEngine looks for its libraries, without any prefixes.

```cf3
    # local_libdir = lib
```

**History:** Introduced in CFEngine 3.6, version based sub directory removed in
CFEngine 3.8.

### sys.logdir

The name of the directory where CFEngine log files are saved

```cf3
    # logdir = /var/cfengine/
```

**History:** Introduced in CFEngine 3.6

### sys.license_owner

**History:**

- Removed 3.5.0
- Introduced in version 3.1.4, Enterprise 2.0.2 (2011).

### sys.licenses_granted

**History:**

- Removed 3.5.0
- Was introduced in version 3.1.4, Enterprise 2.0.2 (2011).

### sys.long_arch

The long architecture name for this system kernel. This name is
sometimes quite unwieldy but can be useful for logging purposes.

```cf3
    # long_arch = linux_x86_64_2_6_22_19_0_1_default__1_SMP_2008_10_14_22_17_43__0200
```

**See also:** [`sys.ostype`][sys#sys.ostype]

### sys.maildir

The name of the system email spool directory.

```cf3
    # maildir = /var/spool/mail
```

### sys.masterdir

The name of the directory on the hub where CFEngine looks for inputs to be validated and copied into `sys.inputdir`.

```cf3
    # masterdir = /var/cfengine/masterfiles
```

**History:** Introduced in CFEngine 3.6

### sys.nova_version

The variable gives the version of the running CFEngine Enterprise Edition.

```cf3
# nova_version = 1.1.3
```

### sys.os

The name of the operating system according to the kernel.

```cf3
    # os = linux
```

**See also:** [`sys.ostype`][sys#sys.ostype]

### sys.os_name_human

A human friendly version of the operating system that's running.

**Example policy:**

```cf3
bundle agent __main__
{
   reports:
    "$(sys.os_name_human)";
}
```

**Example policy output:**

```
R: Ubuntu
```

**History:**

* 3.18.0 introduced

### sys.os_release

Information parsed from `/etc/os-release` if present.

```cf3
bundle agent main
{
    reports:
       "$(with)"
         with => string_mustache("{{%-top-}}", @(sys.os_release) );
}
```

Policy Output:

```
R: {
  "BUG_REPORT_URL": "https://bugs.launchpad.net/ubuntu/",
  "HOME_URL": "https://www.ubuntu.com/",
  "ID": "ubuntu",
  "ID_LIKE": "debian",
  "NAME": "Ubuntu",
  "PRETTY_NAME": "Ubuntu 17.10",
  "PRIVACY_POLICY_URL": "https://www.ubuntu.com/legal/terms-and-policies/privacy-policy",
  "SUPPORT_URL": "https://help.ubuntu.com/",
  "UBUNTU_CODENAME": "artful",
  "VERSION": "17.10 (Artful Aardvark)",
  "VERSION_CODENAME": "artful",
  "VERSION_ID": "17.10"
}
```

**History:**

- Added in 3.11.0

### sys.os_version_major

The major version of the operating system that's running.

**Example policy:**

```cf3
bundle agent __main__
{
   reports:
    "$(sys.os_version_major)";
}
```

**Example policy output:**

```
R: 22
```

**History:**

* 3.18.0 introduced


### sys.ostype

Another name for the operating system.

```cf3
    # ostype = linux_x86_64
```

**See also:** [`sys.class`][sys#sys.class]

### sys.piddir

The name of the directory where CFEngine saves the daemon pid files.

```cf3
    # piddir = /var/cfengine/
```

**History:** Introduced in CFEngine 3.6


### sys.policy_entry_basename

The basename of the first policy file read by the agent. For example
```promises.cf``` or ```update.cf```.

**See also:** [`sys.policy_entry_dirname`][sys.policy_entry_dirname] [`sys.policy_entry_filename`][sys.policy_entry_dirname]

**History:**

- Introduced 3.12.0

### sys.policy_entry_dirname

The full path to the directory containing the first policy file read by the agent. For example
```/var/cfengine/inputs``` or ```~/.cfagent/inputs```.

**See also:** [`sys.policy_entry_basename`][sys#sys.policy_entry_basename] [`sys.policy_entry_filename`][sys.policy_entry_filename]


**History:**

- Introduced 3.12.0

### sys.policy_entry_filename

The full path to the first policy file read by the agent. For example
```/var/cfengine/inputs/promises.cf``` or ```~/.cfagent/inputs/promises.cf```.

**See also:** [`sys.policy_entry_basename`][sys#sys.policy_entry_basename] [`sys.policy_entry_dirname`][sys#sys.policy_entry_dirname]


**History:**

- Introduced 3.12.0

### sys.policy_hub

IP of the machine acting as the policy server.

```$(sys.workdir)/policy_server.dat``` stores bootstrap information. If bootstrapped to a hostname, the value is the current IP the hostname resolves to. If bootstrapped to an IP, the value is the stored IP. The variable is undefined if ```$(sys.workdir)/policy_server.dat``` does not exist or is empty.

```cf3
    reports:

     "Policy hub is $(sys.policy_hub)";
```

**History:**

- Introduced in version 3.1.0b1,Enterprise 2.0.0b1 (2010).
- Available in Community since 3.2.0

### sys.policy_hub_port

The default port which ```cf-agent``` will use by default when making outbound
connections to ```cf-serverd```. This defaults to ```5308``` but can be
overridden based on the data provided during bootstrap stored in
```$(sys.workdir)/policy_server.dat```.

**History:**

- Introduced in version 3.10.0 (2016).

### sys.release

The kernel release of the operating system.

```cf3
    # release = 2.6.22.19-0.1-default
```

### sys.resolv

The location of the system resolver file.

```cf3
    # resolv = /etc/resolv.conf
```

### sys.statedir

The name of the state directory where CFEngine looks for its embedded database files.

```cf3
    # statedir = /var/cfengine/state
```

**History:** Introduced in CFEngine 3.7

### sys.sysday

A variable containing the time since the UNIX Epoch (00:00:00 UTC, January 1,
1970), measured in days. It is equivalent to `$(sys.systime)` divided by the
number of seconds in a day, expressed as an integer. No time zone conversion
is performed, the direct result of the time() system call is used. This value
is most commonly used in the /etc/shadow file.

```cf3
   # sysday = 15656

   Corresponds to Monday, November 12, 2012.
```

**History:** Introduced in CFEngine 3.6

### sys.systime

A variable containing the result of the time() system call, which is the
time since the UNIX Epoch (00:00:00 UTC, January 1, 1970), measured in
seconds. See also `$(sys.sysday)`.

```cf3
   # systime = 1352754900

   Corresponds to Mon Nov 12 21:15:00 2012 UTC.
```

**History:** Introduced in CFEngine 3.6

### sys.update_policy_path

The name of the update policy file.

```cf3
    # update_policy_path = /var/cfengine/inputs/update.cf
```

**History:** Introduced in CFEngine 3.6

### sys.uptime

A variable containing the number of minutes which the system has been
online.  (Not implemented on the Windows platform.)

```cf3
   # uptime = 69735

   Equivalent uptime command output:
    16:24:52 up 48 days, 10:15,  1 user,  load average: 0.00, 0.00, 0.00
```

**History:** Introduced in CFEngine 3.6

### sys.user_data

A data container with the user information of the user that started the agent.

```cf3
    # user_data = {
        "description": "root",
        "gid": 0,
        "home_dir": "/root",
        "shell": "/bin/bash",
        "uid": 0,
        "username": "root"
      }

```

**History:** Introduced in CFEngine 3.10

### sys.uqhost

The unqualified name of the current host.

```cf3
    # uqhost = myhost
```

**See also:** [`sys.fqhost`][sys#sys.fqhost]

### sys.version

The version of the running kernel. On Linux, this corresponds to the
output of `uname -v`.

```cf3
    # version = #55-Ubuntu SMP Mon Jan 10 23:42:43 UTC 2011
```

**History:** Was introduced in version 3.1.4,Enterprise 2.0.2 (2011)

### sys.windir

On the Windows version of CFEngine Enterprise, this is the path to the Windows
directory of this system.

```cf3
    # windir = C:\WINDOWS
```

### sys.winprogdir

On the Windows version of CFEngine Enterprise, this is the path to the program
files directory of the system.

```cf3
    # winprogdir = C:\Program Files
```

### sys.winprogdir86

On 64 bit Windows versions of CFEngine Enterprise, this is the path to the 32
bit (x86) program files directory of the system.

```cf3
    # winprogdir86 = C:\Program Files (x86)
```

### sys.winsysdir

On the Windows version of CFEngine Enterprise, this is the path to the Windows
system directory.

```cf3
    # winsysdir = C:\WINDOWS\system32
```

### sys.workdir

The location of the CFEngine work directory and cache.
For the system privileged user this is normally:

```cf3
    # workdir = /var/cfengine
```

For non-privileged users it is in the user's home directory:

```cf3
    # workdir = /home/user/.cfagent
```

On the Windows version of CFEngine Enterprise, it is normally under program
files (the directory name may change with the language of Windows):

```cf3
    # workdir = C:\Program Files\CFEngine
```
-
