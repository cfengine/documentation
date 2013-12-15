---
layout: default
title: upcase
categories: [Reference, Functions, upcase]
published: true
alias: reference-functions-upcase.html
tags: [reference, text functions, functions, text, case, upcase]
---

[%CFEngine_function_prototype(data)%]

**Description:** Returns `data` in uppercase.

[%CFEngine_function_attributes(data)%]

**Example:**

```cf3
body common control
{
      bundlesequence => { "example" };
}

bundle agent example
{
  vars:

      "upcase" string =>  upcase("abc"); # will contain "ABC"
  reports:
      "upcased abc: $(upcase)";
}
```

Output:

```
R: upcased abc: ABC
```

**History:** Introduced in CFEngine 3.6

**See also:** `downcase()`.
