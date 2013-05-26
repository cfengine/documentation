---
layout: default
title: Bundles for Common
categories: [Reference, Common promises]
published: true
alias: reference-bundles-for-common.html
tags: [reference, bundles, common]
---

Common bundles may only contain the promise types that are common to all bodies. Their main function is to define cross-component global definitions.

Common bundles are observed by every agent, whereas the agent specific bundle types are ignored by components other than the intended recipient.

```cf3
     
     bundle common globals
     {
     vars:
     
       "global_var" string = "value";
     
     classes:
     
       "global_class" expression = "value";
     }
     
```
