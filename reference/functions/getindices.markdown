---
layout: default
title: getindices
published: true
tags: [reference, data functions, functions, getindices]
---

[%CFEngine_function_prototype(varref)%]

**Description:** Returns the list of keys in `varref` which can be
the name of an array or container.

Make sure you specify the correct scope when supplying the name of the
variable.

Note the order of the list which getindices returns is not guarenteed to be in any specific order.

[%CFEngine_function_attributes(varref)%]

**Example:**

[%CFEngine_include_snippet(getindices.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(getindices.cf, #\+begin_src\s+example_output\s*, .*end_src)%]
