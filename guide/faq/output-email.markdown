---
layout: default
title: Agent output email
published: true
sorting: 90
tags: [getting started, installation, faq]
---

# How do I set the email where agent reports are sent?

The agent report email functionality is configured in `body executor control`
https://github.com/cfengine/masterfiles/blob/{{site.cfengine.branch}}/controls/cf_execd.cf.
It defaults to `root@$(def.domain)` which is configured in `bundle common def`
https://github.com/cfengine/masterfiles/blob/{{site.cfengine.branch}}/def.cf.

**See Also:** [`def.mailto`][The Policy Framework#mailto (variable)],
[`def.domain`][The Policy Framework#domain (variable)].

# How do I disable agent email output?

You can simply remove or comment out the settings.

The Masterfiles Policy Framework will disable agent email when the class
`cfengine_internal_disable_agent_email` available in `bundle common def` to
switch on/off agent email.

For details see
[cfengine_internal_agent_email][The Policy Framework#cfengine_internal_agent_email (class)].
