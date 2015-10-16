---
layout: default
title: Macros
categories: [Reference, Macros]
published: true
alias: reference-macros.html
tags: [reference, syntax, if, ifdef, macros, minimum_version, feature]
---

### Minimum version

You can conditionally include policy test using the `@if` macro.

For example, you could say

```cf3
bundle agent extractor
{
@if minimum_version(3.8)
# the function `new_function_3_8()` was introduced in 3.8
vars: "container" data => new_function_3_8(...);
@endif
}
```

The text will be inserted verbatim in the policy. This happens before
syntax validation, so any version of CFEngine that supports the `@if`
macro will be able to exclude syntax from later, possibly incompatible
versions. In CFEngine 3.7, the above text will never be seen by the
parser. In 3.8 and later, it will.

`@if` calls have to match up: you can't nest them and each one
requires a matching `@endif` before the end of the file.

### Features

You can conditionally include policy test using the `@if` macro.

```cf3
bundle agent extractor
{
  @if feature(xml)
# the yaml library may not be compiled in
  vars: "container" data => parseyaml(...);
  @endif
}
```

The text will be inserted verbatim in the policy. This happens before
syntax validation, so any CFEngine binary that is not compiled with
the feature support macro will be able to exclude syntax from
possibly incompatible versions.

Currently available features are :
* `xml`
* `yaml`


**History:** Introduced in CFEngine 3.7.0
