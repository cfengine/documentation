---
layout: default
title: registryvalue
published: true
tags: [reference, system functions, functions, registryvalue]
---

[%CFEngine_function_prototype(key, valueid)%]

**Description:** Returns the value of `valueid` in the Windows registry key
`key`.

This function applies only to Windows-based systems. The value is parsed as a
string.

[%CFEngine_function_attributes(key, valueid)%]

**Example:**

[%CFEngine_include_snippet(registryvalue.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(registryvalue.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**Notes:** Currently values of type `REG_SZ` (string), `REG_EXPAND_SZ`
(expandable string) and `REG_DWORD` (double word) are supported.
