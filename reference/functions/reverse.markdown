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
body common control
{
      bundlesequence => { "test" };
}

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

Output:

```
R: Original list is 1
R: Original list is 2
R: Original list is 3
R: Original list is one
R: Original list is two
R: Original list is three
R: Original list is long string
R: The reversed list is three
R: The reversed list is two
R: The reversed list is one
R: The reversed list is long string
R: The reversed list is 3
R: The reversed list is 2
R: The reversed list is 1
```

**See also:** `filter()`, `grep()`, `every()`, `some()`, and `none()`.
