---
layout: default
title: canonifyuniquely
categories: [Reference, Functions, canonifyuniquely]
published: true
alias: reference-functions-canonifyuniquely.html
tags: [reference, data functions, functions, canonify, canonifyuniquely, hash]
---

[%CFEngine_function_prototype(text)%]

**Description:** Convert an arbitrary string `text` into a unique legal class name.

This function turns arbitrary text into class data, appending the
SHA-1 hash for uniqueness.  It is exactly equivalent to
`concat(canonify($(string)), "_", hash($(string),"sha1");` for a given
`$(string)` but is much more convenient to write and remember.

A common use case is when you need unique array keys for each file in
a list, but files in the list may have the same name when
`canonify`-ed.

[%CFEngine_function_attributes(text)%]

**Example:**  


```cf3
    commands:

       "/var/cfengine/bin/$(component)"

           ifvarclass => canonifyuniquely("start_$(component)");
```

**See also:** [canonify()][canonify]).
