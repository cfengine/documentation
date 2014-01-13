---
layout: default
title: Packages Bundles and Bodies
categories: [Reference, Standard Library, Packages]
published: true
sorting: 70
alias: reference-standard-library-packages.html
tags: [reference, standard library]
---

See the [`packages` promises][packages] documentation for a
comprehensive reference on the body types and attributes used here.

To use these bodies and bundles, add the following to your policy:

```cf3
body file control
{
	inputs => { "packages.cf" }
}
```




[%CFEngine_library_include(lib/3.6/packages)%]

