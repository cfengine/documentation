---
layout: default
title: Macros
categories: [Reference, Macros]
published: true
alias: reference-macros.html
tags: [reference, syntax, if, ifdef, macros]
---

You can conditionally include policy test using the `@if` macro.

For example, you could say

```cf3
bundle agent extractor
{
@if after_version(3.7)
# the function `data_regextract()` was introduced in 3.7
vars: "container" data => data_regextract(...);
@endif
}
```

The text will be inserted verbatim in the policy. This happens before
syntax validation, so any version of CFEngine that supports the `@if`
macro will be able to exclude syntax from later, possibly incompatible
versions. In CFEngine 3.6, the above text will never be seen by the
parser. In 3.7 and later, it will.

`@if` calls have to match up: you can't nest them and each one
requires a matching `@endif` before the end of the file.

**History:** Introduced in CFEngine 3.6.6
