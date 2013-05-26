---
layout: default
title: file control
categories: [Reference, Common promises, file control]
published: true
alias: reference-common-promises-file-control.html
tags: [body, bodies, common, namespace, promises, bundlesequence]
---

# `file` control promises

    body file control
    {
    namespace => "name1"; 
    }
    
    bundle agent private
    {
    ....
    }



*History*: Was introduced in 3.4.0, Enterprise 3.0.0 (2012)

This directive can be given multiple times within any file,
outside of body and bundle definitions.


    

## `namespace`

**Type**: string

**Allowed input range**: `[a-zA-Z0-9_$(){}\[\].:]+`

**Synopsis**: Switch to a private namespace to protect
current file from duplicate definitions

    body file control
    {
    namespace => "name1"; 
    }

**Notes**:

*History*: Was introduced in 3.4.0, Enterprise 3.0.0 (2012)

This directive can be given within any file, outside of body
and bundle definitions, to change the namespace of
subsequent bundles and bodies, See
[Name spaces](#Name-spaces).

