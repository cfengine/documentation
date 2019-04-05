---
layout: default
title: lsdir
published: true
tags: [reference, files functions, functions, lsdir]
---

[%CFEngine_function_prototype(path, regex, include_base)%]

**Description:** Returns a list of files in the directory `path` matching the regular expression `regex`.

If `include_base` is true, full paths are returned, otherwise only names
relative to the directory are returned.

[%CFEngine_function_attributes(path, regex, include_base)%]

**Example:**

[%CFEngine_include_snippet(lsdir.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(lsdir.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**Tips:**

* Filter out the current (```.```) and parent (```..```)directories with a
  negative look ahead. ```lsdir( "/tmp", "^(?!(\.$|\.\.$)).*", false )```.

**Notes:**

 **History:** Was introduced in 3.3.0, Nova 2.2.0 (2011)

