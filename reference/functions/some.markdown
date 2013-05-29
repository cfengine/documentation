---
layout: default
title: some
categories: [Reference, Functions, some]
published: true
alias: reference-functions-some.html
tags: [reference, functions, some]
---

### Function some

**Synopsis**: some(arg1,arg2) returns type **class**

  
 *arg1* : Unanchored regular expression to find, *in the range* .\*
  
 *arg2* : The name of the list variable to check, *in the range*
[a-zA-Z0-9\_\$(){}\\[\\].:]+   

Return true if any element of the list matches the regular expression.

**Example**:  
   

```cf3
bundle agent test

{
  classes:
      "some1" expression => some("long string", "test");
      "some2" expression => some("none", "test");

  vars:
      "test" slist => {
                        1,2,3,
                        "one", "two", "three",
                        "long string",
                        "four", "fix", "six",
                        "one", "two", "three",
                      };

  reports:
      "The test list is $(test)";
    some1::
      "some() test 1 passed";
    !some1::
      "some() test 1 failed";
    some2::
      "some() test 2 failed";
    !some2::
      "some() test 2 passed";
}
```

**Notes**:  
   
See also `filter`, `every`, and `none`.

The regular expression is unanchored.
