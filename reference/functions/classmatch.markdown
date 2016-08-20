---
layout: default
title: classmatch
published: true
tags: [reference, utility functions, functions, classmatch]
---

[%CFEngine_function_prototype(regex, tag1, tag2, ...)%]

**Description:** Tests whether `regex` matches any currently set class.

Returns true if the [anchored][anchored] regular expression matches any
currently defined class, otherwise returns false.

You can optionally restrict the search by tags, which you can list after the regular expression.

[%CFEngine_function_attributes(regex, tag1, tag2, ...)%]

**Example:**

[%CFEngine_include_snippet(classmatch.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(classmatch.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**See also:** [canonify()][canonify], [classify()][classify], [classesmatching()][classesmatching]
