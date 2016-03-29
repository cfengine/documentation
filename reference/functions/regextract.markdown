---
layout: default
title: regextract
published: true
tags: [reference, data functions, functions, regextract]
---

[%CFEngine_function_prototype(regex, string, backref)%]

**Description:** Returns whether the [anchored][anchored] `regex` matches the
`string`, and fills the array `backref` with back-references.

If there are any back reference matches from the regular expression, then the array will be populated with the values, in the manner:

```
    $(backref[0]) = entire string
    $(backref[1]) = back reference 1, etc
```

[%CFEngine_function_attributes(regex, string, backref)%]

**Example:**

[%CFEngine_include_snippet(regextract.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(regextract.cf, #\+begin_src\s+example_output\s*, .*end_src)%]
