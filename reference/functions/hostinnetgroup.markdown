---
layout: default
title: hostinnetgroup
categories: [Reference, Functions, hostinnetgroup]
published: true
alias: reference-functions-hostinnetgroup.html
tags: [reference, system functions, functions, hostinnetgroup]
---

**Prototype:** `hostinnetgroup(netgroup)`

**Return type:** `class`

**Description:** True if the current host is in the named `netgroup`.

**Arguments**:

* `netgroup` : Netgroup name, in the range `.*`

**Example:**

```cf3
    classes:

      "ingroup" expression => hostinnetgroup("my_net_group");
```
