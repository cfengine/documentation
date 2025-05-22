---
layout: default
title: isnewerthan
published: true
---

[%CFEngine_function_prototype(newer, older)%]

**Description:** Returns whether the file `newer` is newer (modified later)
than the file `older`.

This function compares the modification time (mtime) of the files. Note that
access changes such as ownership and permissions as well as status changes
such as last time the file was read are not included in the mtime timestamp.

[%CFEngine_function_attributes(newer, older)%]

**Example:**

Prepare:

[%CFEngine_include_snippet(isnewerthan.cf, #\+begin_src prep, .*end_src)%]

Run:

[%CFEngine_include_snippet(isnewerthan.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(isnewerthan.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**See also:** `accessedbefore()`, `changedbefore()`
