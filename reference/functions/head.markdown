---
layout: default
title: head
categories: [Reference, Functions, head]
published: true
alias: reference-functions-head.html
tags: [reference, text functions, functions, text, head, substring]
---

[%CFEngine_function_prototype(data, max)%]

**Description:** Returns the first `max` bytes of `data`.

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

      "start" string =>  head("abc", "1"); # will contain "a"
  reports:
      "start of abc = $(start)";

}
```

Output:

```
R: start of abc = a
```

**History:** Introduced in CFEngine 3.6

**See also:** `tail()`, `strlen()`, `reversestring()`.
