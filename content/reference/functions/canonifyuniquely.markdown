---
layout: default
title: canonifyuniquely
aliases:
  - "/reference-functions-canonifyuniquely.html"
---

{{< CFEngine_function_prototype(text) >}}

**Description:** Convert an arbitrary string `text` into a unique legal class name.

This function turns arbitrary text into class data, appending the
SHA-1 hash for uniqueness. It is exactly equivalent to
`concat(canonify($(string)), "_", hash($(string),"sha1"));` for a given
`$(string)` but is much more convenient to write and remember.

A common use case is when you need unique array keys for each file in
a list, but files in the list may have the same name when
`canonify`-ed.

{{< CFEngine_function_attributes(text) >}}

**Example:**

```cf3 {skip TODO}
commands:

   "/var/cfengine/bin/$(component)"

       if => canonifyuniquely("start_$(component)");
```

**See also:** `canonify()`.
