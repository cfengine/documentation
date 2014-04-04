---
layout: default
title: Guest Environments Bundles and Bodies
published: true
sorting: 50
tags: [reference, standard library]
---

See the [`guest_environments` promises][guest_environments] documentation for a
comprehensive reference on the body types and attributes used here.

To use these bodies, add the following to your policy:

```cf3
body file control
{
	inputs => { "guest_environments.cf" }
}
```



[%CFEngine_library_include(lib/3.6/guest_environments)%]
