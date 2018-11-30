---
layout: default
title: lib/files.cf
published: true
sorting: 160
tags: [reference, standard library, files, MPF]
---

See the [`files` promises][files] and [`edit_line` bundles][edit_line]
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
