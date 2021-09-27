---
layout: default
title: Secure Bootstrap
published: true
sorting: 20
tags: [guide, installation, install, security]
---

This guide presumes that you already have CFEngine properly installed
and running on the policy hub, the machine that distributes the policy
to all the clients. It also presumes that CFEngine is installed, but not
yet configured, on a number of clients.

We present a step-by-step procedure to securely bootstrapping a
number of servers (referred to as *clients*) to the policy hub, over a
possibly unsafe network.

## Introduction

CFEngine's trust model is based on the secure exchange of keys. This
exchange of keys between *client* and *hub*, can either happen manually
or automatically. Usually this step is automated as a dead-simple
"bootstrap" procedure:

`cf-agent --bootstrap $HUB_IP`

It is presumed that during this first key exchange, *the network is
trusted*, and no attacker will hijack the connection. After
"bootstrapping" is complete, the node can be deployed in the open
internet, and all connections are considered secure.

However there are cases where initial CFEngine deployment is happening
over an insecure network, for example the Internet. In such cases we
already have a secure channel to the clients, usually ssh, and we use
this channel to *manually establish trust* from the hub to the clients
and vice-versa.

## Locking down the policy server

We must change the policy we're distributing to fully locked-down
settings. So after we have set-up our hub (using the standard procedure
of `cf-agent --bootstrap $HUB_IP`) we take care of the following:

* `cf-serverd` must never accept a connection from a client presenting an
  untrusted key. [Disable automatic key trust][Masterfiles Policy Framework#trustkeysfrom]
  by providing an empty list for `def.trustkeyfrom`.

## Bootstrap without automatically trusting

In order to securely bootstrap a host you must have the public key of the host
you wish to trust.

Copy the hubs public key (`/var/cfengine/ppkeys/localhost.pub`) to the agent you
wish to bootstrap. And install it using `cf-key`.

```console
[root@host001]# cf-key --trust-key /path/to/hubs/key.pub
```

**Note:** If you are using [protocol_version `1` or `classic`][Components#protocol_version]
you need to supply an IP address before the path to the key.

For example:

```
  notice: Establishing trust might be incomplete. For completeness, use --trust-key IPADDR:filename
```

Next copy the hosts public key (`/var/cfengine/ppkeys/localhost.pub`) to the hub
and install it using `cf-key`.

```console
[root@hub]# cf-key --trust-key /path/to/host001/key.pub
```

Now that the hosts trust each other we can bootstrap the host to the hub.

```console
[root@host001]# cf-agent --trust-server no --bootstrap $HUB 
```

## Manually establishing trust

Get the hub's key and fingerprint, we'll them when configuring the host to trust
the hub:

```console
[root@hub]# HUB_KEY=`cf-key -p /var/cfengine/ppkeys/localhost.pub
```

### On each client we deploy

We will perform a *manual bootstrap*.

* Get the client's key and fingerprint, we'll need it later when establishing
  trust on the hub:

  ```console
  [root@host001]# CLIENT_KEY=`cf-key -p /var/cfengine/ppkeys/localhost.pub`
  ```

* Write the policy hub's IP address to `policy_server.dat`:

  ```console
  [root@host001]# echo $HUB_IP > /var/cfengine/policy_server.dat
  ```

* Put the hub's key into the client's trusted keys:

  ```console
  [root@host001]# scp $HUB_IP:/var/cfengine/ppkeys/localhost.pub /var/cfengine/ppkeys/root-${HUB_KEY}.pub
  ```

### Install the clients public key on the hub

* Put the client's key into the hub's trusted keys. So
  on the hub, run:

  ```console
  [root@hub]# scp $CLIENT_IP:/var/cfengine/ppkeys/localhost.pub /var/cfengine/ppkeys/root-${CLIENT_KEY}.pub
  ```
