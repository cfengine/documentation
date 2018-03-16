---
layout: default
title: Tags for variables, classes, and bundles
published: true
sorting: 14
tags: [tags, meta]
---

## Introduction

*meta tags* can be attached to any promise type using the `meta` attribute.
These tags are useful for cross-referencing related promises. `bundles`, `vars`
and `classes` can be identified and leveraged in different ways within policy
using these tags.

## Problem statement

We'd like to apply tags to variables and classes for many purposes,
from stating their provenance (whence they came, why they exist, and
how they can be used) to filtering them based on tags.

We'd also like to be able to include all the files in a directory and
then run all the discovered bundles if they are tagged appropriately.

## Syntax

Tagging variables and classes is easy with the `meta` attribute. Here's an
example that sets the `inventory` tag on a variable and names the attribute that
it represents. This one is actually built into the standard
[MPF inventory policy][inventory/any.cf#cfe_autorun_inventory_listening_ports],
so it's available out of the box in either Community or Enterprise.

[%CFEngine_include_snippet(inventory/any.cf, bundle\s+(agent|common)\s+cfe_autorun_inventory_listening_ports, \})%]

In the Enterprise Mission Portal, you can then make a report for
"Ports listening" across all your machines. For more details, see
[Enterprise Reporting][Enterprise Reporting]

Class tags work exactly the same way, you just apply them to a
`classes` promise with the `meta` attribute.

Tagging bundles is different because you have to use the `meta`
promise type (different from the `meta` attribute).

An example is easiest:

```cf3
bundle agent run_deprecated
{
  meta:
      "tags" slist => { "deprecated" };
}
```

This declares an agent bundle with a single tag.

## Functions

Several new functions exist to give you access to variable and class
tags, and to find classes and variables with tags.

* `classesmatching`: this used to be somewhat available with the
`allclasses.txt` file. You can now call a function to get all the
defined classes, optionally filtering by name and tags. See
[classesmatching][classesmatching]

* `getvariablemetatags`: get the tags of a variable as an slist. See
[getvariablemetatags][getvariablemetatags]

* `variablesmatching`: just like `classesmatching` but for variables.
See [variablesmatching][variablesmatching]

* `variablesmatching_as_data`: like `variablesmatching` but the matching
variables and values are returned as a merged data container. See
[variablesmatching_as_data][variablesmatching_as_data]

* `getclassmetatags`: get the tags of a class as an slist. See
[getclassmetatags][getclassmetatags]

* `bundlesmatching`: find the bundles matching some tags. See
[bundlesmatching][bundlesmatching]
(the example shows how you'd find a `deprecated` bundle like
`run_deprecated` earlier).

## Module protocol

The module protocol has been extended to support tags. You set the
tags on a line and they persist for every subsequent variable or
class.

```
^meta=inventory
+x
=a=100
^meta=report,attribute_name=My vars
+y
=n=100
```

This will create class `x` and variable `a` with tag `inventory`.

Then it will create class `y` and variable `b` with tags `report` and
`attribute_name=My vars`.

## Enterprise Reporting with tags

In CFEngine Enterprise, you can build reports based on tagged variables and
classes.

Please see [Enterprise Reporting][Enterprise Reporting] for a full tutorial,
including troubleshooting possible errors. In short, this is an extremely easy
way to categorize various data accessible to the agent.

## Dynamic bundlesequence

Dynamic bundlesequences are extremely easy. First you find all the bundles whos
name matches a regular expression and N tags.

```cf3
vars:
  "bundles" slist => bundlesmatching("regex", "tag1", "tag2", ...);
```

Then every bundle matching the regular expression `regex` and **all**
the tags will be found and run.

```cf3
methods:
  "run $(bundles)" usebundle => $(bundles);
```

Note that the discovered bundle names will have the namespace prefix,
e.g. `default:mybundle`. The regular expression has to match that. So
`mybundle` as the regular expression would not work. See
[bundlesmatching][bundlesmatching]
for another detailed example.

In fact we found this so useful we
implemented [services autorun][lib/autorun.cf] in
the [masterfiles policy framework][Masterfiles Policy Framework].

There is only one thing to beware. All the bundles have to have the
same number of arguments (0 in the case shown). Otherwise you will get
a runtime error and CFEngine will abort. We recommend only using
0-argument bundles in a dynamic sequence to reduce this risk.

## Summary

Tagging variables and classes and bundles in CFEngine is easy and allows more
dynamic behavior than ever before. Try it out and see for yourself how it will
change the way you use and think about system configuration policy and CFEngine.
