---
layout: default
title: Bodies
categories: [Manuals, Language Concepts, Bodies]
published: true
alias: manuals-language-concepts-bodies.html
tags: [language, concepts, syntax, body]
---

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

The CFEngine reserved word `body` is used to define parameterized **TODO: no 
example given for parameterized*** templates that encapsulate the details of 
complex attribute values.

```cf3
    files:
        "/home/promiser"
            perms => myexample;
```

The promiser in this example is a file `/tmp/promiser` and the promise is that 
the `perms` attribute type is associated with a named, user-defined promise 
body `myexample`.

```cf3
    body perms myexample
    {
        mode => "644";
        owners => { "mark", "sarah", "angel" };
        groups => { "users", "sysadmins", "mythical_beasts" };
     }
```

The `body` of this `myexample` promise consists of the file permissions, the 
file owners, and the file groups. `myexample` has a type that matches the left 
hand side `perms` of the declaration in the `files` promise.

Such a body can be reused in multiple promises.

#### Implicit, Control Bodies

A special case for bodies are the implicit promises that configure the basic 
operation of CFEngine. These are hard-coded to CFEngine and control the basic 
operation of the agents, such as cf-agent and cf-serverd. Each agent has a 
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
