---
layout: default
title: getgroupinfo
---

{{< CFEngine_function_prototype(optional_gidorname) >}}

**Description:** Return information about the current group or any other, looked up by group ID (GID) or group name.

This function searches for a group known to the system.
If the `optional_gidorname` parameter is omitted, the current group (that is currently running the agent) is retrieved.
If `optional_gidorname` is specified, the group entry is looked up by name or ID, using the standard `getgrgid()` and `getgrnam()` POSIX functions (but note that these functions may in turn talk to LDAP, for instance).
On platforms that don't support these POSIX functions, the function simply fails.

{{< CFEngine_function_attributes(optional_gidorname) >}}

**Example:**

```cf3
bundle agent main
{
  vars:
    "group" data => getgroupinfo(0);

  reports:
    "$(group[name])";
    "$(group[gid])";
    "$(group[members])";
}
```

Output:

```
R: root
R: 0
```

**History:** Introduced in CFEngine 3.27

**See also:** [`getgroups()`][getgroups].
