---
layout: default
title: isexecutable
categories: [Reference, Functions, isexecutable]
published: true
alias: reference-functions-isexecutable.html
tags: [reference, functions, isexecutable]
---

**Prototype**: `isexecutable(filaname)`

**Return type**: `class`

**Description**: Returns whether the named object `filename` has execution rights for the current user.

**Arguments**:

* `filename` : File object name, *in the range* "?(/.\*)

**Example**:

```cf3
classes:

  "yes" expression => isexecutable("/bin/ls");
```

**History**: Was introduced in version 3.1.0b1,Nova 2.0.0b1 (2010)
