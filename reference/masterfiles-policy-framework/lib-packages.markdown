---
layout: default
title: lib/packages.cf
published: true
tags: [reference, standard library, packages, MPF]
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
