---
layout: default
title: lib/vcs.cf
published: true
sorting: 160
tags: [reference, standard library, vcs, MPF]
---

The `vcs.cf` library provides bundles for working with version control tools.

To use these bodies, add the following to your policy:

```cf3
body file control
{
	inputs => { "vcs.cf" }
}
```

[%CFEngine_library_include(lib/vcs)%]
