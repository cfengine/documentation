---
layout: default
title: Network Examples 
published: true
sorting: 9
tags: [Examples]
---

* [Find MAC address][Network#Find MAC address]
* [Client-server example][Network#Client-server example]
* [Read from a TCP socket][Network#Read from a TCP socket]
* [Set up a PXE boot server][Network#Set up a PXE boot server]
* [Resolver management][Network#Resolver management]
* [Mount NFS filesystem][Basic File and Directory Examples#Mount NFS filesystem]
* [Unmount NFS filesystem][Basic File and Directory Examples#Unmount NFS filesystem]
* Find the MAC address
* Mount NFS filesystem

## Find MAC address ##

## Client-server example

```cf3

########################################################

#

# Simple test copy from server connection to cfServer

#

########################################################


 #

 # run this as follows:

 #

 # cf-serverd -f runtest_1.cf [-v]

 # cf-agent   -f runtest_2.cf

 #

 # Notice that the same file configures all parts of cfengine



########################################################


body common control
{
bundlesequence  => { "testbundle" };
version => "1.2.3";
#fips_mode => "true";

}

########################################################


bundle agent testbundle
{
files: 

  "/home/mark/tmp/testcopy" 
        comment  => "test copy promise",
    copy_from    => mycopy("/home/mark/LapTop/words","127.0.0.1"),
    perms        => system,
    depth_search => recurse("inf"),
    classes      => satisfied("copy_ok");

  "/home/mark/tmp/testcopy/single_file" 

        comment  => "test copy promise",
    copy_from    => mycopy("/home/mark/LapTop/Cfengine3/trunk/README","127.0.0.1"),
    perms        => system;

reports:

  copy_ok::

    "Files were copied..";
}

#########################################################


body perms system

{
mode  => "0644";
}

#########################################################


body depth_search recurse(d)

{
depth => "$(d)";
}

#########################################################


body copy_from mycopy(from,server)

{
source      => "$(from)";
servers     => { "$(server)" };
compare     => "digest";
encrypt     => "true";
verify      => "true";
copy_backup => "true";                  #/false/timestamp
purge       => "false";
type_check  => "true";
force_ipv4  => "true";
trustkey => "true";
}

#########################################################


body classes satisfied(x)
{
promise_repaired => { "$(x)" };
persist_time => "0";
}

#########################################################

# Server config

#########################################################


body server control

{
allowconnects         => { "127.0.0.1" , "::1" };
allowallconnects      => { "127.0.0.1" , "::1" };
trustkeysfrom         => { "127.0.0.1" , "::1" };
# allowusers

}

#########################################################


bundle server access_rules()

{

access:

  "/home/mark/LapTop"

    admit   => { "127.0.0.1" };
}
```

## Read from a TCP socket ##
## Set up a PXE boot server ##
## Resolver management ##

## Mount NFS filesystem

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

## Unmount NFS filesystem ##
