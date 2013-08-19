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

You import the CFEngine Standard Library into your CFEngine policy like this:

```cf3
body common control
{
    inputs => { "cfengine_stdlib.cf" };
}
```

## Common Bodies

[%CFEngine_library_include(lib/3.6/common)%]

[%CFEngine_library_include(lib/3.6/bundles)%]

## Commands

[%CFEngine_library_include(lib/3.6/commands)%]

## Databases

[%CFEngine_library_include(lib/3.6/databases)%]

## Files

[%CFEngine_library_include(lib/3.6/files)%]

## Feature

[%CFEngine_library_include(lib/3.6/feature)%]

## Guest Environments

[%CFEngine_library_include(lib/3.6/guest_environments)%]

## Monitor

[%CFEngine_library_include(lib/3.6/monitor)%]

## Packages

[%CFEngine_library_include(lib/3.6/packages)%]

## Paths

[%CFEngine_library_include(lib/3.6/paths)%]

## Processes

[%CFEngine_library_include(lib/3.6/processes)%]

## Services

[%CFEngine_library_include(lib/3.6/services)%]

## Storage

[%CFEngine_library_include(lib/3.6/storage)%]
