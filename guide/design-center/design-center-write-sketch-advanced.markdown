---
layout: default
title: sketchify - Write A New Sketch From An Existing Bundle
published: true
sorting: 40
tags: [design center, sketchify, sketch, bundle, write sketches]
---

### Enterprise and Community Users can Write Sketches from the Command Line

## Overview

This page describes how to create a Design Center sketch by converting an existing policy
into a sketch and by using the `sketchify` tool in `cf-sketch` to complete the process.
These steps are followed:

[Step 1. Select a policy to convert into a sketch][sketchify - Write A New Sketch From An Existing Bundle#Step 1. Select a policy to convert into a sketch]

[Step 2. Define a sketch name][sketchify - Write A New Sketch From An Existing Bundle#Step 2. Define a sketch name]

[Step 3. Define the sketch interface][sketchify - Write A New Sketch From An Existing Bundle#Step 3. Define the sketch interface]

[Step 4. Revise the policy file as necessary][sketchify - Write A New Sketch From An Existing Bundle#Step 4. Revise the policy file as necessary]

[Step 5. Use the sketchify command to wrap the policy file into a sketch structure][sketchify - Write A New Sketch From An Existing Bundle#Step 5. Use the sketchify command to wrap the policy file into a sketch structure]

[Step 6. Verify that the new sketch is ready for installation and use][sketchify - Write A New Sketch From An Existing Bundle#Step 6. Verify that the new sketch is ready for installation and use]

Refer to the `password_expiration()` bundle [example][sketchify - Write A New Sketch From An Existing Bundle#Example] as you
follow the steps outlined on this page.

_This information is from Diego Zamboni's book, [Learning CFEngine 3](http://shop.oreilly.com/basket.do?nav=ext).
Used with permission. It has been updated, reformatted and edited for website consistency._

### Before you Begin

This is an advanced topic; we assume that you know how to write
CFEngine policy, and that you are familiar with the Design Center
[command line tools][Command Line Sketches] and, if you are an
Enterprise user, with the
[Design Center UI][Design Center UI].

## Instructions

### Step 1. Select a policy to convert into a sketch

The foundation of any Design Center sketch should be a working piece of CFEngine
policy in the form of a bundle of type agent that performs the appropriate functionality.
This bundle can call other bundles or bodies as appropriate, but it should be callable
as a single point of entry. Until you become more familiar with how sketches
are structured, write your bundles first as regular CFEngine
policy, and then convert them to sketches. The instructions on this page create a sketch from the
`password_expiration()` [bundle][sketchify - Write A New Sketch From An Existing Bundle#Example].

### Step 2. Define a sketch name

Arbitrary names are acceptable, but
the Design Center by convention encourages us to use names of the form `Category::Sketch`,
or even `Category::Subcategory::Sketch`. For our password-expiration configuration
sketch, use `Security::password_expiration`.

### Step 3. Define the sketch interface

#### Identify and name configurable parameters

In our original example, all the
parameters are specified as variables inside the `password_expiration()` bundle. For
a sketch, however, we want those values as parameters to be specified by the user when they
configure the sketch. The next step, then, is to look through the original code, make a
list of what those configurable parameters should be, and decide on their names:

```
pass_max_days
 The maximum password age in days.
pass_min_days
 The minimum password age, also in days.
pass_warn_age
 The warning period before a password expires, in days.
min_uid
 The minimum UID for setting password-expiration parameters. Users with UID below this threshold will not be modified.
skipped_users
 A comma-separated list of usernames to skip when setting password-expiration parameters.
skipped_uids
 A comma-separated list of UIDs to skip when setting password-expiration parameters.
```

All of these parameters can be specified as strings, just as they are in the original policy code.

#### Create a namespace

You must also decide on a **namespace** in which to place the sketch. Namespaces are top-level
naming divisions that help avoid conflicts in bundle, body, or class names.  Use a
namespace that contains the following:

* a reference to the origin of the sketch. For example, all CFEngine-produced sketches have
namespaces that start with **cfdc_**  for **CFEngine Design Center**
* the name of the sketch, or a shortened, representative version of it.

For this example, use **cflearn_password_expiration**.


### Step 4. Revise the policy file as necessary

Once the sketch interface is defined, rewrite the policy file as necessary to make it ready to
use as a sketch. Below is the updated code, with some comments about the changes made
As you go through these, compare them to the original code in the password_expiration() [bundle][sketchify - Write A New Sketch From An Existing Bundle#Example]:

```cf3
bundle agent password_expiration(pass_max_days, pass_min_days, pass_warn_age,
     min_uid, skipped_users, skipped_uids)                                           # <1>
{
  vars:
    # We store the individual parameters in an array,
    # for easier reference and file editing
    "logindefs[PASS_MAX_DAYS]" string => "$(pass_max_days)";                         # <2>
    "logindefs[PASS_MIN_DAYS]" string => "$(pass_min_days)";
    "logindefs[PASS_WARN_AGE]" string => "$(pass_warn_age)";

    # Position of each parameter in /etc/shadow
    "fieldnum[PASS_MIN_DAYS]" string => "4";
    "fieldnum[PASS_MAX_DAYS]" string => "5";
    "fieldnum[PASS_WARN_AGE]" string => "6";

    # List of parameters to modify
    "params" slist => getindices("logindefs");

    # Get list of users, and also generate them in canonified form
    # This list already excludes users specified by UID or name.
    "users" slist => getusers("$(skipped_users)", "$(skipped_uids)");
    "cusers[$(users)]" string => canonify("$(users)");

  classes:
    # Define classes for users that must not be modified by UID threshold
    "skip_$(cusers[$(users)])" expression => islessthan(getuid("$(users)"),
                                                           "$(min_uid)");

  files:
   linux::                                                                           # <3>
    "/etc/login.defs"
     handle => "edit_logindefs",
     comment => "Set desired login.defs parameters",
     edit_line =>
      default:set_config_values(
       "cflearn_password_expiration:password_expiration.logindefs");                 # <4>

    "/etc/shadow"
     handle => "edit_shadow_$(params)",
     comment => "Modify $(params) for individual users.",
     edit_defaults => default:backup_timestamp,                                      # <5>
     edit_line => default:set_user_field("$(users)",
                                         "$(fieldnum[$(params)])",
                                         "$(logindefs[$(params)])"),
     ifvarclass => "!skip_$(cusers[$(users)])";

  reports:
   !linux::                                                                          # <6>
    "Warning: Security::password_expiration only works on Linux for now.";
}
```

**Point by Point:**

The logic of the code has not changed, but a few things have been updated or rearranged:

<1>  We have added all the configurable parameters we determined earlier as arguments
to our `password_expiration()` bundle. All of these values are now accepted as arguments
instead of being hardcoded into the policy. This is the entry point for our sketch.

<2>  We use the new parameters throughout the code, instead of the hard-coded values
we had before.

<3>  We have added a class expression to limit the execution of the sketch to systems
that support its behavior. This is necessary because a sketch might be activated on
many different systems, and it needs to do the right thing regardless of
where it is running. In this case, we have limited it to Linux systems, in which we
know the `password-expiration` parameters are configured using the `/etc/login.defs`
file.

<4>  Here is the first use of namespaces, in two places: We have added the
`default:` namespace specification to the standard library bundle
`set_config_values()`, and we have specified our sketch namespace in the fully-qualified
name of the `logindefs` array that we pass to `set_config_values()`. The
fully-qualified name of the array (`cflearn_password_expiration:password_expiration.logindefs`)
contains the namespace, the bundle name, and the array name.

<5>  We must add the `default:` namespace to all the standard library components we
use and, in this case, also to the `backup_timestamp` body and the `set_user_field()` bundle.

<6>  Finally, and to complement the limitation of functionality of the sketch to Linux
systems, we have added a `reports:` promise that prints a warning on non-Linux systems to let
users know that the sketch is non-functional on them.

We now have the policy file in a shape that is well suited for conversion into a sketch.

### Step 5. Use the sketchify command to wrap the policy file into a sketch structure

The next step is to actually wrap the revised policy file into the appropriate structure required
by a sketch, which includes putting the file into its own directory. Add to that directory
a `README`  file and a file named `sketch.json` that contains all the metadata about the
sketch, as well as all the information needed to configure and invoke it. You can find
the full specification in the
[Writing a Design Center Sketch](https://github.com/cfengine/design-center/blob/master/howto/etch_a_sketch.md)
guide, but you can also
use the `sketchify` command in `cf-sketch` to do it automatically. The `sketchify` command reads the
policy file, asks you for the appropriate information, and produces a ready-to-use sketch
in your local checkout of the Design Center repository.

The `sketchify` command takes as its only argument the file that contains our policy file,
which it reads and analyzes for bundles of type `agent`. Our policy file contains only one
bundle, so it is used automatically as the entry point for the sketch (if more than one
agent bundle is found, you will be asked which one you want to use as the sketch entry
point):

```
# /var/cfengine/design-center/bin/cf-sketch sketchify /vagrant/password_expiration.cf
Reading file '/vagrant/password_expiration.cf'.
Automatically choosing the only agent bundle in /vagrant/password_expiration.cf:
        'password_expiration'
I will now prompt you for the data needed to generate the sketch.
Please enter STOP at any prompt to interrupt the process.
```

**Note:** The Design Center framework supports sketches with more than one
entry point, but sketchify as of this writing lets you choose only one of
them.

Next, sketchify asks for general information about the sketch, including its
name, description, version number, license (most sketches in the Design Center use
the [MIT license](http://opensource.org/licenses/MIT)), tags, and author information. You
can also enter the names of other
CFEngine policy files that should be included in this sketch. Most sketches are contained
in a single **.cf** file, but if you have a very complex sketch, the ability to package
multiple **.cf** files within the same sketch could be useful:


```
Sketch name: Security::password_expiration
One-line description for the new sketch: Manage password expiration and warning periods
Sketch version number: 1.0
Sketch license: MIT
Sketch tags (comma-separated list): security,cflearn,passwords
Authors (comma-separated list, preferably of the form 'Name <email>'): Diego Zamboni <diego.zamboni@cfengine.com>
Please enter any other files that need to be included with this sketch (press Enter to stop):
```

**Note:** This has nothing to do with sketch dependencies—any file(s) you specify
here will be included within the sketch you are creating. As of this writing,
sketchify does not handle sketch dependencies. You must include
them by hand in the generated `sketch.json` file.

Next, `sketchify` queries us for the information needed for defining
the sketch API. For each parameter of the entry bundle, `sketchify`
prompts for its type, a description, and a optional default and
example values (the example value is shown in the Design Center app in
CFEngine Enterprise). In our example, we give default values for all
the parameters except `skipped_users` and `skipped_uids`:

```
Thank you. I will now prompt you for the information regarding the parameters
of the entry point for the sketch.
For each parameter, you need to provide a type, a description, and optional default and example values.
(enter STOP at any prompt to abort)

For parameter 'pass_max_days':
  Type [(1) string, (2) boolean, (3) list, (4) array]: : 1
  Short description: : Maximum password age in days
  Default value (empty for no default): : 180
  Example value (empty for no example): : 180
For parameter 'pass_min_days':
  Type [(1) string, (2) boolean, (3) list, (4) array]: : 1
  Short description: : Minimum password age in days
  Default value (empty for no default): : 5
  Example value (empty for no example): : 5
For parameter 'pass_warn_age':
  Type [(1) string, (2) boolean, (3) list, (4) array]: : 1
  Short description: : Warning period before password expires, in days
  Default value (empty for no default): : 2
  Example value (empty for no example): : 2
For parameter 'min_uid':
  Type [(1) string, (2) boolean, (3) list, (4) array]: : 1
  Short description: : Minimum UID to consider when updating existing accounts
  Default value (empty for no default): : 500
  Example value (empty for no example): : 500
For parameter 'skipped_users':
  Type [(1) string, (2) boolean, (3) list, (4) array]: : 1
  Short description: : Comma-separated list of usernames to skip when updating existing accounts
  Default value (empty for no default): :
  Example value (empty for no example): : diego,joe
For parameter 'skipped_uids':
  Type [(1) string, (2) boolean, (3) list, (4) array]: : 1
  Short description: : Comma-separated list of UIDs to skip when updating existing accounts
  Default value (empty for no default): :
  Example value (empty for no example): : 550,1027

We are done with the API!
```

Having defined the sketch API, sketchify now queries you for information about the
namespace to use for this sketch. We decided before which namespace to use, but the
namespace declaration does not yet appear in the policy file we are using, so sketchify
offers to insert it automatically:

```
Now checking the namespace declaration.

The file '/vagrant/password_expiration.cf' does not have a namespace declaration.
It is recommended that every sketch has its own namespace to avoid potential naming conflicts with other sketches or policies.
I can insert the appropriate namespace declaration, and have generated a suggested namespace for you: cfdc_security_password_expiration
Please enter the namespace to use for this sketch: : cfdc_security_password_expiration
```

**Note:** If you insert the namespace declaration in the policy file by hand, before
running it through sketchify, the command will automatically detect and use the declaration.

In addition to the parameters defined in the API, a sketch entry bundle can receive two
special parameters of type `environment` and `metadata`. If used, these parameters will be
automatically generated and passed by the Design Center framework when executing
the sketch.

* The `environment` parameter contains the name of the environment with which the
sketch has been activated. This allows the sketch to access the characteristics of
the environment, including the verbose and testing fields (interpreted as classes)
so that the sketch can easily use them as conditions to alter its behavior.

* The `metadata` parameter contains the name of an array in which the Design Center
framework automatically stores all the sketch metadata, including its name and
description, authors, etc.

If these parameters are not already passed to the entry bundle in the input file,
sketchify will ask you if you want to add them:

```
The entry point 'password_expiration' doesn't seem to receive
parameters of type 'environment' or 'metadata'.

These arguments are useful for the sketch to respond to different run
environment parameters (i.e. test or verbose mode) or to have access
to its own metadata.  I can automatically add these parameters to the
bundle, together with some boilerplate code to put their information
in classes and variables.

Would you like me to add environment/metadata parameters and code to
the sketch? (Y/n) : y
```

In addition to adding the parameters to the bundle, sketchify also adds some
boilerplate code to do the following:

* Extract the values of all fields defined in the active environment (at least
`activated`, `verbose`, and `testing`, and possibly others if defined) into both classes and
variables. For example, it will create a string variable named `verbose` that contains
the class expression stored in that field, and also a class named `verbose` that will
be set to the result of evaluating that class expression. You can then use that class
within your sketch to easily enable additional reports when verbose mode has been
activated in the current environment.

* Add some other information for better integration of the sketch into
  the CFEngine Enterprise Design Center app.

As of this writing, the following code is automatically inserted by sketchify at the top
of the bundle. This line is automatically expanded into the contents
of the template file which can be found at
`/var/cfengine/design-center/sketches/sketch_template/standard.inc`.

```cf3
#@include "REPO/sketch_template/standard.inc"
```

`sketchify` now asks you for the location under the currently-used
sketch repository where the new sketch should be stored:

```
Thank you! We are almost done.
Please enter the directory where the new sketch will be stored.
If you enter a relative path, it will be used within the currently configure sketch repository (/var/cfengine/design-center/sketches). If you enter an absolute path, it will be used as-is. The directory will be created if needed.
I have generated a suggestion based on your sketch name: security/password_expiration
Directory: security/password_expiration
```

Before writing the sketch, `sketchify` shows you a menu with all the
parameters you entered, and gives you a chance to modify them. If you
made any mistakes or want to change anything, enter the number of the
corresponding parameter and `sketchify` will prompt you for the values
again.

```
You now have a chance to modify any of the information you entered.

These are the current sketch parameters:
    1. Sketch name: Security::password_expiration
    2. One-line description for the new sketch: Manage password expiration and warning periods
    3. Sketch version number: 1.0
    4. Sketch license: MIT
    5. Sketch tags: cflearn, enterprise_compatible, passwords, security, sixified, sketchify_generated
    6. Authors: Diego Zamboni <diego.zamboni@cfengine.com>
    7. Extra manifest files:

    8. Sketch API:
         For bundle password_expiration
           pass_max_days: string (Maximum password age in days) [default value: '180']
           pass_min_days: string (Minimum password age in days) [default value: '5']
           pass_warn_age: string (Warning period before password expires, in days) [default value: '2']
           min_uid: string (Minimum UID to consider when updating existing accounts) [default value: '500']
           skipped_users: string (Comma-separated list of users to skip when updating existing accounts)
           skipped_uids: string (Comma-separated list of UIDs to skip when updating existing accounts)
    9. Namespace: cfdc_security_password_expiration
    10. Runenv and metadata parameters: Environment and metadata parameters and boilerplate code WILL be added
    11. Output directory: /var/cfengine/design-center/sketches/
Please enter the number of the part you want to modify (1-11, Enter to
continue)
```

Finally, when you press "Enter" in the prompt above, `sketchify`
writes all the files for the sketch in the appropriate directory:

```
Your new sketch will be stored under /var/cfengine/design-center/sketches/security/password_expiration
Writing /var/cfengine/design-center/sketches/security/password_expiration/sketch.json
Transferring /vagrant/password_expiration.cf to /var/cfengine/design-center/sketches/security/password_expiration/password_expiration.cf
Regenerating sketch index in /var/cfengine/design-center/sketches
Generating a README file for the new sketch.

We are done! Please check your new sketch under
/var/cfengine/design-center/sketches/security/password_expiration.
```

The sketch is created; the process is complete.

### Step 6. Verify that the new sketch is ready for installation and use

Verify this using `cf-sketch`. Search for the **password** sketch:

```
cf-sketch> search password

The following sketches match your query:

Security::password_expiration Manage password expiration and warning periods

cf-sketch> install Security::password_expiration

Sketch Security::password_expiration installed under
/var/cfengine/masterfiles/sketches.

cf-sketch> info -v Security::password_expiration

The following sketches match your query:

Sketch Security::password_expiration
Description: Manage password expiration and warning periods
Authors: Diego Zamboni <diego.zamboni@cfengine.com>
Version: 1.0
License: MIT
Tags: passwords, security, sketchify_generated, cflearn
Installed: Yes, under /var/cfengine/masterfiles/sketches
Activated: No
Parameters:
  For bundle password_expiration
    pass_max_days: string (Maximum password age in days) [default value: '180']
    pass_min_days: string (Minimum password age in days) [default value: '5']
    pass_warn_age: string (Warning period before password expires, in days)
      [default value: '2']
    min_uid: string (Minimum UID to consider when updating existing accounts)
      [default value: '500']
    skipped_users: string (Comma-separated list of usernames to skip when updating existing accounts)
    skipped_uids: string (Comma-separated list of UIDs to skip when updating existing accounts)
```

While sketchify automates most of the process of creating a sketch from an existing bundle,
it cannot handle a few items. Thus, look at the files
it generates for sanity checking. Here are some of the things you might want or need to fix by hand:

* Dependencies: If your sketch depends on other sketches, you must add them by hand to
the `depends` metadata element in the generated sketch.json file. At the moment, sketchify
automatically inserts a dependency on CFEngine 3.5.0, which is the minimum recommended
version of using Design Center sketches.

* Multiple entry points: The Design Center framework supports multiple entry
points per sketch (to different bundles). This is not supported at the moment by
sketchify, so you must add any additional entry points by hand.

* Calls to standard library bundles and bodies need to be prefixed
with `default:` so that they are correctly found when called from the
sketch namespace.

<hr>
### Example

#### password_expiration() bundle

Below is the existing policy example that is used to turn into a sketch. Refer to it as
you follow the steps for creating a sketch.

```cf3
bundle agent password_expiration
{
 vars:
    # Maximum password age
    "logindefs[PASS_MAX_DAYS]"                      string => "180";
    # Minimum password age (minimum days between changes)
    "logindefs[PASS_MIN_DAYS]"                      string =>"10";
    # Warning period (in days) before password expires
    "logindefs[PASS_WARN_AGE]"                      string => "5";
    # Position of each parameter in /etc/shadow
    "fieldnum[PASS_MIN_DAYS]"  string => "4";
    "fieldnum[PASS_MAX_DAYS]"  string => "5";
    "fieldnum[PASS_WARN_AGE]"  string => "6";

    # List of parameters to modify
    "params" slist => getindices("logindefs");
    # UIDs below this threshold will not be touched
    "uidthreshold" int => "500";
    # Additionally, these users and UIDs will not be touched.
    # These are comma-separated lists.
    "skipped_users" string => "vboxadd,nobody";
    "skipped_uids"  string => "1000,1005";

    # Get list of users, and also generate them in canonified form
    "users" slist => getusers("$(skipped_users)", "$(skipped_uids)");
    "cusers[$(users)]" string => canonify("$(users)");

 classes:
    # Define classes for users that must not be modified,
    # either by UID threshold or by username
    "skip_$(cusers[$(users)])" expression => islessthan(getuid("$(users)"),
                                                        "$(uidthreshold)");

 files:
    "/etc/login.defs"
     handle => "edit_logindefs",
     comment => "Set desired login.defs parameters",
     edit_line => set_config_values("password_expiration.logindefs");

    "/etc/shadow"
     handle => "edit_shadow_$(params)",
     comment => "Modify $(params) for individual users.",
     edit_defaults => backup_timestamp,
     edit_line => set_user_field("$(users)",
                               "$(fieldnum[$(params)])",
                               "$(logindefs[$(params)])"),
    ifvarclass => "!skip_$(cusers[$(users)])";
}
```



