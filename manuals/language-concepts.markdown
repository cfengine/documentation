---
layout: default
title: Language Concepts
categories: [Manuals, Language Concepts]
published: true
alias: manuals-language-concepts.html
tags: [manuals, language, syntax, concepts, promises]
---

You can recognize *everything* in CFEngine 3 from just a few concepts.

* *Promise*

A declaration about the *state* we desire to maintain (e.g., the permissions 
or contents of a file, the availability or absence of a service, the 
(de)installation of a package).

* *Promise bundles*

A collection of promises.

* *Promise bodies*

A part of a promise which details and constrains its nature.

* *Data types*

An interpretation of a scalar value: string, integer or real number.

* *Variables*

An association of the form "LVALUE *represents* RVALUE", where rval may be a 
scalar value or a list of scalar values.

* *Functions*

Built-in parameterized rvalues.

* *Classes*

CFEngine's boolean classifiers that describe context.

See the  reference documentation for more information about
[Syntax, identifiers and names](reference-syntax.html).
