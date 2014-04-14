---
layout: default
title: CFEngine Intermediate Examples 
published: true
sorting: 2
tags: [Examples]
---

* [Centralized Management][CFEngine Intermediate Examples#Centralized Management]
* [All hosts the same][CFEngine Intermediate Examples#All hosts the same]
* [Variation in hosts][CFEngine Intermediate Examples#Variation in hosts]
* [Updating from a central hub][CFEngine Intermediate Examples#Updating from a central hub]
* [Change detection][CFEngine Intermediate Examples#Change detection]
* [Garbage collection][CFEngine Intermediate Examples#Garbage collection]
* [Distribute root passwords][CFEngine Intermediate Examples#Distribute root passwords]
* [Distribute ssh keys][CFEngine Intermediate Examples#Distribute ssh keys]
* [Laptop support configuration][CFEngine Intermediate Examples#Laptop support configuration]
* [Find MAC address][CFEngine Intermediate Examples#Find MAC address]
* [Log rotation][CFEngine Intermediate Examples#Log rotation]
* [Manage a system file][CFEngine Intermediate Examples#Manage a system file]
* [Simple template][CFEngine Intermediate Examples#Simple template]
* [Simple versioned template][CFEngine Intermediate Examples#Simple versioned template]
* [Macro template][CFEngine Intermediate Examples#Macro template]
* [Custom editing][CFEngine Intermediate Examples#Custom editing]
* [Manage a system process][CFEngine Intermediate Examples#Manage a system process]
* [Ensure running][CFEngine Intermediate Examples#Ensure running]
* [Ensure not running][CFEngine Intermediate Examples#Ensure not running]
* [Prune processes][CFEngine Intermediate Examples#Prune processes]
* [Manage users][CFEngine Intermediate Examples#Manage users]
* [Add users][CFEngine Intermediate Examples#Add users]
* [Remove users][CFEngine Intermediate Examples#Remove users]
* [Postfix mail configuration][CFEngine Intermediate Examples#Postfix mail configuration]
* [Set up HPC clusters][CFEngine Intermediate Examples#Set up HPC clusters]
* [Set up name resolution][CFEngine Intermediate Examples#Set up name resolution]
* [Set up sudo][CFEngine Intermediate Examples#Set up sudo]
* [Set up a web server][CFEngine Intermediate Examples#Set up a web server]
* [Templating][CFEngine Intermediate Examples#Templating]

## Centralized Management

These examples show a simple setup for starting with a central approach to management of servers. Centralization of management is a simple approach suitable for small environments with few requirements. It is useful for clusters where systems are all alike.

    All hosts the same
    Variation in hosts
    Updating from a central hub

### All hosts the same

This shows the simplest approach in which all hosts are the same. It is too simple for most environments, but it serves as a starting point. Compare it to the next section that includes variation.

```cf3
body common control
   {
   bundlesequence  => { "central" };
   }


############################################


bundle agent central

{
vars:

  "policy_server" string => "myhost.domain.tld";

  "mypackages" slist => { 
                        "nagios"
                        "gcc",
                        "apache2", 
                        "php5" 
                        };

files:

  # Password management can be very simple if all hosts are identical


  "/etc/passwd" 

    comment   => "Distribute a password file",
    perms     => mog("644","root","root"),
    copy_from => secure_cp("/home/mark/LapTop/words/RoadAhead","$(policy_server)");

packages:

  "$(mypackages)"

     package_policy => "add",
     package_method => generic;


# Add more promises below ...

     
}


#########################################################

# Server config

#########################################################


body server control

{
allowconnects         => { "127.0.0.1" , "::1", "10.20.30" };
allowallconnects      => { "127.0.0.1" , "::1", "10.20.30" };
trustkeysfrom         => { "127.0.0.1" , "::1", "10.20.30" };
# allowusers

}

#########################################################


bundle server access_rules()

{
access:

 # myhost.domain.tld makes this file available to 10.20.30*


 myhost_domain_tld::  

  "/etc/passwd"

     admit   => { "127.0.0.1", "10.20.30" };
}

```

### Variation in hosts

```cf3
body common control
   {
   bundlesequence  => { "central" };
   }


############################################


bundle agent central

{
classes:

  "mygroup_1" or => { "myhost", "host1", "host2", "host3" };
  "mygroup_2" or => { "host4", "host5", "host6" };

vars:

  "policy_server" string => "myhost.domain.tld";

 mygroup_1::

  "mypackages" slist => { 
                        "nagios"
                        "gcc",
                        "apache2", 
                        "php5" 
                        };

 mygroup_2::

  "mypackages" slist => { 
                        "apache"
                        "mysql",
                        "php5" 
                        };


files:

  # Password management can be very simple if all hosts are identical


  "/etc/passwd" 

    comment   => "Distribute a password file",
    perms     => mog("644","root","root"),
    copy_from => secure_cp("/etc/passwd","$(policy_server)");

packages:

  "$(mypackages)"

     package_policy => "add",
     package_method => generic;


# Add more promises below ...

     
}


#########################################################

# Server config

#########################################################


body server control

{
allowconnects         => { "127.0.0.1" , "::1", "10.20.30" };
allowallconnects      => { "127.0.0.1" , "::1", "10.20.30" };
trustkeysfrom         => { "127.0.0.1" , "::1", "10.20.30" };
# allowusers

}

#########################################################


bundle server access_rules()

{
access:

 # myhost.domain.tld makes this file available to 10.20.30*


 myhost_domain_tld::  

  "/etc/passwd"

     admit   => { "127.0.0.1", "10.20.30" };
}

```

### Updating from a central hub

The configuration bundled with the CFEngine source code contains an example of centralized updating of policy that covers more subtleties than this example, and handles fault tolerance. Here is the main idea behind it. For simplicity, we assume that all hosts are on network 10.20.30.* and that the central policy server/hub is 10.20.30.123.

```cf3
bundle agent update
{
vars:

 "master_location" string => "/var/cfengine/masterfiles";

 "policy_server"   string => "10.20.30.123";
                   comment => "IP address to locate your policy host.";

files:

  "$(sys.workdir)/inputs" 

    perms => system("600"),
    copy_from => remote_cp("$(master_location)",$(policy_server)),
    depth_search => recurse("inf");

  "$(sys.workdir)/bin" 

    perms => system("700"),
    copy_from => remote_cp("/usr/local/sbin","localhost"),
    depth_search => recurse("inf");
}

#######################################################


body server control

{
allowconnects         => { "127.0.0.1" , "10.20.30" };
allowallconnects      => { "127.0.0.1" , "10.20.30" };
trustkeysfrom         => { "127.0.0.1" , "10.20.30" };
}

#######################################################


bundle server access_rules()
{
access:

 10_20_30_123::

  "/var/cfengine/masterfiles"

    admit   => { "127.0.0.1", "10.20.30" };
}

```


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
   
######################################################################
#

# Root password distribution

# 

######################################################################


body common control

{
version => "1.2.3";
bundlesequence  => { "SetRootPassword" };
}

########################################################


bundle common g
{
vars:

  "secret_keys_dir" string => "/tmp";
}

########################################################


bundle agent SetRootPassword

{
files:

  "/var/cfengine/ppkeys/rootpw.txt"

      copy_from => scp("$(sys.fqhost)-root.txt","master_host.example.org");

      # or $(pw_class)-root.txt


  # Or get variables directly from server woth Nova


 "remote-passwd" string => remotescalar("rem_password","127.0.0.1","yes");

  # Test this on a copy


  "/tmp/shadow"

       edit_line => SetRootPw;

}

########################################################


bundle edit_line SetRootPw
  {
  vars:

   # Assume this file contains a single string of the form root:passwdhash:

   # with : delimiters to avoid end of line/file problems


   "pw" int => readstringarray("rpw","$(sys.workdir)/ppkeys/rootpw.txt",
                                                    "#[^\n]*",":","1","200");

  field_edits:

   "root:.*"

      # Set field of the file to parameter


      edit_field => col(":","2","$(rpw[1])","set");
  }

########################################################


bundle server passwords
{
vars:

  # Read a file of format

  #

  # classname: host1,host2,host4,IP-address,regex.*,etc

  #


       "pw_classes" int => readstringarray("acl","$(g.secret_keys_dir)/classes.txt",
                                                       "#[^\n]*",":","100","4000");  
  "each_pw_class" slist => getindices("acl");
 
access:

  "/secret/keys/$(each_pw_class)-root.txt"

        admit   => splitstring("$(acl[$(each_pw_class)][1])" , ":" , "100"),
    ifencrypted => "true";

}

## Distribute ssh keys

# Assume that we have collected all users' public keys into a single source area
# on the server. First copy the ones we need to localhost, and then edit them into

# the the user's local keyring.


  # vars:

  #

  #  "users" slist => { "user1", "user2", ...};

  #

  # methods:

  #

  #  "any" usebundle => allow_ssh_login_from_authorized_keys(@(users),"sourcehost");

  #


########################################################################


bundle agent allow_ssh_rootlogin_from_authorized_keys(user,sourcehost)
{
vars:

  "local_cache"       string => "/var/cfengine/ssh_cache"; 
  "authorized_source" string => "/master/CFEngine/ssh_keys";

files:

   "$(local_cache)/$(user).pub"

         comment => "Copy public keys from a an authorized cache into a cache on localhost",
           perms => mo("600","root"),
       copy_from => remote_cp("$(authorized_source)/$(user).pub","$(sourcehost)"),
          action => if_elapsed("60");

   "/root/.ssh/authorized_keys" 

         comment => "Edit the authorized keys into the user's personal keyring",
       edit_line => insert_file_if_no_line_matching("$(user)","$(local_cache)/$(user).pub"),
          action => if_elapsed("60");
}

########################################################################


bundle agent allow_ssh_login_from_authorized_keys(user,sourcehost)
{
vars:

  "local_cache"       string => "/var/cfengine/ssh_cache"; 
  "authorized_source" string => "/master/CFEngine/ssh_keys";

files:

   "$(local_cache)/$(user).pub"

         comment => "Copy public keys from a an authorized cache into a cache on localhost",
           perms => mo("600","root"),
       copy_from => remote_cp("$(authorized_source)/$(user).pub","$(sourcehost)"),
          action => if_elapsed("60");

   "/home/$(user)/.ssh/authorized_keys" 

         comment => "Edit the authorized keys into the user's personal keyring",
       edit_line => insert_file_if_no_line_matching("$(user)","$(local_cache)/$(user).pub"),
          action => if_elapsed("60");
}

########################################################################


bundle edit_line insert_file_if_no_line_matching(user,file)
{
classes:

  "have_user" expression => regline("$(user).*","$(this.promiser)");

insert_lines:

  !have_user::

    "$(file)" 
         insert_type => "file";
}

```

## Laptop support configuration

Laptops do not need a lot of confguration support. IP addresses are set by DHCP and conditions are changeable. But you want to set your DNS search domains to familiar settings in spite of local DHCP configuration, and another useful trick is to keep a regular backup of disk changes on the local disk. This won't help against disk destruction, but it is a huge advantage when your user accidentally deletes files while travelling or offline.

```cf3
#######################################################
#

# Laptop

#

#######################################################


body common control

{
bundlesequence  => { 
                   "update",
                   "garbage_collection",
                   "main",
                   "backup",
                   };

inputs          => {
                   "update.cf",
                   "site.cf",
                   "library.cf" 
                   };
}

#######################################################


body agent control
{
# if default runtime is 5 mins we need this for long jobs

ifelapsed => "15";
}

#######################################################


body monitor control
{
forgetrate => "0.7";
}

#######################################################


body executor control

{
splaytime => "1";
mailto => "mark@iu.hio.no";
smtpserver => "localhost";
mailmaxlines => "30";

# Instead of a separate update script, now do this


exec_command => "$(sys.workdir)/bin/cf-agent -f failsafe.cf && $(sys.workdir)/bin/cf-agent";
}

#######################################################

# General site issues can be in bundles like this one

#######################################################


bundle agent main

{
vars:

  "component" slist => { "cf-monitord", "cf-serverd" };

 # - - - - - - - - - - - - - - - - - - - - - - - -


files:

  "$(sys.resolv)"  # test on "/tmp/resolv.conf" #

     create        => "true",
     edit_line     => resolver,
     edit_defaults => def;

processes:

  "$(component)" restart_class => canonify("start_$(component)");

 # - - - - - - - - - - - - - - - - - - - - - - - -


commands:

   "$(sys.workdir)/bin/$(component)"

       ifvarclass => canonify("start_$(component)");
}

#######################################################

# Backup

#######################################################


bundle agent backup
{
files:

  "/home/backup"

     copy_from => cp("/home/mark"),
  depth_search => recurse("inf"),
   file_select => exclude_files,
        action => longjob;

}

#######################################################

# Garbage collection issues

#######################################################


bundle agent garbage_collection
{
files:

  "$(sys.workdir)/outputs" 

    delete => tidy,
    file_select => days_old("3"),
    depth_search => recurse("inf");


}

```

## Find the MAC address

Finding the ethernet address can be hard, but on Linux it is straightforward.

```cf3
bundle agent test
{
vars:

linux::
 "interface" string => execresult("/sbin/ifconfig eth0","noshell");

solaris::
 "interface" string => execresult("/usr/sbin/ifconfig bge0","noshell");

freebsd::
 "interface" string => execresult("/sbin/ifconfig le0","noshell");

darwin::
 "interface" string => execresult("/sbin/ifconfig en0","noshell");

classes:

 linux::

   "ok" expression => regextract(
                                ".*HWaddr ([^\s]+).*(\n.*)*",
                                "$(interface)",
                                "mac"
                                );

 solaris::

   "ok" expression => regextract(
                                ".*ether ([^\s]+).*(\n.*)*",
                                "$(interface)",
                                "mac"
                                );

 freebsd::

   "ok" expression => regextract(
                                ".*ether ([^\s]+).*(\n.*)*",
                                "$(interface)",
                                "mac"
                                );

 darwin::

   "ok" expression => regextract(
                                "(?s).*ether ([^\s]+).*(\n.*)*",
                                "$(interface)",
                                "mac"
                                );

reports:

ok::

  "MAC address is $(mac[1])";

}

## Log rotation

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

## Manage a system process

    Ensure running
    Ensure not running
    Prune processes

### Ensure running

The simplest example might look like this:

```cf3
bundle agent restart_process
{
processes:

  "httpd" 

      comment => "Make sure apache web server is running",
      restart_class => "restart_httpd";

commands:

 restart_httpd::

     "/etc/init.d/apache2 restart";

}
```

This example shows how the CFEngine components could be started using a pattern.

```cf3
bundle agent CFEngine_processes
{
vars:

  "components" slist => { "cf-execd", "cf-monitord", "cf-serverd", "cf-hub" };

processes:

  "$(components)" 

      comment => "Make sure server parts of CFEngine are running",
      restart_class => canonify("start_$(component)");

commands:

   "$(sys.workdir)/bin/$(component)"

          comment => "Make sure server parts of CFEngine are running",
       ifvarclass => canonify("start_$(components)");

}
```

### Ensure not running

```cf3
bundle agent restart_process
{
vars:

  "killprocs" slist => { "snmpd", "gameserverd", "irc", "crack" };

processes:

  "$(killprocs)" 

      comment => "Make processes are not running",
      signals => { "term", "kill" };
;
}
```

### Prune processes

This example kills processes owned by a particular user that have exceeded 100000 bytes of resident memory.

```cf3
body common control
{
bundlesequence  => { "testbundle"  };
}

########################################################


bundle agent testbundle

{
processes:

 ".*"

    process_select  => big_processes("mark"),
            signals => { "term" };
}

########################################################


body process_select big_processes(o)

{
process_owner => { "$(o)" };
rsize => irange("100000","900000");
process_result => "rsize.process_owner";
}
```

## Manage users

There are many approaches to managing users. You can edit system files like /etc/passwd directly, or you can use commands on some systems like ‘useradd’ or ‘adduser’. In all cases it is desirable to make this a data-driven process.

    Add users
    Remove users

### Add users

A simple approach which adds new users to the password file, and to a group called ‘users’ in the group file. Is shown below. This example does not edit the shadow file. A simple pattern that can be modified for use is shown below.

Note that, although this is a simple minded approach, it is the most efficient of the approaches shown here as all operations can be carried out in a single operation for each file.

```cf3
bundle agent addusers
{
vars:

  # Add some users


  "pw[mark]" string => "mark:x:1000:100:Mark Burgess:/home/mark:/bin/bash";
  "pw[fred]" string => "fred:x:1001:100:Right Said:/home/fred:/bin/bash";
  "pw[jane]" string => "jane:x:1002:100:Jane Doe:/home/jane:/bin/bash";

  "users" slist => getindices("pw");

files:

  "/etc/passwd"
     edit_line => append_users_starting("addusers.pw");

#  "/etc/shadow"

#     edit_line => append_users_starting("$(users):defaultpasswd:::::::");


  "/etc/group"
       edit_line => append_user_field("users","4","@(addusers.users)");

  "/home/$(users)/."

     create => "true",
      perms => mog("755","$(users)","users");
}
```

A second approach is to use the shell commands supplied by some operating systems; this assumes that suitable defaults have been set up manually. Also the result is not repairable in a simple convergent manner. The command needs to edit multiple files for each user, and is quite inefficient.

```cf3
bundle agent addusers
{
vars:

  "users" slist => { "mark", "fred", "jane" };

commands:

   "/usr/sbin/useradd $(users)";
}
```

An alternative approach is to use a method to wrap around the handling of a user. Although this looks nice, it is less efficient than the first method because it must edit the files multiple times.

```cf3
bundle agent addusers
{
vars:

  # Add some users


  "pw[mark]" string => "mark:x:1000:100:Mark Burgess:/home/mark:/bin/bash";
  "pw[fred]" string => "fred:x:1001:100:Right Said:/home/fred:/bin/bash";
  "pw[jane]" string => "jane:x:1002:100:Jane Doe:/home/jane:/bin/bash";

  "users" slist => getindices("pw");

methods:

  "any" usebundle => user_add("$(users)","$(pw[$(users)])");

}

bundle agent user_add(x,pw)
{
files:

  "/etc/passwd"
     edit_line => append_users_starting("addusers.pw");

#  "/etc/shadow"

#     edit_line => append_users_starting("$(users):defaultpasswd:::::::");


  "/etc/group"
       edit_line => append_user_field("users","4","@(addusers.users)");

  "/home/$(users)/."

     create => "true",
      perms => mog("755","$(users)","users");
}

### Remove users

## Postfix mail configuration

#######################################################
#

# Postfix

#

#######################################################


body common control

{
any::

  bundlesequence  => {
                     postfix
                     };   
}

#######################################################


bundle agent postfix

{
vars:

 "prefix"     string => "/etc";
 "smtpserver" string => "localhost";
 "mailrelay"  string => "mailx.example.org";

files:

  "$(prefix)/main.cf"     
      edit_line => prefix_postfix;

  "$(prefix)/sasl-passwd" 
      create    => "true",
      perms     => mo("0600","root"),
      edit_line => append_if_no_line("$(smtpserver) _$(sys.fqhost):chmsxrcynz4etfrejizhs22");
}

#######################################################

# For the library

#######################################################


bundle edit_line prefix_postfix

{
#

# Value have the form NAME = "quoted space separated list"

#

vars:

  "ps[relayhost]"                  string => "[$(postfix.mailrelay)]:587";
  "ps[mydomain]"                   string => "iu.hio.no";
  "ps[smtp_sasl_auth_enable]"      string => "yes";
  "ps[smtp_sasl_password_maps]"    string => "hash:/etc/postfix/sasl-passwd";
  "ps[smtp_sasl_security_options]" string => "";
  "ps[smtp_use_tls]"               string => "yes";
  "ps[default_privs]"              string => "mailman";
  "ps[inet_protocols]"             string => "all";
  "ps[inet_interfaces]"            string => "127.0.0.1";

  "parameter_name" slist => getindices("ps");

delete_lines: 

  "$(parameter_name).*";

insert_lines:

  "$(parameter_name) = $(ps[$(parameter_name)])";

}

########################################################


bundle edit_line AppendIfNSL(parameter)
  {
  insert_lines:

    "$(parameter)"; # This is default
  }
```

## Set up HPC clusters

HPC cluster machines are usually all identical, so the CFEngine configuration is very simple. HPC clients value CPU and memory resources, so we can shut down unnecessary services to save CPU. We can also change the scheduling rate of CFEngine to run less frequently, and save a little:

```cf3
#######################################################


body executor control

{
splaytime => "1";
mailto => "cfengine@example.com";
smtpserver => "localhost";
mailmaxlines => "30";

# Once per hour, on the hour


schedule     => { "Min00_05" };
}

#######################################################


bundle agent services_disable
{
vars:

   # list all of xinetd services (case sensitive)


   "xinetd_services" slist => {
                               "imap",
                               "imaps",
                               "ipop2",
                               "ipop3",
                               "krb5-telnet",
                               "klogin",
                               "kshell",
                               "ktalk",
                               "ntalk",
                               "pop3s",

                              };
methods:

   # perform the actual disable all xinetd services according to the list above


   "any"  usebundle => disable_xinetd("$(xinetd_services)");

processes:

  "$(xinetd_services)"

           signals => { "kill" };

}

###############################################################################


bundle agent disable_xinetd(name)
{
 vars:
   "status" string => execresult("/sbin/chkconfig --list $(name)", "useshell");

 classes:
   "on"  expression => regcmp(".*on.*","$(status)");
   
 commands:
   on::
      "/sbin/chkconfig $(name) off",
        comment => "disable $(name) service";

 reports:
   on::
      "disable $(name) service.";
   
}
```

## Set up name resolution

There are many ways to do name resolution setup1 We write a reusable bundle using the editing features.

A simple and straightforward approach is to maintain a separate modular bundle for this task. This avoids too many levels of abstraction and keeps all the information in one place. We implement this as a simple editing promise for the /etc/resolv.conf file.

```cf3
bundle agent system_files

{
files:

  "$(sys.resolv)"  # test on "/tmp/resolv.conf" #

     comment       => "Add lines to the resolver configuration",
     create        => "true",
     edit_line     => resolver,
     edit_defaults => std_edits;

   # ...other system files ...


}

#######################################################


bundle edit_line resolver

{
delete_lines:

  # delete any old name servers or junk we no longer need


  "search.*";
  "nameserver 80.65.58.31";
  "nameserver 80.65.58.32";
  "nameserver 82.103.128.146";
  "nameserver 78.24.145.4";
  "nameserver 78.24.145.5";
  "nameserver 128.39.89.10";

insert_lines:

  "search mydomain.tld" location => start;

 special_net::

  "nameserver 128.39.89.8";
  "nameserver 128.39.74.66";

 !special_net::

  "nameserver 128.38.34.12";

 any::

  "nameserver 212.112.166.18";
  "nameserver 212.112.166.22";
}
```

A second approach is to try to conceal the operational details behind a veil of abstraction.

```cf3
bundle agent system_files
{
vars:

 "searchlist"  string => "iu.hio.no CFEngine.com";

 "nameservers" slist => { 
                        "128.39.89.10", 
                        "128.39.74.16",
                        "192.168.1.103"
                        };
files:

  "$(sys.resolv)"  # test on "/tmp/resolv.conf" #
      create        => "true",
      edit_line     => doresolv("$(s)","@(this.n)"),
      edit_defaults => empty;

 # ....


}

#######################################################


bundle edit_line doresolv(search,names)

{
insert_lines:
  "search $(search)";
  "nameserver $(names)";
}
```

DNS is not the only name service, of course. Unix has its older /etc/hosts file which can also be managed using file editing. We simply append this to the system_files bundle.

```cf3
bundle agent system_files
{

# ...


files:

   "/etc/hosts"

     comment => "Add hosts to the /etc/hosts file",
   edit_line => fix_etc_hosts;
}

###########################################################


bundle edit_line fix_etc_hosts
{
vars:

 "names[127.0.0.1]"    string => "localhost localhost.CFEngine.com";
 "names[128.39.89.12]" string => "myhost myhost.CFEngine.com";
 "names[128.39.89.13]" string => "otherhost otherhost.CFEngine.com";

 # etc


 "i" slist => getindices("names");

insert_lines:

 "$(i)     $(names[$(i)])";

}
```

## Set up sudo

Setting up sudo is straightforward, and is best managed by copying trusted files from a repository.

```cf3
bundle agent system_files
{
vars:

 "masterfiles" string => "/subversion_projects/masterfiles";

# ...


files:

   "/etc/sudoers"

     comment => "Make sure the sudo configuration is secure and up to date",
       perms => mog("440","root","root"),
   copy_from => secure_cp("$(masterfiles)/sudoers","$(policy_server)");

}
```

## Set up a web server

Adapt this template to your operating system by adding multiple classes. Each web server runs something like the present module, which is entered into the bundlesequence like this:

```cf3
#####################################################
#

# Apache webserver module

# 

#####################################################


bundle agent web_server(state)
{
vars:

  "document_root" string => "/";

 ####################################################

 # Site specific configuration - put it in this file

 ####################################################


  "site_http_conf" string => "/home/mark/CFEngine-inputs/httpd.conf";

 ####################################################

 # Software base

 ####################################################


  "match_package" slist => { 
                           "apache2", 
                           "apache2-mod_php5",
                           "apache2-prefork",
                           "php5" 
                           };

 #########################################################


processes:

  web_ok.on::

   "apache2"
 
     restart_class => "start_apache";

  off::

   "apache2"

     process_stop => "/etc/init.d/apache2 stop";


 #########################################################


commands:

 start_apache::

   "/etc/init.d/apache2 start"; # or startssl

 #########################################################


packages:

  "$(match_package)"

     package_policy => "add",
     package_method => zypper,
     classes => if_ok("software_ok");

 #########################################################


files:

 software_ok::

  "/etc/sysconfig/apache2" 

     edit_line => fixapache,
     classes => if_ok("web_ok");

 #########################################################


reports:

 !software_ok.on::

    "The web server software could not be installed";
 
 #########################################################


classes:

  "on"  expression => strcmp("$(state)","on");
  "off" expression => strcmp("$(state)","off");
}

#######################################################

# For the library

#######################################################


bundle edit_line fixapache

{
vars:

 "add_modules"     slist => { 
                            "ssl", 
                            "php5" 
                            };

 "del_modules"     slist => { 
                            "php3",
                            "php4",
                            "jk"
                            };

insert_lines:

 "APACHE_CONF_INCLUDE_FILES=\"$(web_server.site_http_conf)\"";

field_edits:

 #####################################################################

 # APACHE_MODULES="actions alias ssl php5 dav_svn authz_default jk" etc..

 #####################################################################


   "APACHE_MODULES=.*"

      # Insert module "columns" between the quoted RHS 

      # using space separators


      edit_field => quotedvar("$(add_modules)","append");

   "APACHE_MODULES=.*"

      # Delete module "columns" between the quoted RHS 

      # using space separators


      edit_field => quotedvar("$(del_modules)","delete");

   # if this line already exists, edit it  


}
```


## Templating

With CFEngine you have a choice between editing `deltas' into files or distributing more-or-less finished templates. Which method you should choose depends should be made by whatever is easiest.

    If you are managing only part of the file, and something else (e.g. a package manager) is managing most of it, then it makes sense to use CFEngine file editing.
    If you are managing everything in the file, then it makes sense to make the edits by hand and install them using CFEngine. You can use variables within source text files and let CFEngine expand them locally in situ, so that you can make generic templates that apply netwide.

Example template:

```cf3
#
# System file X

#


MYVARIABLE = something or other
HOSTNAME = $(sys.host)           # CFEngine fills this in

# ...
```


To copy and expand this template, you can use a pattern like this:

```cf3
bundle agent test
{
methods:

 "any" usebundle => get_template("/etc/sudoers","400");
 "any" usebundle => get_template("/etc/hosts","644");

}
```

The the following driving code (based on `copy then edit') can be placed in a library, after configuring to your environmental locations:

```cf3
bundle agent get_template(final_destination,mode)
{
vars:

 # This needs to ne preconfigured to your site


 "masterfiles"   string => "/home/mark/tmp";
 "this_template" string => lastnode("$(final_destination)","/");

files:

  "$(final_destination).staging"

       comment => "Get template and expand variables for this host",
         perms => mo("400","root"),
     copy_from => remote_cp("$(masterfiles)/templates/$(this_template)","$(policy_server)"),
        action => if_elapsed("60");

  "$(final_destination)"

       comment => "Expand the template",
        create => "true",
     edit_line => expand_template("$(final_destination).staging"),
 edit_defaults => empty,
         perms => mo("$(mode)","root"),
        action => if_elapsed("60");

}
```
