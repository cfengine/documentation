---
layout: default
title: getacls
---

[%CFEngine_function_prototype(path, type)%]

**Description:** Return the Access Control List (ACL) for a given file- or directory path.

This function returns the ACLs for a file or directory given by the `path`
argument. The `type` argument indicates whether to get the _access_ or
_default_ ACLs.

The _access_ ACLs defines the permissions for the given file or directory.
I.e., who (users, groups, others) can perform what actions (read, write,
execute) on that particular object.

The _default_ ACLs acts like a template of permissions to be inherited by
objects created within that directory. Please note that only directories can
have default ACLs.

If ACLs are not supported on the filesystem the function will return an empty
list.

**Arguments:**

- `path` : Absolute path to file or directory
- `type` : In the range `(access|default)`

**Example:**

```cf3
bundle agent __main__
{
  vars:
    "default_acls"
      slist => getacls("/tmp/foo/", "default");
    "access_acls"
      slist => getacls("/tmp/bar", "access");
}
```

**History:**

- Introduced in 3.27.0

**See also:** `filestat()`
