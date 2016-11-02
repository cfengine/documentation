---
layout: default
title: Commands Bundles and Bodies
published: false
sorting: 20
tags: [reference, standard library]
---

See the [`commands` promises][commands] documentation for a
comprehensive reference on the body types and attributes used here.

To use these bodies, add the following to your policy:

```cf3
body file control
{
	inputs => { "commands.cf" }
}
```


[%CFEngine_library_include(lib/commands)%]
