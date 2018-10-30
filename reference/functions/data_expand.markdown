---
layout: default
title: data_expand
published: true
tags: [reference, data functions, functions, json, container, expand, inline_json]
---

[%CFEngine_function_prototype(data_container)%]

**Description:** Transforms a data container to expand all variable references.

This function will take a data container and expand variable
references **once** in all keys and values.

[This function can accept many types of data parameters.][Functions#collecting functions]

Any compound (arrays or maps) data structures will be expanded
recursively, so for instance data in a map inside another map will be
expanded.

This function is chiefly useful if you want to read data from an
external source and it can contain variable references.

[%CFEngine_function_attributes(data_container)%]

**Example:**

Prepare to run the example policy:

[%CFEngine_include_snippet(data_expand.cf, #\+begin_src prep, .*end_src)%]

Policy:

[%CFEngine_include_snippet(data_expand.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(data_expand.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**Notes:**

**History:** Was introduced in version 3.7.0 (2015). The [collecting functions][Functions#collecting functions] behavior was added in 3.9.

**See also:** `readcsv()`, `readjson()`, `readyaml()`, `mergedata()`, [about collecting functions][Functions#collecting functions], and `data` documentation.
