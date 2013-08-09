---
layout: default
title: maplist
categories: [Reference, Functions, maplist]
published: true
alias: reference-functions-maplist.html
tags: [reference, data functions, functions, maplist]
---

[%CFEngine_function_prototype(pattern, list)%]

**Description:** Return a list with each element in `list` modified by a 
pattern.

The `$(this)` variable expands to the currently processed entry from `list`. 
This is essentially like the map() function in Perl, and applies to
lists.

[%CFEngine_function_attributes(pattern, list)%]

**Example:**

```cf3
bundle agent test
{
vars:

  "oldlist" slist => { "a", "b", "c" };
  "newlist" slist => maplist("Element ($(this))","oldlist");

reports:
  "Transform: $(newlist)";
}
```

**History:** Was introduced in 3.3.0, Nova 2.2.0 (2011)
