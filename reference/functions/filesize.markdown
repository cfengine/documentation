---
layout: default
title: filesize
published: true
tags: [reference, files functions, functions, filesize]
---

[%CFEngine_function_prototype(filename)%]

**Description:** Returns the size of the file `filename` in bytes.

If the file object does not exist, the function call fails and the
variable does not expand.

[%CFEngine_function_attributes(filename)%]

**Example:**

Run:

[%CFEngine_include_snippet(filesize.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(filesize.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**History:** Was introduced in version 3.1.3, Nova 2.0.2 (2010).
