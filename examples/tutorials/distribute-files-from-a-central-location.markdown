---
layout: default
title: Distribute files from a central location
sorting: 10
published: true
tags: [Examples, Tutorials, file distribution]
---

CFEngine can manage many machines simply by distributing policies to all its hosts.
This tutorial describes how to distribute files to hosts from a central policy server location.
For this example, we will distribute software patches.

Files are centrally stored on the policy server (hub). In our example, they are stored in `/storage/patches`.
These patch files must also exist on the agent host (client) in `/storage/deploy/patches`. To do this,
perform the following instructions:

## Check out masterfiles from your central repository

CFEngine stores the master copy of all policy in the `/var/cfengine/masterfiles` directory.
Ensure that you are working with the latest version of your `masterfiles`.


    git clone url
or

    git pull origin master

## Make policy changes

### Define locations

Before files can be copied we must know where files should be copied from and
where files should be copied to. If these locations are used by multiple
components, then defining them in a [common bundle][Bundles]
can reduce repetition. Variables and classes that are defined in common bundles are
accessible by all [CFEngine components][Overview#CFEngine Component Applications and Daemons]. This is
especially useful in the case of file copies because the same variable
definition can be used both by the policy server when granting access and by the agent host
when performing the copy.

The policy framework includes a common bundle called ```def```. In this example, we
will add two variables--`dir_patch_store` and `dir_patch_deploy`--to this existing bundle.
These variables provide path definitions for storing and deploying patches.

Add the following variable information to the `masterfiles/def.cf` file:

```
"dir_patch_store"
  string => "/storage/patches",
  comment => "Define patch files source location",
  handle => "common_def_vars_dir_patch_store";

"dir_patch_deploy"
  string => "/storage/deploy/patches",
  comment => "Define patch files deploy location",
  handle => "common_def_vars_dir_patch_deploy";

}
```

These common variables can be referenced from the rest of the policy by using their fully
 [qualified names][Variables#Scalar Referencing and Expansion],
`$(def.dir_patch_store)` and `$(def.dir_patch_deploy)`

### Grant file access

Access must be granted before files can be copied. The right to access a file
is provided by `cf-serverd`, the server component of CFEngine. Enter access information using the `access`
promise type in a `server` bundle. The default access rules defined by the MPF (Masterfiles Policy Framework) can be found in
`controls/cf_serverd.cf`.

There is no need to modify the vendored policy, instead define your own server bundle. For our example, add the following to `services/main.cf`:

```cf3
bundle server my_access_rules
{
  access:
    "$(def.dir_patch_store)"
      handle => "server_access_grant_locations_files_patch_store_for_hosts",
      admit => { ".*$(def.domain)", @(def.acl) },
      comment => "Hosts need to download patch files from the central location";
}
```

### Create a custom library for reusable synchronization policy

You might need to frequently synchronize or copy a directory structure from the policy server to
an agent host. Thus, identifying reusable parts of policy and abstracting them for later
use is a good idea. This information is stored in a custom library.

Create a custom library called `lib/custom/files.cf`. Add the following content:

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
This reusable policy will be used to synchronize a directory on the policy server to a
directory on the agent host.

### Create a patch policy

Organize in a way that makes the most sense to you and your team. We recommend organizing
policy by services.

Create `services/patching.cf` with the following content:

```cf3
    # Patching Policy

    bundle agent patching
    # @brief Ensure various aspects of patching are handeled

    # We can break down the various parts of patching into separate bundles. This
    # allows us to become less overwhelmed by details if numerous specifics
    # exist in one or more aspect for different host classifications.
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
          comment => "If the destination directory does not exist, we have no place
                      to which to copy the patches.";

      methods:

        "Patches"
          handle    => "patch_distribution_methods_patches_from_policyserver_def_dir_patch_store_to_def_dir_patch_deploy",
          usebundle => sync_from_policyserver("$(def.dir_patch_store)", "$(def.dir_patch_deploy)"),
          comment   => "Patches need to be present on host systems so that we can use
                       them. By convention we use the policy server as the central
                       distribution point.";
    }
```

The above policy contains two bundles. We have separated a top-level patching
bundle from a more specific `patch_distribution` bundle. This is an
illustration of how to use bundles in order to abstract details. You
might, for example, have some hosts that you don’t want to fully
synchronize so you might use a different method or copy from a
different path. Creating numerous bundles allows you to move those details away from the top
level of what is involved in patching. If people are interested in what
is involved in patch distribution, they can view that bundle for specifics.

## Integrate the policy

Now that all the pieces of the policy are in place, they must be integrated
into the policy so they can be activated. Add each policy file to the [`inputs`][Components#inputs]
section which is found under `body common control`. Once the policy file is included in
inputs, the bundle can be activated. Bundles can be activated by adding them to either the
`bundlesequence` or they can be called as a `methods` type promise.

Add the following entries to `promises.cf` under `body common control` -> [`inputs`][Components#inputs]:

    "lib/custom/files.cf",
    "services/patching.cf",

and the following to `promises.cf` under `body common control` -> `bundlesequence`:

    "patching",

Now that all of the policy has been edited and is in place, check for syntax errors by
running `cf-promises -f ./promises.cf`. This promise is activated from the **service_catalogue**
bundle.


## Commit Changes

### Set up trackers in the Mission Portal (Enterprise Users Only)

Before committing the changes to your repository, log in to the Mission Portal
and set up a Tracker so that you can see the policy as it goes out. To do this, perform the
following:

Navigate to the **Hosts** section. Select **All hosts**. Select the **Events** tab, located
in the right-hand panel. Click **Add new tracker**.

![Mission Portal Host Event](hosts-add-new-tracker.png)


Name it *Patch Failure*. Set the
**Report Type** to *Promise not Kept*. Under **Watch**, enter **.patch**.  Set the **Start Time** to **Now**
and then click **Done** to close the Start Time window. Click **Start** to save the new tracker.
This tracker watches for  any promise handle that includes the string patch where a promise is not kept.

![Add New Tracker](add-new-tracker.png)

Add another tracker called *Patch Repaired*. Set the **Report Type** to *Promise Repaired*.
Enter the same values as above for **Watch** and **Start Time**. Click **Start** to save the new tracker.
This tracker allows you to see how the policy reacts as it is activated on your infrastructure.

### Deploy changes (Enterprise and Community Users)

Always inspect what you expect. `git status` shows the status of your current branch.

    git status

Inspect the changes contained in each file. Once satisfied, add them to Git's commit staging area.

    git diff file
    git add file

Iterate over using git **diff**, **add**, and **status** until all of the changes that you
expected are listed as **Changes to be committed**. Check the status once more before you
commit the changes.

    git status

Commit the changes to your local repository.

    git commit

Push the changes to the central repository so they can be pulled down to
your policy server for distribution.

    git push origin master
