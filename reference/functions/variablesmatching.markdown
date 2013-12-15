---
layout: default
title: variablesmatching
categories: [Reference, Functions, variablesmatching]
published: true
alias: reference-functions-variablesmatching.html
tags: [reference, utility functions, functions, variablesmatching]
---

[%CFEngine_function_prototype(regex, tag1, tag2, ...)%]

**Description:** Return the list of variables matching `regex` and any tags given.

This function searches for the [unanchored][unanchored] regular expression in 
the list of currently defined variables.

When any tags are given, only the variables with those tags are returned.

[%CFEngine_function_attributes(regex, tag1, tag2, ...)%]

**Example:**  


```cf3
body common control
{
      bundlesequence => { run };
}

bundle agent run
{
  vars:
      "all" slist => variablesmatching(".*");
      "c" slist => variablesmatching("sys");
      "c_plus_plus" slist => variablesmatching("sys", "plus");
  reports:
      "All classes = $(all)";
      "Classes matching 'sys' = $(c)";
      "Classes matching 'sys' with the 'plus' tag = $(c_plus_plus)";
}

```

Output:

```
R: All classes = default:sys.cf_version_major
R: All classes = default:sys.systime
R: All classes = default:sys.ipv4_3[eth0]
R: All classes = default:sys.local_libdir
R: All classes = default:sys.cpus
R: All classes = default:sys.ipv4[eth0]
R: All classes = default:sys.exports
R: All classes = default:const.r
R: All classes = default:sys.hardware_mac[eth0]
R: All classes = default:sys.host
R: All classes = default:sys.cdate
R: All classes = default:sys.libdir
R: All classes = default:sys.hardware_flags
R: All classes = default:sys.resolv
R: All classes = default:sys.interface_flags[lo]
R: All classes = default:sys.arch
R: All classes = default:sys.cf_version_patch
R: All classes = default:sys.class
R: All classes = default:sys.interface
R: All classes = default:sys.fqhost
R: All classes = default:sys.ip_addresses
R: All classes = default:sys.ipv4[lo]
R: All classes = default:sys.cf_version_minor
R: All classes = default:control_common.bundlesequence
R: All classes = default:sys.os
R: All classes = default:sys.flavour
R: All classes = default:sys.ipv4_1[eth0]
R: All classes = default:const.t
R: All classes = default:sys.cf_agent
R: All classes = default:sys.uptime
R: All classes = default:sys.interface_flags[eth0]
R: All classes = default:sys.uqhost
R: All classes = default:const.dollar
R: All classes = default:sys.interface_flags[br0]
R: All classes = default:sys.masterdir
R: All classes = default:sys.ipv4_2[lo]
R: All classes = default:const.endl
R: All classes = default:sys.cf_promises
R: All classes = default:sys.ipv4_2[eth0]
R: All classes = default:sys.cf_twin
R: All classes = default:sys.ipv4_2[br0]
R: All classes = default:sys.piddir
R: All classes = default:sys.update_policy_path
R: All classes = default:sys.ipv4_1[br0]
R: All classes = default:sys.hardware_addresses
R: All classes = default:sys.ipv4_3[br0]
R: All classes = default:const.n
R: All classes = default:sys.cf_version
R: All classes = default:sys.fstab
R: All classes = default:sys.version
R: All classes = default:run.c
R: All classes = default:sys.interfaces
R: All classes = default:sys.failsafe_policy_path
R: All classes = default:sys.flavor
R: All classes = default:sys.date
R: All classes = default:sys.maildir
R: All classes = default:sys.release
R: All classes = default:sys.inputdir
R: All classes = default:sys.workdir
R: All classes = default:sys.hardware_mac[br0]
R: All classes = default:sys.ipv4
R: All classes = default:sys.crontab
R: All classes = default:sys.long_arch
R: All classes = default:run.all
R: All classes = default:run.c_plus_plus
R: All classes = default:sys.logdir
R: All classes = default:sys.sysday
R: All classes = default:sys.ostype
R: All classes = default:sys.ipv4_3[lo]
R: All classes = default:sys.domain
R: All classes = default:sys.ipv4_1[lo]
R: All classes = default:sys.bindir
R: All classes = default:sys.doc_root
R: All classes = default:sys.ipv4[br0]
```

**History:** Introduced in CFEngine 3.6
