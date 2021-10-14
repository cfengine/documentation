---
layout: default
title: const
published: true
tags: [reference, variables, const, const]
---

CFEngine defines a number of variables for embedding unprintable values
or values with special meanings in strings.

[%CFEngine_include_example(const.cf)%]

### const.at

```cf3
    reports:

       "The value of $(const.at) is @";

```

**History:**

* Added in CFEngine 3.19.0

### const.dollar


```cf3
    reports:

       # This will report: The value of $(const.dollar) is $
       "The value of $(const.dollar)(const.dollar) is $(const.dollar)";

       # This will report: But the value of $(dollar) is $(dollar)
       "But the value of $(dollar) is $(dollar)";
```

### const.dirsep


```cf3
    reports:

       # On Unix hosts this will report: The value of $(const.dirsep) is /
       # On Windows hosts this will report: The value of $(const.dirsep) is \\
       "The value of $(const.dollar)(const.dirsep) is $(const.dirsep)";
```

### const.endl

```cf3
    reports:

      "A newline with either $(const.n) or with $(const.endl) is ok";
      "But a string with \n in it does not have a newline!";
```

### const.n

```cf3
    reports:

      "A newline with either $(const.n) or with $(const.endl) is ok";
      "But a string with \n in it does not have a newline!";
```

### const.r

```cf3
    reports:

      "A carriage return character is $(const.r)";
```

### const.t

```cf3
    reports:

      "A report with a$(const.t)tab in it";
```
