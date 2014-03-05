---
layout: default
title: getvalues
categories: [Reference, Functions, getvalues]
published: true
alias: reference-functions-getvalues.html
tags: [reference, data functions, functions, getvalues]
---

[%CFEngine_function_prototype(varref)%]

**Description:** Returns the list of values in `varref` which can be
the name of an array or container.

If the array contains list values, then all of the list elements are flattened 
into a single list to make the return value a list.

If the data container contains non-scalar values (e.g. nested
containers) they are skipped.  The special values `true`, `false`, and
`null` are serialized to their string representations.  Numerical
values are serialized to their string representations.

Make sure you specify the correct scope when supplying the name of the
variable.

[%CFEngine_function_attributes(varref)%]

**Example:**

[%CFEngine_include_snippet(getvalues.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(getvalues.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**Notes:**
