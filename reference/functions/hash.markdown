---
layout: default
title: hash
categories: [Reference, Functions, hash]
published: true
alias: reference-functions-hash.html
tags: [reference, data functions, functions, hash]
---

[%CFEngine_function_prototype(input, algorithm)%]

**Description:** Return the hash of `input` using the hash `algorithm`.

Hash functions are extremely sensitive to input. You should not expect
to get the same answer from this function as you would from every other
tool, since it depends on how whitespace and end of file characters are
handled.

[%CFEngine_function_attributes(input, algorithm)%]

**Example:**

```cf3
bundle agent example

{     
vars:

  "md5" string => hash("CFEngine is not cryptic","md5");

reports:
    "Hashed to: $(md5)";
}
```

