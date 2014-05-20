---
layout: default
title: System Information Examples
published: true
sorting: 11
tags: [Examples,System Information]
---

* [Change detection][System Information Examples#Change detection]
* [Hashing for change detection (tripwire)][System Information Examples#Hashing for change detection (tripwire)]
* [Check filesystem space][System Information Examples#Check filesystem space]
* [Class match example][System Information Examples#Class match example]
* [Global classes][System Information Examples#Global classes]
* [Logging][System Information Examples#Logging]
* Check filesystem space

## Change detection

```cf3
body common control

{
bundlesequence  => { "testbundle"  };

inputs => { "cfengine_stdlib.cf" };
}

########################################################


bundle agent testbundle

{
files:

  "/usr" 

       changes      => detect_all_change,
       depth_search => recurse("inf"),
       action       => background;
}
```

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

## Class match example

```cf3

body common control

{
bundlesequence  => { "example" };
}

###########################################################


bundle agent example

{     
classes:

  "do_it" and => { classmatch(".*_3"), "linux" }; 

reports:

  do_it::

    "Host matches pattern";

}
```

## Global classes

```cf3
body common control
{
bundlesequence => { "g","tryclasses_1", "tryclasses_2" };

}

#################################


bundle common g
{
classes:

  "one" expression => "any";

  "client_network" expression => iprange("128.39.89.0/24");
}

#################################


bundle agent tryclasses_1
{
classes:

  "two" expression => "any";
}

#################################


bundle agent tryclasses_2
{
classes:

  "three" expression => "any";

reports:

  one.three.!two::

    "Success";
}


###### Global classes

```cf3
body common control
{
bundlesequence => { "g","tryclasses_1", "tryclasses_2" };

}

#################################


bundle common g
{
classes:

  "one" expression => "any";

  "client_network" expression => iprange("128.39.89.0/24");
}

#################################


bundle agent tryclasses_1
{
classes:

  "two" expression => "any";
}

#################################


bundle agent tryclasses_2
{
classes:

  "three" expression => "any";

reports:

  one.three.!two::

    "Success";
}


#################################
```

## Logging

```cf3
body common control
{
bundlesequence => { "test" };
}

bundle agent test
{
vars:

  "software" slist => { "/root/xyz", "/tmp/xyz" };

files:

  "$(software)"

    create => "true",
     action => logme("$(software)");

}

#


body action logme(x)
{
log_kept => "/tmp/private_keptlog.log";
log_failed => "/tmp/private_faillog.log";
log_repaired => "/tmp/private_replog.log";
log_string => "$(sys.date) $(x) promise status";
}


body common control
{
bundlesequence => { "one" };
}



bundle agent one
{
files:

  "/tmp/xyz"

       create => "true",
       action => log;

}

body action log
{
log_level => "inform";
}
```