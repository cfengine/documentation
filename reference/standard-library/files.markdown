---
layout: default
title: Files Bundles and Bodies
published: true
sorting: 40
tags: [reference, standard library]
---

See the [`files` promises][files] and [`edit_line` bundles][bundle edit_line]
documentation for a comprehensive reference on
the bundles, body types, and attributes used here.

To use these bodies and bundles, add the following to your policy:

```cf3
body file control
{
	inputs => { "files.cf" }
}
```


[%CFEngine_library_include(lib/files)%]
