---
layout: default
title: regextract
categories: [Reference, Functions, regextract]
published: true
alias: reference-functions-regextract.html
tags: [reference, data functions, functions, regextract]
---

[%CFEngine_function_prototype(regex, string, backref)%]

**Description:** Returns whether the [anchored][anchored] `regex` matches the 
`string`, and fills the array `backref` with back-references.

If there are any back reference matches from the regular expression, then the array will be populated with the values, in the manner:

```cf3
    $(backref[0]) = entire string
    $(backref[1]) = back reference 1, etc
```

[%CFEngine_function_attributes(regex, string, backref)%]

**Example:**

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

**History:** This function was introduced in CFEngine version 3.0.4
(2010)
