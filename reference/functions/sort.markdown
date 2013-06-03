---
layout: default
title: sort
categories: [Reference, Functions, sort]
published: true
alias: reference-functions-sort.html
tags: [reference, functions, sort]
---

**Prototype**: `sort(list, mode)`

**Return type**: `slist`

**Description**: Returns `list` sorted according to `mode`.

Only lexicographical sorting is supported currently.

**Arguments**:

* `list` : The name of the list variable, *in the range*
[a-zA-Z0-9\_\$(){}\\[\\].:]+
* `mode` : Sorting mode *in the range* lex

**Example**:

```cf3
    bundle agent test
    {
      vars:
          "a" slist => { "b", "c", "a" };
          "b" slist => { "100", "9", "10" };
          "c" slist => { };
          "d" slist => { "", "a", "", "b" };
          "e" slist => { "a", "1", "b" };

          "ja" string => join(",", "sa");
          "jb" string => join(",", "sb");
          "jc" string => join(",", "sc");
          "jd" string => join(",", "sd");
          "je" string => join(",", "se");

          "sa" slist => sort("a", "lex");
          "sb" slist => sort("b", "lex");
          "sc" slist => sort("c", "lex");
          "sd" slist => sort("d", "lex");
          "se" slist => sort("e", "lex");

          "jsa" string => join(",", "sa");
          "jsb" string => join(",", "sb");
          "jsc" string => join(",", "sc");
          "jsd" string => join(",", "sd");
          "jse" string => join(",", "se");

      reports:
          "sorted '$(ja)' = '$(jsa)'";
          "sorted '$(jb)' = '$(jsb)'";
          "sorted '$(jc)' = '$(jsc)'";
          "sorted '$(jd)' = '$(jsd)'";
          "sorted '$(je)' = '$(jse)'";
    }
```

Output:

```
    sorted 'a,b,c' = 'a,b,c'
    sorted '10,100,9' = '10,100,9'
    sorted '' = ''
    sorted ',,a,b' = ',,a,b'
    sorted '1,a,b' = '1,a,b'
```

**Notes**:  

See also `shuffle`.
