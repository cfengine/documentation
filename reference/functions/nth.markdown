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

`list` can be an slist or a data container.  If it's a slist, the
offset is simply the position in the list.  If it's a data container,
the meaning of the `position` depends on its top-level contents: for
a list like `[1,2,3,4]` you will get the list element at `position`.
For a key-value map like `{ a: 100, b: 200 }` you get the value at
`position`, using the canonical JSON-style ordering of the keys.

[%CFEngine_function_attributes(list, position)%]

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

      "nth" slist => { 1, 2, 6, 10, 11, 1000 };

      "test[$(nth)]" string => nth("test", $(nth));
      "test[0]" string => nth("test", 0);

  reports:
      "The test list is $(test)";
      "element #$(nth) of the test list: $(test[$(nth)])";
      "element #0 of the test list: $(test[0])";
}
```

Output:

```
R: The test list is 1
R: The test list is 2
R: The test list is 3
R: The test list is one
R: The test list is two
R: The test list is three
R: The test list is long string
R: The test list is four
R: The test list is fix
R: The test list is six
R: element #1 of the test list: 2
R: element #2 of the test list: 3
R: element #6 of the test list: long string
R: element #10 of the test list: one
R: element #11 of the test list: two
R: element #1000 of the test list: $(test[1000])
R: element #0 of the test list: 1
```

**See also:** [`length()`][length].
