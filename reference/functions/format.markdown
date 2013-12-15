---
layout: default
title: format
categories: [Reference, Functions, format]
published: true
alias: reference-functions-format.html
tags: [reference, data functions, functions, format]
---

[%CFEngine_function_prototype(string, ...)%]

**Description:** Applies sprintf-style formatting to a given `string`.

This function will format numbers (`o`, `x`, `d` and `f`) or strings (`s`) but 
not potentially dangerous things like individual characters or pointer 
offsets.

This function will fail if it doesn't have enough arguments; if any
format *specifier* contains the *modifiers* `hLqjzt`; or if any format
*specifier* is not one of `doxfs`.

**Example:**  

```cf3
body common control
{
      bundlesequence => { "run" };
}

bundle agent run
{
  vars:
      "v" string => "2.5.6";
      "vlist" slist => splitstring($(v), "\.", 3);
      "padded" string => format("%04d%04d%04d", nth("vlist", 0), nth("vlist", 1), nth("vlist", 2));
      "a" string => format("%10.10s", "x");
      "b" string => format("%-10.10s", "x");
      "c" string => format("%04d", 1);
      "d" string => format("%07.2f", 1);
      "e" string => format("hello %s, my IP is %s", $(sys.policy_hub), $(sys.ipv4));

  reports:
      "version $(v) => padded $(padded)";
      "%10.10s on 'x' => '$(a)'";
      "%-10.10s on 'x' => '$(b)'";
      "%04d on '1' => '$(c)'";
      "%07.2f on '1' => '$(d)'";
      "hello my IP is... => '$(e)'";
}
```

Output:

```
R: version 2.5.6 => padded 000200050006
R: %10.10s on 'x' => '         x'
R: %-10.10s on 'x' => 'x         '
R: %04d on '1' => '0001'
R: %07.2f on '1' => '0001.00'
R: hello my IP is... => '$(e)'
```

**Note:** the underlying `sprintf` system call may behave differently on some platforms for some formats.  Test carefully.  For example, the format `%08s` will use spaces to fill the string up to 8 characters on libc platforms, but on Darwin (Mac OS X) it will use zeroes.  According to [SUSv4][http://pubs.opengroup.org/onlinepubs/9699919799/functions/sprintf.html] the behavior is undefined for this specific case.
