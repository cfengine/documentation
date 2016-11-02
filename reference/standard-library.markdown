---
layout: default
title: Standard Library
published: false
sorting: 90
tags: [reference, standard library]
---

The standard library contains commonly-used promise bundles and bodies. It provides definitions
that you can use to build up solutions within CFEngine. The standard library is an interface
layer that brings industry-wide standardization of CFEngine configuration
scripting and hides the technical details.

To import elements of the CFEngine Standard Library into your CFEngine policy, enter the following:

```cf3
body file control
{
    inputs => { "$(sys.libdir)/files.cf", "$(sys.libdir)/packages.cf" };
}
```

You may wish to use `$(sys.libdir)` (absolute) or
`$(sys.local_libdir)` (relative) to locate these libraries, depending
on your specific policy layout.

The available pieces are:

* bodies and bundles for a specific promise type
  * `commands.cf`: see `commands`
  * `databases.cf`: see `databases`
  * `files.cf`: see `files`
  * `monitor.cf`: see `monitor`
  * `packages.cf`: see `packages`
  * `processes.cf`: see `processes`
  * `services.cf`: see `services`
  * `storage.cf`: see `storage`
  * `users.cf`: see `users`
* bodies that apply to all promise types
  * `common.cf`: `action` and [`classes`][Promise Types and Attributes#classes] bodies
* utility bundles
  * `bundles.cf`: cron jobs, log rotating, `filestat()` interface, `rm_rf`, Git-related bundles
  * `paths.cf`: standard place to find the path for many common tools and system files
  * `feature.cf`: set and unset persistent classes easily

To import the entire CFEngine Standard Library, enter the following:

```cf3
body file control
{
      # relative path
      "inputs" slist => { "$(sys.local_libdir)/stdlib.cf" };
      # absolute path
      "inputs" slist => { "$(sys.libdir)/stdlib.cf" };
}
```

Note this will not work with CFEngine 3.5 or older.  For backward
compatibility, you need to follow the approach shown in the standard
`promises.cf` main entry point for policy:

```cf3
bundle common cfengine_stdlib
{
  vars:
    cfengine_3_4::
      # This is the standard library for CFEngine 3.4 and earlier
      # (only 3.4 is explicitly supported)
      "inputs" slist => { "libraries/cfengine_stdlib.cf" };
    cfengine_3_5::
      # 3.5 doesn't have "body file control" so all the includes are listed here
      "inputs" slist => {
                          "lib/3.5/paths.cf",
                          "lib/3.5/common.cf",
                          "lib/3.5/commands.cf",
                          "lib/3.5/packages.cf",
                          "lib/3.5/files.cf",
                          "lib/3.5/services.cf",
                          "lib/3.5/processes.cf",
                          "lib/3.5/storage.cf",
                          "lib/3.5/databases.cf",
                          "lib/3.5/monitor.cf",
                          "lib/3.5/guest_environments.cf",
                          "lib/3.5/bundles.cf",
      };

    !(cfengine_3_4||cfengine_3_5)::
      # CFEngine 3.6 and higher can include through a secondary file
      "inputs" slist => { "$(sys.local_libdir)/stdlib.cf" };

  reports:
    verbose_mode::
      "$(this.bundle): defining inputs='$(inputs)'";
}
```

And then include `@(cfengine_stdlib.inputs)` in your main policy
inputs.  This is recommended **only** if you need to support CFEngine
clients running 3.5 or older!

## Feature

To use these bundles, add the following to your policy:

```cf3
body file control
{
	inputs => { "features.cf" }
}
```


[%CFEngine_library_include(lib/feature)%]

## Paths

To use these bundles, add the following to your policy:

```cf3
body file control
{
	inputs => { "paths.cf" }
}
```


[%CFEngine_library_include(lib/paths)%]
