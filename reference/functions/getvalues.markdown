---
layout: default
title: getvalues
categories: [Reference, Functions, getvalues]
published: true
alias: reference-functions-getvalues.html
tags: [reference, data functions, functions, getvalues]
---

[%CFEngine_function_prototype(array)%]

**Description:** Returns the list of values in `array`.

If the array contains list values, then all of the list elements are flattened 
into a single list to make the return value a list.

Make sure you specify the correct scope when supplying the name of the
variable.

[%CFEngine_function_attributes(array)%]

**Example:**

```cf3
bundle agent example
{
vars:

  "v[index_1]" string => "value_1";
  "v[index_2]" string => "value_2";

  "values" slist => getvalues("v");

reports:
   "Found values: $(values)";

}
```

**Notes:**
