---
layout: default
title: CFEngine Basic Examples
published: true
sorting: 1
tags: [Examples]
---


* [Basic Example][CFEngine Basic Examples#Basic Example]
* [Create files and directories][CFEngine Basic Examples#Create files and directories]
* [Copy single files][CFEngine Basic Examples#Copy single files]
* [Copy directory trees][CFEngine Basic Examples#Copy directory trees]
* [Editing password or group files][CFEngine Basic Examples#Editing password or group files]
* [Editing password or group files custom][CFEngine Basic Examples#Editing password or group files custom]
* [Disabling and rotating files][CFEngine Basic Examples#Disabling and rotating files]
* [Hashing for change detection - tripwire][CFEngine Basic Examples#Hashing for change detection - tripwire]
* [Command or script execution][CFEngine Basic Examples#Command or script execution]
* [Kill process][CFEngine Basic Examples#Kill process]
* [Restart process][CFEngine Basic Examples#Restart process]
* [Check filesystem space][CFEngine Basic Examples#Check filesystem space]
* [Mount a filesystem][CFEngine Basic Examples#Mount a filesystem]
* [Software and patch installation][CFEngine Basic Examples#Software and patch installation]

## Basic Example ##

To get started with CFEngine, you can imagine the following template for entering examples. This part of the code is common to all the examples.

```cf3
body common control
{
bundlesequence => { "main" };
inputs => { "cfengine_stdlib.cf" };
}


bundle agent main
{
# example

}

```

Then you enter the cases as below. The general pattern of the syntax is like this (colors in html version: red, CFEngine word; blue, user-defined word):

```cf3
# The general pattern

bundle component name(parameters)
{ 
what_type:
 where_when::

  # Traditional comment


  "promiser" -> { "promisee1", "promisee2" },
        comment => "The intention ...",
         handle => "unique_id_label",
    attribute_1 => body_or_value1,
    attribute_2 => body_or_value2;
}

```

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

## Editing password or group files ##

To change the password of a system, we need to edit a file. A file is a complex object – once open there is a new world of possible promises to make about its contents. CFEngine has bundles of promises that are specially for editing.

```cf3
body common control
{
bundlesequence => { "edit_passwd" };
}

bundle agent edit_passwd
{

vars:

 "userset" slist => { "user1", "user2", "user3" };

files:

  "/etc/passwd"
     edit_line => 
        set_user_field("mark","7","/set/this/shell");


  "/etc/group"
     edit_line => 
        append_user_field("root","4","@(main.userset)");

}
```

## Editing password or group files custom ##

In this example the bundles from the Community Open Promise-Body Library are included directly in the policy instead of being input as a separate file.

```cf3
body common control
{
bundlesequence => { "addpasswd" };
}

bundle agent addpasswd
{
vars:

  # want to set these values by the names of their array keys


  "pwd[mark]" string => "mark:x:1000:100:Mark Burgess:/home/mark:/bin/bash";
  "pwd[fred]" string => "fred:x:1001:100:Right Said:/home/fred:/bin/bash";
  "pwd[jane]" string => "jane:x:1002:100:Jane Doe:/home/jane:/bin/bash";

files:


  "/tmp/passwd"

        create => "true",
     edit_line => append_users_starting("addpasswd.pwd");

}

############################################################

# Library stuff

############################################################


bundle edit_line append_users_starting(v)

{
vars:

  "index"        slist => getindices("$(v)");

classes:

  "add_$(index)" not => userexists("$(index)");

insert_lines:

  "$($(v)[$(index)])",

      ifvarclass => "add_$(index)";

}

############################################################


bundle edit_line append_groups_starting(v)

{
vars:

  "index"        slist => getindices("$(v)");

classes:

  "add_$(index)" not => groupexists("$(index)");

insert_lines:

  "$($(v)[$(index)])",

      ifvarclass => "add_$(index)";

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

## Command or script execution ##

Execute a command, for instance to start a MySQL service. Note that simple shell commands like rm or mkdir cannot be managed by CFEngine, so none of the protections that CFEngine offers can be applied to the process. Moreover, this starts a new process, adding to the burden on the system. See CFEngine 3 Best Practices http://cfengine.com/manuals/cf3-bestpractice.html for more information on how to best write policies.

```cf3
body common control
{
bundlesequence  => { "my_commands" };
inputs => { "cfengine_stdlib.cf" };
}


bundle agent my_commands
{
commands:

 Sunday.Hr04.Min05_10.myhost::

  "/usr/bin/update_db";

 any::

  "/etc/mysql/start"

      contain => setuid("mysql");

}
```

## Kill process ##

```cf3
body common control
{
bundlesequence => { "test" };
}



bundle agent test
{
processes:

 "sleep"

   signals => { "term", "kill" };

}
```

## Restart process ##

A basic pattern for restarting processes:

```cf3
body common control
{
bundlesequence => { "process_restart" };
}

#########################################################


bundle agent process_restart
{
processes:

  "/usr/bin/daemon" 
        restart_class => "launch";

commands:

  launch::

   "/usr/bin/daemon";

}
```

This can be made more sophisticated to handle generic lists:

```cf3
body common control
{
bundlesequence => { "process_restart" };
}

#########################################################


bundle agent process_restart
{
vars:

  "component" slist => {
                       "cf-monitord", 
                       "cf-serverd", 
                       "cf-execd" 
                       };
processes:

  "$(component)" 
        restart_class => canonify("start_$(component)");

commands:

   "/var/cfengine/bin/$(component)"
       ifvarclass => canonify("start_$(component)");

}
```

Why? Separating this into two parts gives a high level of control and conistency to CFEngine. There are many options for command execution, like the ability to run commands in a sandbox or as `setuid'. These should not be reproduced in processes.

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

## Mount a filesystem ##

```cf3
#

# cfengine 3

#

# cf-agent -f ./cftest.cf -K

#


body common control

{
bundlesequence => { "mounts" };
}

#


bundle agent mounts

{
storage:

  "/mnt" mount  => nfs("slogans.iu.hio.no","/home");

}

######################################################################


body mount nfs(server,source)

{
mount_type => "nfs";
mount_source => "$(source)";
mount_server => "$(server)";
#mount_options => { "rw" };

edit_fstab => "true";
unmount => "true";
}
```


## Software and patch installation ##

Example for Debian:

```cf3
# to see list of packages type "apt-cache pkgnames"

# to see list of installed packages type "dpkg --get-selections"

#

# Package managment

#


body common control
{
bundlesequence => { "packages" };
}

body agent control
{
environment => { "DEBIAN_FRONTEND=noninteractive" };
}

#############################################


bundle agent packages
{
vars:

 # Test the simplest case -- leave everything to the yum smart manager


 "match_package" slist => { 
                          "apache2" 
#                          "apache2-mod_php5",

#                          "apache2-prefork",

#                          "php5" 

                          };
packages:

  "$(match_package)"

     package_policy => "add",
     package_method => apt;

}

#############################################


body package_method apt

{
any::

# ii  acpi      0.09-3ubuntu1     


 package_changes => "bulk";
 package_list_command => "/usr/bin/dpkg -l";

 package_list_name_regex    => "ii\s+([^\s]+).*";
 package_list_version_regex => "ii\s+[^\s]+\s+([^\s]+).*";

# package_list_arch_regex    => "none";


 package_installed_regex => ".*"; # all reported are installed

 #package_name_convention => "$(name)_$(version)_$(arch)";

 package_name_convention => "$(name)";

 # Use these only if not using a separate version/arch string

 # package_version_regex => "";

 # package_name_regex => "";

 # package_arch_regex => "";


package_add_command => "/usr/bin/apt-get --yes install";
package_delete_command => "/usr/bin/apt-get --yes remove";
package_update_command =>  "/usr/bin/apt-get --yes dist-upgrade";
#package_verify_command => "/bin/rpm -V";

}
```

Examples MSI for Windows, by name:

```cf3
#

# MSI package managment using file name

#


body common control
{
bundlesequence => { "packages" };
}

#############################################


bundle agent packages
{
vars:

 "match_package" slist => { 
                          "7zip-4.65-x86_64.msi"
                          };
packages:

  "$(match_package)"

     package_policy => "add",

     package_method => msi_fmatch;


}

#############################################


body package_method msi_fmatch

{
 package_changes => "individual";

 package_file_repositories => { "$(sys.workdir)\software_updates\windows", "s:\su" };

 package_installed_regex => ".*";


 package_name_regex    => "^(\S+)-(\d+\.?)+";

 package_version_regex => "^\S+-((\d+\.?)+)";

 package_arch_regex    => "^\S+-(\d+\.?)+(^.+)";

 
 package_name_convention => "$(name)-$(version)-$(arch).msi";


 package_add_command => "\"$(sys.winsysdir)\msiexec.exe\" /qn /i";

 package_update_command => "\"$(sys.winsysdir)\msiexec.exe\" /qn /i";

 package_delete_command => "\"$(sys.winsysdir)\msiexec.exe\" /qn /x";

 }
```

Windows MSI by version:

```cf3
#

# MSI package managment using version criteria

#


body common control
{
bundlesequence => { "packages" };
}

#############################################


bundle agent packages
{
vars:

 "match_package" slist => { 
                          "7zip"
                          };
packages:

  "$(match_package)"

     package_policy => "update",
     package_select => ">=",
     package_architectures => { "x86_64" },
     package_version => "3.00",
     package_method => msi_vmatch;

}

#############################################


body package_method msi_vmatch

{
 package_changes => "individual";
 package_file_repositories => { "$(sys.workdir)\software_updates\windows", "s:\su" };

 package_installed_regex => ".*";
 
 package_name_convention => "$(name)-$(version)-$(arch).msi";

 package_add_command => "\"$(sys.winsysdir)\msiexec.exe\" /qn /i";
 package_update_command => "\"$(sys.winsysdir)\msiexec.exe\" /qn /i";
 package_delete_command => "\"$(sys.winsysdir)\msiexec.exe\" /qn /x";
}
```

Examples for solaris are more complex:

```cf3
#

# Package managment

#


body common control
{
bundlesequence => { "packages" };
inputs => { "cfengine_stdlb.cf" };
}

#############################################


bundle agent packages
{
vars:

  "solaris_packages[SMCzlib]" string => "zlib-1.2.3-sol10-sparc-local";
  "admin_file"                string => "cfengine_admin_file";

  "package_names"              slist => getindices("solaris_packages");

files:

  "/tmp/$(admin_file)"
	create => "true",
	edit_defaults => empty_file,
	edit_line => create_solaris_admin_file;

packages:

  "$(package_names)"

     package_policy => "add",
     package_method => solaris("$(package_names)", "$(solaris_packages[$(package_names)])", "$(admin_file)");

}
```

Examples for yum based systems:

```cf3
#

# Package managment

#


body common control
{
bundlesequence => { "packages" };
inputs => { "cfengine_stdlib.cf" }
}

#############################################


bundle agent packages
{
vars:

 # Test the simplest case -- leave everything to the yum smart manager


 "match_package" slist => { 
                          "apache2", 
                          "apache2-mod_php5",
                          "apache2-prefork",
                          "php5" 
                          };
packages:

  "$(match_package)"

     package_policy => "add",
     package_method => yum;

}
```

SuSE Linux's package manager zypper is the most powerful alternative:

```cf3
#

# Package managment

#


body common control
{
bundlesequence => { "packages" };
inputs => { "cfengine_stdlib.cf" }
}

#############################################


bundle agent packages
{
vars:

 # Test the simplest case -- leave everything to the zypper smart manager


 "match_package" slist => { 
                          "apache2", 
                          "apache2-mod_php5",
                          "apache2-prefork",
                          "php5" 
                          };
packages:

  "$(match_package)"

     package_policy => "add",
     package_method => zypper;

}
```