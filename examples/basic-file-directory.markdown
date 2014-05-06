---
layout: default
title: File and Directory Examples
published: true
sorting: 6
tags: [Examples][Files][Directories]
---

* [Create files and directories][Basic File and Directory Examples#Create files and directories]
* [Copy single files][Basic File and Directory Examples#Copy single files]
* [Copy directory trees][Basic File and Directory Examples#Copy directory trees]
* [Disabling and rotating files][Basic File and Directory Examples#Disabling and rotating files]
* [Add lines to a file][Basic File and Directory Examples#Add lines to a file]
* [Check file or directory permissions][Basic File and Directory Examples#Check file or directory permissions]
* [Commenting lines in a file][Basic File and Directory Examples#Commenting lines in a file]
* [Copy files][Basic File and Directory Examples#Copy files]
* [Copy and flatten directory][Basic File and Directory Examples#Copy and flatten directory]
* [Copy then edit a file convergently][Basic File and Directory Examples#Copy then edit a file convergently]
* [Creating files and directories][Basic File and Directory Examples#Creating files and directories]
* [Deleting lines from a file][Basic File and Directory Examples#Deleting lines from a file]
* [Deleting lines exception][Basic File and Directory Examples#Deleting lines exception]
* [Editing files][Basic File and Directory Examples#Editing files]
* [Editing tabular files][Basic File and Directory Examples#Editing tabular files]
* [Inserting lines in a file][Basic File and Directory Examples#Inserting lines in a file]
* [Back references in filenames][Basic File and Directory Examples#Back references in filenames]
* [Add variable definitions to a file][Basic File and Directory Examples#Add variable definitions to a file]
* [Linking files][Basic File and Directory Examples#Linking files]
* [Listing files-pattern in a directory][Basic File and Directory Examples#Listing files-pattern in a directory]
* [Locate and transform files][Basic File and Directory Examples#Locate and transform files]
* [BSD flags][Basic File and Directory Examples#BSD flags]
* [Search and replace text][Basic File and Directory Examples#Search and replace text]
* [Selecting a region in a file][Basic File and Directory Examples#Selecting a region in a file]
* [Warn if matching line in file][Basic File and Directory Examples#Warn if matching line in file]
* Copy single files
* Create files and directories
* Change detection

## Create files and directories ##

Create files and directories and set permissions.

```cf3
########################################################

#

# Simple test create files

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

  "/home/mark/tmp/test_plain" 

       perms => system,
       create => "true";

  "/home/mark/tmp/test_dir/." 

       perms => system,
       create => "true";

}

#########################################################


body perms system

{
mode  => "0640";
}

#########################################################
```

## Copy single files ##

Copy single files, locally (local_cp) or from a remote site (secure_cp). The Community Open Promise-Body Library (COPBL; cfengine_stdlib.cf) should be included in the /var/cfengine/inputs/ directory and input as below.

```cf3
body common control
{
bundlesequence  => { "mycopy" };
inputs => { "cfengine_stdlib.cf" };
}

bundle agent mycopy
{
files:

  "/home/mark/tmp/test_plain"

    copy_from => local_cp("$(sys.workdir)/bin/file");

  "/home/mark/tmp/test_remote_plain"

    copy_from => secure_cp("$(sys.workdir)/bin/file","serverhost");
}
```

## Copy directory trees ##

Copy directory trees, locally (local_cp) or from a remote site (secure_cp). (depth_search => recurse("")) defines the number of sublevels to include, ("inf") gets entire tree.

```cf3
body common control
{
bundlesequence  => { "my_recursive_copy" };
inputs => { "cfengine_stdlib.cf" };
}

bundle agent my_recursive_copy
{
files:

  "/home/mark/tmp/test_dir"

      copy_from => local_cp("$(sys.workdir)/bin/."),
   depth_search => recurse("inf");

  "/home/mark/tmp/test_dir"

      copy_from => secure_cp("$(sys.workdir)/bin","serverhost"),
   depth_search => recurse("inf");

}
```

## Disabling and rotating files ##

Use the following simple steps to disable and rotate files. See the Community Open Promise-Body Library if you wish more details on what disable and rotate does.

```cf3
body common control
{
bundlesequence  => { "my_disable" };
inputs => { "cfengine_stdlib.cf" };
}

bundle agent my_disable
{

files:

  "/home/mark/tmp/test_create"
      rename => disable;
 
 "/home/mark/tmp/rotate_my_log"
      rename => rotate("4");

}
```

## Add lines to a file ##

There are numerous approaches to adding lines to a file. Often the order of a configuration file is unimportant, we just need to ensure settings within it. A simple way of adding lines is show below.

```cf3
body common control

{
any::

  bundlesequence  => { "insert" };   
}

#######################################################


bundle agent insert

{
vars:

  "lines" string => 
                "
                One potato
                Two potato
                Three potatoe
                Four
                ";
 
files:

  "/tmp/test_insert"

            create => "true",
         edit_line => append_if_no_line("$(insert.lines)");

}
```

Also you could write this using a list variable:

```cf3
body common control

{
any::

  bundlesequence  => { "insert" };   
}

#######################################################


bundle agent insert

{
vars:

  "lines" slist => { "One potato", "Two potato",
                "Three potatoe", "Four" };
 
files:

  "/tmp/test_insert"

            create => "true",
         edit_line => append_if_no_line("@(insert.lines)");

}
```

## Check file or directory permissions

```cf3
bundle agent check_perms
{
vars:

  "ns_files" slist => {
                      "/local/iu/logs/admin",
                      "/local/iu/logs/security",
                      "/local/iu/logs/updates",
                      "/local/iu/logs/xfer"
                      };
files:

   NameServers::

    "/local/dns/pz"

            perms => mo("644","dns")
     depth_search => recurse("1"),
      file_select => exclude("secret_file");

    "/local/iu/dns/pz/FixSerial"

            perms => m("755"),
      file_select => plain;

    "$(ns_files)"

            perms => mo("644","dns"),
      file_select => plain;


    "$(ftp)/pub"      
             perms => mog("644","root","other");

    "$(ftp)/pub"      
             perms => m("644"),
      depth_search => recurse("inf");

    "$(ftp)/etc"        perms => mog("111","root","other");
    "$(ftp)/usr/bin/ls" perms => mog("111","root","other");
    "$(ftp)/dev"        perms => mog("555","root","other");
    "$(ftp)/usr"        perms => mog("555","root","other");
}
```

## Commenting lines in a file ##
## Copy files ##
## Copy and flatten directory ##
## Copy then edit a file convergently ##
## Creating files and directories ##
## Deleting lines from a file ##
## Deleting lines exception ##
## Editing files ##
## Editing tabular files ##
## Inserting lines in a file ##

## Back references in filenames

```cf3

######################################################################

#

# File editing - back reference

#

######################################################################



body common control

{
version => "1.2.3";
bundlesequence  => { "testbundle"  };
}

########################################################


bundle agent testbundle

{
files:

  # The back reference in a path only applies to the last link

  # of the pathname, so the (tmp) gets ignored


  "/tmp/(cf3)_(.*)"

       edit_line => myedit("second $(match.2)");


  # but ...


#  "/tmp/cf3_test"

#       create    => "true",

#       edit_line => myedit("second $(match.1)");



}

########################################################


bundle edit_line myedit(parameter)
  {
  vars:

   "edit_variable" string => "private edit variable is $(parameter)"; 

  insert_lines:

     "$(edit_variable)";
  
  }
```

## Add variable definitions to a file

```cf3

body common control
{
bundlesequence => { "setvars" };
inputs => { "cf_std_library.cf" };
}


bundle agent setvars
{
vars:

  # want to set these values by the names of their array keys


  "rhs[lhs1]" string => " Mary had a little pig";
  "rhs[lhs2]" string => "Whose Fleece was white as snow";
  "rhs[lhs3]" string => "And everywhere that Mary went";

  # oops, now change pig -> lamb


files:

  "/tmp/system"

        create => "true",
     edit_line => set_variable_values("setvars.rhs");

}
```

Results in:

lhs1= Mary had a little pig
lhs2=Whose Fleece was white as snow
lhs3=And everywhere that Mary went

An example of this would be to add variables to /etc/sysctl.conf on Linux:

```cf3
body common control
{
bundlesequence => { "setvars" };
inputs => { "cf_std_library.cf" };
}


bundle agent setvars
{
vars:

  # want to set these values by the names of their array keys


  "rhs[net/ipv4/tcp_syncookies]" string => "1";
  "rhs[net/ipv4/icmp_echo_ignore_broadcasts]" string => "1";
  "rhs[net/ipv4/ip_forward]" string => "1";

  # oops, now change pig -> lamb


files:

  "/etc/sysctl"

        create => "true",
     edit_line => set_variable_values("setvars.rhs");

}

    Application baseline
    Array example
    Back references in filenames
    BSD flags
    Change directory for command
```

## Linking files ##
## Listing files-pattern in a directory ##
## Locate and transform files ##

## BSD flags ##

```cf3
body common control
{
bundlesequence => { "test" };
}

bundle agent test
{
files:

 freebsd::

   "/tmp/newfile"

       create => "true",
       perms => setbsd;

}


body perms setbsd
{
bsdflags => { "+uappnd","+uchg", "+uunlnk", "-nodump" };
}
```

## Search and replace text ##
## Selecting a region in a file ##
## Warn if matching line in file ##