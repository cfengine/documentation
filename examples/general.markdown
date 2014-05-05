---
layout: default
title: General Examples 
published: true
sorting: 1
tags: [Examples]
---

* [Basic Example][General Examples#Basic Example]
* [Hello world][General Examples#Hello world]
* [Array example][General Examples#Array example]

## Basic Example ##

To get started with CFEngine, you can imagine the following template for entering examples. This part of the code is common to all the examples.

```cf3
body common control
{
bundlesequence => { "main" };
inputs => { "cfengine_stdlib.cf" };
}


bundle agent main
{
# example

}

```

Then you enter the cases as below. The general pattern of the syntax is like this (colors in html version: red, CFEngine word; blue, user-defined word):

```cf3
# The general pattern

bundle component name(parameters)
{ 
what_type:
 where_when::

  # Traditional comment


  "promiser" -> { "promisee1", "promisee2" },
        comment => "The intention ...",
         handle => "unique_id_label",
    attribute_1 => body_or_value1,
    attribute_2 => body_or_value2;
}

```