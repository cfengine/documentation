---
layout: default
title: System File Examples
published: true
sorting: 13
tags: [Examples,System Administration,System Files]
---

* [Editing password or group files][System Files#Editing password or group files]
* [Editing password or group files custom][System Files#Editing password or group files custom]
* [Log rotation][System Files#Log rotation]
* [Garbage collection][System Files#Garbage collection]
* [Manage a system file][System Files#Manage a system file]
* [Custom editing][System Files#Custom editing]

## Editing password or group files ##

To change the password of a system, we need to edit a file. A file is a complex object – once open there is a new world of possible promises to make about its contents. CFEngine has bundles of promises that are specially for editing.

```cf3
body common control
{
bundlesequence => { "edit_passwd" };
}

bundle agent edit_passwd
{

vars:

 "userset" slist => { "user1", "user2", "user3" };

files:

  "/etc/passwd"
     edit_line => 
        set_user_field("mark","7","/set/this/shell");


  "/etc/group"
     edit_line => 
        append_user_field("root","4","@(main.userset)");

}
```

## Editing password or group files custom ##

In this example the bundles from the Community Open Promise-Body Library are included directly in the policy instead of being input as a separate file.

```cf3
body common control
{
bundlesequence => { "addpasswd" };
}

bundle agent addpasswd
{
vars:

  # want to set these values by the names of their array keys


  "pwd[mark]" string => "mark:x:1000:100:Mark Burgess:/home/mark:/bin/bash";
  "pwd[fred]" string => "fred:x:1001:100:Right Said:/home/fred:/bin/bash";
  "pwd[jane]" string => "jane:x:1002:100:Jane Doe:/home/jane:/bin/bash";

files:


  "/tmp/passwd"

        create => "true",
     edit_line => append_users_starting("addpasswd.pwd");

}

############################################################

# Library stuff

############################################################


bundle edit_line append_users_starting(v)

{
vars:

  "index"        slist => getindices("$(v)");

classes:

  "add_$(index)" not => userexists("$(index)");

insert_lines:

  "$($(v)[$(index)])",

      ifvarclass => "add_$(index)";

}

############################################################


bundle edit_line append_groups_starting(v)

{
vars:

  "index"        slist => getindices("$(v)");

classes:

  "add_$(index)" not => groupexists("$(index)");

insert_lines:

  "$($(v)[$(index)])",

      ifvarclass => "add_$(index)";

}
```