---
layout: default
title: CFEngine Architecture
categories: [Manuals, Architecture]
published: true
alias: manuals-architecture.html
tags: [manuals, systems,configuration management, automation]
---

CFEngine was designed to enable scalable configuration management in
any kind of environment, with an emphasis on supporting large, Unix-like 
systems that are connected via TCP/IP.

CFEngine doesn't depend on or assume the presence of reliable
infrastructure. It works opportunistically in any environment, using
the fewest possible resources, and it has a limited set of software
dependencies. It can run anywhere, and this lean approach to
CFEngine's architecture makes it possible to support both traditional
server-based approaches to configuration as well as more novel
platforms for configuration including embedded and mobile systems.

CFEngine's design allows you to create fault-tolerant, available systems
which are independent of external requirements. CFEngine works in all
the places you think it should, and all the new places you haven't even
thought of yet.

### Managing Expectations with Promises

CFEngine works on a simple notion of **promises**. A promise is the 
documentation of an intention to act or behave in some manner. When you make a 
promise, it is an effort to improve trust. Trust is an economic time-saver. If 
you can't trust you have to verify everything, and that is expensive.

Everything in CFEngine can be thought of as a promise to be kept by different 
resources in the system. In a system that delivers a web site with Apache 
`httpd`, an important promise may be to make sure that `httpd` is installed, 
running, and accessible on port 80. In a system which needs to satisfy mid-day 
traffic on a busy web site, a promise may be to ensure that there are 200 
application servers running during normal business hours.

These promises are not top-down directives for a central authority to push 
through the system. Try running a large organization on top-down authority 
alone. Try to manage a group of people without empowering and trusting them to 
make independent decisions.

CFEngine is a system that emphasizes the promises a client makes to the 
overall CFEngine network. They are the rules which clients are responsible for 
implementing. We can create large systems of scale because we don't create a 
bulky centralized authority. There is no single point-of-failure both when 
managing machines and people.

Combining promises with patterns to describe where and when promises should 
apply is what CFEngine is all about.

****

Next: [Automation with CFEngine](manuals-architecture-automation.html)
