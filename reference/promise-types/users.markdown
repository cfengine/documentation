---
layout: default
title: users
categories: [Reference, Promise Types, users]
published: true
alias: reference-promise-types-users.html
tags: [reference, bundle agent, cf-agent, users, promise types]
---

User promises are promises made about local users on a host. They
express which users should be present on a system, and which
attributes and group memberships they should have.

Every user promise has at least one attribute, `policy`, which
describes whether the user should be present on the system or not.
Other attributes are optional, but allow you to specify UID, home
directory, login shell, group membership, description and password.

It is also possible to associate a bundle with a user promise, which
will be used when the user is created in order to do house keeping
tasks in their home directory, like putting default configuration
files in place, installing encryption keys, storing a login picture,
etc.

**History:** Introduced in CFEngine 3.6.0

**Example:**

```cf3
      users:
         "jsmith"
            policy => "present",
            description => "John Smith",
            home_dir => "/remote/home/jsmith",
            group_primary => "users",
            groups_secondary => { "printers", "webadmin" },
            shell => "/bin/bash";
```

****

## Attributes

### description

**Description:** The `description` string sets the description
associated with a user.

Exactly what this string is used for depends on the operating system,
but most systems treat it as the full name of the user and will
display on graphical login terminals.

[%CFEngine_promise_attribute()%]

**Example:**

```cf3
      users:
         "jsmith"
            policy => "present",
            description => "John Smith";
```

### group_primary

**Description:** The `group_primary` attributes sets which group the
user should have as his/her primary group.

**Note:** On Windows there is no difference between primary and
secondary groups, and specifying either one will work.

[%CFEngine_promise_attribute()%]

**Example:**

```cf3
      users:
         "jsmith"
            policy => "present",
            group_primary => "users";
```

### groups_secondary

**Description:** The `groups_secondary` attributes sets which groups
the user should be a member of, in addition to his/her primary group.

**Note:** On Windows there is no difference between primary and
secondary groups, and specifying either one will work.

[%CFEngine_promise_attribute()%]

**Example:**

```cf3
      users:
         "jsmith"
            policy => "present",
            groups_secondary => { "site_a", "tester" };
```

### home_bundle

**Description:** The `home_bundle` attribute specifies a bundle that
will be evaluated when the user is created.

If the user already exists, the bundle will not be evaluated.

The name of the promised user will not be passed to the bundle
directly, but you can specify a bundle with parameters in order to
pass that in.

Note that this attribute will not set the home directory in the user
database. For that you need to use the `home_dir` attribute.

[%CFEngine_promise_attribute()%]

**Example:**

```cf3
   bundle agent main
   {
      vars:
         "users" slist => { "jack", "john" };
      users:
         "$(users)"
            policy => "present",
            home_dir => "/home/$(users)",
            home_bundle => setup_home_dir("$(users)");
   }

   bundle agent setup_home_dir(user)
   {
      files:
         "/home/$(user)/."
            create => "true";
   }
```

This example uses implicit looping to create the two users, "jack"
and "john". Each will have their respective home directory created by
the `files` promise.

### home_bundle_inherit

**Description:** The `home_bundle_inherit` attribute specifies whether
classes set in the current bundle are inherited by the bundle
specified in the `home_bundle` attribute.

[%CFEngine_promise_attribute()%]

**Example:**

```cf3
   bundle agent main
   {
      vars:
         "user" string => "jack";
      classes:
         "should_have_home_dir" expression => regcmp("j.*", "$(user)");
      users:
         "$(user)"
            policy => "present",
            home_dir => "/home/$(user)",
            home_bundle => setup_home_dir("$(user)");
   }

   bundle agent setup_home_dir(user)
   {
      files:
         should_have_home_dir::
            "/home/$(user)/."
               create => "true";
   }
```

The user "jack" will have his home directory created, since his
username starts with "j".

### home_dir

**Description:** The `home_dir` attribute associates a user with the
given home directory.

Note that this attribute will not create the directory. For that you
need to use the `home_bundle` attribute. This just sets the home
directory in the user database.

[%CFEngine_promise_attribute()%]

**Example:**

```cf3
      users:
         "jsmith"
            policy => "present",
            home_dir => "/home/j/jsmith";
```

### password

**Description:** The `password` attribute specifies a `password` body
that contains information about a user's password.

**Note:** On Windows there is no difference between primary and
secondary groups, and specifying either one will work.

**Type:** `body password`

**Example:**

```cf3
    body password user_password
    {
        format => "hash";
          data => "jiJSlLSkZuVLE"; # "CFEngine"
    }
```

#### format

**Description:** Specifies the format of the given password data.

If the value is "hash" then the `data` attribute is expected to
contain a string with a password in hashed format. Note that CFEngine
does not do any validation that the given hash format is supported by
the platform. This is up to the system administrator to verify this.
However, CFEngine will continue to run even in the event of an
unsupported password format, so it can always be corrected by updating
the policy.

If the value is "plaintext" then the `data` attribute should contain
the password in plain text.

**Note:** On Windows only the "plaintext" password type is supported,
because of lack of support from the operating system for setting
hashed passwords.

[%CFEngine_promise_attribute()%]

**Example:**

```cf3
    body password user_password
    {
        format => "plaintext";
          data => "CFEngine";
    }
```
#### data

**Description:** Specifies the password data.

The format of the password data depends on the `format` attribute.

[%CFEngine_promise_attribute()%]

**Example:**

```cf3
    body password user_password
    {
        format => "plaintext";
          data => "CFEngine";
    }
```

### policy

**Description:** The `policy` attribute specifies what state the user
account should have on the system.

If the policy is "present", then the user will be present and active
on the system. Note that an unset password may still prevent the user
from logging in.

If the policy is "locked", the user will exist on system, but be
prevented from logging in. Note that only logins via the PAM framework
will be prevented. This includes normal console logins and SSH logins
on most systems.

If the policy is "absent", the user will not exist on the system. Note
that if a user previously existed, his/her files will not
automatically be removed. You will need a separate `files` promise for
this.

[%CFEngine_promise_attribute()%]

**Example:**

```cf3
      users:
         "jsmith"
            policy => "locked";
```

### shell

**Description:** The `shell` attribute specifies the user's login
shell.

[%CFEngine_promise_attribute()%]

**Example:**

```cf3
      users:
         "jsmith"
            shell => "/bin/bash";
```

### uid

**Description:** The `uid` attribute which UID number the user should
have.

Note that if the UID of an existing user is changed, the files owned
by that user will not automatically change ownership. You need a
separate `files` promise for this.

[%CFEngine_promise_attribute()%]

**Example:**

```cf3
      users:
         "jsmith"
            uid => "1357";
```
