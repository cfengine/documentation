---
layout: default
title: Bodies
published: true
sorting: 20
tags: [language, concepts, syntax, body]
---

While the idea of a promise is very simple, the definition of a promise can 
grow complicated. Complex promises are best understood by breaking them down 
into independent, re-usable components. The CFEngine reserved word `body` is 
used to encapsulate the details of complex promise attribute values. Bodies 
can optionally have parameters.

```cf3
    bundle agent example
    {
      files:
        !windows::
          "/etc/passwd"
            handle => "example_files_not_windows_passwd",
            perms => system;
    
          "/home/bill/id_rsa.pub"
            handle => "example_files_not_windows_bills_priv_ssh_key",
            perms => mog("600", "bill", "sysop"),
            create => "true";
    }
```

The promisers in this example are the files `/etc/passwd` and
`/home/bill/id_rsa.pub`. The promise is that the `perms` attribute type is
associated with a named, user-defined promise body `system` and `mog`
respectively.

```cf3
    body perms system
    {
      mode => "644";
      owners => { "root" };
      groups => { "root" };
    }
    
    body perms mog(mode,user,group)
    {
      owners => { "$(user)" };
      groups => { "$(group)" };
      mode   => "$(mode)";
    }
```

Like [bundles][bundles], bodies have a *type*. The type of the body has to match the left-hand side of the promise attribute in which it is used. In this case, `files` promises have an attribute `perms` that can be associated with any body of type `perms`.

The attributes within the body are then type specific. Bodies of type `perms` consist of the file permissions, the file owner, and the file group, which the instance `system` sets to `644`, `root` and `root`, respectively.

Such bodies can be reused in multiple promises. Like bundles, bodies can have parameters. The body `mog` also consists of the file permissions, file owner, and file group, but the values of those attributes are passed in as parameters.

#### Body Inheritance

CFEngine 3.8 introduced body inheritance via the `inherit_from`
attribute. It's a parameterized single-inheritance system, so a body
can only inherit from one other body, and it can apply parameters. The
two bodies **must** have the same type.

Let's see it with the `system` and `mog` bodies from earlier:

```cf3
    body perms system
    {
      mode => "644";
      owners => { "root" };
      groups => { "root" };
    }

    body perms system_inherited
    {
      inherit_from => mog("644", "root", "root");
    }

```

The earlier `system` body and this `system_inherited` body have the
same effect, eventually applying mode `644`, owner `root`, and group
`root`. But they are created differently: the first by explicitly
listing the parameters; the other by applying parameters to the
`inherit_from` chain of inheritance.

Which one is better? Usually, inheriting from a more generic
specification is considered a better design pattern because it reduces
horizontal complexity. But it's less explicit and some users and sites
will prefer a more explicit listing of body attributes and their
values, as in the `system` body. CFEngine will accomodate either.

Body parameters can be used in the inheritance chain. Here's another
body that inherits from `mog` but takes a mode. All its other
parameters are specified inside the body. So
`system_inherited_mode("234")` is exactly like `mog("234", "root",
"root")`.

```cf3
    body perms system_inherited_mode(mode)
    {
      inherit_from => mog($(mode), "root", "root");
    }

```

Again, whether you prefer this or directly calling the `mog` body is
your choice. Keep in mind that if you want to maintain compatibility
with 3.7 and earlier, `inherit_from` is not available.

Body inheritance simply copies attributes down the chain to the newest
body. The latest wins. Let's see an example with a chain of
inheritance from the `system` body from earlier:

```cf3
    body perms system
    {
      mode => "644";
      owners => { "root" };
      groups => { "root" };
    }

    body perms system_once(x)
    {
      inherit_from => system;
      owners => { $(x) };
      mode => "645";
    }

    body perms system_twice
    {
      inherit_from => system_once("mark");
      mode => "646";
    }

```

The inheritance chain goes from `system` to `system_once` to
`system_twice`. The `owners` attribute in `system_once` will be
whatever `$(x)` is, **overwriting** the value from `system`. Then
`system_twice` will inherit that same `owners` value which is now `"mark"`.

The `mode` attribute will be **overwritten** to `645` in `system_once`
and then **overwritten** to `646` in `system_twice`.

If this gets complicated, just think *"latest wins"*.

#### Implicit, Control Bodies

A special case for bodies are the implicit promises that configure the basic 
operation of CFEngine. These are hard-coded to CFEngine and control the basic 
operation of the agents, such as `cf-agent` and `cf-serverd`. Each agent has a 
special body whose name is `control`.

```cf3
    body agent control
    { 
        bundlesequence => { "test" };
    }
```

This promise bodies configures the `bundlesequence` to execute on a cf-agent.

```cf3
    body server control
    {
        allowconnects         => { "127.0.0.1" , "::1", @(def.acl) };
    }
```

This promise body defines the clients allowed to connect to a cf-serverd. 
For more information, see the reference documentation about the [CFEngine 
Agents][Components and Common Control]

#### Default bodies

CFEngine 3.9 introduced a way to create default bodies. It allows defining, for given
promise and body types, a body that will be used each time no body is defined.
To use a body as default, name it `<promise_type>_<body_type>` and put it
in the `bodydefault` namespace. For example, a default `action` body for `files`
promises will be named `files_action`, and in each `files` promise, if no
`action` attribute is set, the `files_action` action will be used.

**Note:** The default bodies **only** apply to promises in the `default` namespace.

In the following example, we define a default `action` body for `files`
promises, that specifies an `action_policy => "warn"` to prevent actually modifying files
and to only warn about considered modifications. We define it once,
and don't have to explicitly put this body in all our `files` promises.

```cf3
body file control
{
   namespace => "bodydefault";
}

body action files_action
{
    action_policy => "warn";
}

body file control
{
    namespace => "default";
}
```
