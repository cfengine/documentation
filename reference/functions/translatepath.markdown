---
layout: default
title: translatepath
categories: [Reference, Functions, translatepath]
published: true
alias: reference-functions-translatepath.html
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

```cf3
bundle agent test
{
  vars:
      "inputs_dir" string => translatepath("$(sys.workdir)/inputs");

  reports:

    windows::
      "The path has backslashes: $(inputs_dir)";

    !windows::
      "The path has slashes: $(inputs_dir)";
}
```

**Notes:** Be careful when using this function in combination with regular
expressions, since backslash is also used as escape character in
regex's. For example, in the regex `dir/.abc`, the dot represents the
regular expression "any character", while in the regex `dir\.abc`, the
backslash-dot represents a literal dot character.
