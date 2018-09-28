---
layout: default
title: standalone_self_upgrade.cf
published: true
sorting: 150
tags: [reference, policy entry, MPF]
---

`$(sys.inputdir)/standalone_self_upgrade.cf` is an independent policy set entry
like `promises.cf` and `update.cf`. The policy is executed by an independent
agent executed from the `update.cf` entry when the class `trigger_upgrade` is
defined and the host is not seen to be running the desired version of the agent.
The policy is designed for use with Enterprise packages, but can be customized
for use with community packages.

***

[%CFEngine_library_include(standalone_self_upgrade)%]
