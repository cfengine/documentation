---
layout: default
title: Common Bodies and Bundles
published: true
sorting: 10
tags: [reference, standard library]
---

See the [common promise attributes][Promise Types and Attributes#Common Attributes] 
documentation for a comprehensive reference on the body types and attributes used here.

To use these bodies, add the following to your policy:

```cf3
body file control
{
	inputs => { "common.cf", "bundles.cf" }
}
```




[%CFEngine_library_include(lib/common)%]

# Re-usable agent bundles

These agent bundles can be used via `usebundle` in `methods` promises.

```cf3
methods:
    usebundle => library_bundle(parameters)
```

To use these bundles, add the following to your policy:

```cf3
body file control
{
	inputs => { "bundles.cf" }
}
```




[%CFEngine_library_include(lib/bundles)%]

