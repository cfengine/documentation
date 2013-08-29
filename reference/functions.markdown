---
layout: default
title: Functions
categories: [Reference, Functions]
published: true
sorting: 30
alias: reference-functions.html
tags: [Reference, Functions]
---

Functions are parameterized "RVALUES". Parameter values need to be of the
type and range as documented for each functions. Some functions are documented
with a `...`, in which case they take an arbitrary amount of parameters.

They can return scalar and list values:

```cf3
    vars:
      "random" int => randomint("0", "100");
      "list" slist => readstringlist("/tmp/listofstring", "#.*", "\s", 10, 400);
```

In addition, functions with return type `boolean` evaluate to `true` or 
`false`. The class on the left-hand side is set if the function evaluates to 
true. If the function evaluates to false, then the class remains unchanged.

```cf3
    bundle agent test
    {
    vars:
      "five" int => "5";
      "seven" " int => "7";
    classes:
      "ok" expression => islessthan("$(five)","$(seven)");

    reports:

      ok::
        "$(five) is smaller than $(seven)";

     !ok::
        "$(seven) is smaller than $(five)";

    }
```

**TODO:** document that the return value of functions that return true/false can be passed into class expressions (clists) or function parameters that expect a string.

## List of all functions

There are a large number of functions built into CFEngine. The following 
tables might make it easier for you to find the function you need.

[%CFEngine_function_table()%]
