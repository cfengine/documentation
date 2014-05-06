---
layout: default
title: File Template Examples 
published: true
sorting: 7
tags: [Examples]
---

* [Templating][File Templates#Templating]

## Templating

With CFEngine you have a choice between editing `deltas' into files or distributing more-or-less finished templates. Which method you should choose depends should be made by whatever is easiest.

    If you are managing only part of the file, and something else (e.g. a package manager) is managing most of it, then it makes sense to use CFEngine file editing.
    If you are managing everything in the file, then it makes sense to make the edits by hand and install them using CFEngine. You can use variables within source text files and let CFEngine expand them locally in situ, so that you can make generic templates that apply netwide.

Example template:

```cf3
#
# System file X

#


MYVARIABLE = something or other
HOSTNAME = $(sys.host)           # CFEngine fills this in

# ...
```


To copy and expand this template, you can use a pattern like this:

```cf3
bundle agent test
{
methods:

 "any" usebundle => get_template("/etc/sudoers","400");
 "any" usebundle => get_template("/etc/hosts","644");

}
```

The the following driving code (based on `copy then edit') can be placed in a library, after configuring to your environmental locations:

```cf3
bundle agent get_template(final_destination,mode)
{
vars:

 # This needs to ne preconfigured to your site


 "masterfiles"   string => "/home/mark/tmp";
 "this_template" string => lastnode("$(final_destination)","/");

files:

  "$(final_destination).staging"

       comment => "Get template and expand variables for this host",
         perms => mo("400","root"),
     copy_from => remote_cp("$(masterfiles)/templates/$(this_template)","$(policy_server)"),
        action => if_elapsed("60");

  "$(final_destination)"

       comment => "Expand the template",
        create => "true",
     edit_line => expand_template("$(final_destination).staging"),
 edit_defaults => empty,
         perms => mo("$(mode)","root"),
        action => if_elapsed("60");

}
```