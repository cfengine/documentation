---
layout: default
title: Controlling frequency
published: true
sorting: 90
---

By default CFEngine runs relatively frequently (every 5 minutes) but you may not
want every promise to be evaluated each agent execution. Classes and promise
locks are the two primary ways in which a promises frequency can be controlled.
Classes are the canonical way of controlling if a promise is in context and
should be evaluated. Promise locks control frequency based on the number of
minutes since the last promise actuation.

## Controlling frequency using classes

Classes are the canonical way of controlling promise executions in CFEngine.

Use time based classes to restrict promises to run during a specific period of time. For example, here `sshd` promises to be the latest version available, but only on Tuesdays during the first 15 minutes of the 5:00 hour.

```cf3
bundle agent __main__
{
  packages:
    Tuesday.Hr05_Q1::
    "sshd"
      version => "latest",
      comment => "Make sure sshd is at the latest version, but only Tuesday between 5:00 and 5:15am";
}
```

Persistent classes can exist for a period of time, across multiple executions of
`cf-agent`. Persistent classes can be used to avoid re-execution of a promise.
For example, here `/tmp/heartbeat.dat` promises to update it's timestamp when
`heartbeat_repaired` is not defined. When the file is repaired the class
`heartbeat_repaired` is defined for 10 minutes causing the promise to be out of
context during subsequent executions for the next 10 minutes.

```cf3
bundle agent __main__
{
  files:
    !heartbeat_repaired::
      "/tmp/heartbeat.dat"
        create => "true",
        touch => "true",
        classes => persistent_results( "heartbeat", 10 );
}
body classes persistent_results( prefix, time )
{
    inherit_from => results( "namespace", "$(prefix)" );
    persist_time => "$(time)";
}
```

## Controlling frequency using promise locks

CFEngine incorporates a series of locks which prevent it from checking
promises too often, and which prevent it from spending too long trying to
check promises it has recently verified. This locking mechanism works in such
a way that you can start several CFEngine components simultaneously without
them interfering with each other. You can control two things about each kind
of action in CFEngine:

* `ifelapsed` - The minimum time (in minutes) which should have passed since the
  last time that promise was verified. It will not be executed again until this
  amount of time has elapsed. If the value is `0` the promise has no lock and
  will always be executed when in context. Additionally, a value of `0` disables
  function caching. Default time is `1` minute.

* `expireafter` - The maximum amount (in minutes) of time `cf-agent` should wait
  for an old instantiation to finish before killing it and starting again. You
  can think about [`expireafter`][cf-agent#expireafter] as a timeout to use when
  a promise verification may involve an operation that could wait indefinitely.
  Default time is `120` minutes.

You can set these values either globally (for all actions) or for each action
separately. If you set global and local values, the local values override the
global ones. All times are written in units of minutes. The following global
setting is defined in `body agent control`.

```cf3
body agent control
{
    ifelapsed => "60";	# one hour
}
```

This setting tells CFEngine not to verify promises until 60 minutes have
elapsed, ie ensures that the global frequency for all promise verification is
one hour. This global setting of one hour could be changed for a specific
promise body by setting [`ifelapsed`][Promise types#ifelapsed] in the promise body.

```cf3
body action example
{
    ifelapsed => "90";	# 1.5 hours
}
```

This promise which overrides the global 60 minute time period and defines a
frequency of 90 minutes.

These locks do not prevent the whole of `cf-agent` from running, only
atomic promise checks on the same objects (packages, users, files,
etc.). Several different `cf-agent` instances can run concurrently.
The locks ensure that promises will not be verified by two cf-agents
at the same time or too soon after a verification.

For example, here the `sshd` package promises to be at the latest version. It
has the `if_elapsed_day` action body attached which sets `ifelapsed` to `1440`
causing the promise lock to persist for a day effectively restricting the
promise to run just once a day.

```cf3
bundle agent __main__
{
  packages:
    "sshd"
      version => "latest",
      action => if_elapsed_day,
      comment => "Make sure sshd is at the latest version, but just once a day.";
}
```

Note: Promise locks are ignored when CFEngine is run with the `--no-lock` or
`-K` option, e.g. a common **manual** execution of the agent, `cf-agent -KI`
would not respect promises that are locked from a recent execution. Furthermore,
locks are purged in order to maintain the integrity and health of the underlying
lock database.

**See also:** [cf_lock.lmdb][CFEngine directory structure#state/cf_lock.lmdb]
