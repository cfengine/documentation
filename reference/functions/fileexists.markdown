---
layout: default
title: fileexists
published: true
tags: [reference, files functions, functions, fileexists]
---

[%CFEngine_function_prototype(filename)%]

**Description:** Returns whether the file `filename` can be accessed.

The file must exist, and the user must have access permissions to the file for
this function to return true.

[%CFEngine_function_attributes(filename)%]

**Example:**

[%CFEngine_include_snippet(fileexists.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(fileexists.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

