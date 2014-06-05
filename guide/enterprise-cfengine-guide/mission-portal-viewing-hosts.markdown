---
layout: default
title: Viewing Hosts in Mission Portal
sorting: 100
published: true
tags: [overviews, mission portal, hosts]
---

## Host App ##

CFEngine collects data on `promise` compliance. `Hosts` are then sorted into three different groups: erroneous, fully compliant, and lacking data.

    A `host` is considered erroneous if less than 100% of its `promises` were kept.
    A `host` is considered fully compliant if 100% of its `promises` were kept.
    A `host` is considered lacking data either if the `hub` is not able to connect to it within a set time interval (unreachable `host`). The time interval can be set in `Mission Portal` Settings.
    Or a `host` is considered lacking data if the `policy` did not get executed for the last three runs. This could be caused by `cf-execd` not running on the `host` (scheduling deviation) or an error in `policy` that stops its execution. The `hub` is still able to contact the `host`, but it will return stale data because of this deviation.

You can look at a specific sub-set of your `hosts` by selecting a category from the menu on the left.

### Events ###

A `tracker` represents an easy way to monitor specific `promises` or trace the impact of `policy` changes and roll outs at a detailed level. Choose between three types of `tracker`:

    `Promises` not kept: Lists unkept `promises` as they happen
    `Promises` repaired: List repaired `promises` as they happen
    `Classes`: List the `hosts` that satisfy the selected `class`

You have to specify a `promise handle` or `class` (or pattern in `promise handle`/`class`) to watch in order to avoid flooding the `tracker` with too much data. Also select a start time to identify the time interval that you are interested in.

### Host Info ###

Here you will find extensive information on single `hosts` that CFEngine detects automatically in your environment. Since this is data gathered per `host`, you need to select a single `host` from the menu on the left first.



