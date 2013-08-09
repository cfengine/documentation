---
layout: default
title: none
categories: [Reference, Functions, none]
published: true
alias: reference-functions-none.html
tags: [reference, data functions, functions, none]
---

[%CFEngine_function_prototype(regex, list)%]

**Description:** Returns whether no element in `list` matches the regular 
expression `regex`.

[%CFEngine_function_attributes(regex, list)%]

The regular expression is [unanchored][unanchored].

**Example:**

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

**See also:** [`filter()`][filter], [`every()`][every], and [`some()`][some].
