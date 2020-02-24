---
layout: default
title: Macros
categories: [Reference, Macros]
published: true
alias: reference-macros.html
tags: [reference, syntax, if, ifdef, macros, minimum_version, feature]
---

Macros allow you to target different versions of the CFEngine binaries / parser.
They can be used to conditionally include or exclude parts of the policy file, depending on version number, or supported features.
A typical use case is to use new functionality or syntax on newer binaries which support it, and provide a different implementation on older versions.

Macros are evaluated in the lexer, before syntax checking.
This allows you to put syntax inside a macro which is not valid in all versions.
Note that all your binaries must support the _macro_ that you are using.
Don't start using new macros until you know that the macro is supported on all versions you are running.

`@if` calls have to match up: you can't nest them and each one requires a matching `@endif` before the end of the file.

Versions with less specificity are considered equal to the more specific, so `3.15.4` is equal to `3.15`, which is also equal to `3`.
This applies to all version macros.

### Minimum version

The contained policy is only included if the version is greater than or equal to  the specified version.

```cf3
bundle agent extractor
{
@if minimum_version(3.8)
# the function `new_function_3_8()` was introduced in 3.8
vars: "container" data => new_function_3_8(...);
@endif
}
```

**History:** This macro was introduced in CFEngine 3.7.0

### Maximum version

The contained policy is only included if the version is lower than or equal to  the specified version.

**Example:**

```cf3
bundle agent extractor
{
@if maximum_version(3.15)
  # This policy will only be parsed on versions 3.15 and earlier
  vars:
    "container" data => old_function_3_15(...);
@endif
}
```

**Note:** Don't start using new macros until all your hosts support them.

**History:** This macro was introduced in CFEngine 3.16.0, 3.15.1, 3.12.4.

### At version

The contained policy is only included if the version is equal to the specified version.

**Example:**

```cf3
bundle agent extractor
{
@if at_version(3.15)
  # This policy will only be parsed on 3.15 clients
  vars:
    "container" data => old_function_3_15(...);
@endif
}
```

**Note:** Don't start using new macros until all your hosts support them.

**History:** This macro was introduced in CFEngine 3.16.0, 3.15.1, 3.12.4.

### Between versions

The contained policy is only included if the version is between (inclusive) the two specified versions.

**Example:**

```cf3
bundle agent extractor
{
@if between_versions(3.12, 3.15)
  # Policy specific to 3.12, 3.13, 3.14, 3.15
  vars:
    "container" data => workaround_3_12_3_15(...);
@endif
}
```

**Note:** Don't start using new macros until all your hosts support them.

**History:** This macro was introduced in CFEngine 3.16.0, 3.15.1, 3.12.4.

### Before version

The contained policy is only included if the version is below the specified version (Not inclusive).

**Example:**

```cf3
bundle agent extractor
{
@if before_version(3.15)
  # Policy to work around issue which was fixed in 3.15
  vars:
    "container"
      data => workaround_pre_3_15(...);
@endif
}
```

**Note:** Don't start using new macros until all your hosts support them.

**History:** This macro was introduced in CFEngine 3.16.0, 3.15.1, 3.12.4.

### After version

The contained policy is only included if the version is above the specified version (Not inclusive).

**Example:**

```cf3
bundle agent extractor
{
@if after_version(3.15)
  # This policy is only parsed on 3.16+
  vars:
    "container"
      data => not_neded_on_3_15(...);
@endif
}
```

**Note:** Don't start using new macros until all your hosts support them.

**History:** This macro was introduced in CFEngine 3.16.0, 3.15.1, 3.12.4.

### Else

Must come after an `@if` macro, and before the matching `@endif`.
Inverts the skipping state from the `@if` macro.
If the policy before `@else` was skipped due to the `@if` macro, the policy after will not be skipped, and vice versa.

**Example:**

```cf3
bundle agent extractor
{
@if minimum_version(3.16)
  # Implementation for 3.16+
  vars:
    "container"
      data => classfiltercsv(...);
@else
  # Implementation for versions before 3.16
  vars:
    "container"
      data => readcsv(...);
@endif
}
```

**Note:** Don't start using new macros until all your hosts support them.

**History:** This macro was introduced in CFEngine 3.16.0, 3.15.1, 3.12.4.

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
* `curl`


**History:** This macro was introduced in CFEngine 3.8.0
