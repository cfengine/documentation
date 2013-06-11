---
layout: default
title: none
categories: [Reference, Functions, none]
published: true
alias: reference-functions-none.html
tags: [reference, functions, none]
---

**Prototype**: `none(regex, list)`

**Return type**: `class`

**Description**: Returns whether no element in `list` matches the regular 
expression `regex`.

**Arguments**:

* `regex` : [Unanchored][unanchored] regular expression to find, in the range `.*`
* `list` : The name of the list variable to check, in the range
`[a-zA-Z0-9_$(){}\[\].:]+`

**Example**:

```cf3
bundle agent example
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

**See also**: [`filter()`][filter], [`every()`][every], and [`some()`][some].
