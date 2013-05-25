---
layout: default
title: Loops
categories: [Manuals, Concept Guide, Loops]
published: true
alias: manuals-concept-loops.html
tags: [manuals, concepts, loops, language]
---

### Loops

If you are looking for loops in CFEngine then we need to reprogram you a little, as you are thinking like a programmer! 

There are no loops.  There is no imperative, procedural language involved in CFEngine promises. CFEngine is not a programming language that is meant to give you low level control, but rather a set of declarations that embody processes.  Loops are executed implicitly in CFEngine, but there is no visible mechanism for it – because that would steal attention from the intention of the promises. The way to express them is through lists.

Loops are really a way to iterate a variable over a list. Try the following.

```cf3
    body common control
    {
        bundlesequence  => { "example" };
    }

    bundle agent example
    {
        vars:
            "component" slist => { "cf-monitord", "cf-serverd", "cf-execd" };

            "array[cf-monitord]" string => "The monitor";
            "array[cf-serverd]" string => "The server";
            "array[cf-execd]" string => "The executor, not executionist";

        reports:
            cfengine_3::
                "$(component) is $(array[$(component)])";
    }
````

The output looks something like this:
 
     /usr/local/sbin/cf-agent -f ./unit_loops.cf -K
     
     cf-monitord is The monitor
     cf-serverd is The server
     cf-execd is The executor, not executionist

You see from this that, if we refer to a list variable using the scalar reference operator ‘$()’, CFEngine interprets this to mean “please iterate over all values of the list”. Thus, we have effectively a `foreach' loop, without the attendant syntax.
