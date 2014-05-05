---
layout: default
title: System Information Examples
published: true
sorting: 11
tags: [Examples][System Information]
---

* [Change detection][System Information#Change detection]
* [Hashing for change detection (tripwire)][System Information#Hashing for change detection (tripwire)]
* [Check filesystem space][System Information#Check filesystem space]
* [Class match example][System Information#Class match example]
* [Global classes][System Information#Global classes]
* [Logging][System Information#Logging]
* Check filesystem space

## Change detection ##
## Hashing for change detection (tripwire) ##

Change detection is a powerful and easy way to monitor your environment, increase awareness and harden your system against security breaches.

```cf3
########################################################

#

# Change detect

#

########################################################


body common control

{
bundlesequence  => { "testbundle"  };
}

########################################################


bundle agent testbundle

{
files:

  "/home/mark/tmp/web" -> "me"

   changes      => detect_all_change,
   depth_search => recurse("inf");
}

#########################################################


body changes detect_all_change

{
report_changes => "all";  
update_hashes  => "true";
}

#########################################################


body depth_search recurse(d)

{
depth        => "$(d)";
}
```

## Check filesystem space ##

```cf3
body common control

{
bundlesequence  => { "example" };
}

###########################################################


bundle agent example

{     
vars:

  "free" int => diskfree("/tmp"); 

reports:

  cfengine_3::

    "Freedisk $(free)";

}
```

## Class match example ##
## Global classes ##
## Logging ##