---
layout: default
title: Language Concepts
categories: [Manuals, Language Concepts]
published: true
alias: manuals-language-concepts.html
tags: [manuals, language, syntax, concepts, promises]
---

You can recognize *everything* in CFEngine 3 from just a few concepts.

* [**Promise**](manuals-language-concepts-promises.html)

A declaration about the *state* we desire to maintain (e.g., the permissions 
or contents of a file, the availability or absence of a service, the 
(de)installation of a package).

* [**Promise bundles**](manuals-language-concepts-bundles.html)

A collection of promises.

* [**Promise bodies**](manuals-language-concepts-bodies.html)

A part of a promise which details and constrains its nature.

* [**Classes**](manuals-language-concepts-classes.html)

CFEngine's boolean classifiers that describe context.

* [**Variables and Datatypes**](manuals-language-concepts-variables.html)

An association of the form "LVALUE *represents* RVALUE", where rval may be a 
scalar value or a list of scalar values. An interpretation of a scalar value: 
string, integer or real number.

This documentation about the language concepts introduces in addition

* [**normal ordering**](manuals-language-concepts-normal-ordering.html),
* [**loops**](manuals-language-concepts-loops.html),
* [**pattern matching and 
referencing**](manuals-language-concepts-pattern-matching-and-referencing.html), and
* [*namespaces*](manuals-language-concepts-namespaces.html)

See the reference documentation for more information about
[Syntax, identifiers and names](reference-syntax.html).

****

Next: [*Promises*](manuals-language-concepts-promises.html)
