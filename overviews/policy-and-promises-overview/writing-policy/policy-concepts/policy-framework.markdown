---
layout: default
title: Policy Framework
published: true
sorting: 20
tags: [manuals, masterfiles, policy, framework]
---

The policy framework (master files) for CFEngine is located in the /var/cfengine/masterfiles directory on
the Policy Server. When Hosts (clients) are bootstrapped, they can pull policy from the 
master files in order to locally store and run them. 

Below is a brief description of the  default master files that you receive with a new install. 
Keep the master files updated with every new CFEngine release. 

## Files
### def.cf

This file contains common/global settings such as variables and classes. It lists the acl 
settings, or which servers are allowed to connect to your policy server. It contains other
settings to purge policies that don't exist, encrypt the transfer of policies, or to do a 
log rotation.

**Tip:** Make certain that the Hosts that are connecting to your policy server are included 
in the acl list.

### promises.cf

This file contains the basic CFEngine policy; thus, CFEngine loads and executes it by default. 
Every policy file that you want to include 
must be added to the **inputs** (and possibly **bundlesequence**). Add the path to the file 
that contains the policy so that it can be evaluated. If you want it to be executed (such 
as the bundle inside the file), you must either add it to the bundlesequence or add a methods 
promise to call them.

**Tip:** Create a customized promises.cf file and include all of your promises in it. This 
helps to avoid upgrade issues and conflicts in the master file. Add this customized promise 
file to inputs so that it can get evaluated. Add the bundle name to the bundlesequence list.

<!-- This is a good place to add a training slide that shows how cf-agent checkes the 
promises.cf file on the policy server for recent updates. -->

### update.cf

This file contains the basic update policy. It is always evaluated before promises.cf is 
run to ensure that all files are properly updated. Policies that are driven by this file 
are located in the **update** directory. 

## Directories

### bootstrap
This directory contains the policy that's used for bootstrapping. It includes the 
**failsafe.cf** file, which CFEngine uses for recovery if the primary failsafe/update loses 
functionality due to modifications made by the user. This file cannot be edited. 

### cfe_interal
This directory contains Enterprise-related policies that should not be modified.

### controls

This directory contains the controls for each component of the agent:

* **cf_agent.cf** Manages the `cf-agent` component.
* **cf_execd.cf** Controls the execution of CFEngine. Specifically, it includes splaytime settings 
and mail settings for email reports. It also includes the schedule to run the cf-agent and the 
command to run it. 
* **cf_hub.cf** Manages the `cf-hub` component. It 
includes settings for collecting information from Hosts for analysis and reporting purposes. 
This is Enterprise-specific.
* **cf_monitor.cf** Manages the `cf-monitor` component.
* **cf_runagent.cf** Manages the `cf-runagent` component.
The most important parameter is the list of hosts that the agent will poll for connections.
* **cf_serverd.cf** Contains the general IP access policy for the connection protocol (i.e. access 
to the server itself). Access to specific files must also be granted.

### inventory  (New in 3.6)
This directory contains inventory modules that are loaded before anything else in order to 
discover facts about the system.

<!-- Add more later. -->

### lib

This directory contains the 3.5 and 3.6 versions of the Standard Library. The standard library 
contains and extensive amount of commonly-used bundles and bodies that you can use to implement 
different tasks with CFEngine. 

Import individual files from the CFEngine Standard Library into your CFEngine policy as follows:

```cf3
body common control
{
    inputs => { "lib/3.6/common.cf",
                "lib/3.6/files.cf",
                "lib/3.6/commands.cf" };
}
```

The following files make up the Standard Library:

* **bundles.cf** Contains standalone agent bundles that perform common tasks, such as
`fileinfo()` (extract file information using the `filestat()` function) and
`logrotate()` (rotate log files by size).
* **commands.cf** Defines a number of `contain` bodies for use with `commands:` promises.
* **common.cf** Defines bodies that can be used with all promise types, such as `action` and
`classes` bodies.
* **databases.cf** Contains database_server bodies to use with `databases:` promises.
* **feature.cf** NEW in 3.6  
* **files.cf**  Includes all bundles and bodies that can be used with `files:` promises, including
`edit_line` bundles, `edit_field` bodies, `copy_from` bodies, etc.
* **guest_environments.cf**  Includes `environment_resources` bodies to use in defining virtual machines for
`guest_environments:` promises.
* **monitor.cf**  Includes bodies that can be used with `measurements:` promises (only in CFEngine
Enterprise), such as `match_value` bodies.
* **packages.cf**  Includes all `package_method` body definitions, to use with `packages:` promises
to interact with different package and software managers.
* **paths.cf**  Contains the paths common bundle, which defines the paths for many common
system binaries in different operating systems. By using this bundle, you
can make your policies system-independent by avoding hard-coded command
paths.
* **processes.cf**  Includes `process_select` and `process_count` bodies for use with `processes:`
promises.
* **services.cf**  Includes the `standard_services()` bundle, which provides the built-in support
for most common services in different operating systems, and implements the
default behavior of `services:` promises.
* **storage.cf**  storage.cf
Defines `volume` and `mount` bodies to use with `storage:` promises.

Definitions of the Standard Library files provided by 
[Diego Zamboni][[Learning CFEngine 3](http://shop.oreilly.com/basket.do?nav=ext)]. 

### libraries

The directory contains older versions of the Standard Library.

### services

This is the location of user's policy files (the .cf files). Two policies are included:
`init_msg.cf` (initial message display) and `file_change.cf` (change management).

### sketches

This is the location of user's sketches. If you activate a sketch, it goes here. It contains 
the meta/api-runfile.cf file, which calls two bundles:
cfsketch_g Defines common variables that are necessary to execute sketches.
cfsketch_run Executes the sketches.

### update

This directory contains files that drive the update.cf file, or the basic update policy.

* **mongod.conf** Mongo database update information.
* **update_bins.cf** Updates the binaries.
* **update_masterfiles**_internal.cf Updates the masterfiles 
* **update_policy.cf** Copies updates files from /var/cfengine/masterfiles/ on the policy server to 
/var/cfengine/inputs all machines (policy server and hosts).
* **update_processes.cf** Starts tasks that should be running.


<!-- Should I add anything about .gitignore, Makefile, Makefile.am, README? -->