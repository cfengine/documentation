---
layout: default
title: Monitor Bundles and Bodies
categories: [Reference, Standard Library, Monitor]
published: true
sorting: 60
alias: reference-standard-library-monitor.html
tags: [reference, standard library]
---

See the documentation of [`measurements` promises][measurements] for a
comprehensive reference on the body types and attributes used here.

To use these bodies, add

```cf3
body file control
{
	inputs => { "monitor.cf" }
}
```

to your policy.


[%CFEngine_library_include(lib/3.6/monitor)%]

