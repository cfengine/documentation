---
layout: default
title: unique
categories: [Reference, Functions, unique]
published: true
alias: reference-functions-unique.html
tags: [reference, data functions, functions, unique]
---

[%CFEngine_function_prototype(list)%]

**Description:** Returns list of unique elements from `list`.

[%CFEngine_function_attributes(list)%]

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

Output:

```
R: The test list is 1,2,3,one,two,three,long string,four,fix,six,one,two,three
R: The unique elements of the test list: 1,2,3,one,two,three,long string,four,fix,six
```
