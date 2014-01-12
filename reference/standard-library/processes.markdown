---
layout: default
title: Processes Bundles and Bodies
categories: [Reference, Standard Library, Processes]
published: true
sorting: 80
alias: reference-standard-library-processes.html
tags: [reference, standard library]
---

See the documentation of [`processes` promises][processes] for a
comprehensive reference on the body types and attributes used here.

To use these bodies, add

```cf3
body file control
{
	inputs => { "processes.cf" }
}
```

to your policy.


[%CFEngine_library_include(lib/3.6/processes)%]

