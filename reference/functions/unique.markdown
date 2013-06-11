---
layout: default
title: unique
categories: [Reference, Functions, unique]
published: true
alias: reference-functions-unique.html
tags: [reference, data functions, functions, unique]
---

**Prototype:** `unique(list)`

**Return type:** `slist`

**Description:** Returns list of unique elements from `list`.

**Arguments**:

* `list` : The name of the list variable, in the range
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
                        "four", "fix", "six",
                        "one", "two", "three",
                      };

      "test_str" string => join(",", "test");
      "test_unique" slist => unique("test");
      "unique_str" string => join(",", "test_unique");

  reports:
      "The test list is $(test_str)";
      "The unique elements of the test list: $(unique_str)";
}
```
