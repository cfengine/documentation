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
          "test_exact1" slist => reverse("one", "test", "false", "false", 999);
          "test_exact2" slist => reverse(".", "test", "false", "false", 999);
          "test_invert" slist => reverse("[0-9]", "test", "true", "true", 999);
          "test_max2" slist => reverse(".*", "test", "true", "false", 2);
          "test_max0" slist => reverse(".*", "test", "true", "false", 0);
          "grep" slist => grep("[0-9]", "test");

      reports:
          "The test list is $(reversed)";
    }
```

**See also:** `filter()`, `grep()`, `every()`, `some()`, and `none()`.
