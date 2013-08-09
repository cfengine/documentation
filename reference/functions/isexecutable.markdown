---
layout: default
title: isexecutable
categories: [Reference, Functions, isexecutable]
published: true
alias: reference-functions-isexecutable.html
tags: [reference, files functions, functions, isexecutable]
---

[%CFEngine_function_prototype(filename)%]

**Description:** Returns whether the named object `filename` has execution rights for the current user.

[%CFEngine_function_attributes(filename)%]

**Example:**

```cf3
classes:

  "yes" expression => isexecutable("/bin/ls");
```

**History:** Was introduced in version 3.1.0b1,Nova 2.0.0b1 (2010)
