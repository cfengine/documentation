---
layout: default
title: System File Examples
published: true
sorting: 13
tags: [Examples,System Administration,System Files]
---

* [Editing password or group files][System File Examples#Editing password or group files]
* [Editing password or group files custom][System File Examples#Editing password or group files custom]
* [Log rotation][System File Examples#Log rotation]
* [Garbage collection][System File Examples#Garbage collection]
* [Manage a system file][System File Examples#Manage a system file]
* [Templating][System File Examples#Templating]
* [Simple template][System File Examples#Simple template]
* [Simple versioned template][System File Examples#Simple versioned template]
* [Macro template][System File Examples#Macro template]
* [Custom editing][System File Examples#Custom editing]

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

## Log rotation

```cf3
body common control
   {
   bundlesequence  => { "testbundle" };
   }


############################################


bundle agent testbundle

{
files:

  "/home/mark/tmp/rotateme"

      rename => rotate("4");
}

############################################


body rename rotate(level)

{
rotate => "$(level)";
}
```

## Garbage collection

```cf3
body common control
{
bundlesequence => { "garbage_collection" };
inputs => { "cfengine_stdlib.cf" };
}


bundle agent garbage_collection
{
files:

 Sunday::

  "$(sys.workdir)/nova_repair.log" 

    comment => "Rotate the promises repaired logs each week",
    rename => rotate("7"),
    action => if_elapsed("10000");

  "$(sys.workdir)/nova_notkept.log" 

    comment => "Rotate the promises not kept logs each week",
    rename => rotate("7"),
    action => if_elapsed("10000");

  "$(sys.workdir)/promise.log" 

    comment => "Rotate the promises not kept logs each week",
    rename => rotate("7"),
    action => if_elapsed("10000");

 any::

  "$(sys.workdir)/outputs" 

    comment => "Garbage collection of any output files",
    delete => tidy,
    file_select => days_old("3"),
    depth_search => recurse("inf");

  "$(sys.workdir)/" 

    comment => "Garbage collection of any output files",
    delete => tidy,
    file_select => days_old("14"),
    depth_search => recurse("inf");

  # Other resources


  "/tmp" 

    comment => "Garbage collection of any temporary files",
    delete => tidy,
    file_select => days_old("3"),
    depth_search => recurse("inf");
  
  "/var/log/apache2/.*bz" 

    comment => "Garbage collection of rotated log files",
    delete => tidy,
    file_select => days_old("30"),
    depth_search => recurse("inf");

  "/var/log/apache2/.*gz" 

    comment => "Garbage collection of rotated log files",
    delete => tidy,
    file_select => days_old("30"),
    depth_search => recurse("inf");

  "/var/log/zypper.log"

    comment => "Prevent the zypper log from choking the disk",
    rename => rotate("0"),
    action => if_elapsed("10000");

}	
	
```	

## Manage a system file

    Simple template
    Simple versioned template
    Macro template
    Custom editing

### Simple template

```cf3
bundle agent hand_edited_config_file
{
vars:

  "file_template" string =>

"
# Syntax:

#

# IP-Address  Full-Qualified-Hostname  Short-Hostname

#


127.0.0.1       localhost
::1             localhost ipv6-localhost ipv6-loopback
fe00::0         ipv6-localnet
ff00::0         ipv6-mcastprefix
ff02::1         ipv6-allnodes
ff02::2         ipv6-allrouters
ff02::3         ipv6-allhosts
10.0.0.100      host1.domain.tld host1
10.0.0.101      host2.domain.tld host2
10.0.0.20       host3.domain.tld host3
10.0.0.21       host4.domain.tld host4
";

##############################################################


files:

   "/etc/hosts"

       comment => "Define the content of all host files from this master source",
        create => "true",
     edit_line => append_if_no_lines("$(file_template)"),
 edit_defaults => empty,
         perms => mo("$(mode)","root"),
        action => if_elapsed("60");
}
```

### Simple versioned template

The simplest approach to managing a file is to maintain a master copy by hand, keeping it in a version controlled repository (e.g. svn), and installing this version on the end machine.

We'll assume that you have a version control repository that is located on some independent server, and has been checked out manually once (with authentication) in /mysite/masterfiles.

```cf3
bundle agent hand_edited_config_file
{
vars:

  "masterfiles"   string => "/mysite/masterfiles";
  "policy_server" string => "policy_host.domain.tld";

files:

   "/etc/hosts"

        comment => "Synchronize hosts with a hand-edited template in svn",
          perms => m("644"),
      copy_from => remote_cp("$(masterfiles)/trunk/hosts_master","$(policy_server)");

commands:


   "/usr/bin/svn update" 

        comment => "Update the company document repository including manuals to a local copy",
        contain => silent_in_dir("$(masterfiles)/trunk"),
     ifvarclass => canonify("$(policy_server)");

}
```

### Macro template

The next simplest approach to file management is to add variables to the template that will be expanded into local values at the end system, e.g. using variables like ‘$(sys.host)’ for the name of the host within the body of the versioned template.

```cf3
bundle agent hand_edited_template
{
vars:

  "masterfiles"   string => "/mysite/masterfiles";
  "policy_server" string => "policy_host.domain.tld";

files:

   "/etc/hosts"

        comment => "Synchronize hosts with a hand-edited template in svn",
          perms => m("644"),
        create => "true",
     edit_line => expand_template("$(masterfiles)/trunk/hosts_master"),
 edit_defaults => empty,
        action => if_elapsed("60");

commands:


   "/usr/bin/svn update" 

        comment => "Update the company document repository including manuals to a local copy",
        contain => silent_in_dir("$(masterfiles)/trunk"),
     ifvarclass => canonify("$(policy_server)");

}
```

The macro template file may contain variables, as below, that get expanded by CFEngine.

```cf3
     # Syntax:
     #
     # IP-Address  Full-Qualified-Hostname  Short-Hostname
     #
     
     127.0.0.1       localhost $(sys.host)
     ::1             localhost ipv6-localhost ipv6-loopback
     fe00::0         ipv6-localnet
     ff00::0         ipv6-mcastprefix
     ff02::1         ipv6-allnodes
     ff02::2         ipv6-allrouters
     ff02::3         ipv6-allhosts
     10.0.0.100      host1.domain.tld host1
     10.0.0.101      host2.domain.tld host2
     10.0.0.20       host3.domain.tld host3
     10.0.0.21       host4.domain.tld host4
     
     # Add below this line
     
     $(definitions.more_hosts)
```	 

### Custom editing

If you do not control the starting state of the file, because it is distributed by an operating system vendor for instance, then editing the final state is the best approach. That way, you will get changes that are made by the vendor, and will ensure your own modifications are kept even when updates arrive.

```cf3
bundle agent modifying_managed_file
{
vars:

  "data"   slist => { "10.1.2.3 sirius", "10.1.2.4 ursa-minor", "10.1.2.5 orion"};

files:

   "/etc/hosts"

        comment => "Append a list of lines to the end of a file if they don't exist",
          perms => m("644"),
        create => "true",
     edit_line => append_if_no_lines("modifying_managed_file.data"),
        action => if_elapsed("60");


}
```

Another example shows how to set the values of variables using a data-driven approach and methods from the standard library.

```cf3
#######################################################
#

# Edit variable = value in a text file

#

#######################################################


body common control

{
bundlesequence  => { "testsetvar" };   
}

#######################################################


bundle agent testsetvar

{
vars:

  "v[variable_1]" string => "value_1";
  "v[variable_2]" string => "value_2";

files:

  "/tmp/test_setvar"

     edit_line => set_variable_values("testsetvar.v");
}
```