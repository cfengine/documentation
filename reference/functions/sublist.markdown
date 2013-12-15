---
layout: default
title: sublist
categories: [Reference, Functions, sublist]
published: true
alias: reference-functions-sublist.html
tags: [reference, data functions, functions, sublist]
---

[%CFEngine_function_prototype(list, head_or_tail, max_elements)%]

**Description:** Returns list of up to `max_elements` of `list`, obtained from head or tail depending on `head_or_tail`.

[%CFEngine_function_attributes(list, head_or_tail, max_elements)%]

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
      };

      "test_head9999" slist => sublist("test", "head", 9999);
      "test_head1" slist => sublist("test", "head", 1);
      "test_head0" slist => sublist("test", "head", 0);

      "test_tail9999" slist => sublist("test", "tail", 9999);
      "test_tail10" slist => sublist("test", "tail", 10);
      "test_tail2" slist => sublist("test", "tail", 2);
      "test_tail1" slist => sublist("test", "tail", 1);
      "test_tail0" slist => sublist("test", "tail", 0);

  reports:
      "The test list is $(test)";
      "This line should not appear: $(test_head0)";
      "The head(1) of the test list is $(test_head1)";
      "The head(9999) of the test list is $(test_head9999)";
      "This line should not appear: $(test_tail0)";
      "The tail(1) of the test list is $(test_tail1)";
      "The tail(10) of the test list is $(test_tail10)";
      "The tail(2) of the test list is $(test_tail2)";
      "The tail(9999) of the test list is $(test_tail9999)";
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
R: The head(1) of the test list is 1
R: The head(9999) of the test list is 1
R: The head(9999) of the test list is 2
R: The head(9999) of the test list is 3
R: The head(9999) of the test list is one
R: The head(9999) of the test list is two
R: The head(9999) of the test list is three
R: The head(9999) of the test list is long string
R: The head(9999) of the test list is four
R: The head(9999) of the test list is fix
R: The head(9999) of the test list is six
R: The tail(1) of the test list is six
R: The tail(10) of the test list is 1
R: The tail(10) of the test list is 2
R: The tail(10) of the test list is 3
R: The tail(10) of the test list is one
R: The tail(10) of the test list is two
R: The tail(10) of the test list is three
R: The tail(10) of the test list is long string
R: The tail(10) of the test list is four
R: The tail(10) of the test list is fix
R: The tail(10) of the test list is six
R: The tail(2) of the test list is fix
R: The tail(2) of the test list is six
R: The tail(9999) of the test list is 1
R: The tail(9999) of the test list is 2
R: The tail(9999) of the test list is 3
R: The tail(9999) of the test list is one
R: The tail(9999) of the test list is two
R: The tail(9999) of the test list is three
R: The tail(9999) of the test list is long string
R: The tail(9999) of the test list is four
R: The tail(9999) of the test list is fix
R: The tail(9999) of the test list is six
```

**Notes:**  

