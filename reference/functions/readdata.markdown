---
layout: default
title: readdata
published: true
tags: [reference, io functions, functions, readcsv, readjson, readyaml, readdata, readenvfile, CSV, JSON, YAML, ENV, container]
---

[%CFEngine_function_prototype(filename, filetype)%]

**Description:** Parses CSV, JSON, or YAML data from file `filename`
and returns the result as a `data` variable.

When `filetype` is `auto`, the file type is guessed from the extension
(ignoring case): `.csv` means CSV; `.json` means JSON; `.yaml` or `.yml` means
YAML. If the file doesn't match any of those names, JSON is used.

When `filetype` is `CSV`,`JSON`,`YAML` or `ENV`,
this function behaves like `readcsv()`, `readjson()`, `readyaml()` or `readenvfile()` respectively.
These functions have an optional parameter `maxbytes` (default: `inf`).
`maxbytes` can not be set using `readdata()`, if needed use one of the mentioned functions instead.

[%CFEngine_function_attributes(filename, filetype)%]

**Example:**

Prepare:

[%CFEngine_include_snippet(readdata.cf, #\+begin_src prep, .*end_src)%]

Run:

[%CFEngine_include_snippet(readdata.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(readdata.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**See also:** `readcsv()`, `readyaml()`, `readjson()`, `readenvfile()`, `validdata()`, `data` documentation.

**History:** Was introduced in 3.7.0.
