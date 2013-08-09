---
layout: default
title: regarray
categories: [Reference, Functions, regarray]
published: true
alias: reference-functions-regarray.html
tags: [reference, data functions, functions, regarray]
---

[%CFEngine_function_prototype(array, regex)%]

**Description:** Returns whether `array` contains elements matching the
[anchored][anchored]regular expression `regex`.

[%CFEngine_function_attributes(array, regex)%]

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
