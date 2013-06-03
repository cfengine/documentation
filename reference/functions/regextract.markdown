---
layout: default
title: regextract
categories: [Reference, Functions, regextract]
published: true
alias: reference-functions-regextract.html
tags: [reference, functions, regextract]
---

**Prototype**: `regextract(regex, string, backref)`

**Return type**: `class`

**Description**: Returns whether `regex` matches the `string`, and fills the array `backref` with back-references.

If there are any back reference matches from the regular expression, then the array will be populated with the values, in the manner:

```cf3
    $(identifier[0]) = entire string
    $(identifier[1]) = back reference 1, etc
```

**Arguments**:

* `regex` : Regular expression, *in the range* .\*

A regular expression containing one or more parenthesized back
references. The regular expression is anchored, meaning it must match
the entire string

* `string` : Match string, *in the range* .\*
* `backref` : Identifier for back-references, *in the range*
[a-zA-Z0-9\_\$(){}\\[\\].:]+

**Example**:

```cf3
    bundle agent example
    {
    classes:

        # Extract regex backreferences and put them in an array

        "ok" expression => regextract(
                                     "xx ([^\s]+) ([^\s]+).* xx",
                                     "xx one two three four xx",
                                     "myarray"
                                     );
    reports:

     ok::

       "ok - \"$(myarray[0])\" = xx + \"$(myarray[1])\" + \"$(myarray[2])\" + .. + xx";
    }
```

**History**: This function was introduced in CFEngine version 3.0.4
(2010)
