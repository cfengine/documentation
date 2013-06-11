---
layout: default
title: some
categories: [Reference, Functions, some]
published: true
alias: reference-functions-some.html
tags: [reference, functions, some]
---

**Prototype**: `some(regex, list)`

**Return type**: `class`

**Description:** Return whether any element of the list matches the regular 
expression.

**Arguments**:

* `regex` : [Unanchored][unanchored] regular expression to find, in the range `.*`
* `list` : The name of the list variable to check, in the range
`[a-zA-Z0-9_$(){}\[\].:]+`

**Example:**

```cf3
    bundle agent test
    {
      classes:
          "some1" expression => some("long string", "test");
          "some2" expression => some("none", "test");

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
        some1::
          "some() test 1 passed";
        !some1::
          "some() test 1 failed";
        some2::
          "some() test 2 failed";
        !some2::
          "some() test 2 passed";
    }
```

**See also:** [`filter()`][filter], [`every()`][every], and [`none()`][none].
