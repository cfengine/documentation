---
layout: default
title: Masterfiles Policy Framework Upgrade
published: true
sorting: 14
tags: [MPF, upgrade, masterfiles, tutorial]
---

# Introduction

Upgrading the Masterfiles Policy Framework (MPF) is an *optional* but **highly
recommended** first step when upgrading CFEngine.

Upgrading the MPF is not an exact process as the details highly depend on the
specifics of the changes made to the default policy. This tutorial leverages
`git` and shows an example of upgrading a simple policy set based on 3.6.7 to
3.7.4 and can be used as a reference for upgrading your own policy sets.

# Prepare a git clone of your working masterfiles

If you are not using git and instead editing directly in
`$(sys.workdir/masterfiles)` you can simply copy your masterfiles into a new
directory and initalize a new git repository.

If you're using git already simply clone your repository and skip to the next
step.

```console
[root@hub MPF_upgrade]# rsync -a /var/cfengine/masterfiles/ MPF_upgrade/

```

Then initialize the new git repository and add all the files to it.

```console
[root@hub ~]# cd MPF_upgrade/
[root@hub MPF_upgrade]# git init
Initialized empty Git repository in /root/MPF_upgrade/.git/
[root@hub MPF_upgrade]# git add -A
[root@hub MPF_upgrade]# git commit -m "Before Upgrade"
[master (root-commit) 108c210] Before Upgrade
 78 files changed, 19980 insertions(+)
 create mode 100644 CUSTOM/policy1.cf
 create mode 100644 cf_promises_release_id
 create mode 100644 cf_promises_validated
 create mode 100644 cfe_internal/CFE_cfengine.cf
 create mode 100644 cfe_internal/CFE_hub_specific.cf
 create mode 100644 cfe_internal/CFE_knowledge.cf
 create mode 100644 cfe_internal/cfengine_processes.cf
 create mode 100644 cfe_internal/ha/ha.cf
 create mode 100644 cfe_internal/ha/ha_def.cf
 create mode 100644 cfe_internal/host_info_report.cf
 create mode 100644 controls/3.4/cf_serverd.cf
 create mode 100644 controls/cf_agent.cf
 create mode 100644 controls/cf_execd.cf
 create mode 100644 controls/cf_hub.cf
 create mode 100644 controls/cf_monitord.cf
 create mode 100644 controls/cf_runagent.cf
 create mode 100644 controls/cf_serverd.cf
 create mode 100644 def.cf
 create mode 100644 inventory/any.cf
 create mode 100644 inventory/debian.cf
 create mode 100644 inventory/generic.cf
 create mode 100644 inventory/linux.cf
 create mode 100644 inventory/lsb.cf
 create mode 100644 inventory/macos.cf
 create mode 100644 inventory/os.cf
 create mode 100644 inventory/redhat.cf
 create mode 100644 inventory/suse.cf
 create mode 100644 inventory/windows.cf
 create mode 100644 lib/3.5/bundles.cf
 create mode 100644 lib/3.5/cfe_internal.cf
 create mode 100644 lib/3.5/commands.cf
 create mode 100644 lib/3.5/common.cf
 create mode 100644 lib/3.5/databases.cf
 create mode 100644 lib/3.5/feature.cf
 create mode 100644 lib/3.5/files.cf
 create mode 100644 lib/3.5/guest_environments.cf
 create mode 100644 lib/3.5/monitor.cf
 create mode 100644 lib/3.5/packages.cf
 create mode 100644 lib/3.5/paths.cf
 create mode 100644 lib/3.5/processes.cf
 create mode 100644 lib/3.5/reports.cf
 create mode 100644 lib/3.5/services.cf
 create mode 100644 lib/3.5/storage.cf
 create mode 100644 lib/3.6/bundles.cf
 create mode 100644 lib/3.6/cfe_internal.cf
 create mode 100644 lib/3.6/cfengine_enterprise_hub_ha.cf
 create mode 100644 lib/3.6/commands.cf
 create mode 100644 lib/3.6/common.cf
 create mode 100644 lib/3.6/databases.cf
 create mode 100644 lib/3.6/edit_xml.cf
 create mode 100644 lib/3.6/examples.cf
 create mode 100644 lib/3.6/feature.cf
 create mode 100644 lib/3.6/files.cf
 create mode 100644 lib/3.6/guest_environments.cf
 create mode 100644 lib/3.6/monitor.cf
 create mode 100644 lib/3.6/packages.cf
 create mode 100644 lib/3.6/paths.cf
 create mode 100644 lib/3.6/processes.cf
 create mode 100644 lib/3.6/reports.cf
 create mode 100644 lib/3.6/services.cf
 create mode 100644 lib/3.6/stdlib.cf
 create mode 100644 lib/3.6/storage.cf
 create mode 100644 lib/3.6/users.cf
 create mode 100644 lib/3.6/vcs.cf
 create mode 100644 promises.cf
 create mode 100644 services/autorun.cf
 create mode 100644 services/autorun/custom_policy2.cf
 create mode 100644 services/autorun/hello.cf
 create mode 100644 services/file_change.cf
 create mode 100644 sketches/meta/api-runfile.cf
 create mode 100644 templates/host_info_report.mustache
 create mode 100644 update.cf
 create mode 100644 update/cfe_internal_dc_workflow.cf
 create mode 100644 update/cfe_internal_local_git_remote.cf
 create mode 100644 update/cfe_internal_update_from_repository.cf
 create mode 100644 update/update_bins.cf
 create mode 100644 update/update_policy.cf
 create mode 100644 update/update_processes.cf
[root@hub MPF_upgrade]# git status
# On branch master
nothing to commit, working directory clean
```

Now we have a git repository that we can start merging in the changes from
upstream.

# Merge the upstream changes to the MPF into your policy

## Remove everything except the .git directory.

By first removing everything we will easily be able so see which files are
*new*, *changed*, *moved* or *removed* upstream.

```console
[root@hub MPF_upgrade]# rm -rf *


[root@hub MPF_upgrade]# git status
On branch master
Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	deleted:    CUSTOM/policy1.cf
	deleted:    cf_promises_release_id
	deleted:    cf_promises_validated
	deleted:    cfe_internal/CFE_cfengine.cf
	deleted:    cfe_internal/CFE_hub_specific.cf
	deleted:    cfe_internal/CFE_knowledge.cf
	deleted:    cfe_internal/cfengine_processes.cf
	deleted:    cfe_internal/ha/ha.cf
	deleted:    cfe_internal/ha/ha_def.cf
	deleted:    cfe_internal/host_info_report.cf
	deleted:    controls/3.4/cf_serverd.cf
	deleted:    controls/cf_agent.cf
	deleted:    controls/cf_execd.cf
	deleted:    controls/cf_hub.cf
	deleted:    controls/cf_monitord.cf
	deleted:    controls/cf_runagent.cf
	deleted:    controls/cf_serverd.cf
	deleted:    def.cf
	deleted:    inventory/any.cf
	deleted:    inventory/debian.cf
	deleted:    inventory/generic.cf
	deleted:    inventory/linux.cf
	deleted:    inventory/lsb.cf
	deleted:    inventory/macos.cf
	deleted:    inventory/os.cf
	deleted:    inventory/redhat.cf
	deleted:    inventory/suse.cf
	deleted:    inventory/windows.cf
	deleted:    lib/3.5/bundles.cf
	deleted:    lib/3.5/cfe_internal.cf
	deleted:    lib/3.5/commands.cf
	deleted:    lib/3.5/common.cf
	deleted:    lib/3.5/databases.cf
	deleted:    lib/3.5/feature.cf
	deleted:    lib/3.5/files.cf
	deleted:    lib/3.5/guest_environments.cf
	deleted:    lib/3.5/monitor.cf
	deleted:    lib/3.5/packages.cf
	deleted:    lib/3.5/paths.cf
	deleted:    lib/3.5/processes.cf
	deleted:    lib/3.5/reports.cf
	deleted:    lib/3.5/services.cf
	deleted:    lib/3.5/storage.cf
	deleted:    lib/3.6/bundles.cf
	deleted:    lib/3.6/cfe_internal.cf
	deleted:    lib/3.6/cfengine_enterprise_hub_ha.cf
	deleted:    lib/3.6/commands.cf
	deleted:    lib/3.6/common.cf
	deleted:    lib/3.6/databases.cf
	deleted:    lib/3.6/edit_xml.cf
	deleted:    lib/3.6/examples.cf
	deleted:    lib/3.6/feature.cf
	deleted:    lib/3.6/files.cf
	deleted:    lib/3.6/guest_environments.cf
	deleted:    lib/3.6/monitor.cf
	deleted:    lib/3.6/packages.cf
	deleted:    lib/3.6/paths.cf
	deleted:    lib/3.6/processes.cf
	deleted:    lib/3.6/reports.cf
	deleted:    lib/3.6/services.cf
	deleted:    lib/3.6/stdlib.cf
	deleted:    lib/3.6/storage.cf
	deleted:    lib/3.6/users.cf
	deleted:    lib/3.6/vcs.cf
	deleted:    promises.cf
	deleted:    services/autorun.cf
	deleted:    services/autorun/custom_policy2.cf
	deleted:    services/autorun/hello.cf
	deleted:    services/file_change.cf
	deleted:    sketches/meta/api-runfile.cf
	deleted:    templates/host_info_report.mustache
	deleted:    update.cf
	deleted:    update/cfe_internal_dc_workflow.cf
	deleted:    update/cfe_internal_local_git_remote.cf
	deleted:    update/cfe_internal_update_from_repository.cf
	deleted:    update/update_bins.cf
	deleted:    update/update_policy.cf
	deleted:    update/update_processes.cf

no changes added to commit (use "git add" and/or "git commit -a")
```

## Install the new MPF

The new MPF can be obtained from any community package, enterprise hub
package, the separate tarball, or directly from github.

We will install the MPF from source obtained
directly from github.

**Note:** You will need =automake= to install from source.

First clone the masterfiles repository for the version you are installing. And
verify you have the correct tag checked out.

**Note:** Directly checking out a tag as in the example below is only
supported in git versions 1.7.9.5 and newer.

```console
[root@hub MPF_upgrade]# cd ..
[root@hub ~]# git clone -b 3.7.4 https://github.com/cfengine/masterfiles
[root@hub ~]# cd masterfiles
[root@hub ~]# git describe
3.7.4
```

Now we will install the masterfiles from upstream into the directory where we
are doing the integration.

First we build and install masterfiles to a temporary location.

```console
./autogen.sh
[root@hub masterfiles]# ./autogen.sh
configure.ac:31: installing `./config.guess'
configure.ac:31: installing `./config.sub'
configure.ac:34: installing `./install-sh'
configure.ac:34: installing `./missing'
checking build system type... x86_64-unknown-linux-gnu
checking host system type... x86_64-unknown-linux-gnu
checking target system type... x86_64-unknown-linux-gnu
checking for a BSD-compatible install... /usr/bin/install -c
checking whether build environment is sane... yes
checking for a thread-safe mkdir -p... /bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking how to create a ustar tar archive... gnutar
checking whether to disable maintainer-specific portions of Makefiles... yes
checking for a thread-safe mkdir -p... /bin/mkdir -p
checking for a BSD-compatible install... /usr/bin/install -c

Summary of options:
Core directory       -> not set - tests are disabled
Enterprise directory -> not set - some tests are disabled
Install prefix       -> /var/cfengine

configure: generating makefile targets
configure: creating ./config.status
config.status: creating Makefile
config.status: creating controls/3.5/update_def.cf
config.status: creating controls/3.6/update_def.cf
config.status: creating controls/3.7/update_def.cf
config.status: creating modules/packages/Makefile
config.status: creating promises.cf
config.status: creating tests/acceptance/Makefile
config.status: creating tests/unit/Makefile

DONE: Configuration done. Run "make install" to install CFEngine Masterfiles.
[root@hub masterfiles]# ./configure --prefix /tmp/masterfiles-3.7.4
checking build system type... x86_64-unknown-linux-gnu
checking host system type... x86_64-unknown-linux-gnu
checking target system type... x86_64-unknown-linux-gnu
checking for a BSD-compatible install... /usr/bin/install -c
checking whether build environment is sane... yes
checking for a thread-safe mkdir -p... /bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking how to create a ustar tar archive... gnutar
checking whether to disable maintainer-specific portions of Makefiles... yes
checking for a thread-safe mkdir -p... /bin/mkdir -p
checking for a BSD-compatible install... /usr/bin/install -c

Summary of options:
Core directory       -> not set - tests are disabled
Enterprise directory -> not set - some tests are disabled
Install prefix       -> /tmp/masterfiles-3.7.4

configure: generating makefile targets
configure: creating ./config.status
config.status: creating Makefile
config.status: creating controls/3.5/update_def.cf
config.status: creating controls/3.6/update_def.cf
config.status: creating controls/3.7/update_def.cf
config.status: creating modules/packages/Makefile
config.status: creating promises.cf
config.status: creating tests/acceptance/Makefile
config.status: creating tests/unit/Makefile

DONE: Configuration done. Run "make install" to install CFEngine Masterfiles.
```

Then after running `make install` we move the installed masterfiles into our
integration directory.

```console
[root@hub masterfiles]# mv /tmp/masterfiles-3.7.4/masterfiles/* ../MPF_upgrade
[root@hub masterfiles]# cd ../MPF_upgrade/
```

## Merge differences

Now we can use `git status` to see an overview of the changes to the
repository between our starting point and the new MPF.

```console
[root@hub MPF_upgrade]# git status
On branch master
Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	deleted:    CUSTOM/policy1.cf
	deleted:    cf_promises_release_id
	deleted:    cf_promises_validated
	modified:   cfe_internal/CFE_cfengine.cf
	deleted:    cfe_internal/CFE_hub_specific.cf
	deleted:    cfe_internal/CFE_knowledge.cf
	deleted:    cfe_internal/cfengine_processes.cf
	deleted:    cfe_internal/ha/ha.cf
	deleted:    cfe_internal/ha/ha_def.cf
	deleted:    cfe_internal/host_info_report.cf
	deleted:    controls/3.4/cf_serverd.cf
	deleted:    controls/cf_agent.cf
	deleted:    controls/cf_execd.cf
	deleted:    controls/cf_hub.cf
	deleted:    controls/cf_monitord.cf
	deleted:    controls/cf_runagent.cf
	deleted:    controls/cf_serverd.cf
	deleted:    def.cf
	modified:   inventory/any.cf
	modified:   inventory/linux.cf
	modified:   inventory/lsb.cf
	modified:   lib/3.5/cfe_internal.cf
	modified:   lib/3.5/common.cf
	modified:   lib/3.5/files.cf
	modified:   lib/3.5/packages.cf
	deleted:    lib/3.5/reports.cf
	modified:   lib/3.6/cfe_internal.cf
	modified:   lib/3.6/common.cf
	modified:   lib/3.6/files.cf
	modified:   lib/3.6/packages.cf
	deleted:    lib/3.6/reports.cf
	modified:   lib/3.6/services.cf
	modified:   lib/3.6/stdlib.cf
	modified:   promises.cf
	deleted:    services/autorun.cf
	deleted:    services/autorun/custom_policy2.cf
	deleted:    services/file_change.cf
	modified:   sketches/meta/api-runfile.cf
	modified:   update.cf
	deleted:    update/cfe_internal_dc_workflow.cf
	deleted:    update/cfe_internal_local_git_remote.cf
	deleted:    update/cfe_internal_update_from_repository.cf
	deleted:    update/update_bins.cf
	deleted:    update/update_policy.cf
	deleted:    update/update_processes.cf

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	cfe_internal/core/
	cfe_internal/enterprise/
	cfe_internal/update/
	controls/3.5/
	controls/3.6/
	controls/3.7/
	inventory/freebsd.cf
	lib/3.6/autorun.cf
	lib/3.6/cfe_internal_hub.cf
	lib/3.7/
	services/main.cf

no changes added to commit (use "git add" and/or "git commit -a")
```

All of the *Untracked files* are new additions from upstream so they should be
safe to take.

```console
[root@hub MPF_upgrade]# git add cfe_internal/core/ \
cfe_internal/enterprise/ \
cfe_internal/update/ \
controls/3.5/ \
controls/3.6/ \
controls/3.7/ \
inventory/freebsd.cf \
lib/3.6/autorun.cf \
lib/3.6/cfe_internal_hub.cf \
lib/3.7/ \
services/main.cf
```

We can run git status again to see the current overview:

```console
[root@hub MPF_upgrade]# git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	new file:   cfe_internal/core/deprecated/cfengine_processes.cf
	new file:   cfe_internal/core/host_info_report.cf
	new file:   cfe_internal/core/limit_robot_agents.cf
	new file:   cfe_internal/core/log_rotation.cf
	new file:   cfe_internal/core/main.cf
	new file:   cfe_internal/enterprise/CFE_hub_specific.cf
	new file:   cfe_internal/enterprise/CFE_knowledge.cf
	new file:   cfe_internal/enterprise/file_change.cf
	new file:   cfe_internal/enterprise/ha/ha.cf
	new file:   cfe_internal/enterprise/ha/ha_def.cf
	new file:   cfe_internal/enterprise/ha/ha_update.cf
	new file:   cfe_internal/enterprise/main.cf
	new file:   cfe_internal/update/cfe_internal_dc_workflow.cf
	new file:   cfe_internal/update/cfe_internal_local_git_remote.cf
	new file:   cfe_internal/update/cfe_internal_update_from_repository.cf
	new file:   cfe_internal/update/update_bins.cf
	new file:   cfe_internal/update/update_policy.cf
	new file:   cfe_internal/update/update_processes.cf
	new file:   controls/3.5/cf_agent.cf
	new file:   controls/3.5/cf_execd.cf
	new file:   controls/3.5/cf_hub.cf
	new file:   controls/3.5/cf_monitord.cf
	new file:   controls/3.5/cf_runagent.cf
	new file:   controls/3.5/cf_serverd.cf
	new file:   controls/3.5/def.cf
	new file:   controls/3.5/def_inputs.cf
	new file:   controls/3.5/reports.cf
	new file:   controls/3.5/update_def.cf
	new file:   controls/3.5/update_def_inputs.cf
	new file:   controls/3.6/cf_agent.cf
	new file:   controls/3.6/cf_execd.cf
	new file:   controls/3.6/cf_hub.cf
	new file:   controls/3.6/cf_monitord.cf
	new file:   controls/3.6/cf_runagent.cf
	new file:   controls/3.6/cf_serverd.cf
	new file:   controls/3.6/def.cf
	new file:   controls/3.6/def_inputs.cf
	new file:   controls/3.6/reports.cf
	new file:   controls/3.6/update_def.cf
	new file:   controls/3.6/update_def_inputs.cf
	new file:   controls/3.7/cf_agent.cf
	new file:   controls/3.7/cf_execd.cf
	new file:   controls/3.7/cf_hub.cf
	new file:   controls/3.7/cf_monitord.cf
	new file:   controls/3.7/cf_runagent.cf
	new file:   controls/3.7/cf_serverd.cf
	new file:   controls/3.7/def.cf
	new file:   controls/3.7/def_inputs.cf
	new file:   controls/3.7/reports.cf
	new file:   controls/3.7/update_def.cf
	new file:   controls/3.7/update_def_inputs.cf
	new file:   inventory/freebsd.cf
	new file:   lib/3.6/autorun.cf
	new file:   lib/3.6/cfe_internal_hub.cf
	new file:   lib/3.7/autorun.cf
	new file:   lib/3.7/bundles.cf
	new file:   lib/3.7/cfe_internal.cf
	new file:   lib/3.7/cfe_internal_hub.cf
	new file:   lib/3.7/cfengine_enterprise_hub_ha.cf
	new file:   lib/3.7/commands.cf
	new file:   lib/3.7/common.cf
	new file:   lib/3.7/databases.cf
	new file:   lib/3.7/edit_xml.cf
	new file:   lib/3.7/examples.cf
	new file:   lib/3.7/feature.cf
	new file:   lib/3.7/files.cf
	new file:   lib/3.7/guest_environments.cf
	new file:   lib/3.7/monitor.cf
	new file:   lib/3.7/packages.cf
	new file:   lib/3.7/paths.cf
	new file:   lib/3.7/processes.cf
	new file:   lib/3.7/services.cf
	new file:   lib/3.7/stdlib.cf
	new file:   lib/3.7/storage.cf
	new file:   lib/3.7/users.cf
	new file:   lib/3.7/vcs.cf
	new file:   services/main.cf

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	deleted:    CUSTOM/policy1.cf
	deleted:    cf_promises_release_id
	deleted:    cf_promises_validated
	modified:   cfe_internal/CFE_cfengine.cf
	deleted:    cfe_internal/CFE_hub_specific.cf
	deleted:    cfe_internal/CFE_knowledge.cf
	deleted:    cfe_internal/cfengine_processes.cf
	deleted:    cfe_internal/ha/ha.cf
	deleted:    cfe_internal/ha/ha_def.cf
	deleted:    cfe_internal/host_info_report.cf
	deleted:    controls/3.4/cf_serverd.cf
	deleted:    controls/cf_agent.cf
	deleted:    controls/cf_execd.cf
	deleted:    controls/cf_hub.cf
	deleted:    controls/cf_monitord.cf
	deleted:    controls/cf_runagent.cf
	deleted:    controls/cf_serverd.cf
	deleted:    def.cf
	modified:   inventory/any.cf
	modified:   inventory/linux.cf
	modified:   inventory/lsb.cf
	modified:   lib/3.5/cfe_internal.cf
	modified:   lib/3.5/common.cf
	modified:   lib/3.5/files.cf
	modified:   lib/3.5/packages.cf
	deleted:    lib/3.5/reports.cf
	modified:   lib/3.6/cfe_internal.cf
	modified:   lib/3.6/common.cf
	modified:   lib/3.6/files.cf
	modified:   lib/3.6/packages.cf
	deleted:    lib/3.6/reports.cf
	modified:   lib/3.6/services.cf
	modified:   lib/3.6/stdlib.cf
	modified:   promises.cf
	deleted:    services/autorun.cf
	deleted:    services/autorun/custom_policy2.cf
	deleted:    services/file_change.cf
	modified:   sketches/meta/api-runfile.cf
	modified:   update.cf
	deleted:    update/cfe_internal_dc_workflow.cf
	deleted:    update/cfe_internal_local_git_remote.cf
	deleted:    update/cfe_internal_update_from_repository.cf
	deleted:    update/update_bins.cf
	deleted:    update/update_policy.cf
	deleted:    update/update_processes.cf
```

Next we want to bring back any of our custom policy files. Keeping your
polices organized together helps to make this process easy. The custom policy
files in the example policy set are `CUSTOM/policy1.cf` and
`services/autorun/custom_policy2.cf`. Restore them with `git checkout`.

```console
[root@hub MPF_upgrade] git checkout CUSTOM/policy1.cf services/autorun/custom_policy2.cf
```

The files marked as *modified* in the `git status` output are files that have
changed upstream.

```console
[root@hub MPF_upgrade]# git status | grep modified
	modified:   cfe_internal/CFE_cfengine.cf
	modified:   inventory/any.cf
	modified:   inventory/linux.cf
	modified:   inventory/lsb.cf
	modified:   lib/3.5/cfe_internal.cf
	modified:   lib/3.5/common.cf
	modified:   lib/3.5/files.cf
	modified:   lib/3.5/packages.cf
	modified:   lib/3.6/cfe_internal.cf
	modified:   lib/3.6/common.cf
	modified:   lib/3.6/files.cf
	modified:   lib/3.6/packages.cf
	modified:   lib/3.6/services.cf
	modified:   lib/3.6/stdlib.cf
	modified:   promises.cf
	modified:   sketches/meta/api-runfile.cf
	modified:   update.cf
```

For any files that you have not modified (like those in lib) simply add them
to gits staging area with `git add`. Carefully review and merge or
re-integrate your custom changes on top of the upstream files.

The remaining files in `git status` marked as *deleted* are files that have
been moved or removed from upstream.

**NOTE:** It is uncommon for any files to be moved or deleted between patch
releases (e.g. 3.7.1 -> 3.7.2).

```console
[root@hub MPF_upgrade]# git status | grep deleted
	deleted:    cf_promises_release_id
	deleted:    cf_promises_validated
	deleted:    cfe_internal/CFE_hub_specific.cf
	deleted:    cfe_internal/CFE_knowledge.cf
	deleted:    cfe_internal/cfengine_processes.cf
	deleted:    cfe_internal/ha/ha.cf
	deleted:    cfe_internal/ha/ha_def.cf
	deleted:    cfe_internal/host_info_report.cf
	deleted:    controls/3.4/cf_serverd.cf
	deleted:    controls/cf_agent.cf
	deleted:    controls/cf_execd.cf
	deleted:    controls/cf_hub.cf
	deleted:    controls/cf_monitord.cf
	deleted:    controls/cf_runagent.cf
	deleted:    controls/cf_serverd.cf
	deleted:    def.cf
	deleted:    lib/3.5/reports.cf
	deleted:    lib/3.6/reports.cf
	deleted:    services/autorun.cf
	deleted:    services/file_change.cf
	deleted:    update/cfe_internal_dc_workflow.cf
	deleted:    update/cfe_internal_local_git_remote.cf
	deleted:    update/cfe_internal_update_from_repository.cf
	deleted:    update/update_bins.cf
	deleted:    update/update_policy.cf
	deleted:    update/update_processes.cf
```

It's a good idea to review these files as some of them might have contained
modifications, especially `def.cf` and any files under `controls`. Always keep
track of the modifications you make to any of the files that ship with the
MPF. Make sure that any necessary customization's to the deleted files are
carried through to their new locations.

Once the files are no longer needed you can `git rm` them.

```console
[root@hub MPF_upgrade]# git rm def.cf cf_promises_release_id cf_promises_validated cfe_internal/CFE_hub_specific.cf cfe_internal/CFE_knowledge.cf cfe_internal/cfengine_processes.cf cfe_internal/ha/ha.cf cfe_internal/ha/ha_def.cf cfe_internal/host_info_report.cf controls/3.4/cf_serverd.cf controls/cf_agent.cf controls/cf_execd.cf controls/cf_hub.cf controls/cf_monitord.cf controls/cf_runagent.cf controls/cf_serverd.cf lib/3.5/reports.cf lib/3.6/reports.cf services/autorun.cf services/file_change.cf update/cfe_internal_dc_workflow.cf update/cfe_internal_local_git_remote.cf update/cfe_internal_update_from_repository.cf update/update_bins.cf update/update_policy.cf update/update_processes.cf
rm 'def.cf'
rm 'cf_promises_release_id'
rm 'cf_promises_validated'
rm 'cfe_internal/CFE_hub_specific.cf'
rm 'cfe_internal/CFE_knowledge.cf'
rm 'cfe_internal/cfengine_processes.cf'
rm 'cfe_internal/ha/ha.cf'
rm 'cfe_internal/ha/ha_def.cf'
rm 'cfe_internal/host_info_report.cf'
rm 'controls/3.4/cf_serverd.cf'
rm 'controls/cf_agent.cf'
rm 'controls/cf_execd.cf'
rm 'controls/cf_hub.cf'
rm 'controls/cf_monitord.cf'
rm 'controls/cf_runagent.cf'
rm 'controls/cf_serverd.cf'
rm 'lib/3.5/reports.cf'
rm 'lib/3.6/reports.cf'
rm 'services/autorun.cf'
rm 'services/file_change.cf'
rm 'update/cfe_internal_dc_workflow.cf'
rm 'update/cfe_internal_local_git_remote.cf'
rm 'update/cfe_internal_update_from_repository.cf'
rm 'update/update_bins.cf'
rm 'update/update_policy.cf'
rm 'update/update_processes.cf'
```

Review `git status` and make sure that the policy validates then commit your
changes.

```console
[root@hub MPF_upgrade]# git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	deleted:    cf_promises_release_id
	deleted:    cf_promises_validated
	modified:   cfe_internal/CFE_cfengine.cf
	renamed:    cfe_internal/cfengine_processes.cf -> cfe_internal/core/deprecated/cfengine_processes.cf
	renamed:    cfe_internal/host_info_report.cf -> cfe_internal/core/host_info_report.cf
	new file:   cfe_internal/core/limit_robot_agents.cf
	new file:   cfe_internal/core/log_rotation.cf
	new file:   cfe_internal/core/main.cf
	renamed:    cfe_internal/CFE_hub_specific.cf -> cfe_internal/enterprise/CFE_hub_specific.cf
	renamed:    cfe_internal/CFE_knowledge.cf -> cfe_internal/enterprise/CFE_knowledge.cf
	renamed:    services/file_change.cf -> cfe_internal/enterprise/file_change.cf
	new file:   cfe_internal/enterprise/ha/ha.cf
	renamed:    cfe_internal/ha/ha_def.cf -> cfe_internal/enterprise/ha/ha_def.cf
	new file:   cfe_internal/enterprise/ha/ha_update.cf
	new file:   cfe_internal/enterprise/main.cf
	deleted:    cfe_internal/ha/ha.cf
	renamed:    update/cfe_internal_dc_workflow.cf -> cfe_internal/update/cfe_internal_dc_workflow.cf
	renamed:    update/cfe_internal_local_git_remote.cf -> cfe_internal/update/cfe_internal_local_git_remote.cf
	new file:   cfe_internal/update/cfe_internal_update_from_repository.cf
	renamed:    update/update_bins.cf -> cfe_internal/update/update_bins.cf
	renamed:    update/update_policy.cf -> cfe_internal/update/update_policy.cf
	renamed:    update/update_processes.cf -> cfe_internal/update/update_processes.cf
	deleted:    controls/3.4/cf_serverd.cf
	renamed:    controls/cf_agent.cf -> controls/3.5/cf_agent.cf
	new file:   controls/3.5/cf_execd.cf
	renamed:    controls/cf_hub.cf -> controls/3.5/cf_hub.cf
	renamed:    controls/cf_monitord.cf -> controls/3.5/cf_monitord.cf
	renamed:    controls/cf_runagent.cf -> controls/3.5/cf_runagent.cf
	renamed:    controls/cf_serverd.cf -> controls/3.5/cf_serverd.cf
	renamed:    def.cf -> controls/3.5/def.cf
	new file:   controls/3.5/def_inputs.cf
	renamed:    lib/3.5/reports.cf -> controls/3.5/reports.cf
	renamed:    update.cf -> controls/3.5/update_def.cf
	new file:   controls/3.5/update_def_inputs.cf
	new file:   controls/3.6/cf_agent.cf
	new file:   controls/3.6/cf_execd.cf
	new file:   controls/3.6/cf_hub.cf
	new file:   controls/3.6/cf_monitord.cf
	new file:   controls/3.6/cf_runagent.cf
	new file:   controls/3.6/cf_serverd.cf
	new file:   controls/3.6/def.cf
	new file:   controls/3.6/def_inputs.cf
	renamed:    lib/3.6/reports.cf -> controls/3.6/reports.cf
	new file:   controls/3.6/update_def.cf
	new file:   controls/3.6/update_def_inputs.cf
	new file:   controls/3.7/cf_agent.cf
	new file:   controls/3.7/cf_execd.cf
	new file:   controls/3.7/cf_hub.cf
	new file:   controls/3.7/cf_monitord.cf
	new file:   controls/3.7/cf_runagent.cf
	new file:   controls/3.7/cf_serverd.cf
	new file:   controls/3.7/def.cf
	new file:   controls/3.7/def_inputs.cf
	new file:   controls/3.7/reports.cf
	new file:   controls/3.7/update_def.cf
	new file:   controls/3.7/update_def_inputs.cf
	deleted:    controls/cf_execd.cf
	modified:   inventory/any.cf
	new file:   inventory/freebsd.cf
	modified:   inventory/linux.cf
	modified:   inventory/lsb.cf
	modified:   lib/3.5/cfe_internal.cf
	modified:   lib/3.5/common.cf
	modified:   lib/3.5/files.cf
	modified:   lib/3.5/packages.cf
	renamed:    services/autorun.cf -> lib/3.6/autorun.cf
	modified:   lib/3.6/cfe_internal.cf
	renamed:    lib/3.6/cfe_internal.cf -> lib/3.6/cfe_internal_hub.cf
	modified:   lib/3.6/common.cf
	modified:   lib/3.6/files.cf
	modified:   lib/3.6/packages.cf
	modified:   lib/3.6/services.cf
	modified:   lib/3.6/stdlib.cf
	new file:   lib/3.7/autorun.cf
	new file:   lib/3.7/bundles.cf
	new file:   lib/3.7/cfe_internal.cf
	new file:   lib/3.7/cfe_internal_hub.cf
	new file:   lib/3.7/cfengine_enterprise_hub_ha.cf
	new file:   lib/3.7/commands.cf
	new file:   lib/3.7/common.cf
	new file:   lib/3.7/databases.cf
	new file:   lib/3.7/edit_xml.cf
	new file:   lib/3.7/examples.cf
	new file:   lib/3.7/feature.cf
	new file:   lib/3.7/files.cf
	new file:   lib/3.7/guest_environments.cf
	new file:   lib/3.7/monitor.cf
	new file:   lib/3.7/packages.cf
	new file:   lib/3.7/paths.cf
	new file:   lib/3.7/processes.cf
	new file:   lib/3.7/services.cf
	new file:   lib/3.7/stdlib.cf
	new file:   lib/3.7/storage.cf
	new file:   lib/3.7/users.cf
	new file:   lib/3.7/vcs.cf
	modified:   promises.cf
	new file:   services/main.cf
	modified:   sketches/meta/api-runfile.cf
	modified:   update.cf
	deleted:    update/cfe_internal_update_from_repository.cf

[root@hub MPF_upgrade]# cf-promises -cf ./promises.cf
[root@hub MPF_upgrade]# cf-promises -cf ./update.cf
[root@hub MPF_upgrade]# git commit -m "After Policy Upgrade"
 100 files changed, 12521 insertions(+), 1493 deletions(-)
 delete mode 100644 cf_promises_release_id
 delete mode 100644 cf_promises_validated
 rewrite cfe_internal/CFE_cfengine.cf (88%)
 rename cfe_internal/{ => core/deprecated}/cfengine_processes.cf (95%)
 rename cfe_internal/{ => core}/host_info_report.cf (98%)
 create mode 100644 cfe_internal/core/limit_robot_agents.cf
 create mode 100644 cfe_internal/core/log_rotation.cf
 create mode 100644 cfe_internal/core/main.cf
 rename cfe_internal/{ => enterprise}/CFE_hub_specific.cf (85%)
 rename cfe_internal/{ => enterprise}/CFE_knowledge.cf (100%)
 rename {services => cfe_internal/enterprise}/file_change.cf (58%)
 create mode 100644 cfe_internal/enterprise/ha/ha.cf
 rename cfe_internal/{ => enterprise}/ha/ha_def.cf (54%)
 create mode 100644 cfe_internal/enterprise/ha/ha_update.cf
 create mode 100644 cfe_internal/enterprise/main.cf
 delete mode 100644 cfe_internal/ha/ha.cf
 rename {update => cfe_internal/update}/cfe_internal_dc_workflow.cf (100%)
 rename {update => cfe_internal/update}/cfe_internal_local_git_remote.cf (100%)
 create mode 100644 cfe_internal/update/cfe_internal_update_from_repository.cf
 rename {update => cfe_internal/update}/update_bins.cf (97%)
 rename {update => cfe_internal/update}/update_policy.cf (92%)
 rename {update => cfe_internal/update}/update_processes.cf (92%)
 delete mode 100644 controls/3.4/cf_serverd.cf
 rename controls/{ => 3.5}/cf_agent.cf (80%)
 create mode 100644 controls/3.5/cf_execd.cf
 rename controls/{ => 3.5}/cf_hub.cf (100%)
 rename controls/{ => 3.5}/cf_monitord.cf (100%)
 rename controls/{ => 3.5}/cf_runagent.cf (100%)
 rename controls/{ => 3.5}/cf_serverd.cf (87%)
 rename def.cf => controls/3.5/def.cf (74%)
 create mode 100644 controls/3.5/def_inputs.cf
 rename {lib => controls}/3.5/reports.cf (80%)
 rename update.cf => controls/3.5/update_def.cf (59%)
 create mode 100644 controls/3.5/update_def_inputs.cf
 create mode 100644 controls/3.6/cf_agent.cf
 create mode 100644 controls/3.6/cf_execd.cf
 create mode 100644 controls/3.6/cf_hub.cf
 create mode 100644 controls/3.6/cf_monitord.cf
 create mode 100644 controls/3.6/cf_runagent.cf
 create mode 100644 controls/3.6/cf_serverd.cf
 create mode 100644 controls/3.6/def.cf
 create mode 100644 controls/3.6/def_inputs.cf
 rename {lib => controls}/3.6/reports.cf (78%)
 create mode 100644 controls/3.6/update_def.cf
 create mode 100644 controls/3.6/update_def_inputs.cf
 create mode 100644 controls/3.7/cf_agent.cf
 create mode 100644 controls/3.7/cf_execd.cf
 create mode 100644 controls/3.7/cf_hub.cf
 create mode 100644 controls/3.7/cf_monitord.cf
 create mode 100644 controls/3.7/cf_runagent.cf
 create mode 100644 controls/3.7/cf_serverd.cf
 create mode 100644 controls/3.7/def.cf
 create mode 100644 controls/3.7/def_inputs.cf
 create mode 100644 controls/3.7/reports.cf
 create mode 100644 controls/3.7/update_def.cf
 create mode 100644 controls/3.7/update_def_inputs.cf
 delete mode 100644 controls/cf_execd.cf
 create mode 100644 inventory/freebsd.cf
 rename {services => lib/3.6}/autorun.cf (50%)
 rewrite lib/3.6/cfe_internal.cf (67%)
 rename lib/3.6/{cfe_internal.cf => cfe_internal_hub.cf} (77%)
 create mode 100644 lib/3.7/autorun.cf
 create mode 100644 lib/3.7/bundles.cf
 create mode 100644 lib/3.7/cfe_internal.cf
 create mode 100644 lib/3.7/cfe_internal_hub.cf
 create mode 100644 lib/3.7/cfengine_enterprise_hub_ha.cf
 create mode 100644 lib/3.7/commands.cf
 create mode 100644 lib/3.7/common.cf
 create mode 100644 lib/3.7/databases.cf
 create mode 100644 lib/3.7/edit_xml.cf
 create mode 100644 lib/3.7/examples.cf
 create mode 100644 lib/3.7/feature.cf
 create mode 100644 lib/3.7/files.cf
 create mode 100644 lib/3.7/guest_environments.cf
 create mode 100644 lib/3.7/monitor.cf
 create mode 100644 lib/3.7/packages.cf
 create mode 100644 lib/3.7/paths.cf
 create mode 100644 lib/3.7/processes.cf
 create mode 100644 lib/3.7/services.cf
 create mode 100644 lib/3.7/stdlib.cf
 create mode 100644 lib/3.7/storage.cf
 create mode 100644 lib/3.7/users.cf
 create mode 100644 lib/3.7/vcs.cf
 create mode 100644 services/main.cf
 rewrite update.cf (78%)
 delete mode 100644 update/cfe_internal_update_from_repository.cf
```

Now your Masterfiles Policy Framework is upgraded and ready to be tested.
