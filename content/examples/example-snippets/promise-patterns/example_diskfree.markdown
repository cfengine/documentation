---
layout: default
title: Check filesystem space
reviewed: 2013-06-08
reviewed-by: atsaloli
---

Check how much space (in KB) is available on a directory's current partition.

{{< CFEngine_include_example(diskfree.cf) >}}

Example output:

```command
cf-agent -f unit_diskfree.cf
```

```output
R: Freedisk 48694692
```

```command
df -k /tmp
```

```output
Filesystem     1K-blocks     Used Available Use% Mounted on
/dev/sda1      149911836 93602068  48694692  66% /
```
