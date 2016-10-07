---
layout: default
title: getuserinfo
published: true
tags: [reference, user functions, functions, getuserinfo, users, uid, gid, gecos, homedir, shell]
---

[%CFEngine_function_prototype(optional_uidorname)%]

**Description:** Return information about the current user or any other, looked up by user ID (UID) or user name.

This function searches for a user known to the system. If the
`optional_uidorname` parameter is omitted, the current user (that is currently
running the agent) is retrieved. If `optional_uidorname` is specified, the user
entry is looked up by name or ID, using the standard `getpwuid()` and
`getpwnam()` POSIX functions (but note that these functions may in turn talk to
LDAP, for instance).

On platforms that don't support these POSIX functions, the function simply fails.

[%CFEngine_function_attributes(optional_uidorname)%]

**Example:**

```cf3
    vars:
      # note the results here will vary depending on your platform
      "me" data => getuserinfo(); # the current user's info
      "root" data => getuserinfo("root"); # the "root" user's info (usually UID 0)
      "uid0" data => getuserinfo(0); # lookup user info for UID 0 (usually "root")
```

**Typical Results:**

```
  "me": {
    "description": "Mr. Current User",
    "gid": 1000,
    "home_dir": "/home/theuser",
    "shell": "/bin/sh",
    "uid": 1000,
    "username": "theuser"
  }
  
  "root": {
    "description": "root",
    "gid": 0,
    "home_dir": "/root",
    "shell": "/bin/bash",
    "uid": 0,
    "username": "root"
  }

  "uid0": {
    "description": "root",
    "gid": 0,
    "home_dir": "/root",
    "shell": "/bin/bash",
    "uid": 0,
    "username": "root"
  }
```

**History:** Introduced in CFEngine 3.10

**See also:** [`getusers()`][getusers], [`users`][users].
