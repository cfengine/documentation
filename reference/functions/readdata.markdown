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
(ignoring case): `.csv` means CSV; `.json` means JSON; `.yaml` means
YAML. If the file doesn't match any of those names, JSON is used.

When `filetype` is `CSV`, this function behaves exactly like
`readcsv()` and returns the same data structure.

When `filetype` is `JSON`, this function behaves exactly like
`readjson()` and returns the same data structure, except there is no
data size limit (`maxbytes` is `inf`).

When `filetype` is `YAML`, this function behaves exactly like
`readyaml()` and returns the same data structure, except there is no
data size limit (`maxbytes` is `inf`).

When `filetype` is `ENV`, this function behaves exactly like
`readenvfile()` and returns the same data structure, except there is no
data size limit (`maxbytes` is `inf`).

[%CFEngine_function_attributes(filename, filetype)%]

**Example:**

Prepare:

[%CFEngine_include_snippet(readdata.cf, #\+begin_src prep, .*end_src)%]

Run:

[%CFEngine_include_snippet(readdata.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(readdata.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**See also:** `readcsv()`, `readyaml()`, `readjson()`, `readenvfile()`, `data` documentation.

**History:** Was introduced in 3.7.0.
