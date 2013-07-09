---
layout: default
title: ifelse
categories: [Reference, Functions, ifelse]
published: true
alias: reference-functions-ifelse.html
tags: [reference, data functions, functions, ifelse]
---

[%CFEngine_function_prototype(...)%]

**Description:** Evaluate each pair of arguments up to the last one as a (`class`, `value`) tuple, returning `value` if `class` is set.

If none are set, returns the last argument.

**Arguments**:

The `ifelse` function is like a multi-level if-else statement.It was
inspired by Oracle's `DECODE` function. It must have an odd number of
arguments (from 1 to N). The last argument is the default value, like
the `else` clause in standard programming languages. Every pair of
arguments before the last one are evaluated as a pair. If the first
one evaluates true (as if you had used it in a class `expression`, so
it can be more than just a class name, it's a whole context like
`Tuesday.linux.!verbose`) then the second one is returned.

Generally, if `ifelse` were called with arguments `(a1, a2, b1,
b2, c)`, the behavior expressed as pseudo-code is:

```
    if a1 then return a2
    else-if b1 then return b2
    else return c
```

(But again, note that any odd number of arguments is supported.)

The `ifelse` function is extremely useful when you want to avoid
explicitly stating the negative of all the expected cases; this
problem is commonly seen like so:

```cf3
    class1.class2::
      "myvar" string => "x";

    class3.!class2::
      "myvar" string => "y";

    !((class1.class2)||class3.!class2)::
      "myvar" string => "z";
```

That's hard to read and error-prone (do you know how `class2` will
affect the default case?).  Here's the alternative with `ifelse`:

```cf3
    "myvar" string => ifelse("class1.class2", "x",
                             "class3.!class2", "y",
                             "z");
```

**Example:**

```cf3
bundle agent example
{     
  classes:
      "myclass" expression => "any";
      "myclass2" expression => "any";
      "secondpass" expression => "any";
  vars:
      # we need to use the secondpass class because on the first pass,
      # myclass and myclass2 are not defined yet

    secondpass::

      # result: { "1", "single string parameter", "hardclass OK", "bundle class OK", "5 parameters OK" }

      "mylist" slist => {
                          ifelse(1),
                          ifelse("single string parameter"),
                          ifelse("cfengine", "hardclass OK", "hardclass broken"),
                          ifelse("myclass.myclass2", "bundle class OK", "bundle class broken"),
                          ifelse("this is not true", "5 parameters broken",
                                 "this is also not true", "5 parameters broken 2",
                                 "5 parameters OK"),
                        };

  reports:
      "ifelse result list: $(mylist)";
}
```
