---
layout: default
title: Health
sorting: 20
---

<img width="493px" src="Mission-portal-health-dignostics-header.png">

You can get quick access to the health of hosts, including direct links to reports, from the Health drop down at the top of every Enterprise UI screen. Hosts are listed as unhealthy if:

* Missing reporting data : Host has connected to hub (to get policy), but reports have never been collected from it.
* Unreachable hosts : Reports from host has been collected in the past, but not recently (as defined by "Unreachable host threshold").
* Outdated reporting data : The host is communicating correctly and sending its reports, but the data is outdated (there are no recent reports), indicating that there hasn't been any policy runs recently (performed by the cf-agent binary). There is no data to prove that your policy, describing your desired state, is being successfully enforced.
* Policy errors : Reports have recently been collected and cf-agent has completed a run with an error.
* Duplicate IDs : CFEngine hosts are identified by the CFEngine key they use. If two or more hosts use the same key the reports will be very unreliable. This is detected by exchanging randomized cookies(tokens) during report collections. If a client sends a mismatching cookie (compared to last collection), it indicates that multiple hosts are using the same ID.
* Duplicate hostnames: multiple host identities reporting the same host identifier (by default hostname derived from `default:sys.fqhost` variable but changeable in Settings -> Host identifier)

These categories are non-overlapping, meaning a host will only appear in one category at at time even if conditions satisfying multiple categories might be present. This makes reports simpler to read, and makes it easier to detect and fix the root cause of the issue. As one issue is resolved the host might then move to another category.
Regardless of the situation, the data from the host will be from the latest report collection, representing the most recent known state of the host.
