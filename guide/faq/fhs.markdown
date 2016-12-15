---
layout: default
title: Why does cfengine install into /var/cfengine instead of following the FHS?
published: true
sorting: 90
tags: [FAQ, FHS ]
---

The Unix Filesystem Hierarchy Standard is a specification for standardizing
where files and directories get installed on a Unix-like system. When you
install CFEngine from source you can choose to build with FHS support, it places
all files in their expected locations. In addition, you may choose to follow
this standard in locating your master configuration and work areas.

CFEngine was introduced at about the same time as the FHS standard and since
cfengine 2.x, cfengine defaults to placing all components under `/var/cfengine`
(similar to `/var/cron`):

* `/var/cfengine`

* `/var/cfengine/bin`

* `/var/cfengine/inputs`

* `/var/cfengine/outputs`

Installing all components into the same sub-directory of `/var` is intended to
increase the probability that all components are on a *local* file system. This
agrees with the intention of the FHS as described in section 5.1 of the FHS-2.3.
The location of this workspace is configurable, but the default is determined by
backward compatibility. In other words, particular distributions may choose to
use a different location, and some do.

References:
- https://lists.gnu.org/archive/html/help-cfengine/2004-09/msg00181.html
- https://groups.google.com/d/msg/help-cfengine/q9jVopHatXI/M8asmeAWTxQJ
