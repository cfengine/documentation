---
layout: default
title: Storage Bundles and Bodies
published: false
sorting: 95
tags: [reference, standard library]
---

See the [`storage` promises][storage] documentation for a
comprehensive reference on the body types and attributes used here.

To use these bodies, add the following to your policy:

```cf3
body file control
{
	inputs => { "storage.cf" }
}
```



[%CFEngine_library_include(lib/storage)%]
