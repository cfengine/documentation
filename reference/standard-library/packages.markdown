---
layout: default
title: Packages Bundles and Bodies
published: true
sorting: 70
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




[%CFEngine_library_include(lib/packages)%]

