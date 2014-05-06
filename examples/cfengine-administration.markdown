---
layout: default
title: CFEngine Administration Examples
published: true
sorting: 2
tags: [Examples,CFEngine Administration]
---

* [Ordering promises][Basic Examples#Ordering promises]
* [Aborting execution][Software Administration and Execution#Aborting execution]
* Aborting execution
* Updating from a central policy server

## Ordering promises

This counts to five by default. If we change ‘/bin/echo one’ to ‘/bin/echox one’, then the command will fail, causing us to skip five and go to six instead.

This shows how dependencies can be chained in spite of the order of promises in the bundle.

Normally the order of promises in a bundle is followed, within each promise type, and the types are ordered according to normal ordering.

```cf3
##################################################################

#

# cfengine 3 - ordering promises into dependent chains

#

##

#

# cf-agent -f ./cftest.cf -K

#

##################################################################


body common control

{
bundlesequence => { "order" };
}

##################################################################


bundle agent order

{
vars:

 "list" slist => { "three", "four" };

commands:

 ok_later::

   "/bin/echo five";

 otherthing::

   "/bin/echo six";

 any::


  "/bin/echo one"     classes => d("ok_later","otherthing");
  "/bin/echo two";
  "/bin/echo $(list)";

 preserved_class::

  "/bin/echo seven";

}

############################################


body classes d(if,else)

{
promise_repaired => { "$(if)" };
repair_failed => { "$(else)" };
persist_time => "0";
}
```

## Aborting execution ##

```cf3
body common control

{
bundlesequence  => { "testbundle"  };

version => "1.2.3";
}

###########################################


body agent control

{
abortbundleclasses => { "invalid.Hr16" };
}

###########################################


bundle agent testbundle
{
vars:

 "userlist" slist => { "xyz", "mark", "jeang", "jonhenrik", "thomas", "eben" };

methods:

 "any" usebundle => subtest("$(userlist)");

}

###########################################


bundle agent subtest(user)

{
classes:

  "invalid" not => regcmp("[a-z][a-z][a-z][a-z]","$(user)");

reports:

 !invalid::

  "User name $(user) is valid at 4 letters";

 invalid::

  "User name $(user) is invalid";
}
```