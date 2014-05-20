---
layout: default
title: System Administration Examples 
published: true
sorting: 12
tags: [Examples,System Administration]
---

* [Centralized Management][System Administration Examples#Centralized Management]
* [All hosts the same][System Administration Examples#All hosts the same]
* [Variation in hosts][System Administration Examples#Variation in hosts]
* [Updating from a central hub][System Administration Examples#Updating from a central hub]
* [Laptop support configuration][System Administration Examples#Laptop support configuration]
* [Process management][System Administration Examples#Process management]
* [Kill process][System Administration Examples#Kill process]
* [Restart process][System Administration Examples#Restart process]
* [Mount a filesystem][System Administration Examples#Mount a filesystem]
* [Manage a system process][System Administration Examples#Manage a system process]
* [Ensure running][System Administration Examples#Ensure running]
* [Ensure not running][System Administration Examples#Ensure not running]
* [Prune processes][System Administration Examples#Prune processes]
* [Set up HPC clusters][System Administration Examples#Set up HPC clusters]
* [Set up name resolution][System Administration Examples#Set up name resolution]
* [Set up sudo][System Administration Examples#Set up sudo]
* [Environments (virtual)][System Administration Examples#Environments (virtual)]
* [Environment variables][System Administration Examples#Environment variables]
* [Tidying garbage files][System Administration Examples#Tidying garbage files]
* Customize Message of the Day
* Ensure a process is not running
* Restart a Process
* Set up sudo
* Set up time management through NTP
* Set up name resolution with DNS

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

## Process management

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

########################################################

#

# Simple test processes 

#

########################################################


body common control

{
bundlesequence  => { "testbundle"  };
}

########################################################


bundle agent testbundle

{
processes:

 "sleep"

    process_count   => up("sleep");

reports:

 sleep_out_of_control::

   "Out of control";
}

########################################################


body process_count up(s)

{
match_range => "5,10"; # or irange("1","10");
out_of_range_define => { "$(s)_out_of_control" };
}

########################################################

#

# Simple test processes 

#

########################################################


body common control

{
bundlesequence  => { "testbundle"  };
}

########################################################


bundle agent testbundle

{
processes:

 ".*"

    process_select  => proc_finder("a.*"),
    process_count   => up("cfservd");
}

########################################################


body process_count up(s)

{
match_range => "1,10"; # or irange("1","10");
out_of_range_define => { "$(s)_out_of_control" };
}

########################################################


body process_select proc_finder(p)

{
stime_range => irange(ago("0","0","0","2","0","0"),now);
process_result => "stime";
}


########################################################

#

# Simple test processes 

#

########################################################


body common control

{
bundlesequence  => { "testbundle"  };
}

########################################################


bundle agent testbundle

{
processes:

 ".*"

    process_select  => proc_finder("a.*"),
    process_count   => up("cfservd");
}

########################################################


body process_count up(s)

{
match_range => "1,10"; # or irange("1","10");
out_of_range_define => { "$(s)_out_of_control" };
}

########################################################


body process_select proc_finder(p)

{
process_owner  => { "avahi", "bin" };
command        => "$(p)";
pid            => "100,199";
vsize          => "0,1000";
process_result => "command.(process_owner|vsize)";
}


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

########################################################

#

# Simple test process restart

#

########################################################


body common control

{
bundlesequence  => { "testbundle"  };
}

########################################################


bundle agent testbundle

{
processes:

 "cfservd"

        process_count   => up("cfservd");

 cfservd_out_of_control::

   "cfservd"

        signals         => { "stop" , "term" },
        restart_class   => "start_cfserv";


commands:

  start_cfserv::

    "/usr/local/sbin/cfservd";

}

########################################################


body process_count up(s)

{
match_range => "1,10"; # or irange("1","10");
out_of_range_define => { "$(s)_out_of_control" };
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

## Environments (virtual)

```cf3

#######################################################

#

# Virtual environments

#

#######################################################


body common control

{
bundlesequence  => { "my_vm_cloud" };   
}

#######################################################


bundle agent my_vm_cloud

{
vars:

  "vms[atlas]" slist => { "guest1", "guest2", "guest3" };

environments:

 scope||any::  # These should probably be in class "any" to ensure uniqueness

   "$(vms[$(sys.host)])"

       environment_resources => virt_xml("$(xmlfile[$(this.promiser)])"),
       environment_interface => vnet("eth0,192.168.1.100/24"),
       environment_type      => "test",
       environment_host      => "atlas";

      # default environment_state => "create" on host, and "suspended elsewhere"

}

#######################################################


body environment_resources virt_xml(specfile)
{
env_spec_file => "$(specfile)";
}

#######################################################


body environment_interface vnet(primary)
{
env_name      => "$(this.promiser)";
env_addresses => { "$(primary)" };

host1::

  env_network => "default_vnet1";

host2::

  env_network => "default_vnet2";

}
```

## Environment variables

```cf3
#######################################################

#

# Virtual environments

#

#######################################################


body common control

{
bundlesequence  => { "my_vm_cloud" };   
}

#######################################################


bundle agent my_vm_cloud

{
environments:

   "centos5"

       environment_resources => virt_xml,
       environment_type      => "xen",
       environment_host      => "ursa-minor";

      # default environment_state => "create" on host, and "suspended elsewhere"

}

#######################################################


body environment_resources virt_xml
{
env_spec_file => "/srv/xen/centos5-libvirt-create.xml";
}
```

## Tidying garbage files

Emulating the `tidy' feature of CFEngine 2.

```cf3
#######################################################
#

# Deleting files, like cf2 tidy age=0 r=inf

#

#######################################################


body common control

{
 any::

  bundlesequence  => { "testbundle" };   
}

############################################


bundle agent testbundle

{
files:

  "/tmp/test" 

    delete => tidyfiles,
    file_select => zero_age,
    depth_search => recurse("inf");
}

#########################################################


body depth_search recurse(d)

{
#include_basedir => "true";

depth => "$(d)";
}

#########################################################


body delete tidy

{
dirlinks => "delete";
rmdirs   => "false"; 
}

#########################################################


body file_select zero_age

#

# we can build old "include", "exclude", and "ignore" 

# from these as standard patterns - these bodies can

# form a library of standard patterns

#


{
mtime     => irange(ago(1,0,0,0,0,0),now);  
file_result => "mtime"; 
}

    Software distribution
    Trigger classes
```