---
layout: default
title: getvalues
categories: [Reference, Functions, getvalues]
published: true
alias: reference-functions-getvalues.html
tags: [reference, functions, getvalues]
---

**Prototype**: `getvalues(array)`

**Return type**: `slist`

**Description**: Returns the list of values in `array`.

If the array contains list values, then all of the list elements are flattened 
into a single list to make the return value a list.

Make sure you specify the correct scope when supplying the name of the
variable.

**Arguments**:

* `array` : array identifier, *in the range* [a-zA-Z0-9\_\$(){}\\[\\].:]+

**Example**:

```cf3
bundle agent example
{
vars:

  "v[index_1]" string => "value_1";
  "v[index_2]" string => "value_2";

  "values" slist => getvalues("v");

reports:

  Yr2008::

   "Found values: $(values)";

}
```

**Notes**:
