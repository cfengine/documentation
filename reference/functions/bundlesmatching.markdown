---
layout: default
title: bundlesmatching
categories: [Reference, Functions, bundlesmatching]
published: true
alias: reference-functions-bundlesmatching.html
tags: [reference, utility functions, functions, bundlesmatching]
---

[%CFEngine_function_prototype(regex, tag1, tag2, ...)%]

**Description:** Return the list of defined bundles matching `regex` and any tags given.

This function searches for the [unanchored][unanchored] regular expression in 
the list of currently defined bundles.

Every bundle is prefixed with the namespace, usually `default:`.

When any tags are given, only the bundles with those tags are
returned.  Bundle tags are set in the `meta` promises in a `tags`
variable; see the example below.

This function, used together with the `findfiles` function, allows you
to do dynamic inputs and a dynamic bundle call chain.  The dynamic
chain is constrained by an explicit regular expression to avoid
accidental or intentional running of unwanted bundles.

[%CFEngine_function_attributes(regex, tag1, tag2, ...)%]

**Example:**


[%CFEngine_include_snippet(bundlesmatching.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(bundlesmatching.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**See also:** [`findfiles()`][findfiles].
