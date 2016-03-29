---
layout: default
title: The Policy Framework
published: true
sorting: 50
tags: [manuals, writing policy, policy framework, masterfiles, def.cf, update.cf]
---

The CFEngine policy framework is called the **masterfiles** because
the files live in `/var/cfengine/masterfiles` on the policy server (on
the clients, and note the policy server is typically also a client,
they are cached in `/var/cfengine/inputs`).

The following configuration files are part of the default CFEngine
installation in `/var/cfengine/masterfiles`, and have special roles.

## Setting up ##

First, review `update.cf` and `def.cf`.  Most settings you need to change will live here.

### update.cf

Synchronizing clients with the policy server happens here, in
`update.cf`. Its main job is to copy all the files on the policy
server (usually the hub) under `$(sys.masterdir)` (usually
`/var/cfengine/masterfiles`) to the local host into `$(sys.inputdir)`
(usually `/var/cfengine/inputs`).

This file should rarely if ever change. Should you ever change it (or
when you upgrade CFEngine), take special care to ensure the old and
the new CFEngine can parse and execute this file successfully. If not,
you risk losing control of your system (that is, **if CFEngine cannot
successfully execute `update.cf`, it has no mechanism for distributing
new policy files**).

By default, the policy defined in update.cf is executed from two sets of
promise bodies. The "usual" one (defined in the `bundlesequence` in
`promises.cf`) and another in the backup/failsafe `bundlesequence` (defined in
`failsafe.cf`).

This is a standalone policy file. You can actually run it with
`cf-agent -KI -f ./update.cf` but if you don't understand what that
command does, please hold off until you've gone through the CFEngine
documentation. The contents of `update.cf` duplicate other things
under `lib` sometimes, in order to be completely standalone.

To repeat, when `update.cf` is broken, things go bonkers. CFEngine
will try to run a backup `failsafe.cf` you can find in the C core
under `libpromises/failsafe.cf` (that `.cf` file is written into the C
code and can't be modified). If things get to that point, you probably
have to look at why corrupted policies made it into production.

As is typical for CFEngine, the policy and the configuration are
mixed. In `update.cf` you'll find some very useful settings. Keep
referring to
`update.cf` as you
read this.  We are skipping the nonessential ones.

#### How it works ####

There are 4 stages in `update.cf`. See the `bundlesequence`: after
loading the configuration from `update_def`, we take these steps in
order.

##### cfe_internal_dc_workflow

This step implements the auto-deployment of policies. See
[Version Control and Configuration Policy][Best Practices#Version Control and Configuration Policy]
and `cfengine_internal_masterfiles_update` below for details.

##### cfe_internal_update_policy

This step updates the policy files themselves. Basically it's a check
step that looks at `$(sys.inputdir)/cf_promises_validated` and
compares it with the policy server's
`$(sys.masterdir)/cf_promises_validated`. Then there's the actual
copy, which happens only if the `cf_promises_validated` file was
updated in the check step.

Implementation (warning: advanced usage):

[%CFEngine_include_snippet(masterfiles/update/update_policy.cf, .*)%]

##### cfe_internal_update_processes

This step manages the running processes, ensuring `cf-execd` and
`cf-serverd` and `cf-monitord` are running and doing some other tasks.

##### cfe_internal_update_bins

This step does a self-update of CFEngine. See the Enterprise
documentation for details; this functionality is unsupported in
CFEngine Community.

#### update.cf configuration ####

##### input_name_patterns

Change this variable to add more file extensions to the list copied
from the policy server.  By default this is a pretty sparse list.

##### masterfiles_perms_mode

Usually you want to leave this at `0600` meaning the inputs will be
readable only by their owner.

##### cfengine_internal_masterfiles_update

Off by default.

Turn this on (set to `any`) to auto-deploy policies on the policy
server, it has no effect on clients. See
[Version Control and Configuration Policy][Best Practices#Version Control and Configuration Policy]
for details on how to use it.

**This may result in DATA LOSS.**

##### cfengine_internal_encrypt_transfers

Off by default.

Turn this on (set to `any`) to encrypt your policy transfers.

Note it has a duplicate in `def.cf`, see below. If they are not
synchronized, you will get unexpected behavior.

##### cfengine_internal_purge_policies

Off by default.

Turn this on (set to `any`) to delete any files in your
`$(sys.inputdir)` that are not in the policy server's masterfiles.

**This may result in DATA LOSS.**

Note it has a duplicate in `def.cf`, see below. If they are not
synchronized, you will get unexpected behavior.

##### cfengine_internal_preserve_permissions

Off by default.

Turn this on (set to `any`) to preserve the permissions of the policy
server's masterfiles when they are copied.

**This may result in FUNCTIONALITY LOSS if your scripts lose their
exec bits unexpectedly**

Note it has a duplicate in `def.cf`, see below. If they are not
synchronized, you will get unexpected behavior.

### def.cf

After `update.cf` is configured, you can configure the main `def.cf` policy.

This file is included by the main `promises.cf` and you can run that
with `cf-agent -KI -f ./promises.cf` but as before, make sure you
understand what this command does before using it.

Keep referring to `def.cf` as you read this.

Implementation (warning: advanced usage):

[%CFEngine_include_snippet(masterfiles/def.cf, .*)%]

#### How it works ####

`def.cf` has some crucial settings used by the rest of CFEngine. It's
expected that users will edit it but won't normally change the rest of
the masterfiles except in `services` or if they *know* it's necessary.

This is a simple CFEngine policy, so read on for configuring it.

#### def.cf configuration ####

##### domain

Set your `domain` to the right value. By default it's used for mail
and to deduce your file access ACLs.

##### acl #####

The `acl` is crucial. This is used by **every** host, not just the
policy server. Make sure you only allow hosts you want to allow.

##### trustkeysfrom #####

`trustkeysfrom` tells the policy server from which IPs it should accept
connections even if the host's key is unknown, trusting it at connect
time. This is only useful to be open during for bootstrapping these
hosts. As the comments say, empty it after your hosts have been
bootstrapped to avoid unpleasant surprises.

##### services_autorun

Off by default.

Turn this on (set to `any`) to auto-load files in `services/autorun`
and run bundles found that are tagged `autorun`. Here's a simple
example of such a bundle in `services/autorun/hello.cf`:

[%CFEngine_include_snippet(masterfiles/services/autorun/hello.cf, .*)%]


##### cfengine_internal_rotate_logs

On by default. Rotates CFEngine's own logs. Here is the
`cfe_internal_log_rotation` bundle implementation:

[%CFEngine_include_snippet(masterfiles/cfe_internal/CFE_cfengine.cf, .*bundle\s+agent\s+cfe_internal_log_rotation, \})%]

##### cfengine_internal_agent_email

On by default. Enables agent email output from `cf-execd`.

##### cfengine_internal_encrypt_transfers

Duplicate of the one in `update.cf`. They should be set in unison or
you will get unexpected behavior.

##### cfengine_internal_purge_policies

Duplicate of the one in `update.cf`. They should be set in unison or
you will get unexpected behavior.

##### cfengine_internal_preserve_permissions

Duplicate of the one in `update.cf`. They should be set in unison or
you will get unexpected behavior.

##### cfengine_internal_sudoers_editing_enable

Off by default.  Only used on the CFEngine Enterprise hub.

Turn this on (set to `any`) to allow the hub to edit sudoers in order
for the Apache user to run passwordless sudo cf-runagent (part of
Mission Portal troubleshooting).

#### def.cf inventory control ####

The inventory is a cool new feature in 3.6. You can disable pieces
of it (inventory modules) or the whole thing if you wish.

##### disable_inventory

This class is off by default (meaning the inventory is on by default).
Here's the master switch to disable all inventory modules.

##### disable_inventory_lsb

LSB is the Linux Standard Base, see https://wiki.linuxfoundation.org/en/LSB

By default, this class is turned off (and the module is on) if the LSB
executable `/usr/bin/lsb_release` can be found. This inventory module
will populate inventory reports and variables for you with LSB
details. For details, see [LSB][The Policy Framework#LSB]

##### disable_inventory_dmidecode

By default, this class is turned off (and the module is on) if the
executable `/usr/sbin/dmidecode` can be found. This inventory module
will populate inventory reports and variables for you. For details,
see [DMI decoding][The Policy Framework#DMI decoding]

##### disable_inventory_LLDP

LLDP is a protocol for Link Layer Discovery. See
http://en.wikipedia.org/wiki/Link_Layer_Discovery_Protocol

By default, this class is turned off (and the module is on) if the
executable `/usr/bin/lldpctl` can be found. This inventory module will
populate variables for you. For details, see [LLDP][The Policy Framework#LLDP]

##### disable_inventory_package_refresh

By default, this class is turned off (and the module is on). This
inventory module will populate the installed packages for you. On
CFEngine Enterprise, the available packages will also be populated.

##### disable_inventory_mtab

By default, this class is turned off (and the module is on) if
`/etc/mtab` exists. This inventory module will populate variables for
you based on the mounted filesystems. For details, see [mtab][The Policy Framework#mtab]

##### disable_inventory_fstab

By default, this class is turned off (and the module is on) if
`$(sys.fstab)` (usually `/etc/fstab` or `/etc/vfstab`) exists. This
inventory module will populate variables for you based on the defined
filesystems. For details, see [fstab][The Policy Framework#fstab]

##### disable_inventory_proc

By default, this class is turned off (and the module is on) if `/proc`
is a directory. This inventory module will populate variables for you
from some of the contents of `/proc`. For details, see [procfs][The Policy Framework#procfs]

##### disable_inventory_cmdb

By default, this class is turned on (and the module is off).

Turn this on (set to `any`) to allow each client to load a `me.json`
file from the server and load its contents. For details, see [CMDB][The Policy Framework#CMDB]

### promises.cf

#### How it works ####

`promises.cf` is your main run file. Keep referring to your
installation's `promises.cf` as you read this.

`promises.cf` is the first file that `cf-agent` with no arguments will
try to look for. So whenever you see `cf-agent` with no flile
parameter, read it as "run my `promises.cf`".

It should contain all of the basic configuration
settings, including a list of other files to include. In normal
operation, it must also have a `bundlesequence`.

#### promises.cf configuration ####

##### bundlesequence #####

The `bundlesequence` acts like the 'genetic makeup' of the
configuration. Edit the `bundlesequence` to add any bundles you have
defined, or are pre-defined. Consider using the `services_autorun`
facility so you don't have to edit this setting at all.

**BEWARE THAT ONLY VALID (KNOWN) BUNDLES CAN BE ADDED.**

By default, the inventory modules, then internal hub modules, then
Design Center sketches, then the autorun services, and finally
internal management bundles are in the `bundlesequence`.

In a large configuration, you might want to have a different
`bundlesequence` for different classes of host, so that you can build
a complete system like a check-list from different combinations of
building blocks. You can construct different lists by composing them
from other lists, or you can use methods promises as an alternative
for composing bundles for different classes. This is an advanced topic
and a risky area (if you get it wrong, your policies will not
validate) so make sure you test your changes carefully!

##### inputs #####

In order to find bundles, CFEngine needs to know where to look. This
list defines what files are needed. Note there are several dynamic
entries here, coming from other bundles. CFEngine will keep evaluating
the `inputs` and `bundlesequence` until all the bundles are found and
resolved.

Make sure to add any of your own `services` files here if you don't
use the `services_autorun` facility, to ensure the bundles in them are
found.

## failsafe.cf

The `failsafe.cf` file ensures that your system can survive errors and
can upgrade gracefully to new versions even when mistakes are made.
It's literally a failsafe if `promises.cf` and `update.cf` should
fail.

This file is generated during the bootstrapping process, and should
normally never be changed. The only job of `failsafe.cf` is to execute
the update bundle in a “standalone” context should there be a syntax
error somewhere in the main set of promises. In this way, if a client
machine's policies are ever corrupted after downloading erroneous
policy from a server, that client will have a failsafe method for
downloading a corrected policy once it becomes available on the
server. Note that by “corrupted” and “erroneous” we typically mean
“broken via administrator error” - mistakes happen, and the
`failsafe.cf` file is CFEngine's way of being prepared for that
eventuality.

If you ever change `failsafe.cf` (or when you upgrade CFEngine), make
sure the old and the new CFEngine can successfully parse and execute
this file. If not, you risk losing control of your system (that is, if
CFEngine cannot successfully execute this policy file, it has no
failsafe/fallback mechanism for distributing new policy files).

Some general rules (but again, note you **can completely break your
CFEngine installation by editing `failsafe.cf`**):

* Upgrade the software first, then add new features to the configuration.
* Never use advanced features in the failsafe or update file.
* Avoid using library code (including any bodies from `stdlib.cf` or
the files it includes). Copy/paste any bodies you need using a unique
name that does not collide with a name in library (we recommend simply
adding the prefix “u_”). This may mean that you create duplicate
functionality, but that is okay in this case to ensure a 100%
functioning standalone update process). The promises which manage the
update process should not have any dependencies on any other files.

CFEngine will fail-over to the `failsafe.cf` configuration if it is
unable to read or parse the contents successfully. That means that any
syntax errors you introduce (or any new features you utilize in a
configuration) will cause a fail-over, because the parser will not be
able to interpret the policy. If the failover is due to the use of new
features, they will not parse until the software itself has been
updated (so we recommend that you always update CFEngine before
updating policy to use new features). If you accidentally cause a bad
(i.e., unparseable) policy to be distributed to client machines, the
`failsafe.cf` policy on those machines will run (and will eventually
download a working policy, once you fix it on the policy host).

## Further structure ##

* `cfe_internal`: internal CFEngine policies you shouldn't modify or you will get unexpected behavior
* `controls`: configuration of components, e.g. the `cf-agent` or `cf-serverd`, beyond what `def.cf` can offer
* `def.cf`: defaults you can and should configure, see above
* `inventory`: inventory modules (loaded before anything else to discover facts about the system) live here; see above
* `lib`: main library directory.  You'll see `3.5` and `3.6` and `3.7` under it.  These are the supported versions for masterfiles backwards compatibility.
* `promises.cf`: main policy, you will need to configure this, see above
* `services`: your site's policies go here
* `services_autorun`: see above
* `sketches`: Design Center installations use this; do not touch or you will get unexpected behavior
* `update` and `update.cf`: functionality for updating inputs and CFEngine itself, see above.  You shouldn't modify files under `update` or you will get unexpected behavior.

## cf_promises_validated

Several CFEngine components that read policy (e.g. `cf-agent`, `cf-execd`, `cf-serverd`) run `cf-promises` to validate the syntax of their input files before actually running the policy. To illustrate this, if `cf-promises` runs every 5 minutes then there will be 12 checks occurring every hour, 24 hours a day, 7 days a week -- a total of 2016 possible validation checks. Each of those individual validation sessions can take some number of seconds to perform depending on the system, scale, circumstances and configuration.

Starting with CFEngine 3.1.2, the outcome of every run of `cf-promises` was cached, which lets agents skip the validation of input files that have not changed since the previous run.

Starting with CFEngine 3.6, outcome on both hosts and hubs is stored in the file `$(sys.workdir)/masterfiles/cf_promises_validated` (usually `sys.workdir` is `/var/cfengine`). The file can be created by `cf-agent` after it has successfully verified the policy with `cf-promises`. The file can also be created by a user with `cf-promises -T DIRECTORY` which is useful for validating an entire directory.

When the hash content of any file under `WORKDIR/inputs` changes, and validates to be syntactically correct, then a timestamp in `cf_promises_validated` is updated. If not, the run of `cf-promises` is skipped and, at the same time, the cf-execd, cf-serverd and cf-monitord daemons will not reload the policy unless `cf_promises_validated` has an updated timestamp, which `cf-agent` will normally take care of.

In the default installation, the masterfiles are populated
automatically on the policy server and you can even auto-deploy them
from a [version control system][Version Control].

You should configure the masterfiles as described above. Leaving them
at their default settings may expose your masterfiles or worse,
especially the cf-serverd ACL settings. If you are not sure of the
terms used below or what it all means, come back to this page after
you've learned about writing policy and the CFEngine syntax.

## CFEngine 3 Inventory Modules ##

The CFEngine 3 inventory modules are pieces of CFEngine policy that
are loaded and used by the `promises.cf` mechanism in order to
*inventory* the system.

CFEngine Enterprise has specific functionality to show and use
inventory data, but users of the Community Version can use them as
well locally on each host.

## How It Works ##

The inventory modules are called in `promises.cf`:

```
body common control
{
      bundlesequence => {
                        # Common bundle first (Best Practice)
                          inventory_control,
                          @(inventory.bundles),
                          ...
```

As you see, this calls the `inventory_control` bundle, and then each
bundle in the list `inventory.bundles`. That list is built in the
top-level common `inventory` bundle, which will load the right things
for some common cases. The `any.cf` inventory module is always loaded;
the rest are loaded if they are appropriate for the platform. For
instance, Debian systems will load `debian.cf` and `linux.cf` and
`lsb.cf` but may load others as needed.

The effect for users is that the right inventory modules will be
loaded and evaluated.

The `inventory_control` bundle lives in `def.cf` and defines what
inventory modules should be disabled. You can simply set
`disable_inventory` to avoid the whole system, or you can look for the
`disable_inventory_xyz` class to disable module `xyz`.

Any inventory module works the same way, by doing some discovery work
and then tagging its classes and variables with the `report` or
`inventory` tags.  For example:

```
  vars:
      "ports" slist => { @(mon.listening_ports) },
      meta => { "inventory", "attribute_name=Ports listening" };
```

This defines a reported attribute "Ports listening" which contains a
list of strings representing the listening ports. More on this in a
second.

## Your Very Own Inventory Module ##

The good news is, writing an inventory module is incredibly easy.

They are just CFEngine bundles. You can see a simple one that collects
the listening ports in `any.cf`:

```
bundle agent cfe_autorun_inventory_listening_ports
# @brief Inventory the listening ports
#
# This bundle uses `mon.listening_ports` and is always enabled by
# default, as it runs instantly and has no side effects.
{
  vars:
      "ports" slist => { @(mon.listening_ports) },
      meta => { "inventory", "attribute_name=Ports listening" };
}
```

Well, the slist copy is a CFEngine detail (we get the listening ports
from the monitoring daemon), so just assume that the data is correct.
What's important is the second line that starts with
[`meta`][Promise Types and Attributes#meta]. That
defines metadata for the promise that CFEngine will use to determine
that this data is indeed inventory data and should be reported to the
CFEngine Enterprise Hub.

That's it. Really. The comments are optional but nice to have. You
don't have to put your new bundle in a file under the `inventory`
directory, either. The variables and classes can be declared anywhere
as long as they have the right tags. So you can use the `services`
directory or whatever else makes sense to you.

## CFEngine Enterprise vs. Community ##

In CFEngine Enterprise, the reported data is aggregated in the hub and
reported across the whole host population.

In CFEngine Community, users can use the `classesmatching()` and
`variablesmatching()` functions to collect all the inventory variables
and classes and report them in other ways.

### Implementation Best Practice for CFEngine Enterprise ###

It is important that inventory variables and classes are continually
defined. Only inventory variables and classes defined during the last
reported run are available for use by the inventory reporting interface.

Inventory items that change frequently can create a burden on the
Enterprise reporting infrastructure. Generally, inventory attributes
should change infrequently.

If you wish to inventory attributes that frequently change or are expensive to
discover consider implementing a sample interval and caching mechanism.

## What Modules Are Available? ##

As soon as you use the `promises.cf` provided in the parent directory,
quite a few inventory modules will be enabled (if appropriate for your
system). Here's the list of modules and what they provide. Note they
are all enabled by code in `def.cf` as explained above.

### LSB ###

* lives in: `lsb.cf`
* applies to: LSB systems (most Linux distributions, basically)
* runs: `lsb_release -a`
* sample data:

```
Distributor ID:	Ubuntu
Description:	Ubuntu 14.04 LTS
Release:	14.04
Codename:	trusty
```

* provides:
    * classes `lsb_$(os)`, `lsb_$(os)_$(release)`, `lsb_$(os)_$(codename)`
    * variables: `inventory_lsb.os` (Distributor ID), `inventory_lsb.codename`, `inventory_lsb.release`, `inventory_lsb.flavor`, `inventory_lsb.description`
* implementation:
[%CFEngine_include_snippet(masterfiles/inventory/lsb.cf, .* )%]

* sample output:

```
% cf-agent -KI -binventory_control,inventory_lsb

R: inventory_lsb: OS = Ubuntu, codename = trusty, release = 14.04, flavor = Ubuntu_14_04, description = Ubuntu 14.04 LTS
```

### SUSE ###

* lives in: `suse.cf`
* applies to: SUSE Linux
* provides classes: `suse_pure` and `suse_derived`
* implementation:
[%CFEngine_include_snippet(masterfiles/inventory/suse.cf, .* )%]

### Debian ###

* lives in: `debian.cf`
* applies to: Debian and its derivatives
* provides:
    * variables: `inventory_debian.mint_release` and `inventory_debian.mint_codename`
    * classes: `debian_pure`, `debian_derived`, `linuxmint`, `lmde`, `linuxmint_$(mint_release)`, `linuxmint_$(mint_codename)`, `$(mint_codename)`
* implementation:
[%CFEngine_include_snippet(masterfiles/inventory/debian.cf, .* )%]

### Red Hat ###

* lives in: `redhat.cf`
* applies to: Red Hat and its derivatives
* provides classes: `redhat_pure`, `redhat_derived`
* implementation:
[%CFEngine_include_snippet(masterfiles/inventory/redhat.cf, .* )%]

### Windows ###

* lives in: `windows.cf`

### Mac OS X ###

* lives in: `macos.cf`

### Generic (unknown OS) ###

* lives in: `generic.cf` (see `any.cf` for generally applicable inventory modules)

### LLDP ###

* lives in: `any.cf`
* runs `inventory_control.lldpctl_exec` through a Perl filter
* provides variables: `cfe_autorun_inventory_LLDP.K` for each `K` returned by the LLDB executable
* implementation:
[%CFEngine_include_snippet(masterfiles/inventory/any.cf, .*bundle\s+agent\s+cfe_autorun_inventory_LLDP, \})%]

### mtab ###

* lives in: `any.cf`
* parses: `/etc/mtab`
* provides classes: `have_mount_FSTYPE` and `have_mount_FSTYPE_MOUNTPOINT`
* implementation:
[%CFEngine_include_snippet(masterfiles/inventory/any.cf, .*bundle\s+agent\s+cfe_autorun_inventory_mtab, \})%]

* sample output (note this is verbose mode with `-v` because there's a lot of output):

```
% cf-agent -Kv -binventory_control,cfe_autorun_inventory_mtab|grep 'cfe_autorun_inventory_mtab: we have'

R: cfe_autorun_inventory_mtab: we have a ext4 mount under /
...
R: cfe_autorun_inventory_mtab: we have a cgroup mount under /sys/fs/cgroup/systemd
R: cfe_autorun_inventory_mtab: we have a tmpfs mount under /run/shm
```

### fstab ###

* lives in: `any.cf`
* parses: `sys.fstab`
* provides classes: `have_fs_FSTYPE` `have_fs_MOUNTPOINT` and `have_fs_FSTYPE_MOUNTPOINT`
* implementation:
[%CFEngine_include_snippet(masterfiles/inventory/any.cf, .*bundle\s+agent\s+cfe_autorun_inventory_fstab, \})%]

* sample output (note this is verbose mode with `-v` because there's a LOT of output):

```
% cf-agent -Kv -binventory_control,cfe_autorun_inventory_fstab|grep 'cfe_autorun_inventory_fstab: we have'

R: cfe_autorun_inventory_fstab: we have a ext4 fstab entry under /
R: cfe_autorun_inventory_fstab: we have a cifs fstab entry under /backups/load
R: cfe_autorun_inventory_fstab: we have a auto fstab entry under /mnt/cdrom
```

### CMDB ###

* lives in: `any.cf`
* parses: `me.json` (which is copied from the policy server; see implementation)
* provides classes: `CLASS` for each CLASS found under the ```classes``` key in the JSON data
* provides variables: `inventory_cmdb_load.VARNAME` for each VARNAME found under the `vars` key in the JSON data
* implementation:
[%CFEngine_include_snippet(masterfiles/inventory/any.cf, .*bundle\s+agent\s+inventory_cmdb_load, \})%]

### DMI decoding ###

* lives in: `any.cf`
* runs: `dmidecode`
* provides variables: `cfe_autorun_inventory_dmidecode.dmi[K]` for each key K in the `dmidecode` output
* implementation:
[%CFEngine_include_snippet(masterfiles/inventory/any.cf, .*bundle\s+agent\s+cfe_autorun_inventory_dmidecode, \})%]

* sample output (sudo is needed to access the DMI):

```
% sudo /var/cfengine/bin/cf-agent -KI -binventory_control,cfe_autorun_inventory_dmidecode

R: cfe_autorun_inventory_dmidecode: Obtained BIOS vendor = 'Intel Corp.'
R: cfe_autorun_inventory_dmidecode: Obtained BIOS version = 'BLH6710H.86A.0146.2013.1555.1888'
R: cfe_autorun_inventory_dmidecode: Obtained System serial number = ''
R: cfe_autorun_inventory_dmidecode: Obtained System manufacturer = ''
R: cfe_autorun_inventory_dmidecode: Obtained System version = ''
R: cfe_autorun_inventory_dmidecode: Obtained CPU model = 'Intel(R) Core(TM) i7-2600 CPU @ 3.40GHz'
```

### Listening ports ###

* lives in: `any.cf`
* provides variables: `cfe_autorun_inventory_listening_ports.ports` as a copy of `mon.listening_ports`
* implementation:
[%CFEngine_include_snippet(masterfiles/inventory/any.cf, .*bundle\s+agent\s+cfe_autorun_inventory_listening_ports, \})%]

### Disk space ###

* lives in: `any.cf`
* provides variables: `cfe_autorun_inventory_disk.free` as a copy of `mon.value_diskfree`
* implementation:
[%CFEngine_include_snippet(masterfiles/inventory/any.cf, .*bundle\s+agent\s+cfe_autorun_inventory_disk, \})%]

### Available memory ###

* lives in: `any.cf`
* provides variables: `cfe_autorun_inventory_memory.free` as a copy of `mon.value_mem_free` and `cfe_autorun_inventory_memory.total` as a copy of `mon.value_mem_total`
* implementation:
[%CFEngine_include_snippet(masterfiles/inventory/any.cf, .*bundle\s+agent\s+cfe_autorun_inventory_memory, \})%]

### Load average ###

* lives in: `any.cf`
* provides variables: `cfe_autorun_inventory_loadaverage.value` as a copy of `mon.value_loadavg`
* implementation:
[%CFEngine_include_snippet(masterfiles/inventory/any.cf, .*bundle\s+agent\s+cfe_autorun_inventory_loadaverage, \})%]

### procfs ###

* lives in: `any.cf`
* parses: `consoles`, `cpuinfo`, `modules`, `partitions`, `version`
* provides variables: `cfe_autorun_inventory_proc.console_count`, `cfe_autorun_inventory_proc.cpuinfo[K]` for each CPU info key, `cfe_autorun_inventory_proc.paritions[K]` for each partition key
* provides classes: `_have_console_CONSOLENAME`, `have_module_MODULENAME`
* implementation:
[%CFEngine_include_snippet(masterfiles/inventory/any.cf, .*bundle\s+agent\s+cfe_autorun_inventory_proc, \})%]

* sample output (note this is verbose mode with `-v` because there's a LOT of output):

```
% cf-agent -Kv -binventory_control,cfe_autorun_inventory_proc|grep 'cfe_autorun_inventory_proc: we have'

R: cfe_autorun_inventory_proc: we have console tty0

R: cfe_autorun_inventory_proc: we have module snd_seq_midi
...
R: cfe_autorun_inventory_proc: we have module ghash_clmulni_intel

R: cfe_autorun_inventory_proc: we have cpuinfo flags = fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic popcnt tsc_deadline_timer aes xsave avx lahf_lm ida arat epb xsaveopt pln pts dtherm tpr_shadow vnmi flexpriority ept vpid
...
R: cfe_autorun_inventory_proc: we have cpuinfo model name = Intel(R) Core(TM) i7-2600 CPU @ 3.40GHz

R: cfe_autorun_inventory_proc: we have partitions sr0 with 1048575 blocks
...
R: cfe_autorun_inventory_proc: we have partitions sda with 468851544 blocks

R: cfe_autorun_inventory_proc: we have kernel version 'Linux version 3.11.0-15-generic (buildd@roseapple) (gcc version 4.8.1 (Ubuntu/Linaro 4.8.1-10ubuntu8) ) #25-Ubuntu SMP Thu Jan 30 17:22:01 UTC 2014'
```
