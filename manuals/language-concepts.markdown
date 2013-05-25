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
  ~ A declaration about the *state* we desire to maintain (*e.g.,*
    the permissions or contents of a file, the availability or absence
    of a service, the (de)installation of a package).
* *Promise bundles*
  ~ A collection of promises.
* *Promise bodies*
  ~ A part of a promise which details and constrains its nature.
* *Data types*
  ~ An interpretation of a scalar value: string, integer or real
    number.
* *Variables*
  ~ An association of the form "LVALUE *represents* RVALUE", where
    rval may be a scalar value or a list of scalar values.
* *Functions*
  ~ Built-in parameterized rvalues.
* *Classes*
  ~ CFEngine's boolean classifiers that describe context.

## Syntax, identifiers and names

The CFEngine 3 language has a few simple rules:

-   CFEngine built-in words, and identifiers of your choosing (the
    names of variables, bundles, body templates and classes) may only
    contain the usual alphanumeric and underscore characters
    ('a-zA-Z0-9\_').
-   All other 'literal' data must be quoted.
-   Declarations of promise bundles in the form:

                  bundle agent-type identifier
                  {
                  ...
                  }

    Where `agent-type` is the CFEngine component responsible for maintaining the promise.

-   Declarations of promise body-parts in the form:

                  body constraint_type template_identifier
                  {
                  ...
                  }

    matching and expanding on a reference inside a promise of the form
    'constraint\_type =\> template\_identifier'.

-   CFEngine uses many 'constraint expressions' as part of the
    body of a promise. These take the form: left-hand-side (CFEngine
    word) '=\>' right-hand-side (user defined data). This can take
    several forms:

             cfengine_word => user_defined_template(parameters)
                              user_defined_template
                              builtin_function()
                              "quoted literal scalar"
                              { list }

    In each of these cases, the right hand side is a user choice.
