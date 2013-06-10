---
layout: default
title: Classes 
categories: [Reference, Classes]
published: true
sorting: 40
alias: reference-classes.html
tags: [reference, hard classes, soft classes, classes]
---

[Classes](manuals-language-concepts-classes.html) fall into **hard**
(discovered) and **soft** (defined) types. This reference documents the hard 
classes that might be set by CFEngine, and soft classes used by CFEngine's 
default policy.

## Listing Classes

To see all of the classes defined on a particular host, run

    $ cf-promises -v

as a privileged user. Note that some of the classes are set only if a trusted 
link can be established with 
[`cf-monitord`](reference-components-cfmonitord.html), i.e. if both are 
running  with privilege, and the `/var/cfengine/state/env_data` file is 
secure.

You can use
https://github.com/cfengine/design-center/tree/master/tools/hcgrep to
obtain this list in a format suitable for other tools like `grep` (one
class per line).

You can also use the built-in `classesmatching` function to get a list
of all the defined classes in a list, inside CFEngine policy itself.

## Hard Classes

* Operating System Classes
    * Operating System Architecture - `ultrix, sun4`, etc.
* Network Classes
    * Unqualified Name of Host. CFEngine truncates it at the first dot. 
      Note: `www.sales.company.com` and `www.research.company.com` have the
      same unqualified name – `www`
    * The IP address octets of any active interface (in the form
    `ipv4_192_0_0_1`, `ipv4_192_0_0`, `ipv4_192_0`, `ipv4_192`)
    * User-defined Group of Hosts
* Time Classes
    * Day of the Week - `Monday, Tuesday, Wednesday,...`
    * Hour of the Day in Current Time Zone - `Hr00, Hr01,... Hr23`
    * Hour of the Day in GMT - `GMT_Hr00, GMT_Hr01, ...GMT_Hr23`
    * Minutes of the Hour - `Min00, Min17,... Min45`
    * Five Minute Interval of the Hour - `Min00_05, Min05_10,... Min55_00`
    * Quarter of the Hour - `Q1, Q2, Q3, Q4`
    * Day of the Month - `Day1, Day2,... Day31`
    * Month - `January, February,... December`
    * Year - `Yr1997, Yr2004`
    * Period of the Day - `Night, Morning, Afternoon, Evening` (six hour
      blocks starting at 00:00 hours).


-   The name of an operating system architecture e.g. `ultrix`,
    `sun4`, etc.
-   The unqualified name of a particular host (e.g., `www`). If
    your system returns a fully qualified domain name for your host
    (e.g., `www.iu.hio.no`), CFEngine will also define a hard class for
    the fully qualified name, as well as the partially-qualified
    component names `iu.hio.no`, `hio.no`, and `no`.
-   The name of a user-defined group of hosts.
-   A day of the week (in the form
    `Monday, Tuesday, Wednesday, ..`).
-   An hour of the day, in the current time zone (in the form
    `Hr00, Hr01 ... Hr23`).
-   An hour of the day GMT (in the form
    `GMT_Hr00, GMT_Hr01 ... GMT_Hr23`). This is consistent the world
    over, in case you need virtual simulteneity of change coordination.
-   Minutes in the hour (in the form `Min00, Min17 ... Min45`).
-   A five minute interval in the hour (in the form
    `Min00_05, Min05_10 ... Min55_00`).
-   A fifteen minute (quarter-hour) interval (in the form
    `Q1, Q2, Q3, Q4`).
-   An expression of the current quarter hour (in the form
    `Hr12_Q3`).
-   A day of the month (in the form `Day1, Day2, ... Day31`).
-   A month (in the form `January, February, ... December`).
-   A year (in the form `Yr1997, Yr2004`).
-   A shift in `Night,Morning,Afternoon,Evening`, which fall into
    six hour blocks starting at 00:00 hours.
-   A 'lifecycle index', which is the year number modulo 3 (in the
    form `Lcycle_0, Lcycle_1, Lcycle_2`, used in long term resource
    memory).
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
-   On Solaris-10 systems, the zone name (in the form
    `zone_global, zone_foo, zone_baz`).

## Soft Classes

The following classes can be set via 

    $ cf-agent -Dclass

or

    $ cf-runagent -Dclass
    
to change the behavior of CFEngine without having to edit the policy.

### persistent\_disable\_*DAEMON*

**Description**: Disable a CFEngine Enterprise daemon component persistently.

`DAEMON` can be one of `cf_execd`, `cf_monitord` or `cf_serverd`.

This will stop the AGENT from starting automatically.

### clear_persistent\_disable\_*DAEMON*

**Description**: Re-enable a previously disabled CFEngine Enterprise daemon 
component.

`DAEMON` can be one of `cf_execd`, `cf_monitord` or `cf_serverd`.

