---
layout: default
title: lib/databases.cf
published: true
tags: [reference, standard library, databases, MPF]
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

[%CFEngine_library_include(lib/databases)%]
