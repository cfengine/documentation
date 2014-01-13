---
layout: default
title: Storage Bundles and Bodies
categories: [Reference, Standard Library, Storage]
published: true
sorting: 100
alias: reference-standard-library-storage.html
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



[%CFEngine_library_include(lib/3.6/storage)%]
