---
layout: default
title: filesexist
published: true
tags: [reference, files functions, functions, filesexist]
---

[%CFEngine_function_prototype(list)%]

**Description:** Returns whether all the files in `list` can be accessed.

All files must exist, and the user must have access permissions to them for
this function to return true.

[%CFEngine_function_attributes(list)%]

**Example:**

[%CFEngine_include_snippet(filesexist.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(filesexist.cf, #\+begin_src\s+example_output\s*, .*end_src)%]
