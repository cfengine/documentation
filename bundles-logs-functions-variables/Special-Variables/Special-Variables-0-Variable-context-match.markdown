---
layout: default
title: Variable-context-match
categories: [Special-Variables,Variable-context-match]
published: true
alias: Special-Variables-Variable-context-match.html
tags: [Special-Variables,Variable-context-match]
---

### Variable context `match`

\

Each time CFEngine matches a string, these values are assigned to a
special variable context `$(match.`n`)`. The fragments can be referred
to in the remainder of the promise. There are two places where this
makes sense. One is in pattern replacement during file editing, and the
other is in searching for files.

Consider the examples below:

~~~~ {.verbatim}
bundle agent testbundle

{
files:

  "/home/mark/tmp/(cf[23])_(.*)"
       create    => "true",
       edit_line => myedit("second $(match.2)");


  # but more specifically...

  "/home/mark/tmp/cf3_(test)"
       create    => "true",
       edit_line => myedit("second $(match.1)");


}
~~~~

-   [Variable match.0](#Variable-match_002e0)

#### Variable match.0

\

A string matching the complete regular expression whether or not
back-references were used in the pattern.
