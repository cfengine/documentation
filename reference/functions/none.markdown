---
layout: default
title: none
categories: [Reference, Functions, none]
published: true
alias: reference-functions-none.html
tags: [reference, functions, none]
---

**Prototype**: `none(arg1, arg2)`

**Return type**: `class`

* `arg1` : Unanchored regular expression to find, *in the range* .\*
* `arg2` : The name of the list variable to check, *in the range*
[a-zA-Z0-9\_\$(){}\\[\\].:]+

Return true if no element of the list matches the regular expression.

**Example**:

```cf3
bundle agent test

{
  classes:
      "none1" expression => none("jebadiah", "test");
      "none2" expression => none("2", "test");

  vars:
      "test" slist => {
                        1,2,3,
                        "one", "two", "three",
                        "long string",
                        "four", "fix", "six",
                        "one", "two", "three",
                      };

  reports:
      "The test list is $(test)";
    none1::
      "none() test 1 passed";
    !none1::
      "none() test 1 failed";
    none2::
      "none() test 2 failed";
    !none2::
      "none() test 2 passed";
}
```

**Notes**:  
   
See also `filter`, `every`, and `some`.

The regular expression is unanchored.
