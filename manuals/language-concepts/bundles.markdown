---
layout: default
title: Bodies
categories: [Manuals, Language Concepts, Bodies and Bundles]
published: true
alias: manuals-language-concepts-bodies-bundles.html
tags: [language, concepts, syntax, body, bundle]
---

A bundle is a collection of promises. They allow to group related promises 
together into named building blocks that can be thought of as "subroutines" in 
the CFEngine promise language. A number of promises related to configuring a 
web server or a file system you can name those bundles "webserver" or 
"filesystem", respectively.

Like [bodies](manuals-language-concepts-bodies.html), bundles also have 
`types'. Bundles belong to the agent that is used to keep the promises in the 
bundle. So cf-agent has bundles declared as:

    bundle agent my_name
    {
    }

while cf-serverd has bundles declared as:

    bundle server my_name
    {
    }

Bundles can be parameterized, allowing for code re-use. If you need to do the 
same thing over and over again with slight variations, using a promise bundle 
is an easy way to avoid unnecessary duplication in your promises.

**TODO: example for parameterized bundle**

### Scope

Variables and classes defined inside bundles are not directly visible outside 
those bundles. All [variables](manuals-language-concepts-variables.html) in 
CFEngine are globally accessible. However, if you refer to a variable by 
‘$(unqualified)’, then it is assumed to belong to the current bundle. To 
access any other (scalar) variable, you must qualify the name, using the name 
of the bundle in which it is defined:

    $(bundle_name.qualified)

Bundles of type `common` may contain common promises. 
[Classes](manuals-language-concepts-classes.html) defined in `common` bundles 
have global scope.
