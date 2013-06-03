---
layout: default
title: hostswithclass
categories: [Reference, Functions, hostswithclass]
published: true
alias: reference-functions-hostswithclass.html
tags: [reference, functions, hostswithclass]
---

**This function is only available in CFEngine Enterprise.**

**Prototype**: `hostswithclass(class, field)`

**Description**: Returns a list from the CFEngine Database with the information `field` of hosts on which `classs` is set.

On CFEngine Enterprise, this function can be used to return a list of 
hostnames or ip-addresses of hosts that have a given class set. Note that this 
function only works locally on the hub, but allows the hub to construct custom 
configuration files for (classes of) hosts.

**Return type**: `slist`

**Arguments**:

* `class` : Class name to look for, *in the range* [a-zA-Z0-9\_]+
* `field` : Type of return value desired, one of
    * name
    * address   

**Example**:

```cf3
    body common control
    {
    bundlesequence => { "test" };
    inputs => { "cfengine_stdlib.cf" };
    }


    bundle agent test
    {
    vars:

    am_policy_hub::
     "host_list" slist => hostswithclass( "debian", "name" );

    files:
    am_policy_hub::
      "/tmp/master_config.cfg"
             edit_line => insert_lines("host=$(host_list)"),
                create => "true";
    }
```

**History**: Was introduced in 3.3.0, Nova 2.2.0 (2012)
