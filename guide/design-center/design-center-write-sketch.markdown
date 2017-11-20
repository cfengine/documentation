---
layout: default
title: Write a new Sketch
published: false
sorting: 40
tags: [design center, write sketches]
---

### Enterprise and Community Users can Write Sketches

## Overview

This page describes how to create a Design Center sketch from a basic
CFEngine agent bundle. In effect the sketch is a wrapper, taking
parameters from the Design Center API or the CFEngine Enterprise
Mission Portal, and passing them down to the agent bundle.

## The Bundle

The bundle we will wrap with a sketch is a simple use of the `users`
promise type:

```cf3
bundle agent ensure_users(users, group, homedir, shell)
{
  users:
    "$(users)" -> {"PCI-DSS-2", "Baseline_developers_2_3"}
      policy => "present",
      home_dir => "$(homedir)/$(users)",
      group_primary => $(group),
      shell => $(shell),
      handle => "ensure_user_setup",
      home_bundle => setup_home_dir($(users), $(homedir));
}

bundle agent setup_home_dir(user, group, homedir)
{
  files:
    "$(homedir)/$(user)/." create => "true";
}
```

If you don't understand what it does, please look at
[Tutorials][Tutorials] and the CFEngine [Guide][] to learn
more about CFEngine's policy language, syntax, and operation. We will
not worry about the internals except to apply namespaces and testing
guards.

## The sketch.json Metadata

The first step is to define the sketch metadata. This is the annoying
administrivia that makes a package system such as Design Center
useful. Simply take an existing `sketch.json` file such as the one below and modify it:

```
{
    manifest:
    {
        "main.cf": { description: "main file" },
        "README.md": { documentation: true },
    },

    metadata:
    {
        name: "System::Users",
	    description: "Configure users with parameters",
        version: "1.00",
        license: "MIT",
        tags: [ "cfdc", "users", "enterprise_compatible", "enterprise_3_6" ],
        authors: [ "Ted Zlatanov <tzz@lifelogs.com>" ],
        depends: { "CFEngine::sketch_template": {}, cfengine: { version: "3.6.0" }, os: [{ "linux": "Linux", "solaris": "Solaris", "aix": "AIX", "windows": "Windows" }] }
    },

    api:
    {
        // this is the name of the bundle!
        ensure_users:
        [
            { type: "bundle_options", name: "Ensure the users exist as specified" },
            { type: "environment", name: "runenv", },
            { type: "metadata", name: "mymetadata", },
	        { type: "list", name: "users", validation: "LIST_OF_STRING_NONEMPTY", description: "User names to add (separate by commas)" },
	        { type: "string", name: "group", validation: "STRING_NONEMPTY", description: "Primary user group" },
            { type: "string", name: "homedir", default: "/home", validation: "PATH_ABSOLUTE_UNIX_OR_WINDOWS", description: "Location of the user's home directory" },
            { type: "string", name: "shell", default: "/bin/bash", choice: [ "/bin/sh", "/bin/bash", "/bin/csh", "/bin/tcsh", "/bin/zsh" ], description: "User shell" },
        ],
    },

    namespace: "cfdc_users",

    interface: [ "main.cf" ],
}
```

* add any files you distribute with the sketch to the `manifest`
* set the `authors`, `tags`, `name`, `description`, etc. metadata
* define an API, which mirrors the bundle we have.  Here we do a few things extra:
  * add `bundle_options` with the name of the bundle we want to show
  * add `environment` and `metadata` parameters, which carry the "glue" between Design Center and CFEngine
  * bring in the `users`, `group`, `homedir`, and `shell` parameters with a `type`, a `default` if needed, a `validation` or a `choice` as needed, and a `description`
* set the `namespace` as shown to ensure this bundle won't conflict with others
* set the `interface` to the list of files that have to be included by CFEngine for the sketch to work, normally just `main.cf`

## main.cf: The Converted Bundle

Now `main.cf` will start with the original bundle, but we'll modify it.

```cf3
body file control
{
      namespace => "cfdc_users";
}

bundle agent ensure_users(runenv, metadata, users, group, homedir, shell)
{
#@include "REPO/sketch_template/standard.inc"
  users:
    !dc_test::
      "$(users)" -> {"PCI-DSS-2", "Baseline_developers_2_3"}
      policy => "present",
      home_dir => "$(homedir)/$(users)",
      group_primary => $(group),
      shell => $(shell),
      handle => "ensure_user_setup",
      home_bundle => setup_home_dir($(users), $(homedir));

  reports:
    dc_verbose.dc_test::
      "$(dcbundle): simulating user = $(users) with group $(group), home dir $(homedir) and shell $(shell)";
    dc_verbose.!dc_test::
      "$(dcbundle): ensuring user = $(users) with group $(group), home dir $(homedir) and shell $(shell)";
}

bundle agent setup_home_dir(user, group, homedir)
{
  files:
    "$(homedir)/$(user)/." create => "true";
}
```

* add a `namespace` matching `sketch.json`
* add the `#@include` statement which sets up the Design Center machinery
* add the `runenv` and `metadata` parameters (note you don't use them!)
* report on what you'll do, using the classes `dc_verbose` and `dc_test` which mean "you're in verbose mode" and "you're in test mode" respectively
* only make the users if not in `dc_test` mode

## Package The Sketch

This part is really too easy.  We should make it harder so you have something to complain about!

There are two steps:

* put your files in a directory (say `/my/repo/sketches/xyz` if your sketches will live under `/my/repo` and the one you made is called `xyz`). This is just the files from the manifest:
    * `README.md`, which you could cut from the manifest or auto-generate, is just a README file
    * `main.cf` which you just saw above
    * plus `sketch.json` as shown above
* regenerate the sketch index for `/my/repo` and install your sketch into `/var/cfengine/design-center/sketches` (the "live" repository of sketches).  Run the following commands:

```
cp -rp /var/cfengine/share/*Base/sketches/sketch_template /my/repo/sketches/
/var/cfengine/design-center/bin/cf-sketch --make_cfsketches --inputs /my/repo --is=/my/repo/sketches/cfsketches.json
/var/cfengine/design-center/bin/cf-sketch --make_readme --is=/my/repo/sketches/cfsketches.json
/var/cfengine/design-center/bin/cf-sketch --install-all --is=/my/repo/sketches/cfsketches.json --inputs=/var/cfengine/design-center
```

See
[Maintaining your own sketch repository][Maintaining your own sketch repository]
for these exact commands to run, with a longer explanation for each
one.

## You're Done!

That's all there is to writing a sketch. You should now look at
[sketchify - Write A New Sketch From An Existing Bundle][sketchify - Write A New Sketch From An Existing Bundle]
for a guide to using the `sketchify` tool. See
[Maintaining your own sketch repository][Maintaining your own sketch repository]
to find out how to create your own sketch repository and install sketches from it.

Your users can then use the sketch you've written as described in
[Deploy your first Policy][Deploy your first Policy].

