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


## Introduction ##

CFEngine's trust model is based the on secure exchange of keys. This
exchange of keys between *client* and *hub*, can either happen manually
or automatically. Usually this step is automated as a dead-simple
"bootstrap" procedure:

```cf-agent --bootstrap $HUB_IP```

It is presumed that during this first key exchange, *the network is
trusted*, and no attacker will hijack the connection. After
"bootstrapping" is complete, the node can be deployed in the open
internet, and all connections are considered secure.

However there are cases where initial CFEngine deployment is happening
over an insecure network, for example the Internet. In such cases we
already have a secure channel to the clients, usually ssh, and we use
this channel to *manually establish trust* from the hub to the clients
and vice-versa.

## Manual Trust Establishment ##

This procedure concerns CFEngine version 3.6 or earlier. While this
fully manual procedure should always work, from version 3.7 onwards
there is a simpler semi-automatic procedure for establishing trust.

### On the policy hub ###

We must change the policy we're distributing to fully locked-down
settings. So after we have set-up our hub (using the standard procedure
of ```cf-agent --bootstrap $HUB_IP```) we take care of the following:

* Cf-serverd must never accept a connection from a client presenting an
  untrusted key.  So in `body server control` we set:
  ```trustkeysfrom => {};```

* Since we will be manually bootstrapping the clients, we need to
  distribute a proper `failsafe.cf` policy. (**NOTE:**
  `failsafe.cf` is a file auto-generated in the `inputs` directory when
  we run ```cf-agent --bootstrap```).

  In order to do that, we copy hub's `failsafe.cf` to `masterfiles`:
  ```cp /var/cfengine/inputs/failsafe.cf /var/cfengine/masterfiles/```

  We'll edit that copy in `masterfiles` in the next step.

* All `copy_from` files promises must never connect to an untrusted
  server, which means that the following line should not be found
  anywhere:
  ```trustkey => "true"```

  All occurrences of `trustkey` in `masterfiles` directory should be
  changed to "false", or be removed (since it defaults to false
  anyway). It is certain that `failsafe.cf` that we copied in
  the previous step will contain such occurrences that should be
  changed. (Those occurrences are the reason that automatic bootstrapping
  requires a trusted network).

* The previous changes in `masterfiles` need to be properly propagated
  to the `inputs` directory. The automated way to do that is to run the
  update.cf policy:
  ```cf-agent -f update.cf```

* Get the hub's key fingerprint, we'll need it later:
  ```HUB_KEY=`cf-key -p /var/cfengine/ppkeys/localhost.pub` ```

### On each client we deploy ###

We should **not** follow the automatic method, i.e. the
```cf-agent --bootstrap``` command. We will perform a
*manual bootstrap*.

* Generate a private/public key pair by running `cf-key`.

* Get the client's key fingerprint, we'll need it later:
  ```CLIENT_KEY=`cf-key -p /var/cfengine/ppkeys/localhost.pub` ```

* Write the policy hub's IP address to `policy_server.dat`:
  ```echo $HUB_IP > /var/cfengine/policy_server.dat```

* Manually copy the modified `failsafe.cf` from hub's `masterfiles`
  directory into client's `inputs` directory. You should do
  it in a secure manner, for example using `scp` with properly trusted
  fingerprint of the remote host.

* **NOTE:** At this step, you can try running the failsafe policy. Because
  trust between the two hosts has not been established, *you will get a
  failure*, which is totally expected and means everything is correct
  and secure:
  ```
  # cf-agent -f failsafe.cf
  error: TRUST FAILED, server presented untrusted key: MD5=cc27570b8b831192d9f20b54d07dd80b
  error: No suitable server responded to hail
  error: TRUST FAILED, server presented untrusted key: MD5=cc27570b8b831192d9f20b54d07dd80b
  error: No suitable server responded to hail
  [ ... ]
  ```

* Put the hub's key into the client's trusted keys:
  ```scp $HUB_IP:/var/cfengine/ppkeys/localhost.pub /var/cfengine/ppkeys/root-${HUB_KEY}.pub```

### Final steps ###

* Put the client's key into the hub's trusted keys. So
  on the hub, run:
  ```scp $CLIENT_IP:/var/cfengine/ppkeys/localhost.pub /var/cfengine/ppkeys/root-${CLIENT_KEY}.pub```

* If you now run the failsafe policy on each and every client, it should
  succeed:
  ```
  # cf-agent -f failsafe.cf
  ```


  Congratulations, you have performed a fully manual bootstrap procedure
  for your clients!




