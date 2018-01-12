---
layout: default
title: readenvfile
published: true
tags: [reference, io functions, functions, readenvfile, json, env, os-release, container]
---

[%CFEngine_function_prototype(filename, optional_maxbytes)%]

**Description:**
Parses key-value pairs from the file `filename` in env file format (`man os-release`).
Returns the result as a `data` variable.
Keys and values are interpreted as strings.
`maxbytes` is optional, if specified, only the first `maxbytes` bytes are read from `filename`.
[Details of the os-release/env file format on freedesktop.org](https://www.freedesktop.org/software/systemd/man/os-release.html)

[%CFEngine_function_attributes(filename, otpional_maxbytes)%]

**Syntax example:**

```cf3
    vars:
      "loadthis"
         data => readenvfile("/etc/os-release");
```

**Complete example:**

Prepare:

[%CFEngine_include_snippet(readenvfile.cf, #\+begin_src prep, .*end_src)%] <!--**-->

Run:

[%CFEngine_include_snippet(readenvfile.cf, #\+begin_src cfengine3, .*end_src)%] <!--**-->

Output:

[%CFEngine_include_snippet(readenvfile.cf, #\+begin_src\s+example_output\s*, .*end_src)%] <!--**-->

**Notes:**
This function is used internally to load `/etc/os-release` into `sys.os_release`.

**See also:** `readdata()`, `parsejson()`, `parseyaml()`, `storejson()`, `mergedata()`, and `data` documentation.

**History:**

- Introduced in 3.11.0
