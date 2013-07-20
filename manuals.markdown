---
layout: default
title: CFEngine Manuals 
categories: [Manuals]
published: true
sorting: 30
alias: manuals.html
---

At its core, CFEngine is a simple framework which supplies a rich standard 
library of tools to implement and manage very large systems. The following 
diagram captures the scope of CFEngine.

![The Scope of CFEngine](manuals-scope.png)

For many users, CFEngine is simply a configuration tool – i.e. software
for deploying and patching systems according to a policy. Policy is
described using *promises*. Every statement in CFEngine 3 is a promise to
be kept at some time or location. More than this, however, CFEngine is
not like other automation tools that "roll out" an image of some
software once and hope for the best. Every promise that you make in
CFEngine is *continuously verified and maintained*. It is not a one-off
operation, but a process that can repairing itself should anything
deviate from the policy.

That clearly places CFEngine in the realm of automation, which often
begs the question: so it's just another scripting language? Certainly,
CFEngine contains a powerful scripting language, but it is not like any
other. CFEngine language is a *declarative* language of promises, in which you
express very high-level intentions about a system. CFEngine then takes
the promises and compiles them into real-world action.


### Ready to Start?

If you are impatient to [get started][Getting Started] writing promises,
now might be a good time to take a break from concepts and try out your first 
promises. You can study the [examples][CFEngine Examples] and look things up 
in the [reference][CFEngine Reference] as you go along.

If you want a solid foundation for your use of CFEngine, continue reading to 
understand the [design][Design] and [language concepts][Language Concepts] of 
CFEngine.
