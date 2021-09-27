---
layout: default
title: getclassmetatags
published: true
tags: [reference, data functions, functions, getclassmetatags, meta, tags]
---

[%CFEngine_function_prototype(classname, optional_tag)%]

**Description:** Returns the list of [`meta`][Promise Types#meta] tags for class `classname`.

[%CFEngine_function_attributes(classname, optional_tag)%]

The `optional_tag` can be used to look up a specific tag's value. If you format
your tags like `meta => { "mykey=myvalue1", "mykey=myvalue2"}` then the
`optional_tag` of `mykey` will fetch you a list with two entries, `{ "myvalue1",
"myvalue2" }`.

**Example:**

[%CFEngine_include_snippet(getclassmetatags.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(getclassmetatags.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**Notes:**

**See also:** `getvariablemetatags()`

**History:** Function added in 3.6.0. `optional_tag` added in 3.10.0
