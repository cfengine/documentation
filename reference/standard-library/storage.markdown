---
layout: default
title: Storage and Bodies
categories: [Reference, Standard Library, Storage]
published: true
sorting: 100
alias: reference-standard-library-storage.html
tags: [reference, standard library]
---

See the documentation of [`storage` promises][storage] for a
comprehensive reference on the body types and attributes used here.

To use these bodies, add

```cf3
body file control
{
	inputs => { "storage.cf" }
}
```

to your policy.


[%CFEngine_library_include(lib/3.6/storage)%]
