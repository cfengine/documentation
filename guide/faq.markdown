---
layout: default
title: FAQ
published: true
sorting: 5
tags: [getting started, installation, enterprise, faq]
---

* [Enterprise Installation](#enterprise-installation)
* [Enterprise Scalability](#enterprise-scalability)

### Enterprise Installation ###

#### Can I use an existing PostgreSQL installation? ####

Although CFEngine keeps its assumptions about Postgres to a bare minimum, CFEngine should use a dedicated PostgreSQL database instance to ensure there is no conflict with an existing installation.

#### What is the system user for the CFEngine dedicated PostgreSQL database?

Starting with CFEngine 3.6.0 there will be a system user called ```cfpostgres``` for running the dedicated CFEngine PostgreSQL database installation. 

#### Do I need experience with PostgreSQL? ####

PostgreSQL is highly configurable, and you should have some in-house expertise to properly configure your database installation. 

### Enterprise Scalability ###

### Policy Distribution ###

#### I  have added new files in masterfiles but my remote clients are not getting updates. ####

Check that the files you expect to be distributed have matching leaf_name pattern.

In CFEngine 3.6 masterfiles policy framework this is defined as
`input_name_patterns` in the `update_def` bundle.

#### I have updated some non policy files (for example templates) and changes are not distributed to clients. ###

`cf_promises_validated` gates client updates. This file is only updated on the
policy server when new policy is validated. Edits to non policy files do not
trigger an update of `cf_promises_validated`. You can use a seperate promise to
ensure those files are continually distributed, instead of only on policy
updates.

### Manual Execution ###

#### How do I run a standalone policy file? ####

```console
cf-agent -f ./my_standalone_policy.cf
```

#### How do I run a specific bundle? ####

```console
cf-agent -b my_bundle
```

#### How do I define a class for a single run? ####

```console
cf-agent -D my_class
```
