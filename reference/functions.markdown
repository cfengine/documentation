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

In addition, functions with return type `class` evaluate to `true` or `false`. 
The class on the left-hand side is set if the function evaluates to true. If 
the function evaluates to false, then the class remains unchanged.

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

There are a large number of functions built into CFEngine, and finding
the right one to use can be a daunting task. The following tables are
might make it easier for you to find the function you need.

## List of all functions

[%CFEngine_function_table()%]
