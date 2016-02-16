---
layout: default
title: countlinesmatching
published: true
tags: [reference, io functions, functions, countlinesmatching]
---

[%CFEngine_function_prototype(regex, filename)%]

**Description:** Count the number of lines in file `filename` matching
`regex`.

This function matches lines in the named file, using an [anchored][anchored]
regular expression that should match the whole line, and returns the number of
lines matched.

[%CFEngine_function_attributes(regex, filename)%]

**Example:**

[%CFEngine_include_snippet(countlinesmatching.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(countlinesmatching.cf, #\+begin_src\s+example_output\s*, .*end_src)%]
