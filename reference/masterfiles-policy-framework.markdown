---
layout: default
title: Masterfiles Policy Framework
published: true
sorting: 90
tags: [reference, masterfiles, MPF]
---

The Masterfiles Policy Framework or MPF also commonly reffered to as simply
masterfiles is the policy framework that ships with CFEngine.

This is where we should talk about the MPF, how to configure and use it, maybe
link to upgrade docs.


### persistent\_disable\_*DAEMON*

**Description:** Disable a CFEngine Enterprise daemon component persistently.

`DAEMON` can be one of `cf_execd`, `cf_monitord` or `cf_serverd`.

This will stop the AGENT from starting automatically.

### clear_persistent\_disable\_*DAEMON*

**Description:** Re-enable a previously disabled CFEngine Enterprise daemon
component.

`DAEMON` can be one of `cf_execd`, `cf_monitord` or `cf_serverd`.

stdlib

[%CFEngine_include_markdown(../../masterfiles/README.md)%]
