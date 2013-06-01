---
layout: default
title: sublist
categories: [Reference, Functions, sublist]
published: true
alias: reference-functions-sublist.html
tags: [reference, functions, sublist]
---

**Prototype**: `sublist(list, extract_from, max_elements)`

**Return type**: `slist`

 *list* : The name of the list variable, *in the range*
[a-zA-Z0-9\_\$(){}\\[\\].:]+   

 *extract_from* : Whether to extract elements from the beginning or from the end. *in the range* head,tail

 *elements* : Maximum number of elements to return *in the range* 0,999999999

Return list of up to elements of list, obtained from head or tail depending on extract_from.

**Example**:  
   

```cf3
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

**Notes**:  

