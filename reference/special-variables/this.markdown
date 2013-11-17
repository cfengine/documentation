---
layout: default
title: this
categories: [Reference, Special Variables, this]
published: true
alias: reference-special-variables-context-this.html
tags: [reference, variables, this, this]
---

The context `this` is used to access information about promises during
their execution. It is context dependent and not universally meaningful
or available, but provides a context for variables where one is needed
(such as when passing the value of a list variable into a parameterized
`edit_line` promise from a `files` promise).

```cf3
    bundle agent resolver(s,n)
    { 
    files:
      "$(sys.resolv)" 

          create        => "true",
          edit_line     => doresolv("@(this.s)","@(this.n)"),
          edit_defaults => reconstruct;
    }
```

Note that every unqualified variable is automatically considered to be
in context `this`, so that a reference to the variable `$(foo)` is
identical to referencing `$(this.foo)`. You are strongly encouraged to
**not** take advantage of this behavior, but simply to be aware that if
you attempt to declare a variable name with one of the following special
reserved names, CFEngine will issue a warning (and you can reference
your variable by qualifying it with the bundle name in which it is
declared).

### this.bundle

This variable contains the current bundle name.

### this.handle

This variable points to the promise handle of the currently handled
promise; it is useful for referring to the intention in log messages.

### this.namespace

This variable contains the current namespace name.

### this.promise_filename

This variable reveals the name of the file in which the current promise
is defined.

### this.promise_dirname

This variable contains the directory name of the file in which the
current promise is defined.

### this.promise_linenumber

This variable reveals the line number in the file at which it is used.
It is useful to differentiate otherwise identical reports promises.

### this.promiser

The special variable `$(this.promiser)` is used to refer to the current
value of the promiser itself, in a number of allowed cases, typically
when searches can take place. Current promise types that define
`$(this.promiser)` are: `files`, `processes`, `commands`.

This variable is useful in `files` promises, for instance when using
pattern matching or `depth_search` that implicitly match multiple
objects. In that case, `$(this.promiser)` refers to the currently
identified file that makes the promise. For example:

```cf3
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
```
### this.promiser_uid

This variable refers to the `uid` of the user running the `cf-agent` program.

**Note:** This variable is reported by the platform dependent `getuid` function,
and is always an integer.

### this.promiser_gid

This variable refers to the `gid` of the user running the `cf-agent` program.

**Note:** This variable is reported by the platform dependent `getgid` function,
and is always an integer.

### this.service_policy

In a services promise, this variable is set to the value of the promise 
attribute `service_policy`. For example:

```cf3
    services:

      "www"  service_policy => "start";
      service_bundle => non_standard_services;
```

This is typically used in the adaptations for custom services bundles in
the service methods.

### this.this

From version 3.3.0 on, this variable is reserved. It is used by
functions like `maplist()` to represent the current object in a
transformation map.
