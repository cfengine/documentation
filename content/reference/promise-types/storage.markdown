---
layout: default
title: storage
aliases:
  - "/reference-promise-types-storage.html"
---

Storage promises refer to disks and filesystem properties.

```cf3 {skip TODO}
storage:

   "/disk volume or mountpoint"

     volume => volume_body,
     ...;
```

```cf3
bundle agent storage
{
  storage:
    "/usr" volume => mycheck("10%");
    "/mnt" mount => nfs("nfsserv.example.org", "/home");
}

body volume mycheck(free) # reusable template
{
  check_foreign => "false";
  freespace => "$(free)";
  sensible_size => "10000";
  sensible_count => "2";
}

body mount nfs(server, source)
{
  mount_type => "nfs";
  mount_source => "$(source)";
  mount_server => "$(server)";
  edit_fstab => "true";
}
```

---

## Attributes

{{< CFEngine_include_markdown(common-attributes.include.markdown) >}}

### mount

**Type:** `body mount`

When the promised filesystem is not mounted, only that filesystem is mounted.
To mount every entry found in the file system table, use
[`mountfilesystems` in `body agent control`][cf-agent#mountfilesystems].

**See also:** [Common body attributes][Promise types#Common body attributes]

#### edit_fstab

**Description:** true/false add or remove entries to the file system table
("fstab")

The default behavior is to not place edits in the file system table.

When enabled, the file system table entry is kept in agreement with the
promise even if the filesystem is already mounted, so a missing entry is
restored and an entry whose options have drifted is rewritten. An existing
entry is found by its mount point, and it is the options field that decides
whether the entry is rewritten. That field is compared exactly, including
order, because a duplicated or conflicting option is resolved by the kernel in
favor of the last one, which makes the order significant. When
[`mount_options`][storage#mount_options] is not specified, the entry is
written with the platform default options (`defaults` on Linux, `bg,hard,intr`
on AIX, HP-UX and Solaris, `-i,-b` on the BSDs and macOS).

For an `unmount` promise the entry is removed rather than maintained. When the
promised filesystem is mounted at the promiser, it is unmounted and its entry
is removed; when nothing is mounted there, the entry is removed anyway.

If a filesystem _other_ than the promised one is mounted at the promiser, it is
neither unmounted nor removed from the file system table. An `unmount` promise
names a specific filesystem through [`mount_source`][storage#mount_source] and
[`mount_server`][storage#mount_server]; a mount that does not match is not the
one the promise targets, so it is left alone and only reported.

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

<!--cf-promises --syntax-description=json | jq '.bodyTypes.mount.attributes.mount_type.range|split(",")'-->

- `nfs`
- `nfs2`
- `nfs3`
- `nfs4`
- `panfs`
- `cifs`

**Example:**

{{< CFEngine_include_example(storage-cifs.cf) >}}

**History:**

- `cifs`, `panfs` added in 3.15.0

#### mount_source

**Description:** Path of remote file system to mount.

This is the location on the remote device, server, SAN etc.

**Type:** `string`

**Allowed input range:** `"?(/.*)`

**Example:**

```cf3
body mount example
{
  mount_source => "/location/disk/directory";
}
```

#### mount_server

**Description:** Hostname or IP of remote file system server.

When [`remount`][storage#remount] or [`unmount`][storage#unmount] is enabled,
the server is part of the identity of the mount: a filesystem mounted from a
different server than promised does not satisfy the promise. The server of a
running mount cannot be changed by remounting it in place, so correcting it
requires `unmount_mount` in [`remount_methods`][storage#remount_methods].

Without `remount` or `unmount` the server is not compared, so a running mount
from a different server with the promised
[`mount_source`][storage#mount_source] satisfies the promise and is left as it
is. The file system table entry is still maintained from the promise, per
[`edit_fstab`][storage#edit_fstab].

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

The options are always applied to the initial mount and, when
[`edit_fstab`][storage#edit_fstab] is enabled, written to the file system
table. By default they are **not** enforced on a filesystem that is already
mounted with different options. To also reconcile the options of a running
mount, enable [`remount`][storage#remount].

**Type:** `slist`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
body mount example
{
  mount_options => { "rw", "acls" };
}
```

**See also:** [`remount`][storage#remount],
[`remount_methods`][storage#remount_methods],
[`remount_timeout`][storage#remount_timeout],
[`edit_fstab`][storage#edit_fstab]

#### unmount

**Description:** true/false unmount a previously mounted filesystem

[`mount_source`][storage#mount_source] and
[`mount_server`][storage#mount_server] select which mount to act on, so a
single mount can be unmounted (for example one served by a host being
decommissioned) without affecting others. If a filesystem other than the
promised one is mounted at the promiser, it is left mounted and its file
system table entry is left alone.

**Type:** [`boolean`][boolean]

**Default value:** false

**Example:**

```cf3
body mount example
{
  mount_source => "/export/home";
  mount_server => "decommissioned_host.example.org";
  unmount => "true";
  edit_fstab => "true";
}
```

#### remount

**Description:** true/false reconcile the options of an already-mounted
filesystem when they differ from the promise.

By default [`mount_options`][storage#mount_options] only affect the initial
mount and the file system table entry; a filesystem that is already mounted
with different options is left unchanged. When `remount` is enabled, the
promised options are compared against the running (kernel-resolved) mount and
the mount is reconciled if they differ.

Only the options the promise names are enforced; kernel-added options (for
example `vers=`, `rsize=`, `wsize=`, `timeo=`, `addr=`) and any other option
the promise does not mention are ignored. The option list is resolved with the
same "last wins" rule `mount -o` applies, so a later option overrides an
earlier conflicting one — for example `{ "defaults", "ro" }` is a read-only
mount and `{ "ro", "rw" }` is read-write. CFEngine expands `defaults` to `rw`,
`suid`, `dev`, `exec` and `async`, then checks each of those against the running
mount.

The mechanism used to reconcile is controlled by
[`remount_methods`][storage#remount_methods]. When
[`edit_fstab`][storage#edit_fstab] is also enabled, the file system table is
updated after the live mount is reconciled.

`remount` also governs whether a mount point holding a _different_ filesystem
than promised is corrected. Without it such a promise is reported as failed,
since correcting it means unmounting the filesystem and then mounting it
again; with `remount` enabled it is corrected, which additionally requires
`unmount_mount` in [`remount_methods`][storage#remount_methods] when the
source or the server differs.

**Type:** [`boolean`][boolean]

**Default value:** false

**Example:**

```cf3
body mount example
{
  remount => "true";
}
```

**History:** Introduced in 3.29.0

#### remount_methods

**Description:** Ordered list of mechanisms used to reconcile a mounted
filesystem with the promise when [`remount`][storage#remount] is enabled. By
default only the non-disruptive in-place `remount` is tried; add
`unmount_mount` to allow the disruptive fallback.

Each method is attempted in order and the result is verified against the
running mount; the first mechanism that satisfies the promise wins (the
kernel reports success from a remount even when it silently ignores
unsupported options, so the resulting state is re-read rather than trusting
the command's exit status).

- `remount` — remount in place (`mount -o remount,...`). Applies generic
  mount flags such as `ro`/`rw` and the `atime` options, but cannot change
  NFS-negotiated options such as `vers=`, `proto=` or `sec=`.
- `unmount_mount` — unmount and mount again with the promised options.
  Applies any option change and can also correct a wrong mount source, but is
  disruptive and fails if the filesystem is busy.

**Type:** `slist`

**Allowed input range:**

- `remount`
- `unmount_mount`

**Default value:** `{ "remount" }`

**Example:**

```cf3
body mount example
{
  remount => "true";

  # opt in to the disruptive fallback: try an in-place remount, then
  # unmount + mount (needed for options a remount cannot change, or a
  # wrong mount source)
  remount_methods => { "remount", "unmount_mount" };
}
```

**History:** Introduced in 3.29.0

#### remount_timeout

**Description:** Timeout in seconds applied to each mechanism in
[`remount_methods`][storage#remount_methods] when [`remount`][storage#remount]
is enabled.

Guards the potentially blocking unmount/mount path against a hung or
unreachable server.

**Type:** `int`

**Allowed input range:** `0,99999999999`

**Default value:** 60 (the RPC timeout)

**Example:**

```cf3
body mount example
{
  remount => "true";
  remount_timeout => "30";
}
```

**History:** Introduced in 3.29.0

### volume

**Type:** `body volume`

**See also:** [Common body attributes][Promise types#Common body attributes]

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
  check_foreign => "true";
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
