---
layout: default
title: Functions
published: true
sorting: 30
tags: [Reference, Functions]
---

Functions take zero or more values as arguments and return a value.
Argument values need to be of the type and range as documented for each
function. Some functions are documented with a `...`, in which case they
take an arbitrary amount of arguments.

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

During convergence, CFEngine's evaluation model will evaluate
functions multiple times, which can be a performance concern.

Some _system_ functions are particularly expensive:

* `execresult()` and `returnszero()` for shell execution
* `regldap()`, `ldapvalue()`, `ldaparray()`, and `ldaplist()` for LDAP queries
* `host2ip()` and `ip2host()` for DNS queries
* `readtcp()` for TCP interactions
* `hubknowledge()`, `selectservers()`, `remoteclassesmatching()`, and `remotescalar()` for hub queries

As of 3.6.0, the new `cache_system_functions` body common argument is
set to `true` by default and CFEngine's evaluator will use it.
Although you can override it to `false`, in practice you should almost
never need to do so.  The effect of having it `true` (the default) is
that the expensive _system_ functions will be run just once and then
their result will be cached.

Note that caching is per-process so results will not be cached between
runs of e.g. `cf-agent` and `cf-promises`.

## Function Skipping

If a variable passed to a function is unable to be resolved the function will
be skipped. The function will be evaluated during a later pass when all
variables passed as arguments are able to be resolved. The function will never
be evaluated if any argument contains a variable that never resolves.

### Collecting Functions

Some function arguments are marked as *collecting* which means they
can "collect" an argument from various sources. The data is normalized
into the JSON format internally, so all of the following data types
have consistent behavior.

* If a key inside a data container is specified (`mycontainer[key]`),
the value under that key is collected. The key can be a string for
JSON objects or a number for JSON arrays.

* If a single data container, CFEngine array, or slist is specified
(`mycontainer` or `myarray` or `myslist`), the contents of it are
collected.

* If a single data container, CFEngine array, or slist is specified
with `@()` around it (`@(mycontainer)` or `@(myarray)` or
`@(myslist)`), the contents of it are collected.

* If a function call that returns a data container or slist is
  specified, that function call is evaluated and the results are
  inserted, so you can say for instance `sort(data_expand(...), "lex")`
  to expand a data container then sort it.

* If a list (slist, ilist, or rlist) is named, its entries are collected.

* If any CFEngine "classic" array (`array[key]`) is named, it's first
converted to a JSON key-value map, then collected.

* If a literal JSON string like `[ 1,2,3 ]` or `{ "x": 500 }` is
provided, it will be parsed and used.

* If any of the above-mentioned ways to reference variables are used
**inside** a literal JSON string they will be expanded (or the
function call will fail). This is similar to the behavior of
Javascript, for instance.  For example, `mergedata('[ thing, { "mykey": otherthing[123] } ]')`
will wrap the `thing` in a JSON array; then the contents of
`otherthing[123]` will be wrapped in a JSON map which will also go in
the array.

### Delayed Evaluation Functions

Since CFEngine 3.10, some functions are marked as *delayed evaluation* which
means they can evaluate a function call across every element of a collection.
This makes intuitive sense for the collection traversing functions `maparray()`,
`maplist()`, and `mapdata()`.

The practical use is for instance `maplist(format("%03d", $(this)), mylist)`
which will evaluate that `format()` call once for every element of `mylist`.

Before 3.10, the same call would have resulted in running the `format()`
function **before** the list is traversed, which is almost never what the user
wants.

## List of all functions

There are a large number of functions built into CFEngine. The following
tables might make it easier for you to find the function you need.

[%CFEngine_function_table()%]
