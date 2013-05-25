---
layout: default
title: Concept Guide
categories: [Manuals, Concept Guide]
published: true
alias: manuals-concepts.html
tags: [manuals, concepts, language, promise]
---

### What is CFEngine?

At its code, CFEngine is a simple framework based on promises which
supplies a rich standard library of tools to implement and manage very
large systems. The following diagram captures the scope of CFEngine.

![](introduction-cfdude.png)

For many users, CFEngine is simply a configuration tool – i.e. software
for deploying and patching systems according to a policy. Policy is
described using promises. Every statement in CFEngine 3 is a promise to
be kept at some time or location. More than this, however, CFEngine is
not like otherautomation tools that \`roll out' an image of some
software once and hope for the best. Every promise that you make in
CFEngine is continuously verified and maintained. It is not a one-off
operation, but a process that can repairing itself should anything
deviate from the policy.

That clearly places CFEngine in the realm of automation, which often
begs the question: so it's just another scripting language? Certainly,
CFEngine contains a powerful scripting language, but it is not like any
other. CFEngine doesn't use a scripting language like Perl, Python or
Ruby for a reason as these languages often complicate systems and
encourage users to write long procedures instead of declarative
promises. CFEngine language is a language of promises, in which you
express very high-level intentions about a system. CFEngine then takes
the promises and compiles them into real-world action.

### Core concepts

Unlike previous versions of CFEngine, which had no consistent model
for its features, you can recognize *everything* in CFEngine 3 from
just a few concepts.

* *Promise*
  ~ A declaration about the *state* we desire to maintain (*e.g.,*
    the permissions or contents of a file, the availability or absence
    of a service, the (de)installation of a package).
* *Promise bundles*
  ~ A collection of promises.
* *Promise bodies*
  ~ A part of a promise which details and constrains its nature.
* *Data types*
  ~ An interpretation of a scalar value: string, integer or real
    number.
* *Variables*
  ~ An association of the form "LVALUE *represents* RVALUE", where
    rval may be a scalar value or a list of scalar values.
* *Functions*
  ~ Built-in parameterized rvalues.
* *Classes*
  ~ CFEngine's boolean classifiers that describe context.

If you have used CFEngine before then the most visible part of
CFEngine 3 will be its new language interface. Although it has been
clear for a long time that the organically grown language used in
CFEngine 1 and 2 developed many problems, it was not immediately clear
exactly what would be better. It has taken years of research to
simplify the successful features of CFEngine to a single overarching
model. To understand the new CFEngine, it is best to set aside any
preconceptions about what CFEngine is today. CFEngine 3 is a genuine
"next generation" effort, which is a springboard into the future of
system management.



#### Ready to Start?

If you are impatient to get started writing promises, now might be a good time to take a break from Concepts and try out your first promises in the [CFEngine tutorial](http://cfengine.com/manuals/cf3-tutorial.html#First-promises). You may be able to learn promises as you progress through the tutorial, but there are basic concepts such as classes, function, and variables which will in your understand.   If you are in a hurry, go read the Tutorial.  If you want a solid foundation for your use of CFEngine continue reading this concept guide.

