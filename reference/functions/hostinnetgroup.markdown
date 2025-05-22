---
layout: default
title: hostinnetgroup
date: 2025-05-22T00:00:00+00:00
---

[%CFEngine_function_prototype(netgroup)%]

**Description:** True if the current host is in the named `netgroup`.

[%CFEngine_function_attributes(netgroup)%]

**Example:**

```cf3
classes:

  "ingroup" expression => hostinnetgroup("my_net_group");
```
