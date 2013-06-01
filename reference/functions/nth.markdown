---
layout: default
title: nth
categories: [Reference, Functions, nth]
published: true
alias: reference-functions-nth.html
tags: [reference, functions, nth]
---

**Prototype**: nth(arg1,arg2) 

**Return type**: `string`

 *arg1* : The name of the list variable, *in the range*
[a-zA-Z0-9\_\$(){}\\[\\].:]+   

 *arg2* : Zero-based position of element to extract *in the range* 0,999999999

Return the element of arg1 at zero-based position arg2.

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

      "nth" slist => { 1, 2, 6, 10, 11, 1000 };

      "test[$(nth)]" string => nth("test", $(nth));
      "test[0]" string => nth("test", 0);

  reports:
      "The test list is $(test)";
      "element #$(nth) of the test list: $(test[$(nth)])";
      "element #0 of the test list: $(test[0])";
}
```

**Notes**:  

If an invalid position (under 0 or over the size of the list minus 1)
is requested, this function does not return a valid value.

See also `length`.
