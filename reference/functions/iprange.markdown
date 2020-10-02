---
layout: default
title: iprange
published: true
tags: [reference, communication functions, functions, iprange]
---

[%CFEngine_function_prototype(range, interface)%]

**Description:** Returns whether the current host lies in the range of
IP addresses specified, optionally checking only `interface`.

Pattern matching based on IP addresses.

[%CFEngine_function_attributes(range, interface)%]

**Example:**

```cf3
bundle agent example
{
classes:

  "dmz_1" expression => iprange("128.39.89.10-15");
  "lab_1" expression => iprange("128.39.74.1/23");

  "dmz_1_eth0" expression => iprange("128.39.89.10-15", "eth0");
  "lab_1_eth0" expression => iprange("128.39.74.1/23", "eth0");

reports:

  dmz_1::

    "DMZ 1 subnet";

  lab_1::

    "Lab 1 subnet";
}
```

**See also:** `isipinsubnet()`, `host2ip()`, `ip2host()`

**History:** The optional `interface` parameter was introduced in CFEngine 3.9.

