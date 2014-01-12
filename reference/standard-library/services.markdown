---
layout: default
title: Services Bundles and Bodies
categories: [Reference, Standard Library, Services]
published: true
sorting: 90
alias: reference-standard-library-services.html
tags: [reference, standard library]
---

See the documentation of [`services` promises][services] for a
comprehensive reference on the body types and attributes used here.

To use these bodies and bundles, add

```cf3
body file control
{
	inputs => { "services.cf" }
}
```

to your policy.


[%CFEngine_library_include(lib/3.6/services)%]

