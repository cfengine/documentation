---
layout: default
title: getvariablemetatags
published: true
tags: [reference, data functions, functions, getvariablemetatags, meta, tags]
---

[%CFEngine_function_prototype(varname)%]

**Description:** Returns the list of [`meta`][Promise Types and Attributes#meta] tags for variable `varname`.

Make sure you specify the correct scope when supplying the name of the
variable.

[%CFEngine_function_attributes(varname)%]

**Example:**

[%CFEngine_include_snippet(getvariablemetatags.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(getvariablemetatags.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**Notes:**

**See also:** `getclassmetatags()`
