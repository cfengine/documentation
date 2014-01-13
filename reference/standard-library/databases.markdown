---
layout: default
title: Databases Bundles and Bodies
categories: [Reference, Standard Library, databases]
published: true
sorting: 30
alias: reference-standard-library-databases.html
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



[%CFEngine_library_include(lib/3.6/databases)%]

