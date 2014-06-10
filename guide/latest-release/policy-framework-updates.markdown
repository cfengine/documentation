---
layout: default
title: Policy Framework Updates
published: true
sorting: 3
tags: [releases, latest release, 3.6.0, platforms, versions, what's new]
---

## CFEngine Policy Framework Updates for 3.6.0 ##

If you follow the CFEngine masterfiles policy framework (the masterfiles you
get out of the box) we encourage you to upgrade the policy framework each time
you upgrade CFEngine. We reccomend making as few changes as possible to the
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

* Whats new in the 3.6 masterfiles policy framework?
	* README.md
	* Directories
		* templates
		* cfe_internal 
		* inventory
		* sketches
		* update
	* Features defined in def.cf
	* The Standard Library
	* update.cf
* Upgrade Gotchas
	* General
		* Array Keys are not iterated in the decalred order any more.
		* Function Caching
		* Files considered by update.cf have moved and changed
	* Enterprise Users
		* Options controlling which variables to report have moved and changed
		* Host licenses paid deprecated

### README.md ###

That's right. We finally added some documentation inside of
masterfiles. This document explains the general layout of the framework.

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

`def.cf` has contined various global settings
for some time, including various common directories, and simple access control
list definition to control which remote hosts could connect. Comparing def.cf
from 3.5 and 3.6 will reveal many additions

* [services_autorun][Policy Framework#services_autorun] provides automatic loading and activation of policy.
* [cfengine_internal_rotate_logs][Policy Framework#cfengine_internal_rotate_logs] Enables log rotation for CFEngines log files.
* [cfengine_internal_encrypt_transfers][Policy Framework#cfengine_internal_encrypt_transfers] Enables encryption for policy and
binary updates done during the update policy. Note: This setting is mirrored from
update.cf for CFEngine enterprise reporting. This setting is superfluous
when `protocal_version` is set to 2 or higher which enables TLS encryption for
communication.
* [cfengine_internal_purge_policies][Policy Framework#cfengine_internal_purge_policies]: Enables purging of policies that no
longer exist in masterfiles. Note: This setting is mirrored from update.cf for
CFEngine enterprise reporting.
* [postgresql_maintenance][Policy Framework#postgresql_maintenance]: Enables database maintainance for CFEngine
Enterprise Policy hubs.

`def.cf` also sees the addition of `bundle common inventory_control` which is
responsible for controlling the new inventory bundles. Inventory bundles
provide variables and classes that can be useful for both Enterprise reporting
and directly from within policy. LSB (Linux Standards Base), Dmidecode, LLDP
(Link Layer Discovery Protocol), software installed, mounted filesystems
(mtab), configured filesystems (fstab), and proc are some of the inventory
policies provided out of the box.
<LINK REF TO INVENTORY BUNDLES>
This link should explain inventory stuff, but also give examples of how you
can use the inventory information from within other policy .

## The Standard Library ##

The standard library `lib/3.6/*.cf` has seen many improvements. First and foremost is the addition of doxygen
style inline documentation. This inline documentation markup is levereged by
our documentation system to provide a rendered version of the standard library
which is included in the reference manual. Of special note: the
`standard_services` has been improved to make it more dynamic, and now has
support for systemd, sysvinitd, sysvservice, and chkconfig. New convenianence
bundles and bodies for common patterns have been added including
[dir_sync][Files Bundles and Bodies#dir_sync]
[file_copy][Files Bundles and Bodies#file_copy]
[file_empty][Files Bundles and Bodies#file_empty]
[file_hardlink][Files Bundles and Bodies#file_hardlink]
[file_link][Files Bundles and Bodies#file_link]
[file_make][Files Bundles and Bodies#file_make]
[file_mustache_jsonstring][Files Bundles and Bodies#file_mustache_jsonstring]
[file_mustache][Files Bundles and Bodies#file_mustache]
[file_tidy][Files Bundles and Bodies#file_tidy]
[converge]Files Bundles and Bodies#converge]
[fstab_option_editor][Files Bundles and Bodies#fstab_option_editor]
[insert_ini_section][Files Bundles and Bodies#insert_ini_section]
[prepend_if_no_line][Files Bundles and Bodies#prepend_if_no_line]
[resolvconf_o][Files Bundles and Bodies#resolvconf_o]
[set_line_based][Files Bundles and Bodies#set_line_based]
[fstab_options][Files Bundles and Bodies#fstab_options]
[bigger_than][Files Bundles and Bodies#bigger_than]
[linkfrom][Files Bundles and Bodies#linkfrom]
[package_absent][Packages Bundles and Bodies#package_absent]
[package_latest][Packages Bundles and Bodies#package_latest]
[package_present][Packages Bundles and Bodies#package_present]
[package_specific_absent][Packages Bundles and Bodies#package_specific_absent]
[package_specific_latest][Packages Bundles and Bodies#package_specific_latest]
[package_specific][Packages Bundles and Bodies#package_specific]
[package_specific_present][Packages Bundles and Bodies#package_specific_present]
[brew][Packages Bundles and Bodies#brew]
[npm][Packages Bundles and Bodies#npm]
[pip][Packages Bundles and Bodies#pip]
[process_kill][Process Bundles and Bodies#process_kill]
[by_owner][Processes Bundles and Bodies#by_owner]
[logrotate][Common Bodies and Bundles#logrotate]
[prunedir][Common Bodies and Bundles#prunedir]
[cmerge][Common Bodies and Bundles#cmerge]
[rm_rf_depth][Common Bodies and Bundles#rm_rf_depth]
[url_ping][Common Bodies and Bundles#url_ping]
[setuidgid_dir][Commands Bundles and Bodies#setuidgid_dir]
[setuid_gid_umask][Commands Bundles and Bodies#setuid_gid_umask]
[system_owned][Files Bundles and Bodies#system_owned]

## update.cf ##

The `update.cf` policy got broken up from its monolithic form and
now has additional update policies included inside the `update` directory.
bundle common update_def was added to provide a common place to enable
features related to policy updates (much like body common def found in
def.cf).

* *cfengine_internal_masterfiles_update*: This class enables automatic policy
deployment on the policy server. This is designed for use with CFEngine
Enterprise.
* *cfengine_internal_encrypt_transfers* Enables encryption for policy and
binary updates done during the update policy. Note: This setting is mirrored
in def.cf for CFEngine enterprise reporting. This setting is superfluous when
`protocal_version` is set to 2 or higher which enables TLS encryption for
communication.
* *cfengine_internal_purge_policies*: Enables purging of policies that no
longer exist in masterfiles. Note: This setting is mirrored in promises.cf for
CFEngine enterprise reporting.


Now that you have an overview of whats new, lets cover a few things you need
to watch our for when upgrading.

## Upgrade Gotchas ##

### Array Keys are not iterated in the decalred order any more. ###

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

If the resulting list order is important please consider the `sort`() and
`reverse`() functions.


### Function Caching ###

3.6.0 introduces function
caching(https://docs.cfengine.com/docs/master/reference-functions.html#function-caching)
to help further improve performance and execution speed.

This behavior can be disabled by setting the `cache_system_functions` common
control attribute to "false". A function is cached when it is first evaluated
and it's cached result is used until the end of the agent execution. If have
previously depended on function re-evaluation in order to have proper results
after an action has been taken consider guarding the function call to only be
evaluated after a pre-conditional promise using conventional class guards,
or the `ifvarclass` and `depends_on` attributes.

### Files considered by update.cf have moved and changed ###

Previously `body file_select u_input_files` controlled which files were
considered when performing a policy update. That list of extensions has moved
to `update_def.input_name_patterns`. '*.conf', and '*.mustache' files have
been added to the default list.
FAQ: https://docs.cfengine.com/docs/master/guide-faq.html#i-have-added-new-files-in-masterfiles-but-my-remote-clients-are-not-getting-updates

## Enterprise Users ##

### Options controlling which variables to report have moved and changed ###

In 3.6 we begin using tags to identify which variables and classes to report
on. `report_data_select` has moved from `controls/cf_serverd.cf` to
`lib/$(sys.cf_version_major).$(sys.cf_version_minor)/reports.cf`. In 3.6 we
report on variables and `namespace` scope classes that are tagged with
"inventory" or "report" using the new `metatags_include` and
`metatags_exclude` attributes.

The following attributes have been deprecated in 3.6.0, please tag the
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

### Host licenses paid deprecated ###

This option was deprecated in CFEngine 3.5 and is no longer valid syntax.

This information is embedded in your Enterprise license, simply ensure that
`host_license_paid` is not defined in your `body common control`.