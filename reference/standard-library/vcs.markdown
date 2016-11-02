---
layout: default
title: Version Control Bodies and Bundles
published: false
sorting: 100
tags: [reference, standard library]
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
