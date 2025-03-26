---
layout: default
title: Agent output email
published: true
sorting: 90
---

## How do I set the email where agent reports are sent?

The agent report email functionality is configured in `body executor control` ([find in GitHub](https://github.com/search?q=repo%3Acfengine%2Fmasterfiles+mail+path%3A**%2Fcf_execd.cf&type=code)).
It defaults to `root@$(def.domain)` which is configured in `bundle common def` ([find in GitHub](https://github.com/search?q=repo%3Acfengine%2Fmasterfiles+%22mailto%22+path%3A**%2Fdef.cf&type=code)).

**See also:** [`def.mailto`][Masterfiles Policy Framework#mailto].

## How do I disable agent email output?

You can simply remove or comment out the settings.

The Masterfiles Policy Framework will disable agent email when the class
`cfengine_internal_disable_agent_email` available in `controls/def.cf` to
switch on/off agent email.
