---
layout: default
title: Policy Framework Updates
published: true
sorting: 40
tags: [releases, latest release, "3.6", platforms, versions, what's new]
---

## CFEngine Policy Framework Updates for 3.6 ##

If you follow the CFEngine masterfiles policy framework (the masterfiles you
get out of the box) we encourage you to upgrade the policy framework each time
you upgrade CFEngine. We recommend making as few changes as possible to the
shipped masterfiles to make these upgrades as painless as possible. Generally
the best way to accomplish that is to take your custom policy and integrate it
on top of the new masterfiles.

3.6 introduces significant changes to the masterfiles policy framework.
Masterfiles was moved out from core into its own repository and was merged
with the policy framework from CFEngine Enterprise. Now both the core
(CFEngine Community) and CFEngine Enterprise ship with a common masterfiles
policy framework. For us it makes maintanence easier, and for the community
and customers it ensures that improvements that come into the framework are
easily accessible from either product.

Please consult [The Policy Framework] for a map to the policy framework.

* [What is new in the 3.6 masterfiles policy framework][Policy Framework Updates#What is new in the 3.6 masterfiles policy framework]
	* [Directories][Policy Framework Updates#Directories]
		* [templates][Policy Framework Updates#templates]
		* [cfe_internal][Policy Framework Updates#cfe_internal]
		* [inventory][Policy Framework Updates#inventory]
		* [sketches][Policy Framework Updates#sketches]
		* [update][Policy Framework Updates#update]
	* [Features defined in def.cf][Policy Framework Updates#Features defined in def.cf]
	* [The Standard Library][Policy Framework Updates#The Standard Library]
	* [update.cf][Policy Framework Updates#update.cf]
* [Upgrade Gotchas][Policy Framework Updates#Upgrade Gotchas]
	* [General][Policy Framework Updates#General]
		* [Array Keys are not iterated in the decalred order any more][Policy Framework Updates#Array Keys are not iterated in the decalred order any more]
		* [Function Caching][Policy Framework Updates#Function Caching]
		* [Files considered by update.cf have moved and changed][Policy Framework Updates#Files considered by update.cf have moved and changed]
	* [Enterprise Users][Policy Framework Updates#Enterprise Users]
		* [Options controlling which variables to report have moved and changed][Policy Framework Updates#Options controlling which variables to report have moved and changed]
		* [Host licenses paid deprecated][Policy Framework Updates#Host licenses paid deprecated]

## What is new in the 3.6 masterfiles policy framework ##
		
## Directories ##

### templates ###

Many users create a top level templates directory for global
template distribution. We made it easy by creating a `templates/` directory
that's always copied for you.

### cfe_internal ###

The `cfe_internal/` directory contains policies that manage how CFEngine
runs, much of this is in relation to the Enterprise version.

### inventory ###

The `inventory/` directory contains policies that do discovery of various
inventory attributes.

### sketches ###

The `sketches/` directory is where Design Center sketches and their
associated runfile get deployed.

### update ###

The `update/` directory contains policies that have been split out from
the previously monolithic `update.cf`.

### Features defined in def.cf ###

`def.cf` has continued various global settings
for some time, including various common directories, and simple access control
list definition to control which remote hosts could connect. Comparing def.cf
from 3.5 and 3.6 will reveal many additions

* [services_autorun][The Policy Framework#services_autorun] provides automatic loading and activation of policy.
* [cfengine_internal_rotate_logs][The Policy Framework#cfengine_internal_rotate_logs] Enables log rotation for CFEngines log files.
* [cfengine_internal_encrypt_transfers][The Policy Framework#cfengine_internal_encrypt_transfers] Enables encryption for policy and binary updates done during the update policy.

  Note: This setting is mirrored from
  update.cf for CFEngine enterprise reporting. This setting is superfluous
  when `protocol_version` is set to 2 or higher which enables TLS encryption for
  communication.
* [cfengine_internal_purge_policies][The Policy Framework#cfengine_internal_purge_policies]: Enables purging of policies that no longer exist in masterfiles.

  Note: This setting is mirrored from update.cf for [CFEngine Enterprise][] reporting.

* postgresql_maintenance: Enables database maintenance for [CFEngine Enterprise][] Policy hubs.

`def.cf` also sees the addition of `bundle common inventory_control` which is
responsible for controlling the new inventory bundles. Inventory bundles
provide variables and classes that can be useful for both Enterprise reporting
and directly from within policy. LSB (Linux Standards Base), Dmidecode, LLDP
(Link Layer Discovery Protocol), software installed, mounted filesystems
(mtab), configured filesystems (fstab), and proc are some of the inventory
policies provided out of the box.

See [The Policy Framework] to understand inventory modules and learn how you
can use the inventory information from within other policy and from the CFEngine Enterprise Mission Portal.

## The Standard Library ##

The standard library `lib/3.6/*.cf` has seen many improvements. First and foremost is the addition of doxygen
style inline documentation. This inline documentation markup is levereged by
our documentation system to provide a rendered version of the standard library
which is included in the reference manual.

You only need to include `$(sys.libdir)/stdlib.cf` to get the whole
standard library. `sys.libdir` resolves to the right path for your
installation, including the version (3.6, 3.7, etc.)

Of special note: the
`standard_services` has been improved to make it more dynamic, and now has
support for systemd, sysvinitd, sysvservice, and chkconfig. New convenianence
bundles and bodies for common patterns have been added including:

* `dir_sync()`
* `file_copy()`
* `file_empty()`
* `file_hardlink()`
* `file_link()`
* `file_make()`
* `file_mustache_jsonstring()`
* `file_mustache()`
* `file_tidy()`
* `converge()`
* `fstab_option_editor()`
* `insert_ini_section()`
* `prepend_if_no_line()`
* `resolvconf_o()`
* `set_line_based()`
* `fstab_options()`
* `bigger_than()`
* `linkfrom()`
* `package_absent()`
* `package_latest()`
* `package_present()`
* `package_specific_absent()`
* `package_specific_latest()`
* `package_specific()`
* `package_specific_present()`
* `brew()`
* `npm()`
* `pip()`
* `process_kill()`
* `by_owner()`
* `logrotate()`
* `prunedir()`
* `cmerge()`
* `rm_rf_depth()`
* `url_ping()`
* `setuidgid_dir()`
* `setuid_gid_umask()`
* `system_owned()`

## update.cf ##

The `update.cf` policy got broken up from its monolithic form and
now has additional update policies included inside the `update` directory.
bundle common update_def was added to provide a common place to enable
features related to policy updates (much like body common def found in
`def.cf`).  Please see [The Policy Framework] for the full details.

* *cfengine_internal_masterfiles_update*: This class enables automatic policy
deployment on the policy server. This is designed for use with CFEngine
Enterprise.
* *cfengine_internal_encrypt_transfers* Enables encryption for policy and
binary updates done during the update policy. Note: This setting is mirrored
in def.cf for CFEngine enterprise reporting. This setting is superfluous when
`protocol_version` is set to 2 or higher which enables TLS encryption for
communication.
* *cfengine_internal_purge_policies*: Enables purging of policies that no
longer exist in masterfiles. Note: This setting is mirrored in promises.cf for
CFEngine enterprise reporting.
* ...and much more!

Now that you have an overview of whats new, lets cover a few things you need
to watch our for when upgrading.

## Upgrade Gotchas ##

### General ###

#### Array Keys are not iterated in the decalred order any more ####

The order of results returned by getindices function is not necessarily
returned in the order defined.
**Example:**

```cf3
bundle agent example
{
  vars:
    "array[key1]" string => "value1";
    "array[key2]" string => "value2";
    "array[key3]" string => "value3";

    "keys" slist => getindices(array);

 reports:
    "$(keys)";
}
```

The above policy will produce the following output on 3.5:

```
R: key1
R: key2
R: key3
```

The same policy in 3.6 will produce:

```
R: key1
R: key3
R: key2
```

If the resulting list order is important please consider the `sort()` and
`reverse()` functions.


#### Function Caching ####

3.6 introduces function
caching(https://docs.cfengine.com/docs/master/reference-functions.html#function-caching)
to help further improve performance and execution speed.

This behavior can be disabled by setting the `cache_system_functions` common
control attribute to "false". A function is cached when it is first evaluated
and it's cached result is used until the end of the agent execution. If have
previously depended on function re-evaluation in order to have proper results
after an action has been taken consider guarding the function call to only be
evaluated after a pre-conditional promise using conventional class guards,
or the `ifvarclass` and `depends_on` attributes.

#### Files considered by update.cf have moved and changed ####

Previously `body file_select u_input_files` controlled which files were
considered when performing a policy update. That list of extensions has moved
to `update_def.input_name_patterns`. '*.conf', and '*.mustache' files have
been added to the default list.

For more information, see the [FAQ][FAQ#i-have-added-new-files-in-masterfiles-but-my-remote-clients-are-not-getting-updates]

### Enterprise Users ###

#### Options controlling which variables to report have moved and changed ####

In 3.6 we begin using tags to identify which variables and classes to report
on. `report_data_select` has moved from `controls/cf_serverd.cf` to
`lib/$(sys.cf_version_major).$(sys.cf_version_minor)/reports.cf`. In 3.6 we
report on variables and `namespace` scope classes that are tagged with
"inventory" or "report" using the new `metatags_include` and
`metatags_exclude` attributes.

The following attributes have been deprecated in 3.6.  Please tag the
variables and classes you would like to report on appropriately. If you have
any questions please contact support.

* `classes_include`
* `classes_exclude`
* `variables_include`
* `variables_exclude`
* `promise_notkept_log_include`
* `promise_notkept_log_exclude`
* `promise_repaired_log_include`
* `promise_repaired_log_exclude`

#### Host licenses paid deprecated ####

This option was deprecated in CFEngine 3.5 and is no longer valid syntax.

This information is embedded in your Enterprise license, simply ensure that
`host_license_paid` is not defined in your `body common control`.
