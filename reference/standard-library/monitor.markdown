---
layout: default
title: Monitor Bundles and Bodies
categories: [Reference, Standard Library, Monitor]
published: true
sorting: 60
alias: reference-standard-library-monitor.html
tags: [reference, standard library]
---

See the [`measurements` promises][measurements] documentation for a
comprehensive reference on the body types and attributes used here.

To use these bodies, add the following to your policy:

```cf3
body file control
{
	inputs => { "monitor.cf" }
}
```



[%CFEngine_library_include(lib/3.6/monitor)%]

