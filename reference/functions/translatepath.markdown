---
layout: default
title: translatepath
published: true
tags: [reference, files functions, functions, translatepath]
---

[%CFEngine_function_prototype(path)%]

**Description:** Translate separators in `path` from Unix style to the host's
native style and returns the result.

Takes a string argument with slashes as path separators and translate
these to the native format for path separators on the host. For example
translatepath("a/b/c") would yield "a/b/c" on Unix platforms, but
"a\\b\\c" on Windows.

[%CFEngine_function_attributes(path)%]

**Example:**

[%CFEngine_include_snippet(translatepath.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(translatepath.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**Notes:** Be careful when using this function in combination with regular
expressions, since backslash is also used as escape character in
regex's. For example, in the regex `dir/.abc`, the dot represents the
regular expression "any character", while in the regex `dir\.abc`, the
backslash-dot represents a literal dot character.
