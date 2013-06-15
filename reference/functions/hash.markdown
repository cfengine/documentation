---
layout: default
title: hash
categories: [Reference, Functions, hash]
published: true
alias: reference-functions-hash.html
tags: [reference, data functions, functions, hash]
---

**Prototype:** `hash(input, algorithm)`

**Return type:** `string`

**Description:** Return the hash of `input` using the hash `algorithm`.

Hash functions are extremely sensitive to input. You should not expect
to get the same answer from this function as you would from every other
tool, since it depends on how whitespace and end of file characters are
handled.

**Arguments**:

* `input` : Input text, in the range `.*`
* `algorithm` : Hash or digest algorithm, one of
  * md5
  * sha1
  * sha256
  * sha512
  * sha384
  * crypt   

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

