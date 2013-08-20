---
layout: default
title: Distributing files from a central location
sorting: 10
categories: [Examples, Tutorials]
published: true
alias: examples-tutorials-distributing-files-from-a-central-location.html
tags: [Examples, Tutorials, file distribution]
---

We need to distribute files to hosts from a central location.

Files are centrally stored on the policy server in `/storage/patches`.
These patch files should exist on the agent host in `/storage/deploy/patches`.

## Checking out masterfiles from your central repository

Ensure your working with the latest version of your masterfiles.


    git clone url
or
    git pull origin master

## Make policy changes

Before files can be copied we must know where files should be copied from and
where files should be copied to. If these locations are used by multiple
components defining them in a [common bundle][Manuals Language Concepts Bundles]
can reduce repetition. Variables and classes defined in common bundles are
accessible by all [CFEngine components][The CFEngine Components]. This is
especially useful in the case of file copies because the same variable
definition can be used both by the server when granting access and by the agent
when performing the copy.

The policy framework includes a common bundle called def. In this example we
will add our path definitions to this existing bundle.

Here is a diff of what you should add to `def.cf` in your `masterfiles`.

    diff --git a/def.cf b/def.cf
    index 70f4a34..53befac 100755
    --- a/def.cf
    +++ b/def.cf
    @@ -51,4 +51,14 @@ bundle common def
                         comment => "Define modules path",
                          handle => "common_def_vars_dir_modules";

    +   "dir_patch_store"
    +     string => "/storage/patches",
    +     comment => "Define patch files source location",
    +     handle => "common_def_vars_dir_patch_store";
    +
    +   "dir_patch_deploy"
    +     string => "/storage/deploy/patches",
    +     comment => "Define patch files deploy location",
    +     handle => "common_def_vars_dir_patch_deploy";
    +
     }

You can see that we added two variables `dir_patch_store` and
`dir_patch_deploy` defining the locations where patches are centrally stored
and where they are to be deployed to. These common variables can be referenced
from the rest of the policy by using their fully [qualified names][Variables#scalar-referencing-and-expansion],
`$(def.dir_patch_store)` and `$(def.dir_patch_deploy)`

Access must be granted before files can be copied. The right to access a file
is promised by the server component of CFEngine (cf-serverd) using the `access`
promise type in `bundle server access_rules`. Bundle server access_rules is
located in `controls/cf_serverd.cf` in the policy framework.

Here is the diff of what should be added to `controls/cf_serverd.cf`.

    diff --git a/controls/cf_serverd.cf b/controls/cf_serverd.cf
    index 8d70a48..7f0223a 100755
    --- a/controls/cf_serverd.cf
    +++ b/controls/cf_serverd.cf
    @@ -102,6 +102,10 @@ bundle server access_rules()
          report_data_select => default_data_select_policy_hub,
                       admit => { "$(sys.policy_hub)" };

    +    "$(def.dir_patch_store)"
    +      handle => "server_access_grant_locations_files_patch_store_for_hosts",
    +      admit => { ".*$(def.domain)", @(def.acl) },
    +      comment => "Hosts need to download patch files from the central location";

     # Uncomment the promise below to allow cf-runagent to
     # access cf-agent on Windows machines

Synchronizing or copying a directory structure from the policy server to
an agent might be a frequently used method. It's a good idea to identify
reusable parts of policy and abstract them for later use.

Let's create a custom library for our reusable policy to synchronize a
directory on the policy server to a directory on the agent host.

Create `lib/custom/files.cf` with the following content:

```cf3
    bundle agent sync_from_policyserver(source_path, dest_path)
    # @brief Sync files from the policy server to the agent
    #
    # @param source_path  Location on policy server to copy files from
    # @param dest_path Location on agent host to copy files to
    {
      files:
        "$(dest_path)/."
          handle       => "sync_from_policy_server_files_dest_path_copy_from_source_path_sys_policy_hub",
          copy_from    => sync_cp("$(source_path)", "$(sys.policy_hub)"),
          depth_search => recurse("inf"),
          comment      => "Ensure files from $(sys.policy_hub):$(source_path) exist in $(dest_path)";
    }
```

We recommend organizing in a way that makes the most sense to you and your team
but we do believe that organizing things by services is one good way.

Create `services/patch.cf` with the following content.

```cf3
    # Patching Policy

    bundle agent patching
    # @brief Ensure various aspects of patching are handeled

    # We can break down the various parts of patching into seperate bundles. This
    # allows us to not become overwhelemed by details if there are a bunch of
    # specifics for in one or more aspect for different classifications of hosts.
    {
      methods:

        "Patch Distribution"
          handle    => "patching_methods_patch_distribution",
          usebundle => "patch_distribution",
          comment   => "Ensure patches are properly distributed";
    }

    bundle agent patch_distribution
    # @brief Ensures that our patches are distributed to the proper locations
    {
      files:
        "$(def.dir_patch_deploy)/."
          handle  => "patch_distribution_files_def_dir_patch_deploy_exists",
          create  => "true",
          comment => "If the destination directory does not exist we have no place
                      to copy the patches to.";

      methods:

        "Patches"
          handle    => "patch_distribution_methods_patches_from_policyserver_def_dir_patch_store_to_def_dir_patch_deploy",
          usebundle => sync_from_policyserver("$(def.dir_patch_store)", "$(def.dir_patch_deploy)"),
          comment   => "Patches need to be present on host systems so that we can use
                       them. By convention we use the policy server as the central
                       distribution point.";
    }
```

This policy has 2 bundles in it. We have separated a top level patching
bundle from a more specific `patch_distribution` bundle. This is an
illustration of how to use bundles to abstract details. You
might for example have some hosts that you don’t want full
synchronization on and might use a different method or might copy from a
different path. This allows you to move those details away from the top
level of what is involved in patching. If someone is interested in what
is involved in patch distribution they can see that bundle for specifics.

Now that all the pieces of the policy are in place they need to be integrated
into the policy so they can be activated. Each policy file that is to be
included in the policy must be included in `inputs` found in body common
control. After a policy file has been included in inputs a bundle can be
activated. Bundles can be activated by adding them to either the
`bundlesequence` or they can be called as a `methods` type promise.

Make the following edits to `promises.cf`

    diff --git a/promises.cf b/promises.cf
    index 6578765..b36262c 100755
    --- a/promises.cf
    +++ b/promises.cf
    @@ -52,6 +52,7 @@ body common control

                       # COPBL and custom body/bundle library
                         "libraries/cfengine_stdlib.cf",
    +                   "lib/custom/files.cf",

                       # Add update files to build Knowledge Map relationship
                         "update/update_bins.cf",
    @@ -60,6 +61,7 @@ body common control

                       # List of services here
                         "services/file_change.cf",
    +                    "services/patching.cf",


                       # Lessons
    @@ -95,4 +97,9 @@ bundle agent service_catalogue
                        handle => "service_catalogue_change_management",
                     usebundle => change_management;

    +   "Patching"
    +     handle => "service_catalogue_patching",
    +     usebundle => patching,
    +     comment => "A patch a day keeps the hackers away";
    +
     }

Now that all of the policy has been edited and is in place check that
there are no syntax errors by running `cf-promises -f ./promises.cf`


## Enterprise Users

Before committing the changes to your repository lets get logged into
the Mission Portal and setup a Tracker so that you can see the policy as
it goes out.

Navigate to the hosts app, select all hosts and then on the right hand
side select the events tab. Add a new tracker called *Patch Failure* with
report type *Promise not Kept* and for the watch enter `.*patch.*`
(without quotes). This will watch for any promise handle that includes
the string patch where a promise is not kept. Set the start time to now
and click start. Lets add another Tracker called *Patch repaired*. Set the
report type to *Promise Repaired*, set the watch and time as before and
click start. This tracker will allow you to see how the policy reacts as
it is activated on your infrastructure.

Now that you have a couple trackers running go ahead and deploy the
policy changes.

## Committing Changes

Now that all of our changes are ready lets deploy them to our infrastructure.

Always inspect what you expect. `git status` shows the status of your current branch.

    git status


Inspect the changes contained in each file, and when you are sure add them to git's commit staging area.

    git diff file
    git add file

Iterate over using git diff, add, and status until all of the changes that you
expected are listed as Changes to be committed. 

    git status

Commit the changes to your local repository

    git commit

Push the changes to the central repository so that they can be pulled down to
your policy server for distribution.

    git push origin master
