---
layout: default
title: hash
categories: [Reference, Functions, hash]
published: true
alias: reference-functions-hash.html
tags: [reference, functions, hash]
---

**Prototype**: hash(arg1,arg2) 

**Return type**: `string`

 *arg1* : Input text, *in the range* .\*   
 *arg2* : Hash or digest algorithm, *in the range*
md5,sha1,sha256,sha512,sha384,crypt   

Return the hash of arg1, type arg2 and assign to a variable

**Example**:

```cf3

body common control

{
bundlesequence  => { "example" };
}

###########################################################

bundle agent example

{     
vars:

  "md5" string => hash("CFEngine is not cryptic","md5");

reports:

  Yr2008::

    "Hashed to: $(md5)";

}
```

**Notes**:
Hash functions are extremely sensitive to input. You should not expect
to get the same answer from this function as you would from every other
tool, since it depends on how whitespace and end of file characters are
handled.

Valid hash types (depending on availablity) include: `md5`, `sha1`,
`sha256`, `sha512` ,`sha384`, `crypt`.
