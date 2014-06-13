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

<!--- Commenting this out for now, as it is duplicated in the more detailed
      README file included here.

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

-->

[%CFEngine_include_markdown(masterfiles/README.md, .+Setting up, .+Contributing)%]


## cf_promises_validated


Several CFEngine components that read policy (e.g. `cf-agent`, `cf-execd`, `cf-serverd`) run `cf-promises` to validate the syntax of their input files before actually running the policy. To illustrate this, if `cf-promises` runs every 5 minutes then there will be 12 checks occurring every hour, 24 hours a day, 7 days a week -- a total of 2016 possible validation checks. Each of those individual validation sessions can take some number of seconds to perform depending on the system, scale, circumstances and configuration.

Starting with CFEngine 3.1.2, the outcome of every run of `cf-promises` was cached, which lets agents skip the validation of input files that have not changed since the previous run. 

Starting with CFEngine 3.6.0 outcome on both hosts and hubs is stored in the file `$(sys.workdir)/masterfiles/cf_promises_validated` (usually `sys.workdir` is `/var/cfengine`). The file can be created by `cf-agent` after it has successfully verified the policy with `cf-promises`. The file can also be created by a user with `cf-promises -T DIRECTORY` which is useful for validating an entire directory.

When the hash content of any file under `WORKDIR/inputs` changes, and validates to be syntactically correct, then a timestamp in `cf_promises_validated` is updated. If not, the run of `cf-promises` is skipped and, at the same time, the cf-execd, cf-serverd and cf-monitord daemons will not reload the `policy` unless `cf_promises_validated` has an updated timestamp, which `cf-agent` will normally take care of.

In the default installation, the masterfiles are populated
automatically on the policy server and you can even auto-deploy them
from a [version control system][Version Control].

You should configure the masterfiles as described below. Leaving them
at their default settings may expose your masterfiles or worse,
especially the cf-serverd ACL settings. If you are not sure of the
terms used below or what it all means, come back after you've learned
about writing policy and the CFEngine syntax.