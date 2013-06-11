---
layout: default
title: getusers
categories: [Reference, Functions, getusers]
published: true
alias: reference-functions-getusers.html
tags: [reference, system functions, functions, getusers]
---

**Prototype:** `getusers(exclude_names, exclude_ids)`

**Return type:** `slist`

**Description:** Returns a list of all users defined, except those names in `exclude_names` and uids in `exclude_ids`

**Arguments**:

* `exclude_names` : Comma separated list of User names, in the range `.*`
* `exclude_ids` : Comma separated list of UserID numbers, in the range `.*`

**Example:**

```cf3
    vars:
      "allusers" slist => getusers("zenoss,mysql,at","12,0");

    reports:

     linux::

      "Found user $(allusers)";
```

**Notes:**
This function is currently only available on Unix-like systems.

**History:** Was introduced in version 3.1.0b1,Nova 2.0.0b1 (2010).

