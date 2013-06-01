---
layout: default
title: unique
categories: [Reference, Functions, unique]
published: true
alias: reference-functions-unique.html
tags: [reference, functions, unique]
---



**Prototype**: unique(arg1) 

**Return type**: `slist`

 *arg1* : The name of the list variable, *in the range*
[a-zA-Z0-9\_\$(){}\\[\\].:]+   


Return list of unique elements of arg1.

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

**Notes**:  

