---
layout: default
title: getfields
published: true
tags: [reference, data functions, functions, getfields]
---

[%CFEngine_function_prototype(regex, filename, split, array_lval)%]

**Description:** Fill `array_lval` with fields in the lines from file `filename` that match `regex`, split on `split`.

The function returns the number of lines matched. This function is most
useful when you want only the first matching line (e.g., to mimic the
behavior of the *getpwnam(3)* on the file `/etc/passwd`). If you want to
examine *all* lines, use [readstringarray()][readstringarray] instead.

**Arguments**:

* `regex` : Regular expression to match line, in the range `.*`

A regular expression matching one or more lines. The regular expression
is [anchored][anchored], meaning it must match the entire line.

* `filename` : Filename to read, in the range `"?(/.*)`

The name of the file to be examined.

* `split` : Regular expression to split fields, in the range `.*`

A regex pattern that is used to parse the field separator(s) to split up
the file into items

* `array_lval` : Return array name, in the range `.*`

The base name of the array that returns the values.

**Example:**

[%CFEngine_include_snippet(getfields.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(getfields.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**Notes:**
This function matches lines (using a regular expression) in the named
file, and splits the *first* matched line into fields (using a second
regular expression), placing these into a named array whose elements are
`array[1],array[2],..`. This is useful for examining user data in the
Unix password or group files.
