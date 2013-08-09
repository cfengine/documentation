---
layout: default
title: hostinnetgroup
categories: [Reference, Functions, hostinnetgroup]
published: true
alias: reference-functions-hostinnetgroup.html
tags: [reference, system functions, functions, hostinnetgroup]
---

[%CFEngine_function_prototype(netgroup)%]

**Description:** True if the current host is in the named `netgroup`.

[%CFEngine_function_attributes(netgroup)%]

**Example:**

```cf3
    classes:

      "ingroup" expression => hostinnetgroup("my_net_group");
```
