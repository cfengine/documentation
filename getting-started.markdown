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
background in programming. We have found that the following steps are a good way to learn
CFEngine:

* Complete Step 2 of the getting started guide: Deploy your first policy on
   [VirtualBox](https://cfengine.com/enterprise-getting-started-2) or 
   [KVM](https://cfengine.com/cfengine-enterprise-getting-started-using-kvm-step-2)
* **TODO: Continue from there From Zero to Hero**
* Download syntax highlighters for [vim](https://github.com/neilhwatson/vim_cf3) or
  [emacs](https://github.com/cfengine/core/blob/master/contrib/cfengine.el)
* <a href="http://cf-learn.info" target="_blank">"Get the book</a>
* Study the [tutorials and examples](examples.html)
* Read the documentation about [Language Concepts](manuals-language-concepts.html)
  and about [Managing Environments](manuals-managing-environments.html)
* Join the [help and support forums](getting-started-support-and-community.html) and become part
  of the CFEngine Community
* Read [our blog](http://cfengine.com/blog) and follow us on 
  <a href="https://twitter.com/cfengine" target="_blank">twitter</a>,
  <a href="https://www.facebook.com/pages/Cfengine/311003700627?ref=ts" target="_blank">facebook</a> and
  <a href="http://www.linkedin.com/groups?gid=136574&trk=hb_side_g" target="_blank">LinkedIn</a>.
  to stay in touch with what's happening in CFEngine and the Configuration Management industry
* Start contributing to
  <a href="https://github.com/cfengine/design-center" target="_blank">Design Center</a>,
  <a href="https://github.com/cfengine/documentation" target="_blank">Documentation</a> and the
  <a href="https://github.com/cfengine/core" target="_blank">Code</a>

## 3rd party Tutorials, Examples and Documentation

* <a href="http://www.verticalsysadmin.com/cfengine/Getting_Started_with_CFEngine_3.pdf" target="_blank">
	Getting Started with CFEngine 3</a> by Vertical Sysadmin
* <a href="http://www.verticalsysadmin.com/cfengine/beginning_examples/" target="_blank">
	CFEngine 3 Beginning Examples</a> by Vertical Sysadmin
* <a href="http://watson-wilson.ca/2011/05/cfengine-3-cookbook-begins.html" target="_blank">
	CFEngine 3 Tutorial</a> by Neil Watson
