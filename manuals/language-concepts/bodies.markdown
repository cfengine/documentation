---
layout: default
title: Bodies
categories: [Manuals, Language Concepts, Bodies]
published: true
alias: manuals-language-concepts-bodies.html
tags: [language, concepts, syntax, body]
---

Previous: [Bundles](manuals-language-concepts-bundles.html)

****

#### Defining Promises

CFEngine's promises are declarative, you tell CFEngine what promises you want 
it to keep, and it keeps them. With CFEngine you can clearly specify the 
desired end-state of a system in the form of promises and let CFEngine take 
care of the rest.

[Promises](manuals-language-concepts-promises.html) are the fundamental 
statements that make up an entire system based on a series of commitments. 
While the idea of a promise is very simple - a commitment or a guarantee to 
satisfy a condition - the definition of a promise can grow complicated. 
Complex promises are best understood by breaking them down into independent 
components.

### Bodies

The CFEngine reserved word `body` is used to encapsulate the details of complex
attribute values. Bodies can optionally have parameters.

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

The `body` of the `system` promise consists of the file permissions, the 
file owner, and the file group. `system` has a type that matches the left 
hand side `perms` of the declaration in the `files` promise. The `body` of the
`mog` promise also consists of the file permissions, file owner, and file group
but the values of those attributes are passed in as parameters.

Such bodies can be reused in multiple promises.


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
Agents](reference-components.html)

****

Next: [Classes](manuals-language-concepts-classes.html)
