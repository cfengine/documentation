---
layout: default
title: reverse
categories: [Reference, Functions, reverse]
published: true
alias: reference-functions-reverse.html
tags: [reference, data functions, functions, reverse]
---

[%CFEngine_function_prototype(list)%]

**Description:** Reverses a list.

This is a simple function to reverse a list.

**Arguments**:

* list : The name of the list variable to check, in the range
`[a-zA-Z0-9_$(){}\[\].:]+`

**Example:**  


```cf3
    bundle agent test
    {
      vars:
          "test" slist => {
                            1,2,3,
                            "one", "two", "three",
                            "long string",
                            "one", "two", "three",
                          };

          "reversed" slist => reverse("test");

      reports:
          "Original list is $(test)";
          "The reversed list is $(reversed)";
    }
```

**See also:** `filter()`, `grep()`, `every()`, `some()`, and `none()`.
