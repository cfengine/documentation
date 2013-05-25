---
layout: default
title: Promises
categories: [Manuals, Concept Guide, Promises]
published: true
alias: manuals-concepts-promises.html
tags: [manuals, concepts, promises]
---


One concept in CFEngine should stand out from the rest as being the most important: promises.   Everything else is just an abstraction that allows us to declare promises and model the various actors in the system, but if you wanted to summarize CFEngine concepts in a single sentence that sentence would be:

CFEngine is a platform for defining and delivering promises.

In this chapter, we're going to fill out this conceptual model to talk about promises, but also to talk about some of the terminology CFEngine uses to define how promises relate to the systems you are managing.  In this chapter, you'll start to see some of the syntax used to define promises including types and classes.

### Everything is a Promise

Everything in CFEngine 3 can be interpreted as a promise. Promises can be made about all kinds of different subjects, from file attributes, to the execution of commands, to access control decisions and knowledge relationships.   If you are managing a system that serves web pages you may define a promise that port 80 needs to be open on a web server.   This same web server may also define a promise that a particular directory has a particular set of permissions and the proper owner to serve web pages via Apache.  

This simple but powerful idea allows a very practical uniformity in CFEngine syntax. There is only one grammatical form for statements in the language that you need to know and promise definitions follow this general syntax:

    type:
     
    classes::
     
        "promiser" -> { "promisee1", "promisee2", ... }
     
            attribute_1 => value_1,
            attribute_2 => value_2,
            ...
            attribute_n => value_n;

There are many concepts in the previous code listing: type, class, promiser, promisee, attributes, and values.   This chapter will define all of these concepts individually, but let's focus on the promiser and the promisee.

#### Promise Concepts: Type, Class, Attribute, and Value

A +promiser+ is an object affected by a promise, and this can be anything: a file, a port on a network.   Some entity that is making a promise that a certain fact will be true.   These facts are listed in the form of +attributes+ and +values+.  A file could promise that a permission attribute has a particular value (i.e. 775 permission value) and that an owner attribute has another value (i.e. "root").

When a promise is made in CFEngine it is made to another entity - a +promisee+.  This concept guide doesn't dwell on the promisee, but in certain CFEngine administrative tools the promisee can help provide insight to CFEngine users.  For now all you need to know about a promisee is that it is an optional part of a promise declaration that may become relevant as your system grows in complexity.

The +type+ of the promise tells us what the promise is about: what kind of promise we are dealing with.   The type is a label that has meaning to a CFEngine administrator and which dictates how CFEngine interprets the promise body.

The +classes+ in a promise control the conditions that make the promise valid.   You'll see a listing of available classes later in this chapter, but you can have a class that makes a particular promise defition relevant to a particular operating system or any other context you can think of such as the day of the week. 

Not all of these elements are necessary every time, but when you combine them they enable a wide range of behavior.

#### Promise Example

Next, consider a real promise example .   This promise ensures that there is a file named "test_plain" in the directory "/home/mark/tmp".   It is making a promise to some entity named "system blue team", and the promise is that the file will have a list of owners that is defined by a variable named "usernames".  The create attribute instructs CFEngine to create the file if it doesn't exist.  The comment attribute in this example can be added to any promise.  It has no actual function other than to provide more information to the user in error tracing and auditing.

```cf3
     # Promise type
     files:
     
         "/home/mark/tmp/test_plain" -> "system blue team",
     
             comment => "Hello World",
             perms   => owner("@(usernames)"),
             create  => "true";
```

You see several kinds of objects in this example. All literal strings (e.g. "true") in CFEngine 3 must be quoted. This provides absolute consistency and makes type-checking easy and error-correction powerful. All function-like objects (e.g. users("..")) are either built-in special functions or parameterized templates. Not everything in this previous example can be explained without diving into variable references and special functions, but you should be able to decipher what this promise it promising from the clear syntax of a promise.

The key point is that this is a promise that will affect the state of file on the filesystem.   In CFEngine you can do this without having to execute the +touch+, +chmod+, and +chown+ commands.  CFEngine is declarative, you are declaring a contract (or a promise) that you want CFEngine to keep and you are leaving the details up to the tool.

#### Implicit Promises

Promises often contain implicit behavior.   While we generally recommend promise writers be very explicit to make it easy to understand promise, there can be cases which call for simplicity.   For example, the following promise simply prints out a log message "hello world".   In this case, all that was needed was a +type+ "reports" and a string literal which is automatically interpreted as a log message.

```cf3
     reports:
     
     "hello world";
```

The same promise could be implemented using the "commands" type in concert with the echo command:

````cf3
     commands:
     
     "/bin/echo hello world";
````

The two previous promises have default attributes for everything except the `promiser' which isn't needed as both promises simply cause CFEngine to print a message.

#### Promise Types

There is one mystery yet to be explained: what is a type?  The types your seen so far, "commands", "reports", and "files", these are built-in promise types. Promise types generally belong to a particular component of CFEngine, as the components are designed to keep different kinds of promises. A few types, such as vars, classes and reports are common to all the different component bundles.   Here is a list of types available in CFEngine:

    vars::
        A promise to be a variable, representing a value. 

    classes::
        A promise to be a class representing a state of the system. 

    reports::
        A promise to report a message.

These following promise types may be used only in agent bundles

    commands::
        A promise to execute a command. 

    databases::
        A promise to configure a database. 

    files::
        A promise to configure a file, including its existence, attributes and contents. 

    interfaces::
        A promise to configure a network interface. 

    methods::
        A promise to take on a whole bundle of other promises. 

    packages::
        A promise to install a package. 

    storage::
        A promise to verify attached storage.

These promise types belong to other components:

    access::
        A promise to grant or deny access to file objects in cf-serverd. 

    measurements::
        A promise to measure or sample data from the system, for monitoring or reporting in cf-monitord (CFEngine Nova and above). 

    roles::
        A promise to allow certain users to activate certain classes when executing cf-agent remotely, in cf-serverd. 

Some promise types are straightforward.  The "files" promise type deals with file permissions and file content, and the "packages" promise type allows you to work with packaging systems such as rpm and apt.  Other promise types deal with defining variables and classes to be used in CFEngine and are beyond the scope of this concept guide.  For a full explanation of promise types, see the CFEngine reference manual.
