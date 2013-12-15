---
layout: default
title: length
categories: [Reference, Functions, length]
published: true
alias: reference-functions-length.html
tags: [reference, data functions, functions, length]
---

[%CFEngine_function_prototype(list)%]

**Description:** Returns the length of `list`.

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

      "length" int => length("test");
      "test_str" string => join(",", "test");

  reports:
      "The test list is $(test_str)";
      "The test list has $(length) elements";
}
```

Output:

```
R: The test list is 1,2,3,one,two,three,long string,four,fix,six,one,two,three
R: The test list has 13 elements
```

**See also:** [`nth()`][nth].
