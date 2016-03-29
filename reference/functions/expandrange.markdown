---
layout: default
title: expandrange
published: true
tags: [reference, files functions, functions, expandrange]
---

[%CFEngine_function_prototype(string_template, stepsize)%]

**Description:** Generates a list based on an ordered list of numbers selected from a
range of integers, in steps specified by the second argument.

The function is the inverse of functions like `iprange()` which match patterns of numerical ranges that cannot
be represented as regular expressions. The list of strings is composed from the text as quoted
 in the first argument, and a numerical range in square brackets is replaced by successive numbers
from the range.

[%CFEngine_function_attributes(string_template, stepsize)%]

```cf3
vars:

 "int_group1" slist => {
                       "swp10",
                       "swp11",
                       "swp12",
                       expandrange("swp[13-15]", 1)
                       };

interfaces:

 "$(int_group)"

     tagged_vlans => { "100", "145" },
    untagged_vlan => "1",
       link_state => up;
```

**History:** Introduced in CFEngine 3.7
