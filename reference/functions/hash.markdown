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

      "md5" string => hash("Cfengine is not cryptic","md5");
      "sha256" string => hash("Cfengine is not cryptic","sha256");
      "sha384" string => hash("Cfengine is not cryptic","sha384");
      "sha512" string => hash("Cfengine is not cryptic","sha512");

  reports:

      "Hashed to: md5 $(md5)";
      "Hashed to: sha256 $(sha256)";
      "Hashed to: sha384 $(sha384)";
      "Hashed to: sha512 $(sha512)";

}
```

