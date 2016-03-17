---
layout: default
title: getvalues
published: true
tags: [reference, data functions, functions, getvalues, inline_json]
---

[%CFEngine_function_prototype(varref)%]

**Description:** Returns the list of values in `varref` which can be
the name of an array or container.

This is a [collecting function][Functions#collecting functions] so it can accept many types of data parameters.

If the array contains list values, then all of the list elements are flattened 
into a single list to make the return value a list.

If the data container contains non-scalar values (e.g. nested
containers) they are skipped.  The special values `true`, `false`, and
`null` are serialized to their string representations.  Numerical
values are serialized to their string representations.

You can specify a path inside the container. For example, below you'll
look at the values of `d[k]`, not at the top level of `d`.

Make sure you specify the correct scope when supplying the name of the
variable.

[%CFEngine_function_attributes(varref)%]

**Example:**

[%CFEngine_include_snippet(getvalues.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(getvalues.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**History:** The [collecting function][Functions#collecting functions] behavior was added in 3.9.

**See also:** `getindices()`, [about collecting functions][Functions#collecting functions], and `data` documentation.
