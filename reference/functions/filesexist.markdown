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

[This function can accept many types of data parameters.][Functions#collecting functions]

**Arguments:**

* list : The name of the list variable or data container to check, in the range
`[a-zA-Z0-9_$(){}\[\].:]+`

**Example:**

[%CFEngine_include_snippet(filesexist.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(filesexist.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**History:** The [collecting function][Functions#collecting functions] behavior was added in 3.12.

**See also:** [About collecting functions][Functions#collecting functions], `grep()`, `every()`, `some()`, and `none()`.
