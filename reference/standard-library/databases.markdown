---
layout: default
title: Databases Bundles and Bodies
published: true
sorting: 30
tags: [reference, standard library]
---

See the [`databases` promises][databases] documentation for a
comprehensive reference on the body types and attributes used here.

To use these bodies, add the following to your policy:

```cf3
body file control
{
	inputs => { "databases.cf" }
}
```



[%CFEngine_library_include(lib/databases.cf)%]

