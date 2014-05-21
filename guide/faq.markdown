---
layout: default
title: FAQ
published: true
sorting: 6
tags: [getting started, installation, enterprise, faq]
---

* [Enterprise Installation](#enterprise-installation)
* [Enterprise Scalability](#enterprise-scalability)

### Enterprise Installation ###

#### Can I use an existing PostgreSQL installation? ####

Although CFEngine keeps its assumptions about Postgres to a bare minimum,
CFEngine should use a dedicated PostgreSQL database instance to ensure there is
no conflict with an existing installation.

#### What is the system user for the CFEngine dedicated PostgreSQL database?

Starting with CFEngine 3.6.0 there will be a system user called ```cfpostgres``` for running the dedicated CFEngine PostgreSQL database
installation.

#### Do I need experience with PostgreSQL? ####

PostgreSQL is highly configurable, and you should have some in-house expertise
to properly configure your database installation.

### Enterprise Scalability ###

### Policy Distribution ###

#### I  have added new files in masterfiles but my remote clients are not getting updates. ####

Check that the files you expect to be distributed have matching `leaf_name` pattern.

In CFEngine 3.6 masterfiles policy framework this is defined as
`input_name_patterns` in the `update_def` bundle.

#### I have updated some non policy files (for example templates) and changes are not distributed to clients. ###

`cf_promises_validated` gates client updates. This file is only updated on the
policy server when new policy is validated. Edits to non policy files do not
trigger an update of `cf_promises_validated`. You can use a seperate promise to
ensure those files are continually distributed, instead of only on policy
updates.

For details reference
[update/update_policy.cf](https://github.com/cfengine/masterfiles/blob/master/update/update_policy.cf).

### Manual Execution ###

#### How do I run a standalone policy file? ####

The `--file` or `-f` option to `cf-agent` specifys the policy file to be used as the
main entry point. The `-K` or `--no-lock` flag and the `-I` or `--inform`
options are commonly used in combination with the `-f` option to ensure that
all promises are skipped because of locking and for the agent to produce
informational output like successful repairs.

```console
cf-agent -KIf ./my_standalone_policy.cf
```

#### How do I run a specific bundle? ####

A specific bundle can be activated by passing the `-b` or `--bundlesequence`
options to `cf-agent`. This may be used to activate a specific bundle within a
large policy set or to run a standalone policy that does not include a `body
common control`.

```console
cf-agent -b my_bundle
```

If you want to activate multiple bundles in a sequence simply seperate them
with commas (no spaces between).

```console
cf-agent --bundlesequence bundle1,bundle2
```

#### How do I define a class for a single run? ####

You can use the `--define` or `-D` options of `cf-agent`.

```console
cf-agent -D my_class
```

And if you want to define multiple, simply seperate them with commas (no spaces between).

```console
cf-agent --define my_class,my_other_class
```

### Agent Email Reports ###

#### How do I set the email where agent reports are sent? ####

The agent report email functionality is configured in `body executor control`
https://github.com/cfengine/masterfiles/blob/master/controls/cf_execd.cf. It
defaults to `root@$(def.domain)` which is configured in `bundle common def`
https://github.com/cfengine/masterfiles/blob/master/def.cf.

### How do I disable agent email output? ###

You can simply remove or comment out the settings.

In 3.6.x there is a conveniance class `cfengine_internal_agent_email` avaiable
in `bundle common def` to switch on/off agent email.
