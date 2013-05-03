---
layout: default
title: storage-in-agent-promises
categories: [Bundles-for-agent,storage-in-agent-promises]
published: true
alias: Bundles-for-agent-storage-in-agent-promises.html
tags: [Bundles-for-agent,storage-in-agent-promises]
---

### `storage` promises in agent

\

Storage promises refer to disks and filesystem properties.

~~~~ {.smallexample}
     
      storage:
     
         "/disk volume or mountpoint"
     
           volume = volume_body,
           ...;
     
~~~~

In CFEngine 2, storage promises were divided into `disks` or `required`,
and `misc_mounts` types. The old mount-models for binary and home
servers has been deprecated and removed from CFEngine 3. Users who use
these models can reconstruct them from the low-level tools.

\

~~~~ {.verbatim}
bundle agent storage

{
storage:

  "/usr" volume  => mycheck("10%");
  "/mnt" mount   => nfs("nfsserv.example.org","/home");

}

#######################################################

body volume mycheck(free)   # reusable template

{
check_foreign  => "false";
freespace      => "$(free)";
sensible_size  => "10000";
sensible_count => "2";
}

body mount nfs(server,source)

{
mount_type => "nfs";
mount_source => "$(source)";
mount_server => "$(server)";
edit_fstab => "true";
}
~~~~

\

-   [mount in storage](#mount-in-storage)
-   [volume in storage](#volume-in-storage)

#### `mount` (body template)

**Type**: (ext body)

`edit_fstab`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    true
                    false
                    yes
                    no
                    on
                    off
~~~~

**Synopsis**: true/false add or remove entries to the file system table
("fstab")

**Default value:** false

**Example**:\
 \

~~~~ {.verbatim}
     
     body mount example
     {
     edit_fstab => "true";
     }
     
~~~~

**Notes**:\
 \

The default behaviour is to not place edits in the file system table. \

`mount_type`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    nfs
                    nfs2
                    nfs3
                    nfs4
~~~~

**Synopsis**: Protocol type of remote file system

**Example**:\
 \

~~~~ {.verbatim}
     
     body mount example
     {
     mount_type => "nfs3";
     }
     
~~~~

**Notes**:\
 \

This field is mainly for future extensions. \

`mount_source`

**Type**: string

**Allowed input range**: `"?(/.*)`

**Synopsis**: Path of remote file system to mount

**Example**:\
 \

~~~~ {.verbatim}
     
     body mount example
     {
     mount_source "/location/disk/directory";
     }
     
~~~~

**Notes**:\
 \

This is the location on the remote device, server, SAN etc. \

`mount_server`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: Hostname or IP or remote file system server

**Example**:\
 \

~~~~ {.verbatim}
     
     body mount example
     {
     mount_server => "nfs_host.example.org";
     }
     
~~~~

**Notes**:\
 \

Hostname or IP address, this could be on a SAN. \

`mount_options`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: List of option strings to add to the file system table
("fstab")

**Example**:\
 \

~~~~ {.verbatim}
     body mount example
     {
     mount_options => { "rw", "acls" };
     }
     
~~~~

**Notes**:\
 \

This list is concatenated in a form appropriate for the filesystem. The
options must be legal options for the system mount commands. \

`unmount`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    true
                    false
                    yes
                    no
                    on
                    off
~~~~

**Synopsis**: true/false unmount a previously mounted filesystem

**Default value:** false

**Example**:\
 \

~~~~ {.verbatim}
     
     body mount example
     {
     unmount => "true";
     }
     
~~~~

**Notes**:\
 \

#### `volume` (body template)

**Type**: (ext body)

`check_foreign`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    true
                    false
                    yes
                    no
                    on
                    off
~~~~

**Synopsis**: true/false verify storage that is mounted from a foreign
system on this host

**Default value:** false

**Example**:\
 \

~~~~ {.verbatim}
     
     body volume example
     
     {
     #..
     check_foreign  => "false";
     }
     
~~~~

**Notes**:\
 \

CFEngine will not normally perform sanity checks on filesystems that are
not local to the host. If `true` it will ignore a partition's network
location and ask the current host to verify storage located physically
on other systems. \

`freespace`

**Type**: string

**Allowed input range**: `[0-9]+[MBkKgGmb%]`

**Synopsis**: Absolute or percentage minimum disk space that should be
available before warning

**Example**:\
 \

~~~~ {.verbatim}
     
     body volume example1
     {
     freespace => "10%";
     }
     
     body volume example2
     {
     freespace => "50M";
     }
     
~~~~

**Notes**:\
 \

The amount of freespace that is promised on a storage device. Once this
promise is found not to be kept (that is, if the free space falls below
the promised value), warnings are generated. You may also want to use
the results of this promise to control other promises.

See: [classes in \*](#classes-in-_002a). \

`sensible_size`

**Type**: int

**Allowed input range**: `0,99999999999`

**Synopsis**: Minimum size in bytes that should be used on a
sensible-looking storage device

**Example**:\
 \

~~~~ {.verbatim}
     
     body volume example
     {
     sensible_size => "20K";
     }
     
~~~~

**Notes**:\
 \

~~~~ {.verbatim}
     
     body volume control
     {
     sensible_size => "20K";
     }
     
~~~~

\

`sensible_count`

**Type**: int

**Allowed input range**: `0,99999999999`

**Synopsis**: Minimum number of files that should be defined on a
sensible-looking storage device

**Example**:\
 \

~~~~ {.verbatim}
     
     body volume example
     {
     sensible_count => "20";
     }
     
~~~~

**Notes**:\
 \

Files must be readable by the agent. In other words, it is assumed that
the agent has privileges on volumes being checked. \

`scan_arrivals`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    true
                    false
                    yes
                    no
                    on
                    off
~~~~

**Synopsis**: true/false generate pseudo-periodic disk change arrival
distribution

**Default value:** false

**Example**:\
 \

~~~~ {.verbatim}
     
     body volume example
     {
     scan_arrivals => "true";
     }
     
~~~~

**Notes**:\
 \

This operation should not be left \`on' for more than a single run
(maximum once per week). It causes CFEngine to perform an extensive disk
scan noting the schedule of changes between files. This can be used for
a number of analyses including optimum backup schedule computation.
