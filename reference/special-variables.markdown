---
layout: default
title: Special Variables
published: true
sorting: 50
tags: [reference, variables]
---

Variables are promises that can be defined in any promise bundle. Users can create their
own [variables][Variables].

To see all of the variables defined on a particular host, run

    $ cf-promises --show-vars

as a privileged user.  See `Classes` for an explanation of the tags.

CFEngine includes the following **special variables**:

* [const][const]
Variables defined for embedding unprintable values or values with special meanings
in strings.

* [edit][edit]
Variables used to access information about editing promises during their execution.

* [match][match]
Variable used in string matching.

* [mon][mon]
Variables defined in a monitoring context.

* [sys][sys]
Variables defined in order to automate discovery of system values.

* [def][def]
Variables with some default value that can be defined by [augments file][Augments] or in policy.

* [this][this]
Variables used to access information about promises during their execution.
