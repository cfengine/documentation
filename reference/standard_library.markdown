---
layout: default
title: Standard Library
categories: [Reference, Standard Library]
published: true
sorting: 90
alias: reference-standard-library.html
tags: [reference, standard library]
---

The standard library contains commonly-used promise bundles and bodies. It provides definitions 
that you can use to build up solutions within CFEngine. The standard library is an interface 
layer that brings industry-wide standardization of CFEngine configuration 
scripting and hides the technical details.

To import elements of the CFEngine Standard Library into your CFEngine policy, enter the following: 

```cf3
body file control
{
    inputs => { "files.cf", "packages.cf" };
}
```

**TODO**

To import the entire CFEngine Standard Library, enter the following:

```cf3
body file control
{
	inputs => { "cfengine_stdlib.cf"}
}
```

## Feature

To use these bundles, add the following to your policy:

```cf3
body file control
{
	inputs => { "features.cf" }
}
```


[%CFEngine_library_include(lib/3.6/feature)%]

## Paths

To use these bundles, add the following to your policy:

```cf3
body file control
{
	inputs => { "paths.cf" }
}
```


[%CFEngine_library_include(lib/3.6/paths)%]

