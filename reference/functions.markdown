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

Underneath, CFEngine functions that return `boolean` will actually
return a context expression like `any` or `!any` which will then be
deemed true or false by the CFEngine evaluator.  Note the truth of a
context expression or the result of a function call may change during
evaluation, but a class, once defined, will stay defined.

Functions that return a `boolean` can thus sometimes be used in places
where a string is accepted as well, but this behavior is not clearly
defined or supported.  Use at your own discretion.

### Function caching

Some functions are expensive, especially `execresult` and
`returnszero` for shell execution and `ldapvalue` and friends for LDAP
queries.  CFEngine's evaluation model will evaluate functions multiple
times, which is a performance concern.

As of 3.6.0, the new `cache_system_functions` body common parameter is
set to `true` by default and CFEngine's evaluator will use it.
Although you can override it to `false`, in practice you should almost
never need to do so.  The effect of having it `true` (the default) is
that the expensive functions will be run just once and then their
result will be cached.

## List of all functions

There are a large number of functions built into CFEngine. The following 
tables might make it easier for you to find the function you need.

[%CFEngine_function_table()%]
