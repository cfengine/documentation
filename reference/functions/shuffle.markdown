---
layout: default
title: shuffle
categories: [Reference, Functions, shuffle]
published: true
alias: reference-functions-shuffle.html
tags: [reference, data functions, functions, shuffle]
---

[%CFEngine_function_prototype(list, seed)%]

**Description:** Return `list` shuffled with `seed`.

The same seed will produce the same shuffle every time. For a random shuffle, 
provide a random seed with the `randomint` function.

[%CFEngine_function_attributes(list, seed)%]

**Example:**

```cf3
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

**See also:** [`sort()`][sort].
