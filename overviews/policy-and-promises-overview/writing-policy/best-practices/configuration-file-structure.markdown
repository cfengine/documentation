---
layout: default
title: Default Configuration File Structure
published: true
sorting: 40
tags: [manuals, systems, configuration management, automation, policy, failsafe, update, file system]
---

<!---
**TODO: include some extracts, or link to github**
**TODO: Documentation for default policy layout/structure including 
cf_promises_validated and update mechanism**
-->

The following configuration files are part of the default CFEngine 
installation in `/var/cfengine/inputs`, and have special roles.

## promises.cf

This file is the first file that `cf-agent` with no arguments will try to look 
for. It should contain all of the basic configuration settings, including a 
list of other files to include. In normal operation, it must have a 
`bundlesequence`.

This file can stay fixed, except for extending the `bundlesequence`. The 
`bundlesequence` acts like the 'genetic makeup' of the configuration. In a 
large configuration, you might want to have a different `bundlesequence` for 
different classes of host, so that you can build a complete system like a 
check-list from different combinations of building blocks. You can construct 
different lists by composing them from other lists, or you can use methods 
promises as an alternative for composing bundles for different classes.

## update.cf

This file should rarely if ever change. Should you ever change it (or when you 
upgrade CFEngine), take special care to ensure the old and the new CFEngine 
can parse and execute this file successfully. If not, you risk losing control 
of your system (that is, if CFEngine cannot successfully execute this set of 
promises, it has no mechanism for distributing new policy files).

By default, the policy defined in update.cf is executed from two sets of 
promise bodies. The "usual" one (defined in the `bundlesequence` in 
`promises.cf`) and another in the backup/failsafe `bundlesequence` (defined in 
`failsafe.cf`).

## failsafe.cf

This file is generated during the bootstrapping process, and should probably 
never be changed. The only job of failsafe.cf is to execute the update bundle 
in a “standalone” context should there be a syntax error somewhere in the main 
set of promises. In this way, if a client machine's policies are ever 
corrupted after downloading erroneous policy from a server, that client will 
have a failsafe method for downloading a corrected policy once it becomes 
available on the server. Note that by “corrupted” and “erroneous” we typically 
mean “broken via administrator error” - mistakes happen, and the failsafe.cf 
file is CFEngine's way of being prepared for that eventuality.

If you ever change failsafe.cf (or when you upgrade CFEngine), make sure the 
old and the new CFEngine can successfully parse and execute this file. If not, 
you risk losing control of your system (that is, if CFEngine cannot 
successfully execute this policy file, it has no failsafe/fallback mechanism 
for distributing new policy files).

The failsafe.cf file is to make sure that your system can upgrade gracefully 
to new versions even when mistakes are made.


As a general rule:

* Upgrade the software first, then add new features to the configuration.
* Never use advanced features in the failsafe or update file.
* Avoid using library code (including any bodies from cfengine_stdlib.cf). 
Copy/paste any bodies you need using a unique name that does not collide with 
a name in library (we recommend simply adding the prefix “u_”). This may mean 
that you create duplicate functionality, but that is okay in this case to 
ensure a 100% functioning standalone update process). The promises which 
manage the update process should not have any dependencies on any other files.

A CFEngine configuration will fail-over to the failsafe.cf configuration if it 
is unable to read or parse the contents successfully. That means that any 
syntax errors you introduce (or any new features you utilize in a 
configuration) will cause a fail-over, because the parser will not be able to 
interpret the policy. If the failover is due to the use of new features, they 
will not parse until the software itself has been updated (so we recommend 
that you always update CFEngine before updating policy to use new features). 
If you accidentally cause a bad (i.e., unparseable) policy to be distributed 
to client machines, the `failsafe.cf` policy on those machines will run (and 
will eventually download a working policy, once you fix it on the policy 
host).

