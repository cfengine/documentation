---
layout: default
title: Commands Bundles and Bodies
categories: [Reference, Standard Library, commands]
published: true
sorting: 20
alias: reference-standard-library-commands.html
tags: [reference, standard library]
---

See the documentation of [`commands` promises][commands] for a
comprehensive reference on the body types and attributes used here.

To use these bodies, add

```cf3
body file control
{
	inputs => { "commands.cf" }
}
```

to your policy.

[%CFEngine_library_include(lib/3.6/commands)%]

