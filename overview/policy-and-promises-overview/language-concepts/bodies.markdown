---
layout: default
title: Bodies
published: true
sorting: 30
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

This promise bodies defines the clients allowed to connect to a cf-serverd. 
For more information, see the reference documentation about the [CFEngine 
Agents][Components and Common Control]
