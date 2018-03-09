---
layout: default
title: Tags for variables, classes, and bundles
published: true
sorting: 14
tags: [tags, meta]
---

## Introduction

CFEngine 3.6.0 makes great use of the `meta` attribute to set tags
on variables and classes. While that attribute was always in the
language, only in 3.6.0 is it fully utilized

Furthermore, bundles can now be tagged and found by tag, so you can
construct a fully dynamic bundle sequence.

## Problem statement

We'd like to apply tags to variables and classes for many purposes,
from stating their provenance (whence they came, why they exist, and
how they can be used) to filtering them based on tags.

We'd also like to be able to include all the files in a directory and
then run all the discovered bundles if they are tagged appropriately.

## Syntax

Tagging variables and classes is easy with the `meta` attribute.
Here's an example that sets the `inventory` tag on a variable and
names the attribute that it represents. This one is actually built
into the standard 3.6.0 inventory policy under
`masterfiles/inventory/any.cf`, so you have it available out
of the box in either Community or Enterprise.

```cf3
bundle agent cfe_autorun_inventory_listening_ports
# @brief Inventory the listening ports
#
# This bundle uses `mon.listening_ports` and is always enabled by
# default, as it runs instantly and has no side effects.
{
  vars:
      "ports" slist => { @(mon.listening_ports) },
      meta => { "inventory", "attribute_name=Ports listening" };
}
```

In the Enterprise Mission Portal, you can then make a report for
"Ports listening" across all your machines. For more details, see
https://docs.cfengine.com/docs/3.10/enterprise-cfengine-guide-reporting.html

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
https://cfengine.com/docs/master/reference-functions-classesmatching.html

* `getvariablemetatags`: get the tags of a variable as an slist. See
https://cfengine.com/docs/master/reference-functions-getvariablemetatags.html

* `variablesmatching`: just like `classesmatching` but for variables.
See https://cfengine.com/docs/master/reference-functions-variablesmatching.html

* `getclassmetatags`: get the tags of a class as an slist. See
https://cfengine.com/docs/master/reference-functions-getclassmetatags.html

There is also a new function to find bundles.

* `bundlesmatching`: find the bundles matching some tags. See
https://cfengine.com/docs/master/reference-functions-bundlesmatching.html
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

In CFEngine Enterprise 3.6.0, you can build reports based on tagged variables
and classes.

Please see
https://docs.cfengine.com/docs/3.10/enterprise-cfengine-guide-reporting.html
for a full tutorial, including troubleshooting possible errors. In
short, this is extremely easy as long as you:

* allow classes and variables with the `inventory` and `report` tags
to be reported in `controls/cf_serverd.cf`. This is already the case
if you install the stock CFEngine 3.6.0 packages.

* ensure there are no report collection issues due to firewalls (TCP
port 5308 must be open from the hub to the agents, for instance)

## Dynamic bundlesequence

Dynamic bundlesequences are extremely easy.  You simply say

```cf3
vars:
  "bundles" slist => bundlesmatching("regex", "tag1", "tag2", ...);

methods:
  "run $(bundles)" usebundle => $(bundles);
```

Then every bundle matching the regular expression `regex` and **all**
the tags will be found and run.

Note that the discovered bundle names will have the namespace prefix,
e.g. `default:mybundle`. The regular expression has to match that. So
`mybundle` as the regular expression would not work. See
https://cfengine.com/docs/master/reference-functions-bundlesmatching.html
for another detailed example.

In fact we found this so useful we
implemented [services autorun][lib/autorun.cf] in
the [masterfiles policy framework][Masterfiles Policy Framework].

There is only one thing to beware. All the bundles have to have the
same number of arguments (0 in the case shown). Otherwise you will get
a runtime error and CFEngine will abort. We recommend only using
0-argument bundles in a dynamic sequence to reduce this risk.

## Summary

Tagging variables and classes and bundles in CFEngine 3.6.0 is easy
and allows more dynamic behavior than ever before. Try it out and see
for yourself how it will change the way you use and think about
system configuration policy and CFEngine.
