---
layout: default
title: Hard and Soft Classes
categories: [Reference, Classes]
published: true
sorting: 40
alias: reference-classes.html
tags: [reference, hard classes, soft classes, classes]
---

[Classes][classes and decisions] fall into **hard**
(discovered) and **soft** (defined) types. This reference documents the hard 
classes that might be set by CFEngine, and soft classes used by CFEngine's 
default policy.

## Listing Classes

To see all of the classes defined on a particular host, run

    $ cf-promises --show-classes

as a privileged user. Note that some of the classes are set only if a trusted 
link can be established with 
[`cf-monitord`][cf-monitord], i.e. if both are 
running with privilege, and the `/var/cfengine/state/env_data` file is 
secure.

You can use
https://github.com/cfengine/design-center/tree/master/tools/hcgrep to
obtain this list in a format suitable for other tools like `grep` (one
class per line), but all the information it offers should be available
with `cf-promises --show-classes`.

You can also use the built-in `classesmatching()` function to get a
list of all the defined classes in a list, inside CFEngine policy
itself.  `classesmatching()` is especially useful because it also lets
you specify tag regular expressions.

## Tags

Classes and variables have tags that describe their provenance (who
created them) and purpose (why were they created).

While you can provide your own tags for soft classes in policy with
the `meta` attribute, there are some tags applied to hard classes and
other special cases.  This list may change in future versions of
CFEngine.

* `source=agent`: this hard class or variable was created by the agent in the C code.  This tag is useful when you need to find classes or variables that don't match the other sources below.  e.g. `linux`.
* `source=environment`: this hard class or variable was created by the agent in the C code.  It reflects something about the environment like a command-line option, e.g. `-d` sets `debug_mode`, `-v` sets `verbose_mode`, and `-I` sets `inform_mode`.  Another useful option, `-n`, sets `opt_dry_run`.
* `source=bootstrap`: this hard class or variable was created by the agent in the C code based on bootstrap parameters.  e.g. `policy_server` is set based on the IP address or host name you provided when you ran `cf-agent -B host-or-ip`.
* `source=module`: this class or variable was created through the module protocol.
* `source=persistent`: this persistent class was loaded from storage.
* `source=body`: this variable was created by a body with side effects.
* `source=function`: this class or variable was created by a function as a side effect, e.g. see the classes that `selectservers()` sets or the variables that `regextract()` sets.  These classes or variables will also have a `function=FUNCTIONNAME` tag.
* `source=promise`: this soft class was created from policy.
* `inventory`: related to the system inventory, e.g. the network interfaces
  * `attribute_name=none`: has no visual attribute name
  * `attribute_name=X`: has visual attribute name `X`
* `monitoring`: related to the monitoring (`cf-monitord` usually).
* `time_based`: based on the system date, e.g. `Afternoon`
* `derived-from=varname`: for a class, this tells you it was derived from a variable name, e.g. if the special variable `sys.fqhost` is `xyz`, the resulting class `xyz` will have the tag `derived-from=sys.fqhost`.
* `cfe_internal`: internal utility classes and variables

Enterprise only:

* `source=ldap`: this soft class or variable was created from an LDAP lookup.
* `source=observation`: this class or variable came from a `measurements` system observation and will also have the `monitoring` tag.

## Hard Classes

* CFEngine-specific classes
    * `any`: this class is always set
    * `am_policy_hub`, `policy_server`: set when a host is the policy hub
    * `bootstrap_mode`: set when bootstrapping a host
    * `inform_mode`, `verbose_mode`, `debug_mode`: log verbosity levels in order of noisiness
    * `opt_dry_run`: set when the `--dry-run` option is given
    * `failsafe_fallback`: set when the base policy is invalid and the built-in `failsafe.cf` (see `bootstrap.c`) is invoked
    * (`community`, `community_edition`) and (`enterprise`, `enterprise_edition`): the two different CFEngine products, Community and Enterprise, can be distinguished by these mutually exclusive sets of hard classes
* Operating System Classes (note that the presence of these classes doesn't imply platform support)
    * Operating System Architecture -  `arista`, `big_ip`, `debian`, `eos`, `fedora`, `Mandrake`, `Mandriva`, `oracle`, `redhat`, `slackware`, `smartmachine`, `smartos`, `solarisx86`, `sun4`, `SuSE`, `ubuntu`, `ultrix`, the always-favorite `unknown_ostype`, etc.
    * VM or hypervisor specific: `VMware`, `virt_guest_vz`, `virt_host_vz`, `virt_host_vz_vzps`, `xen`, `xen_dom0`, `xen_domu_hv`, `xen_domu_pv`, `oraclevmserver`, etc.
    * On Solaris-10 systems, the zone name (in the form `zone_global, zone_foo, zone_baz`).
    * Windows-specific: `DomainController`, `Win2000`, `WinServer`, `WinServer2003`, `WinServer2008`, `WinVista`, `WinWorkstation`, `WinXP`
    * `have_aptitude`, `powershell`: based on the detected capabilities of the platform or the compiled-in options
    * **See also:** `sys.arch`, `sys.class`, `sys.flavor`, `sys.os`, `sys.ostype`.
* Network Classes
    * Unqualified Name of Host. CFEngine truncates it at the first dot. 
      Note: `www.sales.company.com` and `www.research.company.com` have the
      same unqualified name – `www`
    * The IP address octets of any active interface (in the form
    `ipv4_192_0_0_1`, `ipv4_192_0_0`, `ipv4_192_0`, `ipv4_192`)
    * User-defined Group of Hosts
    * `mac_unknown`: set when the MAC address can't be found
    * **See also:** `sys.domain`, `sys.hardware_addresses`, `sys.sys.host`, `sys.interface`, `sys.interfaces`, `sys.interface_flags`, `sys.ipv4`, `sys.ip_addresses`, `sys.fqhost`, `sys.uqhost`.
* Time Classes
    * note ALL of these have a local and a GMT version.  The GMT classes are consistent the world over, in case you need global change coordination.
    * Day of the Week - `Monday, Tuesday, Wednesday,...GMT_Monday, GMT_Tuesday, GMT_Wednesday,...`
    * Hour of the Day in Current Time Zone - `Hr00, Hr01,... Hr23` and `Hr0, Hr1,... Hr23`
    * Hour of the Day in GMT - `GMT_Hr00, GMT_Hr01, ...GMT_Hr23` and `GMT_Hr0, GMT_Hr1, ...GMT_Hr23`.
    * Minutes of the Hour - `Min00, Min17,... Min45,...` and `GMT_Min00, GMT_Min17,... GMT_Min45,...`
    * Five Minute Interval of the Hour - `Min00_05, Min05_10,... Min55_00` and `GMT_Min00_05, GMT_Min05_10,... GMT_Min55_00`.  Note the second number indicates *up to* what minute the interval extends and does not include that minute.
    * Quarter of the Hour - `Q1, Q2, Q3, Q4` and `GMT_Q1, GMT_Q2, GMT_Q3, GMT_Q4`
    * An expression of the current quarter hour - `Hr12_Q3` and `GMT_Hr12_Q3`
    * Day of the Month - `Day1, Day2,... Day31` and `GMT_Day1, GMT_Day2,... GMT_Day31`
    * Month - `January, February,... December` and `GMT_January, GMT_February,... GMT_December`
    * Year - `Yr1997, Yr2004` and `GMT_Yr1997, GMT_Yr2004`
    * Period of the Day - `Night, Morning, Afternoon, Evening` and `GMT_Night, GMT_Morning, GMT_Afternoon, GMT_Evening` (six hour blocks starting at 00:00 hours).
    * Lifecycle Index - `Lcycle_0, Lcycle_1, Lcycle_2` and `GMT_Lcycle_0, GMT_Lcycle_1, GMT_Lcycle_2` (the year number modulo 3, used in long term resource memory).
    * **See also:** `sys.cdate`, `sys.date`.

-   The unqualified name of a particular host (e.g., `www`). If
    your system returns a fully qualified domain name for your host
    (e.g., `www.iu.hio.no`), CFEngine will also define a hard class for
    the fully qualified name, as well as the partially-qualified
    component names `iu.hio.no`, `hio.no`, and `no`.
    * **See also:** `sys.fqhost`, `sys.uqhost`.
-   An arbitrary user-defined string (as specified in the `-D`
    command line option, or defined in a `classes` promise or body,
    `restart_class` in a `processes` promise, etc).
-   The IP address octets of any active interface (in the form
    `ipv4_192_0_0_1<!-- /@w -->`, `ipv4_192_0_0<!-- /@w -->`,
    `ipv4_192_0<!-- /@w -->`, `ipv4_192<!-- /@w -->`), provided they
    are not excluded by a regular expression in the file
    `WORKDIR/inputs/ignore_interfaces.rx`.
-   The names of the active interfaces (in the form
    `net_iface_xl0`, `net_iface_vr0`).
-   System status and entropy information reported by
    `cf-monitord`.

## Soft Classes

The following classes can be set via 

    $ cf-agent -Dclass

or

    $ cf-runagent -Dclass
    
to change the behavior of CFEngine without having to edit the policy.

*Note*: Classes, once defined, will stay defined either for as long as the
bundle is evaluated (for classes with a `bundle` scope) or until the agent
exits (for classes with a `namespace` scope). See `cancel_kept`,
`cancel_repaired`, and `cancel_notkept` in classes body.

### persistent\_disable\_*DAEMON*

**Description:** Disable a CFEngine Enterprise daemon component persistently.

`DAEMON` can be one of `cf_execd`, `cf_monitord` or `cf_serverd`.

This will stop the AGENT from starting automatically.

### clear_persistent\_disable\_*DAEMON*

**Description:** Re-enable a previously disabled CFEngine Enterprise daemon 
component.

`DAEMON` can be one of `cf_execd`, `cf_monitord` or `cf_serverd`.

