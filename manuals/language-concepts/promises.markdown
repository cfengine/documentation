---
layout: default
title: Promises
categories: [Manuals, Language Concepts, Promises]
published: true
alias: manuals-language-concepts-promises.html
tags: [manuals, language, syntax, concepts, promises]
---

Previous: [*Language Concepts*](manuals-language-concepts.html)

****

One concept in CFEngine should stand out from the rest as being the most 
important: promises. Everything else is just an abstraction that allows us to 
declare promises and model the various actors in the system.

## Everything is a Promise

Everything in CFEngine 3 can be interpreted as a promise. Promises can be made 
about all kinds of different subjects, from file attributes, to the execution 
of commands, to access control decisions and knowledge relationships. If you 
are managing a system that serves web pages you may define a promise that port 
80 needs to be open on a web server. This same web server may also define a 
promise that a particular directory has a particular set of permissions and 
the proper owner to serve web pages via Apache.

This simple but powerful idea allows a very practical uniformity in CFEngine 
syntax. 

### Promise Types

The `promise_type` defines what kind of object is making the promise. The type 
dictates how CFEngine interprets the promise body. These promise types are straightforward: The `files` promise type deals with file permissions and file content, and the `packages` promise type allows you to work with packaging systems such as rpm and apt.

Some promise types are common to all CFEngine components, while others can only be executed by one of them. `cf-serverd` cannot keep `packages` promises, and `cf-agent` cannot keep `access` promises. See the
[Promise Type reference](reference-promise-types.html) for a comprehensive list of promise types.

### The Promiser

The promiser is an object affected by a promise, and this can be anything: a 
file, a port on a network. It is the entity that is making a promise that a 
certain fact will be true. These facts are listed in the form of 
**attributes** and **values**. A file could promise that a permission 
attribute has a particular value (i.e. 775 permission value) and that an owner 
attribute has another value (i.e. "root").

When a promise is made in CFEngine it is made to another entity - a 
**promisee**. A promisee is an optional part of a promise declaration. The 
promisee can help provide insight into the system's configuration, and may 
become relevant as your system grows in complexity.

The **classes** in a promise control the conditions that make the promise 
valid. Examples are the operating system on which the policy is executed, or 
the day of the week. More about that in the [classes and decision 
making](manuals-language-concepts-classes.html) section.

Not all of these elements are necessary every time, but when you combine them 
they enable a wide range of behavior.

### Promise Example

```cf3
     # Promise type
     files:     
         "/home/mark/tmp/test_plain" -> "system blue team",
             create  => "true",
             perms   => owner("@(usernames)"),
             comment => "Hello World";
```

In this example, the promise is about a file named `test_plain` in the 
directory `/home/mark/tmp`, and the promise is made to some entity named 
`system blue team`. The `create` attribute instructs CFEngine to create the 
file if it doesn't exist. It has a list of owners that is defined by a 
variable named "usernames" (see the documentation about 
[Bodies](manuals-language-concepts-bodies.html) for more details on this last 
expression).

The comment attribute in this example can be added to any promise. It has no 
actual function other than to provide more information to the user in error 
tracing and auditing.

This is a promise that will affect the state of a file on the filesystem. In 
CFEngine you can do this without having to execute the `touch`, `chmod`, and 
`chown` commands. CFEngine is declarative: you declare a contract (or a 
promise) that you want CFEngine to keep and you leave the details up to the 
tool.

### Implicit Promises

Some promise types can have implicit behavior. For example, the following 
promise simply prints out a log message "hello world".

```cf3
     reports:     
     "hello world";
```

The same promise could be implemented using the `commands` type, invoking the 
echo command:

````cf3
     commands:     
     "/bin/echo hello world";
````

These two promises have default attributes for everything except the 
`promiser'. Both promises simply cause CFEngine to print a message.

****

Next: [Bundles](manuals-language-concepts-bundles.html)
