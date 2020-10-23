---
layout: default
title: Content Driven Policy
published: true
sorting: 80
tags: [overviews, special topics, guide]
reviewed: 2019-05-06
---

# What is a Content-Driven Policy?


A Content-Driven Policy is a text file with lines containing semi-colon
separated fields, like a spreadsheet or tabular file. Each line in the file is
parsed and results in a specific type of promise being made, depending on which
type the Content-Driven Policy is. The ‘services’ Content-Driven Policy is shown
below.

```
# masterfiles/cdp_inputs/service_list.txt

Dnscache;stop;fix;windows
ALG;start;warn;windows
RemoteRegistry;start;fix;Windows_Server_2008
```

The meaning of the fields are different depending of the policy type, but
explained in the file header. With these three lines, we ensure the correct
status of three services on all our Windows machines and are given specialized
reports on the outcome. The Content-Driven Policy services report is shown
below.

Note: Content-Driven Policy originally from the CFEngine Nova has not been part
of masterfiles since 3.6.0. [`cdp_inputs` was removed](https://github.com/cfengine/masterfiles/commit/4d05f6154098624bc042fe02ff7a9d25b7a16b44) as part of moving to a
unified base for policy that works with both CFEngine Community and CFEngine
Enterprise.

# Why should I use Content-Driven Policies?


As seen in the example above, Content-Driven Policies are easy to write and
maintain, especially for users not very familiar with the CFEngine language.
They are designed to capture the essence of a specific, popular use of CFEngine,
and make it easier. For example, the services Content-Driven Policy above has
the following equivalent in the CFEngine language.

```cf3
bundle agent service_example
{
  services:

    "Dnscache"
      comment            => "Check services status of Dnscache",
      handle             => "srv_Dnscache_windows",
      service_policy     => "stop",
      service_method     => force_deps,
      action             => policy("fix"),
      if                 => "windows";

    "ALG"
      comment            => "Check services status of ALG",
      handle             => "srv_ALG_windows",
      service_policy     => "start",
      service_method     => force_deps,
      action             => policy("warn"),
      if                 => "windows";

    "RemoteRegistry"
      comment            => "Check services status of ALG",
      handle             => "srv_ALG_windows",
      service_policy     => "start",
      service_method     => force_deps,
      action             => policy("fix"),
      if                 => "Windows_Server_2008";
}
```

Writing this policy is clearly more time-consuming and error-prone. On the other
hand, it allows for much more flexibility than Content-Driven Policies, when
that is needed.

CFEngine provides Content-Driven Policies to cover mainstream management tasks
like the following.

* File change/difference management
* Service management
* Database management
* Application / script management

# How do Content-Driven Policies work in detail?


The text files in masterfiles/cdp_inputs/(e.g. ‘registry_list.txt’) are parsed
into CFEngine lists by corresponding cdp_*files in masterfiles/(e.g.
‘cdp_registry.cf’). It is the latter set of files that actually implement the
policies in the text files.

The Knowledge Map contains reports specifically designed to match the
Content-Driven Policies.

# Can I make my own Content-Driven Policies?


It is possible to mimic the structure of the existing Content-Driven Policies to
implement new ones, for new purposes.

[Professional services][professional services] can be engaged to assist you in
development of the correct fit for your organization given your existing data
sources and tooling available.
