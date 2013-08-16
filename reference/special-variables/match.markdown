---
layout: default
title: match
categories: [Reference, Special Variables, match]
published: true
alias: reference-special-variables-context-match.html
tags: [reference, variables, match, strings, file editing, files promises, edit_line]
---

Each time CFEngine matches a string, these values are assigned to a special 
variable context `$(match.`*n*`)`. The fragments can be referred to in the 
remainder of the promise. There are two places where this makes sense. One is 
in pattern replacement during file editing, and the other is in searching for 
files.

```cf3
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
```

### match.0

A string matching the complete regular expression whether or not
back-references were used in the pattern.
