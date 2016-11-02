---
layout: default
title: lib/storage.cf
published: true
sorting: 160
tags: [reference, standard library, storage, MPF]
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
