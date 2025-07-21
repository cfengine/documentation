---
layout: default
title: classfilterdata
---

[%CFEngine_function_prototype(data_container, data_structure, key_or_index)%]

**Description:**
This function filters a data container (`data_container`) based on defined
classes. Records within the data container containing a class expression located
at a given key or index (`key_or_index`) are filtered out when they evaluate to
false in the current context. The interpretation of the data container depends
on the specified data structure (`data_structure`).

If the `data_structure` argument is specified to be:
- `"array_of_arrays"`, the `data_container` argument is interpreted as an array
  of arrays, and the `key_or_index` argument is interpreted as an index within
  the children arrays.
- `"array_of_objects"`, the `data_container` argument is interpreted as an array
  of objects, and the `key_or_index` argument is interpreted as a key within the
  children objects.
- `"auto"`, the interpretation is automatically detected based on the data
  structure.

[%CFEngine_function_attributes(data_container, data_structure, key_or_index)%]

**Example (with array of arrays):**

**Policy:**

[%CFEngine_include_snippet(classfilterdata_array_of_arrays.cf, #\+begin_src cfengine3, .*end_src)%]

**Output:**

[%CFEngine_include_snippet(classfilterdata_array_of_arrays.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**Example (with array of objects):**

**Policy:**

[%CFEngine_include_snippet(classfilterdata_array_of_objects.cf, #\+begin_src cfengine3, .*end_src)%]

**Output:**

[%CFEngine_include_snippet(classfilterdata_array_of_objects.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**Notes:**

This function can accept many types of data parameters _(See [collecting function][Functions#collecting functions])_.

**See also:** [`classfiltercsv()`][classfiltercsv], [`data_expand()`][data_expand], [`classmatch()`][classmatch]

**History:**

- Introduced in CFEngine 3.27
