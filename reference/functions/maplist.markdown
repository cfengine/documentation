---
layout: default
title: maplist
categories: [Reference, Functions, maplist]
published: true
alias: reference-functions-maplist.html
tags: [reference, functions, maplist]
---

**TODO: formulation confusing**

**Prototype**: `maplist(pattern, list)`

**Return type**: `slist`

**Description**: Return a list with each element in `list` modified by a 
pattern based on $(this).

This is essentially like the map() function in Perl, and applies to
lists.

**Arguments**:

* `pattern` : Pattern based on \$(this) as original text, *in the range* .\*
* `list` : The name of the list variable to map, *in the range*
[a-zA-Z0-9\_\$(){}\\[\\].:]+

**Example**:

```cf3
bundle agent test
{
vars:

  "oldlist" slist => { "a", "b", "c" };
  "newlist" slist => maplist("Element ($(this))","oldlist");

reports:
 linux::
  "Transform: $(newlist)";
}
```

**History**: Was introduced in 3.3.0, Nova 2.2.0 (2011)
