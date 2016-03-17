---
layout: default
title: data_expand
published: true
tags: [reference, data functions, functions, json, container, expand]
---

[%CFEngine_function_prototype(data_container)%]

**Description:** Transforms a data container to expand all variable references.

This function will take a data container and expand variable
references **once** in all keys and values.

**NOTE** that the `data_container` can be specified as inline JSON
instead of a separate variable. This is standard across many CFEngine
functions and explained in the `mergedata()` documentation.

Any compound (arrays or maps) data structures will be expanded
recursively, so for instance data in a map inside another map will be
expanded.

This function is chiefly useful if you want to read data from an
external source and it can contain variable references.

[%CFEngine_function_attributes(data_container)%]

**Example:**

[%CFEngine_include_snippet(data_expand.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(data_expand.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**Notes:**  
   
**History:** Was introduced in version 3.7.0 (2015)

**See also:** `readcsv()`, `readjson()`, `readyaml()`, `mergedata()`, and `data` documentation.
