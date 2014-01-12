---
layout: default
title: Standard Library
categories: [Reference, Standard Library]
published: true
sorting: 90
alias: reference-standard-library.html
tags: [reference, standard library]
---

The standard library is a lingua franca of standard nuts'n'bolts definitions 
that you can use to build up solutions within CFEngine. It is an interface 
layer that brings industry-wide standardization of CFEngine configuration 
scripting and hides the technical details.

You import elements of the CFEngine Standard Library into your CFEngine policy like this:

```cf3
body file control
{
    inputs => { "files.cf", "packages.cf" };
}
```

**TODO**

To import the entire standard library, use:

```cf3
body file control
{
	inputs => { "cfengine_stdlib.cf"}
}
```

## Feature

To use these bodies, add

```cf3
body file control
{
	inputs => { "features.cf" }
}
```

to your policy.

[%CFEngine_library_include(lib/3.6/feature)%]

## Paths

To use these bodies, add

```cf3
body file control
{
	inputs => { "paths.cf" }
}
```

to your policy.

[%CFEngine_library_include(lib/3.6/paths)%]

