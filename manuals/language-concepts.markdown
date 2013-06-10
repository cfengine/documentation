---
layout: default
title: Language Concepts
categories: [Manuals, Language Concepts]
published: true
sorting: 40
alias: manuals-language-concepts.html
tags: [manuals, language, syntax, concepts, promises]
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

* [**Bundles**](manuals-language-concepts-bundles.html)

A collection of promises.

* [**Bodies**](manuals-language-concepts-bodies.html)

A part of a promise which details and constrains its nature, possibly in 
separate and re-usable parts.

* [**Classes**](manuals-language-concepts-classes.html)

CFEngine's boolean classifiers that describe context.

* [**Variables and Datatypes**](manuals-language-concepts-variables.html)

An association of the form "LVALUE *represents* RVALUE", where RVALUE may be a 
scalar value or a list of scalar values: a string, integer or real number.

This documentation about the language concepts introduces in addition

* [**normal ordering**](manuals-language-concepts-normal-ordering.html),
* [**loops**](manuals-language-concepts-loops.html),
* [**pattern matching and 
referencing**](manuals-language-concepts-pattern-matching-and-referencing.html), and
* [**namespaces**](manuals-language-concepts-namespaces.html)

See the reference documentation for more information about
[Syntax, identifiers and names](reference-syntax.html).

****

Next: [*Promises*][Promises]
