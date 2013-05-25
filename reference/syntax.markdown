---
layout: default
title: Syntax, identifiers and names
categories: [Reference, Syntax]
published: true
alias: reference-syntax.html
tags: [reference, syntax]
---

The CFEngine 3 language has a few simple rules:

-   CFEngine built-in words, names of variables, bundles, body templates and classes may only contain the usual alphanumeric and underscore characters (`a-zA-Z0-9_`)
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

    matching and expanding on a reference inside a promise of the form `constraint_type => template_identifier`

-   attribute expressions in the body of a promise take the form

      left-hand-side (CFEngine_word) => right-hand-side (user defined data).

    This can take several forms:

             cfengine_word => user_defined_template(parameters)
                              user_defined_template
                              builtin_function()
                              "quoted literal scalar"
                              { list }

    In each of these cases, the right hand side is a user choice.

	CFEngine uses many `constraint expressions' as part of the body of a promise. These take the form: left-hand-side (cfengine word) ‘=>’ right-hand-side (user defined data). This can take several forms:

	    cfengine_word => user_defined_template(parameters)
	        user_defined_template
	        builtin_function()
	        "quoted literal scalar"
	        { list }

	In each of these cases, the right hand side is a user choice.
