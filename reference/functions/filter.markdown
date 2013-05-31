---
layout: default
title: filter
categories: [Reference, Functions, filter]
published: true
alias: reference-functions-filter.html
tags: [reference, functions, filter]
---



**Synopsis**: filter(arg1,arg2,arg3,arg4,arg5) 

**Return type**: `slist`

  
 *arg1* : Anchored regular expression or static string to find, *in the range* .\*
  
 *arg2* : The name of the list variable to check, *in the range*
[a-zA-Z0-9\_\$(){}\\[\\].:]+   

 *arg3* : Boolean: treat arg1 as a regular expression or as a static string. *in the range* true,false

 *arg4* : Boolean: Invert filter. *in the range* true,false

 *arg5* : Maximum number of elements to return *in the range* 0,999999999

Return list of up to arg5 elements of arg2 that match the specified filtering rules.

**Example**:  
   

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

**Notes**:  

This is a generic filtering function to transform a list into a subset thereof.

See also `grep`, `every`, `some`, and `none`.
