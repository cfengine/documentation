---
layout: default
title: reversestring
categories: [Reference, Functions, reversestring]
published: true
alias: reference-functions-reversestring.html
tags: [reference, text functions, functions, text, reverse, reversestring]
---

[%CFEngine_function_prototype(data)%]

**Description:** Returns `data` reversed.

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

      "reversed"

      string =>  reversestring("abc"); # will contain "cba"
  reports:
      "reversed abs = $(reversed)";
}
```

Output:

```
R: reversed abs = cba
```

**History:** Introduced in CFEngine 3.6

**See also:** `head()`, `tail()`, `strlen()`.
