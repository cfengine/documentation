---
layout: default
title: Bundles for monitor
categories: [Reference, Components, cf-monitord, Bundles for monitor]
published: true
alias: reference-components-bundles-for-monitor.html
tags: [reference, components, bundles, monitoring, cf-monitord]
---

Monitor bundles contain user defined promises for system discovery and
monitoring.

```cf3
     
     bundle monitor example
     {
     measurements:
     
       "/bin/df"   # Discover disk device information
     
           handle = "free_diskspace_watch",
           stream_type = "pipe",
           data_type = "slist",
           history_type = "static",
           units = "device",
           match_value = file_systems;
     
     
     }     
```
