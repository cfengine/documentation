---
layout: default
title: getindices
categories: [Reference, Functions, getindices]
published: true
alias: reference-functions-getindices.html
tags: [reference, data functions, functions, getindices]
---

[%CFEngine_function_prototype(array)%]

**Description:** Returns a list of keys in `array`.

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

      "parameter_name" slist => getindices("v");

    reports:
       "Found index: $(parameter_name)";
    }
```
