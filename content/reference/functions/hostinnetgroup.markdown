---
layout: default
title: hostinnetgroup
aliases:
  - "/reference-functions-hostinnetgroup.html"
---

{{< CFEngine_function_prototype(netgroup) >}}

**Description:** True if the current host is in the named `netgroup`.

{{< CFEngine_function_attributes(netgroup) >}}

**Example:**

```cf3 {skip TODO}
classes:

  "ingroup" expression => hostinnetgroup("my_net_group");
```
