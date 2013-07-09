---
layout: default
title: filter
categories: [Reference, Functions, filter]
published: true
alias: reference-functions-filter.html
tags: [reference, data functions, functions, filter]
---

[%CFEngine_function_prototype(filter, list, is_regex, invert, max_return)%]

**Description:** Transforms a list into a subset thereof.

This is a generic filtering function that returns a list of up to `max_return` 
elements in `list` that match the filtering rules specified in `filter`, 
`is_regex` and `invert`.

**Arguments**:

* filter : [Anchored][anchored] regular expression or static string to find, in the range `.*`
* list : The name of the list variable to check, in the range
`[a-zA-Z0-9_$(){}\[\].:]+`
* is_regex_ : Boolean

Treat `filter` as a regular expression or as a static string.

* `invert` : Boolean

Invert filter.

* `max_return` : Maximum number of elements to return in the range `0,999999999`

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

          "test_grep" slist => filter("[0-9]", "test", "true", "false", 999);
          "test_exact1" slist => filter("one", "test", "false", "false", 999);
          "test_exact2" slist => filter(".", "test", "false", "false", 999);
          "test_invert" slist => filter("[0-9]", "test", "true", "true", 999);
          "test_max2" slist => filter(".*", "test", "true", "false", 2);
          "test_max0" slist => filter(".*", "test", "true", "false", 0);
          "grep" slist => grep("[0-9]", "test");

      reports:
          "The test list is $(test)";
          "The grepped list is $(grep)";
          "The filter-grepped list is $(test_grep)";
          "The filter-exact list, looking for 'one' is $(test_exact1)";
          "This line should not appear: $(test_exact2)";
          "The filter-invert list, looking for non-digits, is $(test_invert)";
          "The filter-bound list, matching at most 2 items, is $(test_max2)";
          "This line should not appear: $(test_max0)";
    }
```

**See also:** [`grep()`][grep], [`every()`][every], [`some()`][some], and 
[`none()`][none].
