---
layout: default
title: CFEngine 3.6
published: true
sorting: 1
---

CFEngine is a configuration management system that provides a framework for automated management of IT infrastructure throughout its life cycle.

CFEngine is decentralized and highly scalable. It is powered by autonomous agents that can continuously monitor, self-repair, and update or restore an entire IT system every five minutes, with negligible impact on system resources or performance.

```
body common control
{
bundlesequence => { "cfengine_documentation" };
}

bundle agent cfengine_documentation
{
vars:

  "links[1]" string => "Get an [Introduction to CFEngine][Introduction], an [Overview of CFEngine][Overview] and a [Guide to How CFEngine Works][Guide]."; 
  "links[2]" string => "[Get started][Get Started] with CFEngine."; 
  "links[3]" string => "Read about [Policy Language][Writing Policy and Promises] and see some [Examples of Policy Language][Examples]."; 
  "links[4]" string => "Search the [Reference Documentation][Reference]."; 
  "links[5]" string => "Discover [CFEngine Enterprise Edition][CFEngine Enterprise Guide]."; 
  "links[6]" string => "Learn about [Reporting in the CFEngine Misssion Portal][Reporting in Mission Portal]."; 
  "links[7]" string => "Check release information"; 
}
```
















