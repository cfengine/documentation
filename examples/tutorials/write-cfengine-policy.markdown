---
layout: default
title: Write cfengine policy
published: true
sorting: 3
tags: [getting started, tutorial]
---

To define new Desired States in CFEngine, you need to write policy files. These are plain text-files, traditionally with a `.cf` extension.

## /var/cfengine/inputs and promises.cf

In CFEngine, `cf-agent` executes all policies. `cf-agent` runs every 5 minutes
by default, and it executes policies found locally in the `/var/cfengine/inputs`
directory. The default policy entry is a file called `promises.cf`. In this file
you normally reference bundles and other policy files.

## Bundles, Promise types, and Classes oh my!

These concepts are core to CFEngine so they are covered in brief here. For more
detailed information see the Language Concepts section of the Reference manual.

### Bundles

Bundles are re-usable and blocks of CFEngine policy. The following defines a *bundle* called `my_test`, and it is a bundle for the agent.

```cf3
bundle agent my_test{..policy-code...}
```

A bundle contains one or more promise types.

### Promise types

Think of a promise type as a way to abstract yourself away from details. For
instance, there is a promise type called users. This promise type allows you to
manage local users on your system. Instead of using low-level commands to manage
users, with the promise type, you only have one simple syntax that works across
all operating systems.

The most frequently used promise types are `vars`, `classes`, `files`,
`packages`, `users`, `services`, `commands` and `reports`. Whenever you want to
do some file configuration for example, you would use the files promise type.
The following policy ensures the existence of the `/tmp/hello-world` file:

```cf3
files:
  "/tmp/hello-world"
    create => "true";
```

When defining desired states it is important to be clear about when and where
you want this policy to apply. For that, CFEngine has the concept of classes.

## Classes

A *class* is an identifier which is used by the agent to decide when and where a
part of a policy shall run. A class can either be user-defined, a so called
soft-class, or it can be a hard class which is automatically discovered and
defined by cf-agent during each run. Popular classes include *any* which means
any or all hosts, *policy_server* which means the host is a policy server. There
are more than 50 hard classes, and combined with regular expressions this gives
you very granular control.

To see a list of available classes on your host, just type the following command:

```console
# cf-promises --show-classes
``` 

## Running policy

Now let's put the bundle, promise type and class components together in a
final policy. As for classes we will use linux to define that the file
`/tmp/hello-world` must exists on all hosts of type *linux*:

```cf3
bundle agent my_test{
 files:
  linux::
   "/tmp/hello-world"
     create => "true";
}
bundle agent __main__
{
  methods: "my_test";
}
```

Let’s save this policy in `/tmp/my-policy.cf`.

You can now run this policy either in Distributed (client-server) System or in a
Stand Alone system. The next two sections will cover each of the options.

## Option#1: Running the Policy on a Stand alone system

Since CFEngine is fully distributed we can run policies locally. This can come
in handy as the result of a run is instant, especially during the design phase
where you would like to test out various policies.

To run the file locally, you can log into any of your hosts that has CFEngine
installed and follow these steps. For this tutorial, use your Policy Server for
this as it is the same cf-agent that runs on the hosts as on the Policy Server.

**Tip:** Whenever you make or modify a policy, you can use the `cf-promises`
command to run a syntax check:

```console
# cf-promises -f /tmp/my-policy.cf
```

Unless you get any output, the syntax is correct. Now, to run this policy, simply type:

```console
# cf-agent -Kf /tmp/my-policy.cf
```

As you can see, the response is immediate! Running CFEngine locally like this is
ideal for testing out new policies. To check that the file has been successfully
created type:

```console
# ls /tmp/hello-world -l
```

If you want to see what the agent is doing during its run, you can run the agent
in verbose mode. Try:

```console
# cf-agent -Kf /tmp/my-policy.cf --verbose
```

In a Stand Alone system, to make and run a policy remember to:

### Option#2: Running the Policy on a Distributed System

CFEngine is designed for large-scale systems. It is fully distributed which
means that all the logic and decision making takes place on the end-points, or
hosts as we call them in CFEngine. The hosts fetch their policies from one
central distribution point. To continue with this option you need to have
CFEngine running on at least one host and one policy server.

The CFEngine Server typically acts as a policy distribution point. On each host,
the cf-agent process runs regularly. This process will by default, every 5
minutes, try to connect to cf-serverd on the policy server to check for policy
updates.

By default `cf-serverd` will serve policy from the `/var/cfengine/masterfiles`
directory. When the content changes, cf-agent will download the updated files to
`/var/cfengine/inputs` before executing them locally.

This means that by default you should store all your policies in the
`/var/cfengine/masterfiles` directory on your policy server. So, now create
`/var/cfengine/masterfiles/my-policy.cf` with the content of the test policy
previously authored.

**NOTE:** We recommend that you use a version control system to store the audit
log of your policy.

Now we need to tell CFEngine that there is a new policy in town:

1. Create `/var/cfengine/masterfiles/def.json` with the following content:

```json
{
  "inputs": [ "my-policy.cf" ]
}
```

On the policy server you can run the following command to make sure the syntax
is correct.

```console
# cf-agent -cf /var/cfengine/masterfiles/promises.cf
```

After some period of time (CFEngine runs by default every 5 minutes), log in to
any of the bootstrapped clients and you will find the `/tmp/-hello-world` file
there.

Whenever a host connects to the Policy Server, the host will ensure that it has
the `my-policy.cf` file from the masterfiles directory exists in the local
inputs directory. `def.json` will also be downloaded with the new
instruction that there is a new policy. Within 5 minutes, whether you have 5
Linux hosts or 50,000 Linux hosts, they will all have the `/tmp/hello-world` file
on their system. Yeah!

If you delete the file, it will be restored by CFEngine at its next run. We call
this a promise repaired. If the file exists during a run, the result would be
promise kept.

Congratulations! You now have the basic knowledge needed to write and run
CFEngine policies. Let's continue with an example on how to manage users. Click
here to continue.

