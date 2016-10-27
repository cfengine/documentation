---
layout: default
title: getvariablemetatags
published: true
tags: [reference, data functions, functions, getvariablemetatags, meta, tags]
---

[%CFEngine_function_prototype(varname, optional_tag)%]

**Description:** Returns the list of [`meta`][Promise Types and Attributes#meta] tags for variable `varname`.

Make sure you specify the correct scope when supplying the name of the
variable.

[%CFEngine_function_attributes(varname, optional_tag)%]

The `optional_tag` can be used to look up a specific tag's value. If you format
your tags like `meta => { "mykey=myvalue1", "mykey=myvalue2"}` then the
`optional_tag` of `mykey` will fetch you a list with two entries, `{ "myvalue1",
"myvalue2" }`.

**Example:**

[%CFEngine_include_snippet(getvariablemetatags.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(getvariablemetatags.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**Notes:**

**See also:** `getclassmetatags()`

**History:** Function in 3.6.0. `optional_tag` added in 3.10.0
