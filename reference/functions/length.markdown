---
layout: default
title: length
categories: [Reference, Functions, length]
published: true
alias: reference-functions-length.html
tags: [reference, functions, length]
---

**Prototype**: length(arg1) 

**Return type**: `int`

* `arg1` : The name of the list variable, *in the range*
[a-zA-Z0-9\_\$(){}\\[\\].:]+

Return the length of list arg1.

**Example**:

```cf3
bundle agent test

{
  vars:
      "test" slist => {
                        1,2,3,
                        "one", "two", "three",
                        "long string",
                        "four", "fix", "six",
                        "one", "two", "three",
                      };

      "length" int => length("test");
      "test_str" string => join(",", "test");

  reports:
      "The test list is $(test_str)";
      "The test list has $(length) elements";
}
```

**Notes**:  

See also `nth`.
