---
layout: default
title: Policy Macros
categories: [Reference, Syntax, Macros]
published: false
alias: reference-syntax-macros.html
tags: [reference, syntax, include, macros]
---

You can include a snippet using the `@include` macro.

For example, you could say

```cf3
body file control
{
@include "myfile.cf.snippet"
}
```

And the contents of `myfile.cf.snippet` would be inserted verbatim in
the policy.  This happens before syntax validation so the snippet
doesn't have to be valid CFEngine policy as long as the including file
is.

A relative location may be specified.  It will be resolved relative to
the including file's location.
