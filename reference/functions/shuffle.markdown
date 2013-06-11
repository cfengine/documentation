---
layout: default
title: shuffle
categories: [Reference, Functions, shuffle]
published: true
alias: reference-functions-shuffle.html
tags: [reference, data functions, functions, shuffle]
---

**Prototype:** `shuffle(list, seed)`

**Return type:** `slist`

**Description:** Return `list` shuffled with `seed`.

The same seed will produce the same shuffle every time. For a random shuffle, 
provide a random seed with the `randomint` function.

**Arguments**:

* `list` : The name of the list variable, in the range
`[a-zA-Z0-9_$(){}\[\].:]+`
* `seed` : Shuffle seed in the range `.*`

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
