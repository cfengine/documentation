---
layout: default
title: regcmp
published: true
tags: [reference, data functions, functions, regcmp]
---

[%CFEngine_function_prototype(regex, string)%]

**Description:** Returns whether the [anchored][anchored] regular expression
`regex` matches the `string.`

[%CFEngine_function_attributes(regex, string)%]

**Example:**

[%CFEngine_include_snippet(regcmp.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(regcmp.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

If the string contains multiple lines, then it is necessary to code these
explicitly, as regular expressions do not normally match the end of line
as a regular character (they only match end of string). You can do this
using either standard regular expression syntax or using the additional
features of PCRE (where `(?ms)` changes the way that ., `^` and `$` behave), e.g.


**See Also:** `regline()`, `strcmp()`
