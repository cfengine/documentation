---
layout: default
title: now
published: true
tags: [reference, system functions, functions, now]
---

[%CFEngine_function_prototype()%]

**Description:** Return the time at which this agent run started
in system representation.

In order to provide an immutable environment against which to converge,
this value does not change during the execution of an agent.

**Example:**

```cf3
    body file_select zero_age
    {
      mtime       => irange(ago(1,0,0,0,0,0),now);
      file_result => "mtime";
    }
```
