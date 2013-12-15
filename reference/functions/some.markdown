---
layout: default
title: some
categories: [Reference, Functions, some]
published: true
alias: reference-functions-some.html
tags: [reference, data functions, functions, some]
---

[%CFEngine_function_prototype(regex, list)%]

**Description:** Return whether any element of `list` matches the 
[Unanchored][unanchored] regular expression `regex`.

[%CFEngine_function_attributes(regex, list)%]

**Example:**

```cf3
body common control
{
      bundlesequence => { "test" };
}

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
R: some() test 1 passed
R: some() test 2 passed
```

**See also:** [`filter()`][filter], [`every()`][every], and [`none()`][none].
