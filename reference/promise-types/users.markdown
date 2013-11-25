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
attributes and group memberships the users should have.

Every user promise has at least one attribute, `policy`, which
describes whether or not the user should be present on the system.
Other attributes are optional; they allow you to specify UID, home
directory, login shell, group membership, description, and password.

A bundle can be associated with a user promise, such as 
when a user is created in order to do housekeeping
tasks in his/her home directory, like putting default configuration
files in place, installing encryption keys, and storing a login picture.

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

The exact use of this string depends on the operating system,
but most systems treat it as the full name of the user and therefore
display it on graphical login terminals.

[%CFEngine_promise_attribute()%]

**Example:**

```cf3
      users:
         "jsmith"
            policy => "present",
            description => "John Smith";
```

### group_primary

**Description:** The `group_primary` attribute sets the user's primary group.

**Note:** On Windows, no difference exists between primary and
secondary groups so specifying either one works.

[%CFEngine_promise_attribute()%]

**Example:**

```cf3
      users:
         "jsmith"
            policy => "present",
            group_primary => "users";
```

### groups_secondary

**Description:** The `groups_secondary` attributes sets the user's
secondary group membership(s), in addition to his/her primary group.

**Note:** On Windows, no difference exists between primary and
secondary groups so specifying either one works.

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
is evaluated when the user is created.

If the user already exists, the bundle is not evaluated.

The name of the promised user is not passed to the bundle
directly, but you can specify a bundle with parameters in order to
pass it in.

Note that this attribute does not set the home directory in the user
database. For that, you must use the `home_dir` attribute.

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
and "john." Each has his respective home directory that is created by
the `files` promise.

### home_bundle_inherit

**Description:** The `home_bundle_inherit` attribute specifies if 
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

Note that this attribute does not create the directory. For that you
must use the `home_bundle` attribute. This just sets the home
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

**Note:** On Windows, no difference exists between primary and
secondary groups so specifying either one works.

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

If the value is "hash," then the `data` attribute is expected to
contain a string with a password in hashed format. Note that CFEngine
does not validate that the given hash format is supported by
the platform. The system administrator must verify this.
However, CFEngine continues to run even in the event of an
unsupported password format, so it can always be corrected by updating
the policy.

If the value is "plaintext," then the `data` attribute contains
the password in plain text.

**Note:** On Windows, only the "plaintext" password type is supported,
due to a lack of support from the operating system for setting
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
account has on the system.

If the policy is **present**, the user is present and active
on the system. Note that an unset password might still prevent the user
from logging in.

If the policy is **locked**, the user exists on the system, but is
prevented from logging in. Note that only logins via the PAM framework
are prevented. This includes normal console logins and SSH logins
on most systems.

If the policy is **absent**, the user does not exist on the system. Note
that if a user previously existed, his/her files are not
automatically removed. You must create a separate `files` promise for
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

**Description:** The `uid` attribute specifies the user's UID number.

Note that if the UID of an existing user is changed, the files owned
by that user do not automatically change ownership. You must create a 
separate `files` promise for this.

[%CFEngine_promise_attribute()%]

**Example:**

```cf3
      users:
         "jsmith"
            uid => "1357";
```
