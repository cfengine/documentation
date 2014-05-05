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
## Check file or directory permissions ##
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
## Back references in filenames ##
## Add variable definitions to a file ##
## Linking files ##
## Listing files-pattern in a directory ##
## Locate and transform files ##
## BSD flags ##
## Search and replace text ##
## Selecting a region in a file ##
## Warn if matching line in file ##