---
layout: default
title: shuffle
categories: [Reference, Functions, shuffle]
published: true
alias: reference-functions-shuffle.html
tags: [reference, functions, shuffle]
---

**Prototype**: shuffle(arg1,arg2) 

**Return type**: `slist`

 *arg1* : The name of the list variable, *in the range*
[a-zA-Z0-9\_\$(){}\\[\\].:]+   

 *arg2* : Shuffle seed *in the range* .\*

Return arg1 shuffled with seed arg2.

**Example**:

```cf3
body common control
{
      bundlesequence => { test };
}

bundle agent test
{
  vars:
      "a" slist => { "b", "c", "a" };
      "shuffles" slist => { "xx", "yy", "zz" };

      "sa_$(shuffles)" slist => shuffle("a", $(shuffles));

      "j_$(shuffles)" string => join(",", "sa_$(shuffles)");

  reports:
      "shuffled by $(shuffles) = '$(j_$(shuffles))'";
}
```

Output:

```
shuffled by xx = 'b,a,c'
shuffled by yy = 'a,c,b'
shuffled by zz = 'c,b,a'
```

**Notes**:  

The same seed will produce the same shuffle every time.

If you want a random shuffle, provide a random seed, e.g. with the `randomint` function.

See also `sort`.
