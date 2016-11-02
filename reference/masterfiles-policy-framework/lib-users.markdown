---
layout: default
title: lib/users.cf
published: true
sorting: 160
tags: [reference, standard library, users, MPF]
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
