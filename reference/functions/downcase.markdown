---
layout: default
title: downcase
categories: [Reference, Functions, downcase]
published: true
alias: reference-functions-downcase.html
tags: [reference, text functions, functions, text, case, downcase]
---

[%CFEngine_function_prototype(data)%]

**Description:** Returns `data` in lower case.

[%CFEngine_function_attributes(data)%]

**Example:**

```cf3
    vars:

      "downcase"

         string =>  downcase("ABC"); # will contain "abc"
```

**History:** Introduced in CFEngine 3.6

**See also:** `upcase()`.
