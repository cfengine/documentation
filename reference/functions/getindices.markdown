---
layout: default
title: getindices
categories: [Reference, Functions, getindices]
published: true
alias: reference-functions-getindices.html
tags: [reference, functions, getindices]
---

**Prototype**: `getindices(array)`

**Return type**: `slist`

**Description:** Returns a list of keys in `array`.

Make sure you specify the correct scope when supplying the name of the
variable.

**Arguments**:

* `array` : array identifier, in the range
`[a-zA-Z0-9_$(){}\[\].:]+`

**Example:**

```cf3
bundle agent example
{
vars:

  "v[index_1]" string => "value_1";
  "v[index_2]" string => "value_2";

  "parameter_name" slist => getindices("v");

reports:

  Yr2008::

   "Found index: $(parameter_name)";

}
```
