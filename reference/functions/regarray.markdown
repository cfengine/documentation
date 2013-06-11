---
layout: default
title: regarray
categories: [Reference, Functions, regarray]
published: true
alias: reference-functions-regarray.html
tags: [reference, functions, regarray]
---

**Prototype**: `regarray(array, regex)`

**Return type**: `class`

**Description:** Returns whether `array` contains elements matching the
regular expression `regex`.

* `array` : array identifier, in the range
`[a-zA-Z0-9_$(){}\[\].:]+`
* `regex` : Regular expression, in the range `.*`

A regular expression to match the content. The regular expression is
anchored, meaning it must match the complete array element.

**Example:**

```cf3
    bundle agent example
    {
    vars:

      "myarray[0]" string => "bla1";
      "myarray[1]" string => "bla2";
      "myarray[3]" string => "bla";

    classes:

      "ok" expression => regarray("myarray","b.*2");

    reports:

     ok::

        "Found in list";

     !ok::

        "Not found in list";

    }
```
