---
layout: default
title: Packages Bundles and Bodies
categories: [Reference, Standard Library, Packages]
published: true
sorting: 70
alias: reference-standard-library-packages.html
tags: [reference, standard library]
---

See the documentation of [`packages` promises][packages] for a
comprehensive reference on the body types and attributes used here.

To use these bodies and bundles, add

```cf3
body file control
{
	inputs => { "packages.cf" }
}
```

to your policy.


[%CFEngine_library_include(lib/3.6/packages)%]

