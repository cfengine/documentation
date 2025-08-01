---
layout: default
title: Masterfiles Policy Framework upgrade
sorting: 14
---

Upgrading the Masterfiles Policy Framework (MPF) is the first step in upgrading CFEngine from one version to another. The MPF should always be the same version or newer than the binary versions running.

Upgrading the MPF is not an exact process as the details highly depend on the specifics of the changes made to the default policy. This example leverages `git` and shows an example of upgrading a simple policy set based on `3.18.0` to `3.21.2` and can be used as a reference for upgrading your own policy sets.

# Prepare a Git clone of your working masterfiles

We will perform the integration work in `/tmp/MPF-upgrade/integration`. `masterfiles` should exist in the integration directory and is expected to be both the root of your policy set and a `git` repository.

## Validating expectations

From `/tmp/MPF-upgrade/integration/masterfiles`. Let's inspect what we expect.

Is it the root of a policy set? `promises.cf` will be present if so.

```bash
export INTEGRATION_ROOT="/tmp/MPF-upgrade/integration"
    cd $INTEGRATION_ROOT/masterfiles
if [ -e "promises.cf" ]; then
    echo "promise.cf exists, it's likely the root of a policy set"
else
    echo "promises.cf is missing, $INTEGRATION_ROOT/masterfiles does not seem like the root of a policy set"
fi
```

```output
promise.cf exists, it's likely the root of a policy set
```

Let's see what version of the MPF we are starting from by looking at `version` in `body common control` of `promises.cf`.

```command
grep -P "\s+version\s+=>" $INTEGRATION_ROOT/masterfiles/promises.cf 2>&1 \
    || echo "promises.cf is missing, $INTEGRATION_ROOT/masterfiles does not seem to be the root of a policy set"
```

```output
version => "CFEngine Promises.cf 3.18.0";
```

And finally, is it a git repository, what is the last commit?

```command
git status \
      || echo "$INTEGRATION_ROOT/masterfiles does not appear to be a git repository!" \
      && git log -1
```

```output
On branch master
nothing to commit, working tree clean
commit f4c0e120b0b45bcb9ede01ed8fb465f40b4b1e6f
Author: Nick Anderson <nick@cmdln.org>
Date:   Wed Jul 26 18:43:06 2023 -0500

    CFEngine Policy set prior to upgrade
```

# Merge upstream changes from the MPF into your policy

## Remove everything except the `.git` directory

By first removing everything we will easily be able so see which files are **new**, **changed**, **moved** or **removed** upstream.

```command
rm -rf *
```

Check `git status` to see that all the files have been deleted and are not staged for commit.

```command
git status
```

```output
On branch master
Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	deleted:    cfe_internal/CFE_cfengine.cf
	deleted:    cfe_internal/core/deprecated/cfengine_processes.cf
	deleted:    cfe_internal/core/host_info_report.cf
	deleted:    cfe_internal/core/limit_robot_agents.cf
	deleted:    cfe_internal/core/log_rotation.cf
	deleted:    cfe_internal/core/main.cf
	deleted:    cfe_internal/core/watchdog/templates/watchdog-windows.ps1.mustache
	deleted:    cfe_internal/core/watchdog/templates/watchdog.mustache
	deleted:    cfe_internal/core/watchdog/watchdog.cf
	deleted:    cfe_internal/enterprise/CFE_hub_specific.cf
	deleted:    cfe_internal/enterprise/CFE_knowledge.cf
	deleted:    cfe_internal/enterprise/federation/federation.cf
	deleted:    cfe_internal/enterprise/file_change.cf
	deleted:    cfe_internal/enterprise/ha/ha.cf
	deleted:    cfe_internal/enterprise/ha/ha_def.cf
	deleted:    cfe_internal/enterprise/ha/ha_update.cf
	deleted:    cfe_internal/enterprise/main.cf
	deleted:    cfe_internal/enterprise/mission_portal.cf
	deleted:    cfe_internal/enterprise/templates/httpd.conf.mustache
	deleted:    cfe_internal/enterprise/templates/runalerts.php.mustache
	deleted:    cfe_internal/enterprise/templates/runalerts.sh.mustache
	deleted:    cfe_internal/recommendations.cf
	deleted:    cfe_internal/update/cfe_internal_dc_workflow.cf
	deleted:    cfe_internal/update/cfe_internal_update_from_repository.cf
	deleted:    cfe_internal/update/lib.cf
	deleted:    cfe_internal/update/systemd_units.cf
	deleted:    cfe_internal/update/update_bins.cf
	deleted:    cfe_internal/update/update_policy.cf
	deleted:    cfe_internal/update/update_processes.cf
	deleted:    cfe_internal/update/windows_unattended_upgrade.cf
	deleted:    controls/cf_agent.cf
	deleted:    controls/cf_execd.cf
	deleted:    controls/cf_hub.cf
	deleted:    controls/cf_monitord.cf
	deleted:    controls/cf_runagent.cf
	deleted:    controls/cf_serverd.cf
	deleted:    controls/def.cf
	deleted:    controls/def_inputs.cf
	deleted:    controls/reports.cf
	deleted:    controls/update_def.cf
	deleted:    controls/update_def_inputs.cf
	deleted:    custom-2.cf
	deleted:    def.json
	deleted:    inventory/aix.cf
	deleted:    inventory/any.cf
	deleted:    inventory/debian.cf
	deleted:    inventory/freebsd.cf
	deleted:    inventory/generic.cf
	deleted:    inventory/linux.cf
	deleted:    inventory/lsb.cf
	deleted:    inventory/macos.cf
	deleted:    inventory/os.cf
	deleted:    inventory/redhat.cf
	deleted:    inventory/suse.cf
	deleted:    inventory/windows.cf
	deleted:    lib/autorun.cf
	deleted:    lib/bundles.cf
	deleted:    lib/cfe_internal.cf
	deleted:    lib/cfe_internal_hub.cf
	deleted:    lib/cfengine_enterprise_hub_ha.cf
	deleted:    lib/commands.cf
	deleted:    lib/common.cf
	deleted:    lib/databases.cf
	deleted:    lib/deprecated-upstream.cf
	deleted:    lib/edit_xml.cf
	deleted:    lib/event.cf
	deleted:    lib/examples.cf
	deleted:    lib/feature.cf
	deleted:    lib/files.cf
	deleted:    lib/guest_environments.cf
	deleted:    lib/monitor.cf
	deleted:    lib/packages-ENT-3719.cf
	deleted:    lib/packages.cf
	deleted:    lib/paths.cf
	deleted:    lib/processes.cf
	deleted:    lib/reports.cf
	deleted:    lib/services.cf
	deleted:    lib/stdlib.cf
	deleted:    lib/storage.cf
	deleted:    lib/testing.cf
	deleted:    lib/users.cf
	deleted:    lib/vcs.cf
	deleted:    modules/packages/vendored/WiRunSQL.vbs.mustache
	deleted:    modules/packages/vendored/apk.mustache
	deleted:    modules/packages/vendored/apt_get.mustache
	deleted:    modules/packages/vendored/freebsd_ports.mustache
	deleted:    modules/packages/vendored/msiexec-list.vbs.mustache
	deleted:    modules/packages/vendored/msiexec.bat.mustache
	deleted:    modules/packages/vendored/nimclient.mustache
	deleted:    modules/packages/vendored/pkg.mustache
	deleted:    modules/packages/vendored/pkgsrc.mustache
	deleted:    modules/packages/vendored/slackpkg.mustache
	deleted:    modules/packages/vendored/snap.mustache
	deleted:    modules/packages/vendored/yum.mustache
	deleted:    modules/packages/vendored/zypper.mustache
	deleted:    promises.cf
	deleted:    services/autorun/custom-1.cf
	deleted:    services/autorun/hello.cf
	deleted:    services/custom-3.cf
	deleted:    services/init.cf
	deleted:    services/main.cf
	deleted:    standalone_self_upgrade.cf
	deleted:    templates/cf-apache.service.mustache
	deleted:    templates/cf-execd.service.mustache
	deleted:    templates/cf-hub.service.mustache
	deleted:    templates/cf-monitord.service.mustache
	deleted:    templates/cf-postgres.service.mustache
	deleted:    templates/cf-runalerts.service.mustache
	deleted:    templates/cf-serverd.service.mustache
	deleted:    templates/cfengine3.service.mustache
	deleted:    templates/cfengine_watchdog.mustache
	deleted:    templates/federated_reporting/10-base_filter.sed
	deleted:    templates/federated_reporting/50-merge_inserts.awk
	deleted:    templates/federated_reporting/config.sh.mustache
	deleted:    templates/federated_reporting/dump.sh
	deleted:    templates/federated_reporting/import.sh
	deleted:    templates/federated_reporting/import_file.sh
	deleted:    templates/federated_reporting/log.sh.mustache
	deleted:    templates/federated_reporting/parallel.sh
	deleted:    templates/federated_reporting/psql_wrapper.sh.mustache
	deleted:    templates/federated_reporting/pull_dumps_from.sh
	deleted:    templates/federated_reporting/transport.sh
	deleted:    templates/host_info_report.mustache
	deleted:    templates/json_multiline.mustache
	deleted:    templates/json_serial.mustache
	deleted:    templates/vercmp.ps1
	deleted:    update.cf

no changes added to commit (use "git add" and/or "git commit -a")
```

## Install the new version of the MPF

### Installing from Git

First, clone the desired version of the MPF source.

```bash
export MPF_VERSION="3.21.2"
git clone -b $MPF_VERSION https://github.com/cfengine/masterfiles $INTEGRATION_ROOT/masterfiles-source-$MPF_VERSION
```

```output
Cloning into '/tmp/MPF-upgrade/integration/masterfiles-source-3.21.2'...
Note: switching to 'f495603285f9bd90d5d36df4fec4870aeee751e8'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false
```

Then build and install targeting the integration root directory. When installed from source masterfiles installs into the `masterfiles` directory.

```bash
cd $INTEGRATION_ROOT/masterfiles-source-$MPF_VERSION
export EXPLICIT_VERSION=$MPF_VERSION

./autogen.sh
make
make install prefix=$INTEGRATION_ROOT/
```

```output
./autogen.sh: Running determine-version.sh ...
./autogen.sh: Running determine-release.sh ...
All tags pointing to current commit:
3.21.2
3.21.2-build4
Latest version: 3.21.2
Could not parse it, using default release number 1
./autogen.sh: Running autoreconf ...
configure.ac:40: installing './config.guess'
configure.ac:40: installing './config.sub'
configure.ac:43: installing './install-sh'
configure.ac:43: installing './missing'
parallel-tests: installing './test-driver'
/tmp/MPF-upgrade/integration/masterfiles-source-3.21.2
checking build system type... x86_64-pc-linux-gnu
checking host system type... x86_64-pc-linux-gnu
checking target system type... x86_64-pc-linux-gnu
checking for a BSD-compatible install... /usr/bin/install -c
checking whether build environment is sane... yes
checking for a race-free mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking whether UID '1000' is supported by ustar format... yes
checking whether GID '1000' is supported by ustar format... yes
checking how to create a ustar tar archive... gnutar
checking if GNU tar supports --hard-dereference... yes
checking whether to enable maintainer-specific portions of Makefiles... yes
checking whether make supports nested variables... (cached) yes
checking for pkg_install... no
checking for shunit2... no

Summary:
Version              -> 3.21.2
Release              -> 1
Core directory       -> not set - tests are disabled
Enterprise directory -> not set - some tests are disabled
Install prefix       -> /var/cfengine
bindir               -> /var/cfengine/bin

configure: generating makefile targets
checking that generated files are newer than configure... done
configure: creating ./config.status
config.status: creating Makefile
config.status: creating controls/update_def.cf
config.status: creating promises.cf
config.status: creating standalone_self_upgrade.cf
config.status: creating tests/Makefile
config.status: creating tests/acceptance/Makefile
config.status: creating tests/unit/Makefile

DONE: Configuration done. Run "make install" to install CFEngine Masterfiles.

Making all in tests/
make[1]: Entering directory '/tmp/MPF-upgrade/integration/masterfiles-source-3.21.2/tests'
Making all in .
make[2]: Entering directory '/tmp/MPF-upgrade/integration/masterfiles-source-3.21.2/tests'
make[2]: Nothing to be done for 'all-am'.
make[2]: Leaving directory '/tmp/MPF-upgrade/integration/masterfiles-source-3.21.2/tests'
Making all in unit
make[2]: Entering directory '/tmp/MPF-upgrade/integration/masterfiles-source-3.21.2/tests/unit'
make[2]: Nothing to be done for 'all'.
make[2]: Leaving directory '/tmp/MPF-upgrade/integration/masterfiles-source-3.21.2/tests/unit'
make[1]: Leaving directory '/tmp/MPF-upgrade/integration/masterfiles-source-3.21.2/tests'
make[1]: Entering directory '/tmp/MPF-upgrade/integration/masterfiles-source-3.21.2'
make[1]: Nothing to be done for 'all-am'.
make[1]: Leaving directory '/tmp/MPF-upgrade/integration/masterfiles-source-3.21.2'
Making install in tests/
make[1]: Entering directory '/tmp/MPF-upgrade/integration/masterfiles-source-3.21.2/tests'
Making install in .
make[2]: Entering directory '/tmp/MPF-upgrade/integration/masterfiles-source-3.21.2/tests'
make[3]: Entering directory '/tmp/MPF-upgrade/integration/masterfiles-source-3.21.2/tests'
make[3]: Nothing to be done for 'install-exec-am'.
make[3]: Nothing to be done for 'install-data-am'.
make[3]: Leaving directory '/tmp/MPF-upgrade/integration/masterfiles-source-3.21.2/tests'
make[2]: Leaving directory '/tmp/MPF-upgrade/integration/masterfiles-source-3.21.2/tests'
Making install in unit
make[2]: Entering directory '/tmp/MPF-upgrade/integration/masterfiles-source-3.21.2/tests/unit'
make[3]: Entering directory '/tmp/MPF-upgrade/integration/masterfiles-source-3.21.2/tests/unit'
make[3]: Nothing to be done for 'install-exec-am'.
make[3]: Nothing to be done for 'install-data-am'.
make[3]: Leaving directory '/tmp/MPF-upgrade/integration/masterfiles-source-3.21.2/tests/unit'
make[2]: Leaving directory '/tmp/MPF-upgrade/integration/masterfiles-source-3.21.2/tests/unit'
make[1]: Leaving directory '/tmp/MPF-upgrade/integration/masterfiles-source-3.21.2/tests'
make[1]: Entering directory '/tmp/MPF-upgrade/integration/masterfiles-source-3.21.2'
make[2]: Entering directory '/tmp/MPF-upgrade/integration/masterfiles-source-3.21.2'
make[2]: Nothing to be done for 'install-exec-am'.
 /usr/bin/mkdir -p '/tmp/MPF-upgrade/integration//masterfiles'
 /usr/bin/mkdir -p '/tmp/MPF-upgrade/integration//masterfiles/cfe_internal/core'
 /usr/bin/install -c -m 644  ./cfe_internal/core/host_info_report.cf ./cfe_internal/core/log_rotation.cf ./cfe_internal/core/main.cf ./cfe_internal/core/limit_robot_agents.cf '/tmp/MPF-upgrade/integration//masterfiles/cfe_internal/core'
 /usr/bin/mkdir -p '/tmp/MPF-upgrade/integration//masterfiles/cfe_internal/enterprise/templates'
 /usr/bin/install -c -m 644  ./cfe_internal/enterprise/templates/runalerts.sh.mustache ./cfe_internal/enterprise/templates/httpd.conf.mustache ./cfe_internal/enterprise/templates/apachectl.mustache ./cfe_internal/enterprise/templates/runalerts.php.mustache '/tmp/MPF-upgrade/integration//masterfiles/cfe_internal/enterprise/templates'
 /usr/bin/mkdir -p '/tmp/MPF-upgrade/integration//masterfiles/inventory'
 /usr/bin/install -c -m 644  ./inventory/windows.cf ./inventory/suse.cf ./inventory/macos.cf ./inventory/lsb.cf ./inventory/any.cf ./inventory/os.cf ./inventory/freebsd.cf ./inventory/generic.cf ./inventory/debian.cf ./inventory/linux.cf ./inventory/redhat.cf ./inventory/aix.cf '/tmp/MPF-upgrade/integration//masterfiles/inventory'
 /usr/bin/mkdir -p '/tmp/MPF-upgrade/integration//masterfiles/cfe_internal/enterprise/federation'
 /usr/bin/install -c -m 644  ./cfe_internal/enterprise/federation/federation.cf '/tmp/MPF-upgrade/integration//masterfiles/cfe_internal/enterprise/federation'
 /usr/bin/mkdir -p '/tmp/MPF-upgrade/integration//masterfiles/cfe_internal/core/deprecated'
 /usr/bin/install -c -m 644  ./cfe_internal/core/deprecated/cfengine_processes.cf '/tmp/MPF-upgrade/integration//masterfiles/cfe_internal/core/deprecated'
 /usr/bin/mkdir -p '/tmp/MPF-upgrade/integration//masterfiles/lib/templates'
 /usr/bin/install -c -m 644  ./lib/templates/tap.mustache ./lib/templates/junit.mustache '/tmp/MPF-upgrade/integration//masterfiles/lib/templates'
 /usr/bin/mkdir -p '/tmp/MPF-upgrade/integration//masterfiles/services/autorun'
 /usr/bin/install -c -m 644  ./services/autorun/hello.cf '/tmp/MPF-upgrade/integration//masterfiles/services/autorun'
 /usr/bin/mkdir -p '/tmp/MPF-upgrade/integration//masterfiles/lib'
 /usr/bin/install -c -m 644  ./lib/testing.cf ./lib/examples.cf ./lib/packages.cf ./lib/common.cf ./lib/users.cf ./lib/guest_environments.cf ./lib/cfengine_enterprise_hub_ha.cf ./lib/edit_xml.cf ./lib/files.cf ./lib/bundles.cf ./lib/reports.cf ./lib/event.cf ./lib/storage.cf ./lib/paths.cf ./lib/vcs.cf ./lib/stdlib.cf ./lib/autorun.cf ./lib/databases.cf ./lib/feature.cf ./lib/cfe_internal_hub.cf ./lib/monitor.cf ./lib/services.cf ./lib/packages-ENT-3719.cf ./lib/commands.cf ./lib/processes.cf ./lib/cfe_internal.cf '/tmp/MPF-upgrade/integration//masterfiles/lib'
 /usr/bin/mkdir -p '/tmp/MPF-upgrade/integration//masterfiles/cfe_internal/update'
 /usr/bin/install -c -m 644  ./cfe_internal/update/cfe_internal_dc_workflow.cf ./cfe_internal/update/lib.cf ./cfe_internal/update/update_processes.cf ./cfe_internal/update/windows_unattended_upgrade.cf ./cfe_internal/update/systemd_units.cf ./cfe_internal/update/update_policy.cf ./cfe_internal/update/update_bins.cf ./cfe_internal/update/cfe_internal_update_from_repository.cf '/tmp/MPF-upgrade/integration//masterfiles/cfe_internal/update'
 /usr/bin/mkdir -p '/tmp/MPF-upgrade/integration//masterfiles/controls'
 /usr/bin/install -c -m 644  ./controls/cf_agent.cf ./controls/cf_runagent.cf ./controls/cf_execd.cf ./controls/def_inputs.cf ./controls/cf_monitord.cf ./controls/def.cf ./controls/reports.cf ./controls/update_def_inputs.cf ./controls/cf_serverd.cf ./controls/cf_hub.cf ./controls/update_def.cf '/tmp/MPF-upgrade/integration//masterfiles/controls'
 /usr/bin/mkdir -p '/tmp/MPF-upgrade/integration//masterfiles/cfe_internal/enterprise/ha'
 /usr/bin/install -c -m 644  ./cfe_internal/enterprise/ha/ha_def.cf ./cfe_internal/enterprise/ha/ha.cf ./cfe_internal/enterprise/ha/ha_update.cf '/tmp/MPF-upgrade/integration//masterfiles/cfe_internal/enterprise/ha'
 /usr/bin/mkdir -p '/tmp/MPF-upgrade/integration//masterfiles/modules/packages/vendored'
 /usr/bin/install -c -m 644  ./modules/packages/vendored/apk.mustache ./modules/packages/vendored/msiexec.bat.mustache ./modules/packages/vendored/nimclient.mustache ./modules/packages/vendored/snap.mustache ./modules/packages/vendored/yum.mustache ./modules/packages/vendored/msiexec-list.vbs.mustache ./modules/packages/vendored/apt_get.mustache ./modules/packages/vendored/slackpkg.mustache ./modules/packages/vendored/pkgsrc.mustache ./modules/packages/vendored/pkg.mustache ./modules/packages/vendored/freebsd_ports.mustache ./modules/packages/vendored/zypper.mustache ./modules/packages/vendored/WiRunSQL.vbs.mustache '/tmp/MPF-upgrade/integration//masterfiles/modules/packages/vendored'
 /usr/bin/mkdir -p '/tmp/MPF-upgrade/integration//masterfiles/cfe_internal'
 /usr/bin/install -c -m 644  ./cfe_internal/recommendations.cf ./cfe_internal/CFE_cfengine.cf '/tmp/MPF-upgrade/integration//masterfiles/cfe_internal'
 /usr/bin/install -c -m 644  ./update.cf ./promises.cf ./standalone_self_upgrade.cf '/tmp/MPF-upgrade/integration//masterfiles/.'
 /usr/bin/mkdir -p '/tmp/MPF-upgrade/integration//masterfiles/cfe_internal/core/watchdog'
 /usr/bin/install -c -m 644  ./cfe_internal/core/watchdog/watchdog.cf '/tmp/MPF-upgrade/integration//masterfiles/cfe_internal/core/watchdog'
 /usr/bin/mkdir -p '/tmp/MPF-upgrade/integration//masterfiles/cfe_internal/core/watchdog/templates'
 /usr/bin/install -c -m 644  ./cfe_internal/core/watchdog/templates/watchdog-windows.ps1.mustache ./cfe_internal/core/watchdog/templates/watchdog.mustache '/tmp/MPF-upgrade/integration//masterfiles/cfe_internal/core/watchdog/templates'
 /usr/bin/mkdir -p '/tmp/MPF-upgrade/integration//masterfiles/templates'
 /usr/bin/install -c -m 644  ./templates/cf-execd.service.mustache ./templates/cf-apache.service.mustache ./templates/host_info_report.mustache ./templates/cf-monitord.service.mustache ./templates/json_serial.mustache ./templates/json_multiline.mustache ./templates/cf-hub.service.mustache ./templates/cfengine3.service.mustache ./templates/cf-postgres.service.mustache ./templates/cfengine_watchdog.mustache ./templates/vercmp.ps1 ./templates/cf-runalerts.service.mustache ./templates/cf-serverd.service.mustache ./templates/cf-reactor.service.mustache '/tmp/MPF-upgrade/integration//masterfiles/templates'
 /usr/bin/mkdir -p '/tmp/MPF-upgrade/integration//masterfiles/cfe_internal/enterprise'
 /usr/bin/install -c -m 644  ./cfe_internal/enterprise/CFE_knowledge.cf ./cfe_internal/enterprise/file_change.cf ./cfe_internal/enterprise/CFE_hub_specific.cf ./cfe_internal/enterprise/mission_portal.cf ./cfe_internal/enterprise/main.cf '/tmp/MPF-upgrade/integration//masterfiles/cfe_internal/enterprise'
 /usr/bin/mkdir -p '/tmp/MPF-upgrade/integration//masterfiles/templates/federated_reporting'
 /usr/bin/install -c -m 644  ./templates/federated_reporting/cfsecret.py ./templates/federated_reporting/import_file.sh ./templates/federated_reporting/psql_wrapper.sh.mustache ./templates/federated_reporting/import.sh ./templates/federated_reporting/transfer_distributed_cleanup_items.sh ./templates/federated_reporting/config.sh.mustache ./templates/federated_reporting/distributed_cleanup.py ./templates/federated_reporting/transport.sh ./templates/federated_reporting/log.sh.mustache ./templates/federated_reporting/dump.sh ./templates/federated_reporting/10-base_filter.sed ./templates/federated_reporting/nova_api.py ./templates/federated_reporting/pull_dumps_from.sh ./templates/federated_reporting/50-merge_inserts.awk ./templates/federated_reporting/parallel.sh '/tmp/MPF-upgrade/integration//masterfiles/templates/federated_reporting'
 /usr/bin/mkdir -p '/tmp/MPF-upgrade/integration//masterfiles/services'
 /usr/bin/install -c -m 644  ./services/init.cf ./services/main.cf '/tmp/MPF-upgrade/integration//masterfiles/services'
make[2]: Leaving directory '/tmp/MPF-upgrade/integration/masterfiles-source-3.21.2'
make[1]: Leaving directory '/tmp/MPF-upgrade/integration/masterfiles-source-3.21.2'
```

We no longer need the source, we can clean it up.

```bash
cd $INTEGRATION_ROOT/
rm -rf $INTEGRATION_ROOT/masterfiles-source-$MPF_VERSION
```

## Merge differences

Now we can use `git status` to see an overview of the changes to the repository between our starting point and the new MPF.

```bash
cd $INTEGRATION_ROOT/masterfiles
git status
```

```output
On branch master
Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   cfe_internal/core/watchdog/templates/watchdog.mustache
	modified:   cfe_internal/enterprise/CFE_hub_specific.cf
	modified:   cfe_internal/enterprise/CFE_knowledge.cf
	modified:   cfe_internal/enterprise/federation/federation.cf
	modified:   cfe_internal/enterprise/file_change.cf
	modified:   cfe_internal/enterprise/main.cf
	modified:   cfe_internal/enterprise/mission_portal.cf
	modified:   cfe_internal/enterprise/templates/httpd.conf.mustache
	modified:   cfe_internal/update/cfe_internal_dc_workflow.cf
	modified:   cfe_internal/update/cfe_internal_update_from_repository.cf
	modified:   cfe_internal/update/lib.cf
	modified:   cfe_internal/update/update_bins.cf
	modified:   cfe_internal/update/update_policy.cf
	modified:   cfe_internal/update/update_processes.cf
	modified:   cfe_internal/update/windows_unattended_upgrade.cf
	modified:   controls/cf_agent.cf
	modified:   controls/cf_execd.cf
	modified:   controls/cf_serverd.cf
	modified:   controls/def.cf
	modified:   controls/reports.cf
	modified:   controls/update_def.cf
	deleted:    custom-2.cf
	deleted:    def.json
	modified:   inventory/any.cf
	modified:   inventory/debian.cf
	modified:   inventory/linux.cf
	modified:   inventory/os.cf
	modified:   inventory/redhat.cf
	modified:   lib/autorun.cf
	modified:   lib/bundles.cf
	modified:   lib/cfe_internal_hub.cf
	deleted:    lib/deprecated-upstream.cf
	modified:   lib/files.cf
	modified:   lib/packages.cf
	modified:   lib/paths.cf
	modified:   lib/services.cf
	modified:   modules/packages/vendored/apt_get.mustache
	modified:   modules/packages/vendored/msiexec-list.vbs.mustache
	modified:   modules/packages/vendored/nimclient.mustache
	modified:   modules/packages/vendored/pkg.mustache
	modified:   modules/packages/vendored/zypper.mustache
	modified:   promises.cf
	deleted:    services/autorun/custom-1.cf
	deleted:    services/custom-3.cf
	modified:   services/main.cf
	modified:   standalone_self_upgrade.cf
	modified:   templates/cf-apache.service.mustache
	modified:   templates/cf-execd.service.mustache
	modified:   templates/cf-hub.service.mustache
	modified:   templates/cf-monitord.service.mustache
	modified:   templates/cf-postgres.service.mustache
	modified:   templates/cf-runalerts.service.mustache
	modified:   templates/cf-serverd.service.mustache
	modified:   templates/federated_reporting/config.sh.mustache
	modified:   templates/federated_reporting/dump.sh
	modified:   templates/federated_reporting/import.sh
	modified:   templates/federated_reporting/psql_wrapper.sh.mustache
	modified:   templates/federated_reporting/pull_dumps_from.sh
	modified:   update.cf

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	cfe_internal/enterprise/templates/apachectl.mustache
	lib/templates/
	templates/cf-reactor.service.mustache
	templates/federated_reporting/cfsecret.py
	templates/federated_reporting/distributed_cleanup.py
	templates/federated_reporting/nova_api.py
	templates/federated_reporting/transfer_distributed_cleanup_items.sh

no changes added to commit (use "git add" and/or "git commit -a")
```

All of the **Untracked files** are new additions from upstream so they should be safe to take.

```bash
git add cfe_internal/enterprise/templates/apachectl.mustache
git add lib/templates/junit.mustache
git add lib/templates/tap.mustache
git add templates/cf-reactor.service.mustache
git add templates/federated_reporting/cfsecret.py
git add templates/federated_reporting/distributed_cleanup.py
git add templates/federated_reporting/nova_api.py
git add templates/federated_reporting/transfer_distributed_cleanup_items.sh
```

We can run git status again to see the current overview:

```command
git status
```

```output
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	new file:   cfe_internal/enterprise/templates/apachectl.mustache
	new file:   lib/templates/junit.mustache
	new file:   lib/templates/tap.mustache
	new file:   templates/cf-reactor.service.mustache
	new file:   templates/federated_reporting/cfsecret.py
	new file:   templates/federated_reporting/distributed_cleanup.py
	new file:   templates/federated_reporting/nova_api.py
	new file:   templates/federated_reporting/transfer_distributed_cleanup_items.sh

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   cfe_internal/core/watchdog/templates/watchdog.mustache
	modified:   cfe_internal/enterprise/CFE_hub_specific.cf
	modified:   cfe_internal/enterprise/CFE_knowledge.cf
	modified:   cfe_internal/enterprise/federation/federation.cf
	modified:   cfe_internal/enterprise/file_change.cf
	modified:   cfe_internal/enterprise/main.cf
	modified:   cfe_internal/enterprise/mission_portal.cf
	modified:   cfe_internal/enterprise/templates/httpd.conf.mustache
	modified:   cfe_internal/update/cfe_internal_dc_workflow.cf
	modified:   cfe_internal/update/cfe_internal_update_from_repository.cf
	modified:   cfe_internal/update/lib.cf
	modified:   cfe_internal/update/update_bins.cf
	modified:   cfe_internal/update/update_policy.cf
	modified:   cfe_internal/update/update_processes.cf
	modified:   cfe_internal/update/windows_unattended_upgrade.cf
	modified:   controls/cf_agent.cf
	modified:   controls/cf_execd.cf
	modified:   controls/cf_serverd.cf
	modified:   controls/def.cf
	modified:   controls/reports.cf
	modified:   controls/update_def.cf
	deleted:    custom-2.cf
	deleted:    def.json
	modified:   inventory/any.cf
	modified:   inventory/debian.cf
	modified:   inventory/linux.cf
	modified:   inventory/os.cf
	modified:   inventory/redhat.cf
	modified:   lib/autorun.cf
	modified:   lib/bundles.cf
	modified:   lib/cfe_internal_hub.cf
	deleted:    lib/deprecated-upstream.cf
	modified:   lib/files.cf
	modified:   lib/packages.cf
	modified:   lib/paths.cf
	modified:   lib/services.cf
	modified:   modules/packages/vendored/apt_get.mustache
	modified:   modules/packages/vendored/msiexec-list.vbs.mustache
	modified:   modules/packages/vendored/nimclient.mustache
	modified:   modules/packages/vendored/pkg.mustache
	modified:   modules/packages/vendored/zypper.mustache
	modified:   promises.cf
	deleted:    services/autorun/custom-1.cf
	deleted:    services/custom-3.cf
	modified:   services/main.cf
	modified:   standalone_self_upgrade.cf
	modified:   templates/cf-apache.service.mustache
	modified:   templates/cf-execd.service.mustache
	modified:   templates/cf-hub.service.mustache
	modified:   templates/cf-monitord.service.mustache
	modified:   templates/cf-postgres.service.mustache
	modified:   templates/cf-runalerts.service.mustache
	modified:   templates/cf-serverd.service.mustache
	modified:   templates/federated_reporting/config.sh.mustache
	modified:   templates/federated_reporting/dump.sh
	modified:   templates/federated_reporting/import.sh
	modified:   templates/federated_reporting/psql_wrapper.sh.mustache
	modified:   templates/federated_reporting/pull_dumps_from.sh
	modified:   update.cf
```

Next we want to bring back any of our custom files. Look through the **deleted** files, identify your custom files and restore them with `git checkout`.

```command
git ls-files --deleted
```

```output
custom-2.cf
def.json
lib/deprecated-upstream.cf
services/autorun/custom-1.cf
services/custom-3.cf
```

Keeping your polices organized together helps to make this process easy. The custom policy files in the example policy set are `def.json`, `services/autorun/custom-1.cf`, `custom-2.cf`, and `services/custom-3.cf`.

```bash
git checkout custom-2.cf
git checkout def.json
git checkout services/autorun/custom-1.cf
git checkout services/custom-3.cf
```

```output
Updated 1 path from the index
Updated 1 path from the index
Updated 1 path from the index
Updated 1 path from the index
```

Other deleted files from the upstream framework like `lib/deprecated-upstream.cf` should be deleted with `git rm`.

**Note:** It is uncommon for any files to be moved or deleted between patch releases (e.g. `3.18.0` -> `3.18.5`) like `lib/deprecated-upstream.cf` in this example.

```command
git rm lib/deprecated-upstream.cf
```

```output
rm 'lib/deprecated-upstream.cf'
```

The files marked as **modified** in the `git status` output are files that have changed upstream.

```command
git status
```

```output
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	new file:   cfe_internal/enterprise/templates/apachectl.mustache
	deleted:    lib/deprecated-upstream.cf
	new file:   lib/templates/junit.mustache
	new file:   lib/templates/tap.mustache
	new file:   templates/cf-reactor.service.mustache
	new file:   templates/federated_reporting/cfsecret.py
	new file:   templates/federated_reporting/distributed_cleanup.py
	new file:   templates/federated_reporting/nova_api.py
	new file:   templates/federated_reporting/transfer_distributed_cleanup_items.sh

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   cfe_internal/core/watchdog/templates/watchdog.mustache
	modified:   cfe_internal/enterprise/CFE_hub_specific.cf
	modified:   cfe_internal/enterprise/CFE_knowledge.cf
	modified:   cfe_internal/enterprise/federation/federation.cf
	modified:   cfe_internal/enterprise/file_change.cf
	modified:   cfe_internal/enterprise/main.cf
	modified:   cfe_internal/enterprise/mission_portal.cf
	modified:   cfe_internal/enterprise/templates/httpd.conf.mustache
	modified:   cfe_internal/update/cfe_internal_dc_workflow.cf
	modified:   cfe_internal/update/cfe_internal_update_from_repository.cf
	modified:   cfe_internal/update/lib.cf
	modified:   cfe_internal/update/update_bins.cf
	modified:   cfe_internal/update/update_policy.cf
	modified:   cfe_internal/update/update_processes.cf
	modified:   cfe_internal/update/windows_unattended_upgrade.cf
	modified:   controls/cf_agent.cf
	modified:   controls/cf_execd.cf
	modified:   controls/cf_serverd.cf
	modified:   controls/def.cf
	modified:   controls/reports.cf
	modified:   controls/update_def.cf
	modified:   inventory/any.cf
	modified:   inventory/debian.cf
	modified:   inventory/linux.cf
	modified:   inventory/os.cf
	modified:   inventory/redhat.cf
	modified:   lib/autorun.cf
	modified:   lib/bundles.cf
	modified:   lib/cfe_internal_hub.cf
	modified:   lib/files.cf
	modified:   lib/packages.cf
	modified:   lib/paths.cf
	modified:   lib/services.cf
	modified:   modules/packages/vendored/apt_get.mustache
	modified:   modules/packages/vendored/msiexec-list.vbs.mustache
	modified:   modules/packages/vendored/nimclient.mustache
	modified:   modules/packages/vendored/pkg.mustache
	modified:   modules/packages/vendored/zypper.mustache
	modified:   promises.cf
	modified:   services/main.cf
	modified:   standalone_self_upgrade.cf
	modified:   templates/cf-apache.service.mustache
	modified:   templates/cf-execd.service.mustache
	modified:   templates/cf-hub.service.mustache
	modified:   templates/cf-monitord.service.mustache
	modified:   templates/cf-postgres.service.mustache
	modified:   templates/cf-runalerts.service.mustache
	modified:   templates/cf-serverd.service.mustache
	modified:   templates/federated_reporting/config.sh.mustache
	modified:   templates/federated_reporting/dump.sh
	modified:   templates/federated_reporting/import.sh
	modified:   templates/federated_reporting/psql_wrapper.sh.mustache
	modified:   templates/federated_reporting/pull_dumps_from.sh
	modified:   update.cf
```

It's best to review the diff of **each** modified file to understand the upstream changes as well as identify any local modifications that need to be retained. You should always keep a good record of any modifications made to vendored files to ensure that nothing is lost during future framework upgrades.

For example, here the diff for `promises.cf` shows upstream changes but also highlights where the vendored policy had been customized to integrate a custom policy.

```command
git diff promises.cf
```

Output:

```diff
diff --git a/promises.cf b/promises.cf
index 15c0c40..4611098 100644
--- a/promises.cf
+++ b/promises.cf
@@ -5,7 +5,7 @@
 # MIT Public License
 # http://www.opensource.org/licenses/MIT

-# Copyright 2021 Northern.tech AS
+# Copyright 2022 Northern.tech AS

 # Permission is hereby granted, free of charge, to any person obtaining a copy of
 # this software and associated documentation files (the "Software"), to deal in
@@ -56,10 +56,9 @@ body common control

                          # Agent bundle
                           cfe_internal_management,   # See cfe_internal/CFE_cfengine.cf
-                          main,
+                          mpf_main,
                           @(cfengine_enterprise_hub_ha.management_bundles),
                           @(def.bundlesequence_end),
-custom_2,

       };

@@ -86,35 +85,24 @@ custom_2,
                   @(services_autorun.inputs),

                   "services/main.cf",
-"custom-2.cf",
       };

-      version => "CFEngine Promises.cf 3.18.0";
+      version => "CFEngine Promises.cf 3.21.2";

       # From 3.7 onwards there is a new package promise implementation using package
       # modules in which you MUST provide package modules used to generate
       # software inventory reports. You can also provide global default package module
       # instead of specifying it in all package promises.
-    (debian).!disable_inventory_package_refresh::
+    (debian|redhat|centos|suse|sles|opensuse|amazon_linux).cfe_python_for_package_modules_supported.!disable_inventory_package_refresh::
           package_inventory => { $(package_module_knowledge.platform_default) };

-      # We only define pacakge_invetory on redhat like systems that have a
-      # python version that works with the package module.
-    (redhat|centos|suse|sles|opensuse|amazon_linux).cfe_yum_package_module_supported.!disable_inventory_package_refresh::
-        package_inventory => { $(package_module_knowledge.platform_default) };
-
     (debian|redhat|suse|sles|opensuse|amazon_linux)::
           package_module => $(package_module_knowledge.platform_default);

-      # CFEngine 3.12.2+ and 3.14+ have new package module on Windows
-    windows.cfengine_3_12.!(cfengine_3_12_0|cfengine_3_12_1)::
-          package_inventory => { $(package_module_knowledge.platform_default) };
-          package_module => $(package_module_knowledge.platform_default);
-@if minimum_version(3.14)
     windows::
           package_inventory => { $(package_module_knowledge.platform_default) };
           package_module => $(package_module_knowledge.platform_default);
-@endif
+
     termux::
           package_module => $(package_module_knowledge.platform_default);

@@ -127,6 +115,12 @@ custom_2,
         ignore_missing_inputs => "$(def.control_common_ignore_missing_inputs)";

+    control_common_tls_min_version_defined::
+        tls_min_version => "$(default:def.control_common_tls_min_version)"; # See also: allowtlsversion in body server control
+
+    control_common_tls_ciphers_defined::
+        tls_ciphers => "$(default:def.control_common_tls_ciphers)"; # See also: allowciphers in body server control
+
 }

 bundle common inventory
@@ -136,8 +130,6 @@ bundle common inventory
 #
 # Inventory bundles are simply common bundles loaded before anything
 # else in promises.cf
-#
-# Tested to work properly against 3.5.x
 {
   classes:
       "other_unix_os" expression => "!(windows|macos|linux|freebsd|aix)";
@@ -341,9 +333,7 @@ bundle common services_autorun
 # added to inputs automatically.
 {
   vars:
-    services_autorun::
-      "inputs" slist => { "$(sys.local_libdir)/autorun.cf" };
-
+    services_autorun|services_autorun_inputs::
       "_default_autorun_input_dir"
         string => "$(this.promise_dirname)/services/autorun";
       "_default_autorun_inputs"
@@ -360,23 +350,34 @@ bundle common services_autorun
       "found_inputs" slist => { @(_default_autorun_inputs),
                                 sort( getvalues(_extra_autorun_inputs), "lex") };

-      "bundles" slist => { "autorun" }; # run loaded bundles
-
-    !services_autorun::
+    !(services_autorun|services_autorun_inputs|services_autorun_bundles)::
       # If services_autorun is not enabled, then we should not extend inputs
       # automatically.
       "inputs" slist => { };
       "found_inputs" slist => {};
       "bundles" slist => { "services_autorun" }; # run self

+    services_autorun|services_autorun_inputs|services_autorun_bundles::
+      "inputs" slist => { "$(sys.local_libdir)/autorun.cf" };
+      "bundles" slist => { "autorun" }; # run loaded bundles
+
   reports:
     DEBUG|DEBUG_services_autorun::
       "DEBUG $(this.bundle): Services Autorun Disabled"
-        if => "!services_autorun";
+        if => "!(services_autorun|services_autorun_bundles|services_autorun_inputs)";

       "DEBUG $(this.bundle): Services Autorun Enabled"
         if => "services_autorun";

+      "DEBUG $(this.bundle): Services Autorun Bundles Enabled"
+        if => "services_autorun_bundles";
+
+      "DEBUG $(this.bundle): Services Autorun Inputs Enabled"
+        if => "services_autorun_inputs";
+
+      "DEBUG $(this.bundle): Services Autorun (Bundles & Inputs) Enabled"
+        if => "services_autorun_inputs.services_autorun_bundles";
+
       "DEBUG $(this.bundle): adding input='$(inputs)'"
         if => isvariable("inputs");
```

Carefully review the diffs and merge or re-integrate your custom changes on top of the upstream files. If you identify changes to the vendored files consider re-integrating those changes in a way that does not modify vendored files, here for example we have migrated the integration of the custom policy to Augments (`def.json`).

```command
git diff def.json
```

Output:

```diff
diff --git a/def.json b/def.json
index a7b98e6..60a0ce1 100644
--- a/def.json
+++ b/def.json
@@ -1,8 +1,11 @@
 {
-  "inputs": [ "services/custom-3.cf" ],
+  "inputs": [ "custom-2.cf", "services/custom-3.cf" ],
   "classes": {
     "default:services_autorun": {
       "class_expressions": [ "any::" ],
       "comment": "We want to use the autorun functionality because it is convenient."
-    }
+    },
+  "vars":{
+    "control_common_bundlesequence_end": [ "custom_2" ]
+  }
 }
\ No newline at end of file
```

So, we now want to accept all the changes to `promises.cf` and `def.json`.

```command
git add promises.cf def.json
```

If you are unsure if or how to integrate customizations without modifying vendored policy reach out to support for help. For any modified files that you have not customized simply stage them for commit with `git add`.

```bash
git add cfe_internal/core/watchdog/templates/watchdog.mustache
git add cfe_internal/enterprise/CFE_hub_specific.cf
git add cfe_internal/enterprise/CFE_knowledge.cf
git add cfe_internal/enterprise/federation/federation.cf
git add cfe_internal/enterprise/file_change.cf
git add cfe_internal/enterprise/main.cf
git add cfe_internal/enterprise/mission_portal.cf
git add cfe_internal/enterprise/templates/httpd.conf.mustache
git add cfe_internal/update/cfe_internal_dc_workflow.cf
git add cfe_internal/update/cfe_internal_update_from_repository.cf
git add cfe_internal/update/lib.cf
git add cfe_internal/update/update_bins.cf
git add cfe_internal/update/update_policy.cf
git add cfe_internal/update/update_processes.cf
git add cfe_internal/update/windows_unattended_upgrade.cf
git add controls/cf_agent.cf
git add controls/cf_execd.cf
git add controls/cf_serverd.cf
git add controls/def.cf
git add controls/reports.cf
git add controls/update_def.cf
git add def.json
git add inventory/any.cf
git add inventory/debian.cf
git add inventory/linux.cf
git add inventory/os.cf
git add inventory/redhat.cf
git add lib/autorun.cf
git add lib/bundles.cf
git add lib/cfe_internal_hub.cf
git add lib/files.cf
git add lib/packages.cf
git add lib/paths.cf
git add lib/services.cf
git add modules/packages/vendored/apt_get.mustache
git add modules/packages/vendored/msiexec-list.vbs.mustache
git add modules/packages/vendored/nimclient.mustache
git add modules/packages/vendored/pkg.mustache
git add modules/packages/vendored/zypper.mustache
git add promises.cf
git add services/main.cf
git add standalone_self_upgrade.cf
git add templates/cf-apache.service.mustache
git add templates/cf-execd.service.mustache
git add templates/cf-hub.service.mustache
git add templates/cf-monitord.service.mustache
git add templates/cf-postgres.service.mustache
git add templates/cf-runalerts.service.mustache
git add templates/cf-serverd.service.mustache
git add templates/federated_reporting/config.sh.mustache
git add templates/federated_reporting/dump.sh
git add templates/federated_reporting/import.sh
git add templates/federated_reporting/psql_wrapper.sh.mustache
git add templates/federated_reporting/pull_dumps_from.sh
git add update.cf
```

Review `git status` one more time to make sure the changes are as expected.

```command
git status
```

```output
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   cfe_internal/core/watchdog/templates/watchdog.mustache
	modified:   cfe_internal/enterprise/CFE_hub_specific.cf
	modified:   cfe_internal/enterprise/CFE_knowledge.cf
	modified:   cfe_internal/enterprise/federation/federation.cf
	modified:   cfe_internal/enterprise/file_change.cf
	modified:   cfe_internal/enterprise/main.cf
	modified:   cfe_internal/enterprise/mission_portal.cf
	new file:   cfe_internal/enterprise/templates/apachectl.mustache
	modified:   cfe_internal/enterprise/templates/httpd.conf.mustache
	modified:   cfe_internal/update/cfe_internal_dc_workflow.cf
	modified:   cfe_internal/update/cfe_internal_update_from_repository.cf
	modified:   cfe_internal/update/lib.cf
	modified:   cfe_internal/update/update_bins.cf
	modified:   cfe_internal/update/update_policy.cf
	modified:   cfe_internal/update/update_processes.cf
	modified:   cfe_internal/update/windows_unattended_upgrade.cf
	modified:   controls/cf_agent.cf
	modified:   controls/cf_execd.cf
	modified:   controls/cf_serverd.cf
	modified:   controls/def.cf
	modified:   controls/reports.cf
	modified:   controls/update_def.cf
	modified:   def.json
	modified:   inventory/any.cf
	modified:   inventory/debian.cf
	modified:   inventory/linux.cf
	modified:   inventory/os.cf
	modified:   inventory/redhat.cf
	modified:   lib/autorun.cf
	modified:   lib/bundles.cf
	modified:   lib/cfe_internal_hub.cf
	deleted:    lib/deprecated-upstream.cf
	modified:   lib/files.cf
	modified:   lib/packages.cf
	modified:   lib/paths.cf
	modified:   lib/services.cf
	new file:   lib/templates/junit.mustache
	new file:   lib/templates/tap.mustache
	modified:   modules/packages/vendored/apt_get.mustache
	modified:   modules/packages/vendored/msiexec-list.vbs.mustache
	modified:   modules/packages/vendored/nimclient.mustache
	modified:   modules/packages/vendored/pkg.mustache
	modified:   modules/packages/vendored/zypper.mustache
	modified:   promises.cf
	modified:   services/main.cf
	modified:   standalone_self_upgrade.cf
	modified:   templates/cf-apache.service.mustache
	modified:   templates/cf-execd.service.mustache
	modified:   templates/cf-hub.service.mustache
	modified:   templates/cf-monitord.service.mustache
	modified:   templates/cf-postgres.service.mustache
	new file:   templates/cf-reactor.service.mustache
	modified:   templates/cf-runalerts.service.mustache
	modified:   templates/cf-serverd.service.mustache
	new file:   templates/federated_reporting/cfsecret.py
	modified:   templates/federated_reporting/config.sh.mustache
	new file:   templates/federated_reporting/distributed_cleanup.py
	modified:   templates/federated_reporting/dump.sh
	modified:   templates/federated_reporting/import.sh
	new file:   templates/federated_reporting/nova_api.py
	modified:   templates/federated_reporting/psql_wrapper.sh.mustache
	modified:   templates/federated_reporting/pull_dumps_from.sh
	new file:   templates/federated_reporting/transfer_distributed_cleanup_items.sh
	modified:   update.cf
```

Make sure the policy validates and commit your changes.

```command
git commit -m "Upgraded MPF from 3.18.0 to 3.21.2"
```

```output
[master a5d512c] Upgraded MPF from 3.18.0 to 3.21.2
 64 files changed, 2599 insertions(+), 728 deletions(-)
 create mode 100644 cfe_internal/enterprise/templates/apachectl.mustache
 rewrite inventory/redhat.cf (63%)
 delete mode 100644 lib/deprecated-upstream.cf
 create mode 100644 lib/templates/junit.mustache
 create mode 100644 lib/templates/tap.mustache
 create mode 100644 templates/cf-reactor.service.mustache
 create mode 100644 templates/federated_reporting/cfsecret.py
 create mode 100644 templates/federated_reporting/distributed_cleanup.py
 create mode 100644 templates/federated_reporting/nova_api.py
 create mode 100644 templates/federated_reporting/transfer_distributed_cleanup_items.sh
```

Now your Masterfiles Policy Framework is upgraded and ready to be tested.
