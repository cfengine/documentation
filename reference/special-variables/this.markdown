---
layout: default
title: this
published: true
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
value of the promiser itself.

In `files` promises, where it is practical to use patterns or `depth_search`
to match multiple objects, the variable refers to the file that is currently
making the promise. However, the variable can only be used in selected
attributes:

* `transformer`
* `edit_template`
* [`source`][files#source] in `copy_from`
* `exec_program` in `file_select`
* class names in [`body classes`][Promise Types and Attributes#classes]
* logging attributes in [`body action`][Promise Types and Attributes#action]

For example:

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

This variable refers to the `uid` (user ID) of the user running the `cf-agent` program.

**Note:** This variable is reported by the platform dependent `getuid` function,
and is always an integer.

### this.promiser_gid

This variable refers to the `gid` (group ID) of the user running the `cf-agent` program.

**Note:** This variable is reported by the platform dependent `getgid` function,
and is always an integer.

### this.promiser_pid

This variable refers to the `pid` (process ID) of the `cf-agent` program.

**Note:** This variable is reported by the platform dependent `getpid` function,
and is always an integer.

### this.promiser_ppid

This variable refers to the `ppid` (parent process ID) of the `cf-agent` program.

**Note:** This variable is reported by the platform dependent `getpid` function,
and is always an integer.  On the Windows platform it's always 0.

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
