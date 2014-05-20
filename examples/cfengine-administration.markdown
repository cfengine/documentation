---
layout: default
title: CFEngine Administration Examples
published: true
sorting: 2
tags: [Examples,CFEngine Administration]
---

* [Ordering promises][CFEngine Administration Examples#Ordering promises]
* [Aborting execution][CFEngine Administration Examples#Aborting execution]
* Aborting execution
* Updating from a central policy server

## Ordering promises

This counts to five by default. If we change ‘/bin/echo one’ to ‘/bin/echox one’, then the command will fail, causing us to skip five and go to six instead.

This shows how dependencies can be chained in spite of the order of promises in the bundle.

Normally the order of promises in a bundle is followed, within each promise type, and the types are ordered according to normal ordering.


[%CFEngine_include_example(ordering_promises.cf)%]

## Aborting execution ##


[%CFEngine_include_example(aborting_execution.cf)%]
