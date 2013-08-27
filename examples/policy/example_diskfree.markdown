---
layout: default
title: Check filesystem space
categories: [Examples, Policy, Check filesystem space]
published: true
alias: examples-policy-check-filesystem-space.html
tags: [Examples, Policy, check, filesystem]
reviewed: 2013-06-08
reviewed-by: atsaloli
---

Check how much space (in KB) is available on a directory's current partition.

[%CFEngine_include_example(diskfree.cf)%]

Example output:

```
# cf-agent -f unit_diskfree.cf
R: Freedisk 48694692
# df -k /tmp
Filesystem     1K-blocks     Used Available Use% Mounted on
/dev/sda1      149911836 93602068  48694692  66% /
# 
```
