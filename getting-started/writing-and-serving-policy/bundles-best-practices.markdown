---
layout: default
title: Bundles Best Practices
published: true
sorting: 20
tags: [manuals, bundles, policy, best practices]
---

The following contains practices to remember when creating bundles as
you write policy.

### How to choose and name bundles

Use the name of a bundle to represent a meaningful aspect of system
administration, We recommend using a two- or three-part name that
explains the context, general subject heading, and special instance.
Names should be service-oriented in order to guide non-experts to
understand what they are about.

For example:

* app_mail_postfix
* app_mail_mailman
* app_web_apache
* app_web_squid
* app_web_php
* app_db_mysql
* garbage_collection
* security_check_files
* security_check_processes
* system_name_resolution
* system_xinetd
* system_root_password
* system_processes
* system_files
* win_active_directory
* win_registry
* win_services

### When to make a bundle

Put items into a single bundle if:

* They belong to the same conceptual aspect of system administration.
* They do not need to be switched on or off independently.

Put items into different bundles if:

* All of the promises in one bundle need to the checked before all of the
promises in another bundle.
* You need to re-use the promises with different parameters.

In general, keep the number of bundles to a minimum. This is a knowledge-management issue.
Clarity comes from differentiation, but only if the number of items is small.

### When to use a paramaterized bundle or method

If you need to arrange for a managed convergent collection or sequence of promises that
will occur for a list of (multiple) names or promisers, then use a bundle to simplify the code.

Write the promises (which may or may not be ordered) using a parameter for the different
names, and then call the method passing the list of names as a parameter to reduce the amount of code.

```cf3
     bundle agent testbundle
     {
     vars:

      "userlist" slist => { "mark", "jeang", "jonhenrik", "thomas", "eben" };

     methods:

      "any" usebundle => subtest("$(userlist)");

     }

     ###########################################

     bundle agent subtest(user)

     {
     commands:

      "/bin/echo Fix $(user)";

     files:

      "/home/$(user)/."

         create =>  "true";

     reports:

      linux::

       "Finished doing stuff for $(user)";
     }
```

### When to use classes in common bundles

* When you need to use them in multiple bundles (because classes defined in common bundles
have global scope).

### When to use variables in common bundles

* For rationality, if the variable does not belong to any particular bundle, because it is
used elsewhere. (Qualified variable names such as `$(mybundle.myname)` are always globally
accessible, so this is a cosmetic issue.)

### When to use variables in local bundles

* If they are not needed outside the bundles.
* If they are used for iteration (without qualified scope).
* If they are tied to a specific aspect of system maintenance represented by the bundle, so
that accessing `$(bundle.var)` adds clarity.
