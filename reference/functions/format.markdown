---
layout: default
title: format
published: true
tags: [reference, data functions, functions, format]
---

[%CFEngine_function_prototype(string, ...)%]

**Description:** Applies sprintf-style formatting to a given `string`.

This function will format numbers (`o`, `x`, `d` and `f`) or strings (`s`) but
not potentially dangerous things like individual characters or pointer
offsets.

The `%S` specifier is special and non-standard.  When you use it on a
slist or a data container, the data will be packed into a one-line
string you can put in a log message, for instance.

This function will fail if it doesn't have enough arguments; if any
format *specifier* contains the *modifiers* `hLqjzt`; or if any format
*specifier* is not one of `doxfsS`.

**Example:**

[%CFEngine_include_snippet(format.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(format.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**Note:** the underlying `sprintf` system call may behave differently on some platforms for some formats.  Test carefully.  For example, the format `%08s` will use spaces to fill the string up to 8 characters on libc platforms, but on Darwin (Mac OS X) it will use zeroes.  According to [SUSv4](http://pubs.opengroup.org/onlinepubs/9699919799/functions/sprintf.html) the behavior is undefined for this specific case.

**History:**

* Added in CFEngine 3.6.0
