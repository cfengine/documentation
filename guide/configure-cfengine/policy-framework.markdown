---
layout: default
title: Policy Framework
published: true
sorting: 40
tags: [manuals, writing policy, policy framework, masterfiles, def.cf, update.cf]
---

The CFEngine policy framework is called the **masterfiles** because
the files live in `/var/cfengine/masterfiles` on the policy server (on
the clients, and note the policy server is typically also a client,
they are cached in `/var/cfengine/inputs`).

In the default Enterprise installation, the masterfiles are populated
automatically on the policy server and you can even auto-deploy them
from a version control system. See
[Version Control and Configuration Policy][Version Control and Configuration Policy].

In the default Community installation, the same masterfiles are
available but there is no out-of-the-box integration with version
control.  See [Version Control][Version Control].

You should configure the masterfiles as described below. Leaving them
at their default settings may expose your masterfiles or worse,
especially the cf-serverd ACL settings. If you are not sure of the
terms used below or what it all means, come back after you've learned
about writing policy and the CFEngine syntax.

[%CFEngine_include_markdown(masterfiles/README.md, .+Setting Up, .+Contributing)%]
