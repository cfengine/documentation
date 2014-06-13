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

[%CFEngine_include_markdown(masterfiles/README.md, .+Setting up, .+Contributing)%]

## cf_promises_validated

Several CFEngine components that read policy (e.g. `cf-agent`,
`cf-execd`, `cf-serverd`) run `cf-promises` to validate the syntax of
their input files before actually running the policy. To illustrate
this, if `cf-promises` runs every 5 minutes then there will be 12
checks occurring every hour, 24 hours a day, 7 days a week -- a total
of 2016 possible validation checks. Each of those individual
validation sessions can take some number of seconds to perform
depending on the system, scale, circumstances and configuration.

Starting with CFEngine 3.1.2, the outcome of every run of
`cf-promises` was cached, which lets agents skip the validation of
input files that have not changed since the previous run.

Starting with CFEngine 3.6.0 outcome on both hosts and hubs is stored
in the file `$(sys.workdir)/masterfiles/cf_promises_validated`
(usually `sys.workdir` is `/var/cfengine`). The file can be created by
`cf-agent` after it has successfully verified the policy with
`cf-promises`. The file can also be created by a user with
`cf-promises -T DIRECTORY` which is useful for validating an entire
directory.

When the hash content of any file under `WORKDIR/inputs` changes, and
validates to be syntactically correct, then a timestamp in
`cf_promises_validated` is updated. If not, the run of `cf-promises`
is skipped and, at the same time, the cf-execd, cf-serverd and
cf-monitord daemons will not reload the `policy` unless
`cf_promises_validated` has an updated timestamp, which `cf-agent`
will normally take care of.

In the default installation, the masterfiles are populated
automatically on the policy server and you can even auto-deploy them
from a [version control system][Version Control].

You should configure the masterfiles as described above. Leaving them
at their default settings may expose your masterfiles or worse,
especially the cf-serverd ACL settings. If you are not sure of the
terms used below or what it all means, come back to this page after
you've learned about writing policy and the CFEngine syntax.

[%CFEngine_include_markdown(masterfiles/inventory/README.md)%]
