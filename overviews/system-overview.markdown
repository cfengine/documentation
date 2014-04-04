---
layout: default
title: System Overview
sorting: 2
published: true
tags: [overviews, system overview]
---

## What Does a CFEngine System Look Like? 

### Server vs. Client Host ###

See Also: [Policy Server Overview][Policy Server Overview]

### Files ###

[cf_promises_validated][cf_promises_validated]

### The CFEngine Applications and Daemons ###

CFEngine consists of a number of applications that help manage policies and machines within the overall system.

#### Daemons ####

All machines, whether they are policy servers or hosts, will have these three important daemons running at all times:

[/var/cfengine/bin/cf-execd](#cf-execd)
[/var/cfengine/bin/cf-serverd](#cf-serverd)
[/var/cfengine/bin/cf-monitord](#cf-monitord)

#### Other Applications ####

[/var/cfengine/bin/cf-agent](#cf-agent)
[/var/cfengine/bin/cf-key](#cf-key)
[/var/cfengine/bin/cf-promises](#cf-promises)
[/var/cfengine/bin/cf-runagent](#cf-runagent)
[/var/cfengine/bin/cf-upgrade](#cf-upgrade)
[/var/cfengine/bin/cf-twin](#cf-twin)
[/var/cfengine/bin/lmdump](#lmdump)
[/var/cfengine/bin/mdb_stat](#mdb_stat)
[/var/cfengine/bin/getfacl](#getfacl) 
[/var/cfengine/bin/mdb_copy](#mdb_copy)
[/var/cfengine/bin/rpmvercmp](#rpmvercmp)

#### cf-execd ####

cf-execd is the scheduling daemon for cf-agent. It runs cf-agent locally according to a schedule specified in policy code (executor control body). After a cf-agent run is completed, cf-execd gathers output from cf-agent, and may be configured to email the output to a specified address. It may also be configured to splay (randomize) the execution schedule to prevent synchronized cf-agent runs across a network.

cf-execd keeps the promises made in common bundles, and is affected by common and executor control bodies.

See also: [cf-execd][cf-execd] reference documentation.

#### cf-serverd ####

cf-serverd is a socket listening daemon providing two services: it acts as a file server for remote file copying and it allows an authorized cf-runagent to start a cf-agent run. cf-agent typically connects to a cf-serverd instance to request updated policy code, but may also request additional files for download. cf-serverd employs role based access control (defined in policy code) to authorize requests.

cf-serverd keeps the promises made in common and server bundles, and is affected by common and server control bodies.

See also: [cf-serverd][cf-serverd] reference documentation.

#### cf-monitord ####

cf-monitord is the monitoring daemon for CFEngine. It samples probes defined in policy using measurements type promises and attempts to learn the normal system state based on current and past observations. Current estimates are made available as special variables (e.g. $(mon.av_cpu)) to cf-agent, which may use them to inform policy decisions.

cf-monitord keeps the promises made in commonand monitor bundles, and is affected by common and monitor control bodies.

See also: [cf-monitord][cf-monitord] reference documentation.


#### cf-agent ####

cf-agent evaluates policy code and makes changes to the system. Policy bundles are evaluated in the order of the provided bundlesequence (this is normally specified in the common control body). For each bundle, cf-agent groups promise statements according to their type. Promise types are then evaluated in a preset order to ensure fast system convergence to policy.

cf-agent keeps the promises made in common and agent bundles, and is affected by common and agent control bodies.

See also: [cf-agent][cf-agent] reference documentation.
 
#### cf-key ####

The CFEngine key generator makes key pairs for remote authentication.

See also: [cf-key][cf-key] reference documentation.
    
#### cf-promises ####

cf-promises is a tool for checking CFEngine policy code. It operates by first parsing policy code checking for syntax errors. Second, it validates the integrity of policy consisting of multiple files. Third, it checks for semantic errors, e.g. specific attribute set rules. Finally, cf-promises attempts to expose errors by partially evaluating the policy, resolving as many variable and classes promise statements as possible. At no point does cf-promises make any changes to the system.

In 3.6.0 and later, cf-promises will not evaluate function calls either. This may affect customers who use execresult for instance. Use the new --eval-functions yes command-line option (default is no) to retain the old behavior from 3.5.x and earlier.

See also: [cf-promises][cf-promises] reference documentation.
 
#### cf-runagent ####

cf-runagent connects to a list of running instances of cf-serverd. It allows foregoing the usual cf-execd schedule to activate cf-agent. Additionally, a user may send classes to be defined on the remote host. Two kinds of classes may be sent: classes to decide on which hosts cf-agent will be started, and classes that the user requests cf-agent should define on execution. The latter type is regulated by cf-serverd's role based access control.

See also: [cf-runagent][cf-runagent] reference documentation.

#### cf-upgrade ####
 
#### cf-twin ####

#### lmdump ####
  
#### mdb_stat ####
    
#### getfacl ####
    
#### mdb_copy ####
 
#### rpmvercmp ####


