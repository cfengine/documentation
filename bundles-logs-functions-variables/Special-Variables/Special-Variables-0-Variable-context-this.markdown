---
layout: default
title: Variable-context-this
categories: [Special-Variables,Variable-context-this]
published: true
alias: Special-Variables-Variable-context-this.html
tags: [Special-Variables,Variable-context-this]
---

### Variable context `this`

\

This context this is used to access information about promises during
their execution. It is context dependent and not universally meaningful
or available, but provides a context for variables where one is needed
(such as when passing the value of a list variable into a parameterized
`edit_line` promise from a `file` promise). For example:

~~~~ {.verbatim}
bundle agent resolver(s,n)
{ 
files:
  "$(sys.resolv)" 

      create        => "true",
      edit_line     => doresolv("@(this.s)","@(this.n)"),
      edit_defaults => reconstruct;
}
~~~~

Note that every unqualified variable is automatically considered to be
in context this, so that a reference to the variable `$(foo)` is
identical to referencing `$(this.foo)`. You are strongly encouraged to
**not** take advantage of this behaviour, but simply to be aware that if
you attempt to declare a variable name with one of the following special
reserved names, CFEngine will issue a warning (and you can reference
your variable by qualifying it with the bundle name in which it is
declared).

-   [Variable this.handle](#Variable-this_002ehandle)
-   [Variable
    this.promise\_filename](#Variable-this_002epromise_005ffilename)
-   [Variable
    this.promise\_linenumber](#Variable-this_002epromise_005flinenumber)
-   [Variable this.promiser](#Variable-this_002epromiser)
-   [Variable service\_policy](#Variable-service_005fpolicy)
-   [Variable this.this](#Variable-this_002ethis)

#### Variable this.handle

This variable points to the promise handle of the currently handled
promise; it is useful for referring to the intention in log messages.

#### Variable this.promise\_filename

This variable reveals the name of the file in which the current promise
is defined.

#### Variable this.promise\_linenumber

This variable reveals the line number in the file at which it is used.
It is useful to differentiate otherwise identical reports promises.

#### Variable this.promiser

The special variable `$(this.promiser)` is used to refer to the current
value of the promiser itself, in a number of allowed cases, typically
when searches can take place. Current promise types that define
`$(this.promiser)` are: `files`, `processes`, `commands`.

This variable is useful in `files` promises, for instance when using
pattern matching or `depth_search` that implicitly match multiple
objects. In that case, `$(this.promiser)` refers to the currently
identified file that makes the promise. For example:

~~~~ {.verbatim}
bundle agent find666
{
files:
  "/home"
    file_select => world_writeable,
    transformer => "/bin/echo DETECTED $(this.promiser)",
    depth_search => recurse("inf");

  "/etc/.*"
    file_select => world_writeable,
    transformer => "/bin/echo DETECTED $(this.promiser)";
}

body file_select world_writeable
{
  search_mode => { "o+w" };
  file_result => "mode";
}
~~~~

#### Variable service\_policy

This variable is set to the values of the promise attribute
`service_policy`. For example:

~~~~ {.verbatim}
services:

  "www"  service_policy => "start";
~~~~

This is typically used in the adaptations for custom services bundles in
the service methods (See [service\_method in
services](#service_005fmethod-in-services)).

#### Variable this.this

From version core 3.3.0 this variables is reserved. It is used by
functions like `maplist()` to represent the current object in a
transformation map.
