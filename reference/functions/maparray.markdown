---
layout: default
title: maparray
categories: [Reference, Functions, maparray]
published: true
alias: reference-functions-maparray.html
tags: [reference, functions, maparray]
---

**Prototype**: maparray(arg1,arg2) 

**Return type**: `slist`

* `arg1` : Pattern based on \$(this.k) and \$(this.v) as original text, *in the range* .\*
* `arg2` : The name of the array variable to map, *in the range*
[a-zA-Z0-9\_\$(){}\\[\\].:]+

Return a list with each element modified by a pattern based on \$(this.k) and \$(this.v)

**Example**:

```cf3
body common control
{
      bundlesequence => { run };
}

bundle agent run
{
  vars:
      "todo[1]" string => "2";
      "todo[one]" string => "two";
      "todo[3999]" slist => { "big", "small" };
      "map" slist => maparray("yes $(this.k) $(this.v)", "todo");

  reports:
    cfengine::
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

**Notes**:  

The `this.k` and `this.v` variables will be available for expansion in
the string scope, similar to the way `this` is available for
`maplist`.

If a value in the array is an slist, you'll get one result for each
value (implicit looping).

The order of the array keys is not guaranteed.  Use the `sort`
function if you need order in the resulting output.
