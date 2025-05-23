---
layout: default
title: classify
date: 2025-05-22T00:00:00+00:00
---

[%CFEngine_function_prototype(text)%]

**Description:** Returns whether the canonicalization of `text` is a currently
set class.

This is useful for transforming variables into classes.

[%CFEngine_function_attributes(text)%]

**Example:**

```cf3
classes:

 "i_am_the_policy_host" expression => classify("master.example.org");
```

**See also:** [canonify()][canonify], [classmatch()][classmatch], [classesmatching()][classesmatching]
