---
layout: default
title: storage
published: true
tags: [reference, bundle agent, storage, storage promises, mount, filesystem, disks]
---

Storage promises refer to disks and filesystem properties.

```cf3
      storage:

         "/disk volume or mountpoint"

           volume = volume_body,
           ...;
```


```cf3
    bundle agent storage
    {
      storage:

        "/usr" volume  => mycheck("10%");
        "/mnt" mount   => nfs("nfsserv.example.org","/home");

    }

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
```

***

## Attributes ##

[%CFEngine_include_markdown(common-attributes-include.markdown)%]

### mount

**Type:** `body mount`

[%CFEngine_include_markdown(common-body-attributes-include.markdown)%]

#### edit_fstab

**Description:** true/false add or remove entries to the file system table
("fstab")

The default behavior is to not place edits in the file system table.

**Type:** [`boolean`][boolean]

**Default value:** false

**Example:**

```cf3
     body mount example
     {
       edit_fstab => "true";
     }
```

#### mount_type

**Description:** Protocol type of remote file system

**Type:** (menu option)

**Allowed input range:**

```
    nfs
    nfs2
    nfs3
    nfs4
```

**Example:**

```cf3
     body mount example
     {
     mount_type => "nfs3";
     }
```

**Notes:**
This field is mainly for future extensions.

#### mount_source

**Description:** Path of remote file system to mount.

This is the location on the remote device, server, SAN etc.

**Type:** `string`

**Allowed input range:** `"?(/.*)`

**Example:**

```cf3
     body mount example
     {
     mount_source "/location/disk/directory";
     }
```

#### mount_server

**Description:** Hostname or IP or remote file system server.

**Type:** `string`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
     body mount example
     {
       mount_server => "nfs_host.example.org";
     }
```

#### mount_options

**Description:** List of option strings to add to the file system table
("fstab").

This list is concatenated in a form appropriate for the filesystem. The
options must be legal options for the system mount commands.

**Type:** `slist`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
     body mount example
     {
       mount_options => { "rw", "acls" };
     }
```

#### unmount

**Description:** true/false unmount a previously mounted filesystem

**Type:** [`boolean`][boolean]

**Default value:** false

**Example:**

```cf3
     body mount example
     {
     unmount => "true";
     }
```

### volume

**Type:** `body volume`

[%CFEngine_include_markdown(common-body-attributes-include.markdown)%]

#### check_foreign

**Description:** If true, verify storage that is mounted from a foreign
system on this host.

CFEngine will not normally perform sanity checks on filesystems that are
not local to the host. If `true` it will ignore a partition's network
location and ask the current host to verify storage located physically
on other systems.

**Type:** [`boolean`][boolean]

**Default value:** false

**Example:**

```cf3
     body volume example
     {
       check_foreign  => "true";
     }
```

#### freespace

**Description:** Absolute or percentage minimum disk space that should be
available before warning

The amount of free space that is promised on a storage device. Once this
promise is found not to be kept (that is, if the free space falls below
the promised value), warnings are generated. You may also want to use
the results of this promise to control other promises.

**Type:** `string`

**Allowed input range:** `[0-9]+[MBkKgGmb%]`

**Example:**

```cf3
     body volume example1
     {
     freespace => "10%";
     }

     body volume example2
     {
     freespace => "50M";
     }
```

#### sensible_size

**Description:** Minimum size in bytes that should be used on a
sensible-looking storage device

**Type:** `int`

**Allowed input range:** `0,99999999999`

**Example:**

```cf3
     body volume example
     {
     sensible_size => "20K";
     }
```

#### sensible_count

**Description:** Minimum number of files that should be defined on a
sensible-looking storage device.

Files must be readable by the agent. In other words, it is assumed that
the agent has privileges on volumes being checked.

**Type:** `int`

**Allowed input range:** `0,99999999999`

**Example:**

```cf3
     body volume example
     {
     sensible_count => "20";
     }
```

#### scan_arrivals

**Description:** If true, generate pseudo-periodic disk change arrival
distribution.

This operation should not be left 'on' for more than a single run
(maximum once per week). It causes CFEngine to perform an extensive disk
scan noting the schedule of changes between files. This can be used for
a number of analyses including optimum backup schedule computation.

**Type:** [`boolean`][boolean]

**Default value:** false

**Example:**

```cf3
     body volume example
     {
       scan_arrivals => "true";
     }
```
