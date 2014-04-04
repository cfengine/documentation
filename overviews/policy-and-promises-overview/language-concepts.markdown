---
layout: default
title: Language Concepts
published: true
sorting: 40
tags: [overviews, language, syntax, concepts, promises]
---

There is only one grammatical form for statements in the language:

```cf3
    bundle bundle_type name
    {
    promise_type:

      classes::

        "promiser" -> { "promisee1", "promisee2", ... }

            attribute_1 => value_1,
            attribute_2 => value_2,
            ...
            attribute_n => value_n;
    }
```

You can recognize *everything* in CFEngine from just those few concepts.

* [**Promise**][promises]

A declaration about the *state* we desire to maintain (e.g., the permissions 
or contents of a file, the availability or absence of a service, the 
(de)installation of a package).

* [**Bundles**][bundles]

A collection of promises.

* [**Bodies**][bodies]

A part of a promise which details and constrains its nature, possibly in 
separate and re-usable parts.

* [**Classes**][classes and decisions]

CFEngine's boolean classifiers that describe context.

* [**Variables and Datatypes**][variables]

An association of the form "LVALUE *represents* RVALUE", where RVALUE may be a 
scalar value or a list of scalar values: a string, integer or real number.

This documentation about the language concepts introduces in addition

* [**normal ordering**][Normal Ordering],
* [**loops**][Loops],
* [**pattern matching and referencing**][Pattern Matching and Referencing], 
  and
* [**namespaces**][namespaces]

See the reference documentation for more information about
[Syntax, identifiers and names][Syntax, identifiers and names].
