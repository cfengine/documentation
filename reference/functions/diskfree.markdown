---
layout: default
title: diskfree
published: true
tags: [reference, files functions, functions, diskfree]
---

[%CFEngine_function_prototype(path)%]

**Descriptions**: Return the free space (in KB) available on the current
partition of `path`.

If `path` is not found, this function returns 0.

[%CFEngine_function_attributes(path)%]

**Example:**

[%CFEngine_include_snippet(diskfree.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(diskfree.cf, #\+begin_src\s+example_output\s*, .*end_src)%]
