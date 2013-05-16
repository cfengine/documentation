---
layout: default
title: Function randomint
categories: [Special-functions,Function-randomint]
published: true
alias: Special-functions-Function-randomint.html
tags: [Special functions,Function randomint]
---

### Function randomint

**Synopsis**: randomint(arg1,arg2) returns type **int**

  
 *arg1* : Lower inclusive bound, *in the range* -99999999999,9999999999
  
 *arg2* : Upper inclusive bound, *in the range* -99999999999,9999999999
  

Generate a random integer between the given limits

**Example**:  
   

<<<<<<< HEAD
```cf3
vars:

 "ran"    int => randomint(4,88);
```
=======
```cf3 {.verbatim}
bundle agent randomint_example
# Demonstrate random number calculation
{
  vars:
      "low"    string => "4";
      "high"   string => "60";

      "random"    int => randomint("$(low)", "$(high)"), policy => "free";

    !classes1::
      "random1" 
        string  => "$(random)",
        handle  => "var_random1",
        comment => "this should only be set on the first pass";

    classes1.!classes2::

      "random2" 
        string     => "$(random)",
        handle     => "var_random2",
        comment    => "this should only be set on the second pass";

    classes2::

      "random3" 
        string     => "$(random)",
        handle     => "var_random3",
        comment    => "this should only be set on the third pass";

  classes:
      "classes3" expression => "classes2";
      "classes2" expression => "classes1";
      "classes1" expression => "any";

  reports:
    classes3::
      "Random Numbers: $(random1), $(random2), $(random3)";
}
Example output:
R: Random Numbers: 32, 56, 37
```
>>>>>>> upstream/master

**Notes**:  
   

The limits must be integer values and the resulting numbers are based on
the entropy of the md5 algorithm.

The function will be re-evaluated on each pass if it is not restricted with a
context class expression as shown in the example.
