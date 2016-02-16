---
layout: default
title: Layers of Abstraction in Policy
published: true
sorting: 2
tags: [overviews, writing policy, policy]
---

CFEngine offers a number of layers of abstraction. The most fundamental atom
in CFEngine is the promise. Promises can be made about many system issues, and
you described in what context promises are to be kept.

CFEngine is designed to handle high level simplicity (without sacrificing low
level capability) by working with configuration patterns. After all,
configuration is all about promising consistent patterns in the resources of
the system. Lists, for instance, are a particularly common kind of pattern:
*for each of the following... make a similar promise*. There are several ways
to organize patterns, using containers, lists and associative arrays.

## Menu level

At this high level, a user `selects` from a set of pre-defined `services` (or
bundles in CFEngine parlance). The selection is not made by every host, rather
one places hosts into roles that will keep certain promises.

```cf3
    bundle agent service_catalogue # menu
    {
    methods:
      any:: # selected by everyone
         "everyone" usebundle => time_management,
                    comment => "Ensure clocks are synchronized";
         "everyone" usebundle => garbage_collection,
                    comment => "Clear junk and rotate logs";

      mailservers:: # selected by hosts in class
        "mail server"  -> { "goal_3", "goal_1", "goal_2" }
                      usebundle => app_mail_postfix,
                        comment => "The mail delivery agent";
        "mail server"  -> goal_3,
                      usebundle => app_mail_imap,
                        comment => "The mail reading service";
        "mail server"  -> goal_3,
                      usebundle => app_mail_mailman,
                        comment => "The mailing list handler";
    }
```

## Bundle level

At this level, users can switch on and off predefined features, or re-use
standard methods, e.g. for editing files:

```cf3
    body common control
    {
    bundlesequence => {
                     webserver("on"),
                     dns("on"),
                     security_set("on"),
                     ftp("off")
                     };
    }
```

The set of bundles that can be selected from is extensible by the user.

## Promise level

This is the most detailed level of configuration, and gives full convergent
promise behavior to the user. At this promise level, you can specify every
detail of promise-keeping behavior, and combine promises together, reusing
bundles and methods from standard libraries, or creating your own.

```cf3
    bundle agent addpasswd
    {
    vars:

      # want to set these values by the names of their array keys

      "pwd[mark]" string => "mark:x:1000:100:Mark B:/home/mark:/bin/bash";
      "pwd[fred]" string => "fred:x:1001:100:Right Said:/home/fred:/bin/bash";
      "pwd[jane]" string => "jane:x:1002:100:Jane Doe:/home/jane:/bin/bash";

    files:

      "/etc/passwd"           # Use standard library functions
            create => "true",
           comment => "Ensure listed users are present",
             perms => mog("644","root","root"),
         edit_line => append_users_starting("addpasswd.pwd");
    }
```
