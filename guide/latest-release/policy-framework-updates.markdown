---
layout: default
title: Policy Framework Updates
published: true
sorting: 40
tags: [releases, latest release, platforms, versions, what's new]
---

## CFEngine Policy Framework Updates for {{site.cfengine.branch}} ##

If you follow the CFEngine masterfiles policy framework (the masterfiles you
get out of the box) we encourage you to upgrade the policy framework each time
you upgrade CFEngine. We recommend making as few changes as possible to the
shipped masterfiles to make these upgrades as painless as possible. Generally
the best way to accomplish that is to take your custom policy and integrate it
on top of the new masterfiles.

{{site.cfengine.branch}} introduces some minor re-orginization of policy, and some new
features aimed at making policy framework upgrades easier.

Please consult [The Policy Framework] for a map to the policy framework.

## What is new in the {{site.cfengine.branch}} masterfiles policy framework ##

## CHANGELOG.md
[%CFEngine_include_markdown(masterfiles/CHANGELOG.md)%]

## Makefile

The masterfiles now installs in the traditional UNIX way
using autotools. For example to install it under `/my/path/to/masterfiles`,
you should unpack it and do the following:

```console
./configure --prefix=/my/path/to
make install
```

## def.json

Many featues previously enabled in `def.cf` can now be enabled via this
external data file. The benefit is fewer modifications to the policy framework
that need to be worked out during policy framework upgrades.
