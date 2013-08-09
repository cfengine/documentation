---
layout: default
title: nth
categories: [Reference, Functions, nth]
published: true
alias: reference-functions-nth.html
tags: [reference, data functions, functions, nth]
---

[%CFEngine_function_prototype(list, position)%]

**Description:** Returns the element of `list` at zero-based `position`.

If an invalid position (below 0 or above the size of the list minus 1)
is requested, this function does not return a valid value.

[%CFEngine_function_attributes(list, position)%]

**Example:**

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

**See also:** [`length()`][length].
