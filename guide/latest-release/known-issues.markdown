---
layout: default
title: Known Issues
sorting: 50
published: true
tags: [overviews, releases, latest release, 3.6, platforms, versions, known issues]
---

CFEngine defects are managed in our [bug tracker][bug tracker]. Please report
bugs or unexpected behavior there, following the documented guideline for new
bug reports.

The items below highlight issues that require additional awareness when starting
with CFEngine or when upgrading from a previous version.

* `cf-promises --show-classes` and `cf-promises --show-vars` will only show classes and variables found on a first pass through the policy, since `cf-promises` does not evaluate agent promises.
* the CFEngine protocol versions 1 and 2 are incompatible (the latter is based on TLS).  You must migrate your entire site to 3.6 **or** run a second policy server **or** arrange for an alternate policy distribution method when the policy server is not available.

