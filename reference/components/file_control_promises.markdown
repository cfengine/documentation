---
layout: default
title: file control
categories: [Reference, Components, file control]
published: true
alias: reference-components-file-control.html
tags: [body, bodies, components, common, namespace, promises, bundlesequence]
---


```cf3
    body file control
    {
    namespace => "name1"; 
    }
    
    bundle agent private
    {
    ....
    }
```

*History*: Was introduced in 3.4.0, Enterprise 3.0.0 (2012)

This directive can be given multiple times within any file,
outside of body and bundle definitions.


### namespace

**Synopsis**: Switch to a private namespace to protect
current file from duplicate definitions

**Type**: `string`

**Allowed input range**: `[a-zA-Z0-9_$(){}\[\].:]+`

**Example**:

    body file control
    {
    namespace => "name1"; 
    }

**Notes**:

*History*: Was introduced in 3.4.0, Enterprise 3.0.0 (2012)

This directive can be given within any file, outside of body and bundle 
definitions, to change the 
[namespace](manuals-language-concepts-namespaces.html) of subsequent bundles 
and bodies.
