---
layout: default
title: maparray
categories: [Reference, Functions, maparray]
published: true
alias: reference-functions-maparray.html
tags: [reference, data functions, functions, maparray]
---

[%CFEngine_function_prototype(pattern, array)%]

**Description:** Returns a list with each array element modified by a pattern.

The `$(this.k)` and `$(this.v)` variables expand to the key and value of the 
array element, similar to the way `this` is available for `maplist`.

If a value in the array is an `slist`, you'll get one result for each
value (implicit looping).

The order of the array keys is not guaranteed.  Use the `sort`
function if you need order in the resulting output.

[%CFEngine_function_attributes(pattern, array)%]

**Example:**

```cf3
bundle agent run
{
  vars:
      "todo[1]" string => "2";
      "todo[one]" string => "two";
      "todo[3999]" slist => { "big", "small" };
      "map" slist => maparray("yes $(this.k) $(this.v)", "todo");

  reports:
      "Hello $(map)";
}

```

Output:

```
Hello yes 1 2
Hello yes one two
Hello yes 3999 big
Hello yes 3999 small
```
