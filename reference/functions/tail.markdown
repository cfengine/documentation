---
layout: default
title: tail
categories: [Reference, Functions, tail]
published: true
alias: reference-functions-tail.html
tags: [reference, text functions, functions, text, tail, substring]
---

[%CFEngine_function_prototype(data, max)%]

**Description:** Returns the last `max` bytes of `data`.

[%CFEngine_function_attributes(data, max)%]

**Example:**

```cf3
body common control
{
      bundlesequence => { "example" };
}

bundle agent example
{
  vars:

      "end" string =>  tail("abc", "1"); # will contain "c"
  reports:
      "end of abc = $(end)";

}
```

Output:

```
R: end of abc = c
```

**History:** Introduced in CFEngine 3.6

**See also:** `head()`, `strlen()`, `reversestring()`.
