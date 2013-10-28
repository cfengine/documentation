---
layout: default
title: bundlesmatching
categories: [Reference, Functions, bundlesmatching]
published: true
alias: reference-functions-bundlesmatching.html
tags: [reference, utility functions, functions, bundlesmatching]
---

[%CFEngine_function_prototype(regex)%]

**Description:** Return the list of defined bundles matching `regex`.

This function searches for the [unanchored][unanchored] regular expression in 
the list of currently defined bundles.

Every bundle is prefixed with the namespace, usually `default:`.

This function, used together with the `findfiles` function, allows you
to do dynamic inputs and a dynamic bundle call chain.  The dynamic
chain is constrained by an explicit regular expression to avoid
accidental or intentional running of unwanted bundles.

[%CFEngine_function_attributes(regex)%]

**Example:**


```cf3
body common control
{
      bundlesequence => { mefirst };
}

bundle common g
{
  vars:
      "todo" slist => bundlesmatching("default:run.*");
}

bundle agent mefirst
{
  methods:
      # note this is a dynamic bundle sequence!
      "" usebundle => $(g.todo);
}

bundle agent run_123_456
{
  vars:
      "bundles" slist => bundlesmatching(".*");
      "no_bundles" slist => bundlesmatching("891");
  reports:
      "bundles = $(bundles)";
      "no bundles = $(no_bundles)";
}
```

**See also:** [`findfiles()`][findfiles].
