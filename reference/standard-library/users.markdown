---
layout: default
title: Users Bundles and Bodies
published: true
sorting: 85
tags: [reference, standard library]
---

See the [`users` promises][users] documentation for a
comprehensive reference on the body types and attributes used here.

To use these bodies, add the following to your policy:

```cf3
body file control
{
	inputs => { "users.cf" }
}
```



[%CFEngine_library_include(lib/users)%]
