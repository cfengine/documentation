---
layout: default
title: Why are remote agents not updating?
published: true
sorting: 90
tags: [getting started, installation, faq, cf_promises_validated ]
---

The [masterfiles policy framework][Masterfiles Policy Framework] defaults to using
`cf_promises_validated` as a simple gating mechanism for policy updates. This
gating mechanism helps in avoiding the distribution of broken policy to clients
as well as reducing the burden on the policy server during times policy is not
changing.

The `$(sys.masterdir)/cf_promises_validated` is created by `cf-agent` or any
other CFEngine component after **new** policy in `$(sys.inputdir)` has been
validated.

By default (in the masterfiles policy framework) non policy servers only trigger
a fully policy scan when `$(sys.inputdir)/cf_promises_validated` is repaired.

By default (in the masterfiles policy framework) policy servers always pull all
policy changes to `$(sys.inputdir)`. If the policy successfully validates then
`$(sys.masterdir)/cf_promises_validated` is updated, and remote agents will
update their policy when they notice that change. If the policy does not
validate `$(sys.masterdir)/cf_promises_validated` is not updated, and remote
clients will see no need to scan for updates.

* Check that the policy on in `$(sys.masterdir)` on the hub validates with
  `cf-promises`.
* Check if `$(sys.inputdir)/cf_promsies_validated` differs from the
  `$(sys.masterdir)/cf_promises_validated` on the policy server.
* Trigger a full policy scan with `cf-agent --no-lock --file update.cf --define
  validated_updates_ready`

**Note:** Dynamic inputs could mean different validation results on different
hosts. Be conscious of different perspectives when validating policy.
