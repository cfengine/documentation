---
layout: default
title: Monitor Bundles and Bodies
published: true
sorting: 60
tags: [reference, standard library]
---
**This is an Enterprise-only feature.**

See the [`measurements` promises][measurements] documentation for a
comprehensive reference on the body types and attributes used here.

To use these bodies, add the following to your policy:

```cf3
body file control
{
	inputs => { "monitor.cf" }
}
```



[%CFEngine_library_include(lib/monitor)%]

