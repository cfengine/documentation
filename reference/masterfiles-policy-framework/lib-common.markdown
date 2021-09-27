---
layout: default
title: lib/common.cf
published: true
sorting: 160
tags: [reference, standard library, common, MPF]
---

See
the [common promise attributes][Promise Types#Common Promise Attributes]
documentation for a comprehensive reference on the body types and attributes
used here.

To use these bodies, add the following to your policy:

```cf3
body file control
{
	inputs => { "common.cf" }
}
```

[%CFEngine_library_include(lib/common)%]
