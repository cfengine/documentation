---
layout: default
title: data_sysctlvalues
published: true
tags: [reference, system functions, functions, sysctl, data_sysctlvalues]
---

[%CFEngine_function_prototype()%]

**Description:** Returns all sysctl values using `/proc/sys`.

[%CFEngine_function_attributes()%]

**Example:**

```cf3
    vars:
      "sysctl" data => data_sysctlvalues(); # get everything!
```

Output:

```
{
  "sysctl": {
  ...
    "net.unix.max_dgram_qlen": "512",
  ...
  }
```

**Notes:**

**History:** Was introduced in version 3.11.0 (2017)

**See also:** `sysctlvalue()`
