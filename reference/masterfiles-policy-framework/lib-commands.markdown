---
layout: default
title: lib/commands.cf
published: true
sorting: 160
tags: [reference, standard library, commands, MPF]
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
