---
layout: default
title: isnewerthantime
---

[%CFEngine_function_prototype(file, time)%]

**Description:** Returns whether the file `file` is newer (modified later)
than the time `time`.

This function compares the modification time (mtime) of the file. Note that
access changes such as ownership and permissions as well as status changes
such as last time the file was read are not included in the mtime timestamp.

[%CFEngine_function_attributes(file, time)%]

**Example:**

Prepare:

[%CFEngine_include_snippet(isnewerthantime.cf, #\+begin_src prep, .*end_src)%]

Run:

[%CFEngine_include_snippet(isnewerthantime.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(isnewerthantime.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**See also:** `isnewerthan()`
