---
layout: default
title: CFEngine 3.5
categories: [Getting Started]
published: true
alias: index.html
---

The purpose of configuration management is to keep systems stable
long enough to do useful work.

CFEngine 3 represents the newest and most carefully researched
technology available for configuration management. It is both simpler
and more powerful than previous versions. With CFEngine 3 you can install,
configure and maintain computers using powerful hands-free tools.
You can also integrate knowledge management and diagnosis into the processes.

CFEngine differs from most management systems in being

* Lightweight and generic
* Non-reliant on a working network to function correctly
* Capable of making each and every host autonomous

CFEngine 3 exists in [two editions](https://cfengine.com/cfengine-comparison):

- **[Community Edition](https://cfengine.com/community)** - the core of
CFEngine provides reliable automation of heterogeneous system configuration
(supporting nearly forty UNIX-like operating systems) and basic knowledge
management to help you track why systems are configured, who cares about them,
and what the dependencies are.

- **[Enterprise](https://cfengine.com/enterprise)** - add-ons to the core
provide additional configuration management functionality and advanced knowledge
management to bring stability, predictability and control to complex
heterogeneous distributed systems. 

The Enterprise add-ons:
* increase the reach and range of CFEngine (more platforms and functionality),
* facilitate orchestration,
* enable scalability of complex systems through insight from
system configuration reports; goal, policy and project compliance
reports; pre- and post-change impact analysis; troubleshooting and
diagnostics; and modeling of dependencies and relationships -- all adding
up to stabler systems, tighter integration between business and IT, and
more value from IT to the business, including increased uptime and
reduced labor costs.

This documentation is valid for **all versions** of CFEngine. Whenever
a feature is only available in a specific version, that fact will be
noted in the documentation for that feature. If there is no note,
then that feature is available in all versions.

## History of CFEngine

CFEngine is a suite of programs for integrated autonomic management
of either individual or networked computers. It has existed as a
software suite since 1993.

With CFEngine 3, CFEngine has been changed to be both a more powerful
tool and a much simpler tool. CFEngine 3's language interface is not
backwards compatible with the CFEngine 2 configuration language, but it
interoperates with CFEngine 2 so that it is "run-time compatible".
This means that you can change over to version 3 slowly, with low
risk and at your own speed.
