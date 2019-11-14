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

They can return scalar (string|int|real|bool), list (slist, ilist, rlist) and data values:

[%CFEngine_include_example(function-return-types.cf)%]

### Boolean return type

Functions which return `boolean`, technically return a string `any` or `!any`.
This is for compatibility with other functions and promise attributes which
expect class expressions.

Normally, you don't need to worry about this, you use the function call to
define classes, and use classes instead of boolean values:

```cf3
bundle agent main
{
  vars:
      "five" int => "5";
  classes:
      "is_var" if => isvariable("five");
  reports:
    is_var::
      "Success!";
}
```

There is no boolean data type for `vars` promises.
If you want to store or print the class expression, you can use `concat()`:

```cf3
bundle agent main
{
  vars:
      "five" int => "5";
      "expression" string => concat(isvariable("five"));
  classes:
      "is_var" if => "$(expression)"; # Will be expanded and evaluated
  reports:
    is_var::
      "Success: expression expanded to '$(expression)' and evaluated to true!";
}
```

**Note:** the truth of a class expression or the result of a function call may
change during evaluation, but typically, a class, once defined, will stay defined.

**See also:** [persistence in classes and decisions][Classes and Decisions#persistence]

### Promise attributes and function calls

Promise attributes which use a class expression (string) as input, like `if`
and `unless`, can take a function call which returns string or boolean as well.

* A boolean function will be resolved to `any`, which is always true, or `!any`
  which is always false.
* A string function will be resolved, and the returned string will be
  evaluated as a class expression.

```cf3
bundle agent main
{
  vars:
      "five" int => "5";
      "is_var_class_expression" string => concat(isvariable("$(five)"));
  classes:
      "five_less_than_seven" expression => islessthan("$(five)", 7);
      "five_is_variable" if => "$(is_var_class_expression)";
  reports:
    any::
      "five: $(five)";
      "is_var_class_expression: $(is_var_class_expression)";
    five_less_than_seven::
      "$(five) is smaller than 7";
}
```

### Function caching

During convergence, CFEngine's evaluation model will evaluate
functions multiple times, which can be a performance concern.

Some _system_ functions are particularly expensive:

{% comment %}

It would be nice if we could get this list of cached functions automatically.
This is how you can dive into the code to determine which functions are cached.

git grep -B1 FNCALL_OPTION_CACHED | awk -F'"' '/FnCallTypeNew/ {print $2}'

{% endcomment %}

* `execresult()` and `returnszero()` for shell execution
* `regldap()`, `ldapvalue()`, and `ldaplist()` for LDAP queries
* `findprocesses()`, and `processexists()` for querying processes.
* `host2ip()` and `ip2host()` for DNS queries
* `readtcp()` for TCP interactions
* `hubknowledge()`, and `remotescalar()` for hub queries

When enabled
[cached functions](https://docs.cfengine.com/docs/{{site.cfengine.branch}}/search.html?q=The+return+value+is+cached)
are **not executed on every pass of convergence**. Instead, the function will
only be executed once during the
[agent evaluation step][Normal Ordering#Agent evaluation step]
and its result will be cached until the end of that agent execution.

**Note:** Function caching is *per-process*, so results will not be cached between
separate components e.g. `cf-agent`, `cf-serverd` and `cf-promises`.
Additionally functions are cached by hashing the function arguments. If you have
the exact same function call in two different promises (it does not matter if
they are in the same bundle or not) only the first executed function will be
cached. That cached result will be re-used for other identical function
occurrences.

Function caching can be disabled by setting `cache_system_functions` in body
common control to `false`.

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
