---
layout: default
title: Processes Bundles and Bodies
published: true
sorting: 80
tags: [reference, standard library]
---

See the [`processes` promises][processes] documentation for a
comprehensive reference on the body types and attributes used here.

To use these bodies, add the following to your policy:

```cf3
body file control
{
	inputs => { "processes.cf" }
}
```



[%CFEngine_library_include(lib/processes)%]

