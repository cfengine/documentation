---
layout: default
title: strftime
published: true
tags: [reference, data functions, functions, strftime]
---

[%CFEngine_function_prototype(mode, template, time)%]

**Description:** Interprets a time and date format string at a particular
point in GMT or local time using Unix epoch time.

[%CFEngine_function_attributes(mode, template, time)%]

The `mode` is either `gmtime` (to get GMT times and dates) or
`localtime` (to get times and dates according to the local
timezone, usually specified by the `TZ` environment variable).

The conversion specifications that can appear in the format `template`
are specialized for printing components of the date and time according to the system locale.

**Example:**

[%CFEngine_include_snippet(strftime.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(strftime.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**Notes:** Note that `strftime` is a standard C function and you should consult
its
[reference](https://pubs.opengroup.org/onlinepubs/9699919799/functions/strftime.html)
to be sure of the specifiers allowed.
