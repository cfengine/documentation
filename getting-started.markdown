---
layout: default
title: Getting Started 
categories: [Getting Started]
published: true
alias: getting-started.html
tags: [getting started]
---

Don't have CFEngine yet? Get ready to use
[CFEngine Enterprise in 10 minute](https://cfengine.com/evaluate-enterprise) using a ready-made
[VirtualBox](https://cfengine.com/enterprise-getting-started) or
[KVM](https://cfengine.com/cfengine-enterprise-getting-started-using-kvm) image.

CFEngine is a powerful tool, but the basic architecture is very simple:

* express the desired state of your system in CFEngine policy
* upload the policy files to the CFEngine Server, using file copying or version control systems
* the CFEngine Server makes the policies available to the hosts in your system
* the CFEngine agents on the hosts download the policy at regular intervals
* the CFEngine agents regularly interpret the policy and make the necessary changes to the system
* in Enterprise installations, the CFEngine Database Server collects data about changes made from all hosts

The easiest way to use CFEngine is through the **TODO:[Design Center](manuals-design-center.html)**,
which provides ready-made components that can be directly imported and used in CFEngine policies.
With CFEngine Enterprise you can use the Design Center UI through the Mission Portal.

The CFEngine policy language is declarative and easy to learn, also for users with little
background in programming. We have found the following steps a good way to learn CFEngine:

* Complete Step 2 of the getting started guide: Deploy your first policy on
   [VirtualBox](https://cfengine.com/enterprise-getting-started-2) or 
   [KVM](https://cfengine.com/cfengine-enterprise-getting-started-using-kvm-step-2)
* TODO: Continue from there From Zero to Hero
* TODO: Get the book
* TODO: Study the tutorials and examples
* TODO: Start Contributing (to design center, documentation, code)

## 3rd party Tutorials, Examples and Documentation

* [Getting Started with CFEngine 3](http://www.verticalsysadmin.com/cfengine/Getting_Started_with_CFEngine_3.pdf) by Vertical Sysadmin
* [CFEngine 3 Beginning Examples](http://www.verticalsysadmin.com/cfengine/beginning_examples/) by Vertical Sysadmin.
  This is, basically, a selection from /usr/local/share/doc/cfengine/ which has over 200 examples.
* ["CFEngine 3 Tutorial"](http://watson-wilson.ca/2011/05/cfengine-3-cookbook-begins.html) by Neil Watson
