---
layout: default
title: Variable context const
categories: [Reference, Special Variables, Variable context const]
published: true
alias: reference-special-Variables-Variable-context-const.html
tags: [reference, variables, variable context const, const]
---

CFEngine defines a number of variables for embedding unprintable values
or values with special meanings in strings.

#### Variable const.dollar


```cf3
    reports:
      some:: **TODO:remove all classes here?**

       # This will report: The value of $(const.dollar) is $
       "The value of $(const.dollar)(const.dollar) is $(const.dollar)";

       # This will report: But the value of \$(dollar) is \$(dollar)
       "But the value of \$(dollar) is \$(dollar)";
```

#### Variable const.endl

```cf3
    reports:

     cfengine_3::

      "A newline with either $(const.n) or with $(const.endl) is ok";
      "But a string with \n in it does not have a newline!";
```

#### Variable const.n

```cf3
    reports:

     cfengine_3::

      "A newline with either $(const.n) or with $(const.endl) is ok";
      "But a string with \n in it does not have a newline!";
```

#### Variable const.r

```cf3
    reports:

     cfengine_3::

      "A carriage return character is $(const.r)";
```

#### Variable const.t

```cf3
    reports:

     cfengine_3::

      "A report with a$(const.t)tab in it";
```
