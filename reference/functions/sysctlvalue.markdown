---
layout: default
title: sysctlvalue
published: true
tags: [reference, system functions, functions, sysctl, sysctlvalue]
---

[%CFEngine_function_prototype(key)%]

**Description:** Returns the sysctl value of `key` using `/proc/sys`.

[%CFEngine_function_attributes(key)%]

**Example:**

```cf3
    vars:
      "tested" slist => { "net.ipv4.tcp_mem", "net.unix.max_dgram_qlen" };
      "values[$(tested)]" string => sysctlvalue($(tested));
```

Output:

```
  "values[net.ipv4.tcp_mem]" = "383133\t510845\t766266"
  "values[net.unix.max_dgram_qlen]" = "512"
```

**Notes:**

**History:** Was introduced in version 3.11.0 (2017)

**See also:** `data_sysctlvalues()`
