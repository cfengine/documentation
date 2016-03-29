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


[%CFEngine_include_snippet(basic_example.cf, .* )%]

# The general pattern

The general pattern of the syntax is like this (colors in html version: red, CFEngine word; blue, user-defined word):

```cf3
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

## Hello world


[%CFEngine_include_snippet(hello_world.cf, .* )%]

## Array example ##

[%CFEngine_include_snippet(array_example.cf, .* )%]

