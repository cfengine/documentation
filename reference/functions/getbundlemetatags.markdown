---
layout: default
title: getbundlemetatags
published: true
---

[%CFEngine_function_prototype(bundlename, optional_tag)%]

**Description:** Returns the list of [`meta`][Promise types#meta] tags for bundle `bundlename`.

[%CFEngine_function_attributes(bundlename, optional_tag)%]

The `optional_tag` can be used to look up a specific tag's value. If you have
```
bundle agent example
{
  meta:
    "tags"
      slist => { "mykey=myvalue1", "mykey=myvalue2", "yourkey=yourvalue1" };
}
```
then `getbundlemetatags( "example", "mykey" )` will return a list with two entries, `{ "myvalue1",
"myvalue2" }`.

**Example:**

[%CFEngine_include_snippet(getbundlemetatags.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(getbundlemetatags.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**Notes:**

**See also:** `getvariablemetatags()`, `getclassmetatags()`

**History:**

* Function added in 3.26.0.
