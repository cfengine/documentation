---
layout: default
title: Function-hostswithclass
categories: [Special-functions,Function-hostswithclass]
published: true
alias: Special-functions-Function-hostswithclass.html
tags: [Special-functions,Function-hostswithclass]
---

### Function hostswithclass

**Synopsis**: hostswithclass(arg1,arg2) returns type **slist**

\
 *arg1* : Class name to look for, *in the range* [a-zA-Z0-9\_]+ \
 *arg2* : Type of return value desired, *in the range* name,address \

Extract the list of hosts with the given class set from the hub database
(commercial extension)

**Example**:\
 \

~~~~ {.verbatim}
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
~~~~

**Notes**:\
 \

On CFEngine Nova hubs, this function can be used to return a list of
hostnames or ip-addresses of hosts that has the class given as argument
1. Argument 2 may be address or name, to return IP address or hostname
form.

Note that this function only works locally on the hub, but allows the
hub to construct custom configuration files for (classes of) hosts.

*History*: Was introduced in 3.3.0, Nova 2.2.0 (2012)

Availability: Enterprise editions of CFEngine only.

~~~~ {.verbatim}
~~~~
