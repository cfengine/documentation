---
layout: default
title: const
---

CFEngine defines a number of variables for embedding unprintable values
or values with special meanings in strings.

{{< CFEngine_include_example(const.cf) >}}

### const.at

```cf3
reports:

   "The value of $(const.at) is @";
```

**History:**

* Added in CFEngine 3.19.0, 3.18.1

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

### const.linesep

```cf3
reports:

   # On Unix hosts this will report: The value of $(const.linesep) is \n
   # On Windows hosts this will report: The value of $(const.linesep) is \r\n
   "The value of $(const.dollar)(const.linesep) is $(const.linesep)";
```

**History:** Introduced in CFEngine 3.23.0

### const.endl

```cf3
reports:

  "A newline with either $(const.n) or with $(const.endl) is ok";
  "But a string with \n in it does not have a newline!";
```

**Note:** The variable `const.endl` is an alias for `const.n` and nothing more.
It is commonly mistaken to be a platform agnostic line separator. But this has
never been the case. However, since CFEngine 3.23 we introduced `const.linesep`
which is exactly that.

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
