---
layout: default
title: bundlesmatching
categories: [Reference, Functions, bundlesmatching]
published: true
alias: reference-functions-bundlesmatching.html
tags: [reference, utility functions, functions, bundlesmatching]
---

[%CFEngine_function_prototype(name, tag1, tag2, ...)%]

**Description:** Return the list of defined bundles matching `name` and any
tags given. Both bundlename and tags are regular expressions. `name` is
required, tags are optional.

This function searches for the the given [unanchored][unanchored] `name` and
`tag1, `tag2`,... regular expression in the list of currently defined bundles.

Every bundle is prefixed with the namespace, usually `default:`.

When any tags are given, only the bundles with those tags are
returned.  Bundle tags are set in the `meta` promises in a `tags`
variable; see the example below.

This function, used together with the `findfiles` function, allows you
to do dynamic inputs and a dynamic bundle call chain.  The dynamic
chain is constrained by an explicit regular expression to avoid
accidental or intentional running of unwanted bundles.

[%CFEngine_function_attributes(name, tag1, tag2, ...)%]

**Example:**


[%CFEngine_include_snippet(bundlesmatching.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(bundlesmatching.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**See also:** [`findfiles()`][findfiles].
