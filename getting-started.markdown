---
layout: default
title: Getting Started 
categories: [Getting Started]
published: true
sorting: 10
alias: getting-started.html
tags: [getting started]
---

Don't have CFEngine yet? Start using
[CFEngine Enterprise in 10 minute][evaluate cfengine] 
with the ready-made
[VirtualBox](https://cfengine.com/enterprise-getting-started) or
[KVM](https://cfengine.com/cfengine-enterprise-getting-started-using-kvm) 
image.

****

CFEngine is a powerful tool, but the basic architecture is very simple:

* express the desired state of your system in CFEngine policy
* upload the policy files to the CFEngine Server, using file copying or 
  version control systems
* the CFEngine Server makes the policies available to the hosts in your system
* the CFEngine components on the hosts connect to the server to download new
  policy - every 5 minutes
* the CFEngine components interpret the policy and make the necessary changes
  to the system - every 5 minutes
* in Enterprise installations, the CFEngine Database Server collects data 
  about changes made from all hosts

The easiest way to use CFEngine is through the 
**[Design Center][Design Center]**, which provides ready-made components that 
can be directly imported and used in  CFEngine policies. With CFEngine 
Enterprise you can use the Design Center UI through the Mission Portal, easily 
installing and configuring policies across all your machines.

The CFEngine policy language is declarative and easy to learn, also for users
with little background in programming. Here is the simplest `Hello world' program in CFEngine 3:

```cf3
    bundle agent test
    {
    reports:
        "Hello world";
    }
```

We have found that the following steps are a good way to learn CFEngine:

* Complete Step 2 of the getting started guide: Deploy your first policy on
   [VirtualBox](https://cfengine.com/enterprise-getting-started-2) or 
     [KVM](https://cfengine.com/cfengine-enterprise-getting-started-using-kvm-step-2)
* Download syntax highlighters for
  [vim](https://github.com/neilhwatson/vim_cf3) or
  [emacs](https://github.com/cfengine/core/blob/master/contrib/cfengine.el).
* <a href="http://cf-learn.info" target="_blank">Get the book!</a>
* Study the [tutorials and examples][CFEngine examples].
* Read the documentation about the [Design][Design],
  the [CFEngine Components][The CFEngine Components].
  and [Language Concepts][Language Concepts]
* Find out what CFEngine can do for you in the
  [Promise Type reference][promise types and attributes] documentation
* Join the [help and support forums][Support and Community] and become part
  of the CFEngine Community.
* Read [our blog][cfengine blog] and follow us on 
  <a href="https://twitter.com/cfengine" target="_blank">twitter</a>,
  <a href="https://www.facebook.com/pages/Cfengine/311003700627?ref=ts" 
     target="_blank">facebook</a> and
  <a href="http://www.linkedin.com/groups?gid=136574&trk=hb_side_g" 
     target="_blank">LinkedIn</a>
  to stay in touch with what's happening in CFEngine and the Configuration 
  Management industry
* Start contributing to
  <a href="https://github.com/cfengine/design-center" target="_blank">Design Center</a>,
  <a href="https://github.com/cfengine/documentation" target="_blank">Documentation</a>
  and the <a href="https://github.com/cfengine/core" target="_blank">Code</a>

## 3rd party Tutorials, Examples and Documentation

* <a href="http://www.verticalsysadmin.com/cfengine/Getting_Started_with_CFEngine_3.pdf"
  target="_blank">Getting Started with CFEngine 3</a> by Vertical Sysadmin
* <a href="http://www.verticalsysadmin.com/cfengine/beginning_examples/" 
  target="_blank">CFEngine 3 Beginning Examples</a> by Vertical Sysadmin
* <a href="http://watson-wilson.ca/2011/05/cfengine-3-cookbook-begins.html" 
  target="_blank">CFEngine 3 Tutorial</a> by Neil Watson
* <a href="http://cfengine.com/policy_wizard/" 
  target="_blank">CFEngine 3 Policy Wizard</a> by Joe Netzel
