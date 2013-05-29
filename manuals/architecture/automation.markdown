---
layout: default
title: Automation with CFEngine
categories: [Manuals, Architecture, Automation]
published: true
alias: manuals-architecture-automation.html
tags: [manuals, systems, configuration management, automation]
---

Users are good at researching solutions and making design decisions, but awful 
at repeated execution. Machines are pitiful at making decisions, but very good 
at reliable implementation at very large scale. It makes sense to let each 
side do the job that they are good at. With CFEngine, users make decisions and 
write promises for machines to implement and satisfy.

A CFEngine user will declare a promise in CFEngine, and CFEngine will then 
translate this promise into a series of actions to implement. For the most 
part, CFEngine understands how to deliver on promises, and they don't need to 
be given explicit instructions for completing tasks. It is your job to make 
decisions about the systems you are managing and to describe those in suitable 
promises. It is CFEngine's job to automate and deliver a promise.

<!--- **TODO** decide if any of this is needed at all in the documentation

This separation of concerns is often violated in systems that require
users to write explicit instructions for even the simplest tasks. If the
client isn't given the power to make decisions about how to implement
promises, then you really haven't automated anything. If you can't trust
the "self-discipline" of individual nodes to deliver on simple promise,
then, as a user, you are really the one responsible for writing and
debugging long procedural automation routines.

This user-centric focus on automation often results in configuration
management systems which are full of ad-hoc, one-off implementations of
important process. These ad-hoc systems are often full of mystery. When
a system is based on ad-hoc, user-driven configuration:

- Others have no idea how a system has been assembled and how it is being managed.

- There is no record of changes or intentions. The only way to understand a complex, ad-hoc system is to walk through the code line by line.

- Systems should be considered damaged, they are figuratively "scarred" from the ad-hoc intervention of a user.

People opposed to automation often say that it dehumanizes their work.
In fact the opposite is true: forcing humans to do the work of machines,
in repetitive and reliable ways is what dehumanizes people. The only way
to make progress with a bad habit is to recognize it as one and be
willing to abandon the habit.
-->

| Previous: [CFEngine Architecture](manuals-architecture.html) | Next: [CFEngine Components](manuals-architecture-components.html) |
