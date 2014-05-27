---
layout: default
title: About Policies and Promises
sorting: 1 
published: true
tags: [overviews, promises overview]
---

Central to CFEngine's effectiveness in system administration is an intuitive tool called a `promise`, which defines the intent and expectation of how some part of an overall system should behave. 

CFEngine is a system that emphasizes the promises a client makes to the overall CFEngine network. Combining promises with patterns to describe where and when promises should apply is what CFEngine is all about.

This document describes in brief what a promise is and what a promise does. There are other resources for finding out additional details about `promises` in the See Also section at the end of this document.

## What Are Promises ##

A promise is the documentation or definition of an intention to act or behave in some manner. They are the rules which CFEngine clients are responsible for implementing. 

### The Value of a Promise ###

When you make a promise it is an effort to improve trust, which is an economic time-saver. If you have trust then there is less need to verify, which in turn saves time and money.

When individual components are empowered with clear guidance, independent decision making power, and the trust that they will fulfil their duties, then systems that are complex and scalable, yet still manageable, become possible. 

### Anatomy of a Promise ###

```cf3
bundle agent hello_world
{
  reports:

    any::

      "Hello World!"
        comment => "This is a simple promise saying hello to the world.";

}
```

See Also: [Write Promises and Policy][Write Promises and Policy]



See Also: 

* [Write Promises and Policy][Write Promises and Policy]
* [Authoring Policy Tools & Workflow][Authoring Policy Tools & Workflow]
* [Promises Available in CFEngine][Promises Available in CFEngine]
* [Promises][Promises]



