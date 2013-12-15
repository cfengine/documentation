---
layout: default
title: every
categories: [Reference, Functions, every]
published: true
alias: reference-functions-every.html
tags: [reference, data functions, functions, every]
---

[%CFEngine_function_prototype(regex, list)%]

**Description:** Returns whether every element in the variable `list` matches
the [unanchored][unanchored] `regex`.

**Arguments**:

* `regex` : Regular expression to find, in the range `.*`

* `list` : The name of the list variable to check, in the range
`[a-zA-Z0-9_$(){}\[\].:]+`

**Example:**

```cf3
body common control
{
      bundlesequence => { "test" };
}

bundle agent test

{
  classes:
      "every1" expression => every(".*", "test");
      "every2" expression => every(".", "test");

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
    every1::
      "every() test 1 passed";
    !every1::
      "every() test 1 failed";
    every2::
      "every() test 2 failed";
    !every2::
      "every() test 2 passed";
}
```

Output:

```
R: The test list is 1
R: The test list is 2
R: The test list is 3
R: The test list is one
R: The test list is two
R: The test list is three
R: The test list is long string
R: The test list is four
R: The test list is fix
R: The test list is six
R: every() test 1 passed
R: every() test 2 passed
```

**See also:** [`filter()`][filter], [`some()`][some], and [`none()`][none].
