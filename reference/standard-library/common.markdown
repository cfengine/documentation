---
layout: default
title: Common Bodies and Bundles
categories: [Reference, Standard Library, common]
published: true
sorting: 10
alias: reference-standard-library-common.html
tags: [reference, standard library]
---

See the documentation of the [common promise attributes][Promise Types and Attributes]
for a comprehensive reference on the body types and attributes used here.

[%CFEngine_library_include(lib/3.6/common)%]

# Re-usable agent bundles

These agent bundles can be used via `usebundle` in `methods` promises.

```cf3
methods:
    usebundle => library_bundle(parameters)
```

[%CFEngine_library_include(lib/3.6/bundles)%]

