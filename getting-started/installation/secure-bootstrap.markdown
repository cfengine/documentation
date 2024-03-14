---
layout: default
title: Secure bootstrap
published: true
sorting: 20
---

This guide assumes you already have a working CFEngine hub (installed and bootstrapped), and you have installed CFEngine on a client you want to securely connect to the hub (bootstrap).
See the [Getting started guide][Getting started] for an introduction to CFEngine and how to install it.

CFEngine's trust model is based on the secure exchange of keys.
Usually, when getting started with CFEngine, this step is automated as a dead-simple "bootstrap" procedure:

```command
cf-agent --bootstrap <IP address of hub>
```

CFEngine uses mutual authentication, so this trust goes in both directions.
Both the client and the hub refuse to communicate with an unknown, untrusted host.

## Default configuration

In the default configuration, the policy server (cf-serverd) on the hub machine trusts incoming connections from the same `/16` subnet.
This means that:

* Bootstrapping new clients will work as long as the 2 first numbers in the IP address are identical ([IPv4 dot decimal representation](https://en.wikipedia.org/wiki/Dot-decimal_notation)) .
  The hub and client mutually accept each other's keys, automatically.
* This applies to _all_ IP addresses within that range, not just the 1 IP address belonging to the client you are currently bootstrapping.
* The hub will keep accepting new clients from those IP addresses until you change the configuration.
* If you try to bootstrap a client where those 2 numbers in the IP address do not match the hub, it will fail.

This situation, where the client and hub automatically transfer and trust each other's keys is called _automatic trust_ or _automatic bootstrap_.
When using automatic trust, it is presumed that during this first key exchange, *the network is trusted*, and no attacker will hijack the connection.
Below we will show ways to change the configuration and bootstrap your clients in more secure ways.
The goal here is to illustrate the different approaches, explaining what is needed and the implications of each.
In the end, you will not be running these commands manually, but rather putting them into a provisioning system.

## Allowing only specific IP addresses / subnets

In order to specify and limit which hosts (IP addresses) are considered trusted and allowed to connect and fetch policy files, you can put the trusted IP addresses and subnets into the `acl` variable:

```json
[file=/var/cfengine/masterfiles/def.json]
{
  "variables": {
    "default:def.acl": ["1.2.3.4", "4.3.2.1"]
  }
}
```

**Important:** Replace `1.2.3.4` with the IP address of your hub, `4.3.2.1` with the IP address of your client, and extend the list with any additional IP addresses / subnets.

If you are using CFEngine Build, you can use [this module](https://build.cfengine.com/modules/allow-hosts/), putting the IP addresses as module input, or add the json file above to your project.
(Save it as a file called `def.json` and do `cfbs add ./def.json`).

Once this is set, you are no longer using the default value explained above (the `/16` subnet).
This variable controls 3 different aspects: IP addresses allowed to connect, IP addresses to automatically trust keys from, and IP addresses allowed to fetch policy files.

**Tip:** Setting the variable to `["0.0.0.0/0"]` will open up your hub to all IPv4 addresses, the entire internet.
This is generally not recommended, but can make sense if you disable automatic trust (shown below), need to support clients connecting from the public internet, and/or want to manage firewalling restrictions outside of CFEngine.

## Disabling automatic trust - Locking down the policy server

In all cases, it is recommended to disable automatic trust when you are not using it.
Either immediately after installation (if distributing keys through another channel, see below) or after you are done bootstrapping clients.
You can edit the augments file to achieve this:

```json
[file=/var/cfengine/masterfiles/def.json]
{
  "variables": {
    "default:def.trustkeysfrom": []
  }
}
```

If you are using CFEngine Build, you can achieve this by adding [this module](https://build.cfengine.com/modules/disable-automatic-key-trust/), or adding the json file above to your project.

When combined with the variable above, you can create a very restricted setup:

```json
[file=/var/cfengine/masterfiles/def.json]
{
  "variables": {
    "default:def.acl": ["1.2.3.4", "4.3.2.1"],
    "default:def.trustkeysfrom": []
  }
}
```

Only those 2 IP addresses are allowed to connect, and they must use their existing keys, no new keys are automatically trusted.

## Key location and generation

If you are installing CFEngine using one of our official packages, keys are automatically generated and you can see them in the expected location:

```command
sudo ls /var/cfengine/ppkeys
```
```output
 localhost.priv
 localhost.pub
'root-SHA=caa398e50c6e6ad554ea90e1bd5e8fee269ca097df6ce0c86ce993be16f6f9e3.pub'
```

The keypair of the host itself is always in the `localhost.pub` and `localhost.priv` files.
Additional keypairs from the hosts CFEngine is talking to over the network are in the other `.pub` files.

**Recommendation:** Don't copy, transfer, open, or share the private key (`localhost.priv`).
It is a secret - putting it in more places is not necessary and increases the chances it could be compromised.
When distributing keys for establishing trust, we are distributing the public keys (`.pub` files).

If you are compiling CFEngine from source, or spawning a new VM based on an image / snapshot without keys inside, you can generate a new keypair:

```
sudo cf-key
```

**Tip:** When using "golden images" to spawn machines with CFEngine already installed, ensure the keys in `/var/cfengine/ppkeys` are deleted before generating the snapshot, and generate / insert keys during provisioning.

## Key distribution - boostrapping without automatically trusting

To securely bootstrap a host to a hub, without trusting the network (IP addresses), you need to copy the 2 public keys across some trusted channel.
Below we will be using SSH as the trusted channel, however the commands can easily be translated to however you are able to run commands and transfer files to your hosts.
(This could be via memory stick, a management interface or some other out-of-band management solution).
The same applies to passwordless sudo - we're using sudo commands without password prompts below, if you have configured password prompts for sudo, or another way you need to run privileged commands, please adjust accordingly.

Assuming you are sitting on a laptop / workstation, and have network and SSH access to both the client and the hub, first set up some variables for each of them:

```command
BOOTSTRAP_IP="1.2.3.4" HUB_SSH="ubuntu@1.2.3.4" CLIENT_SSH="ubuntu@4.3.2.1"
```

Edit the 3 variables according to your situation, they represent:

* `BOOTSTRAP_IP` - The IP address of the hub, which you want your client to bootstrap to (connect to).
* `HUB_SSH` - The username / IP combination you would use to connect to the hub with SSH.
* `CLIENT_SSH` - The username / IP combination you would use to connect to the hub with SSH.

### Trusting the client's key on the hub

Inspect the key:

```command
ssh "$CLIENT_SSH" "sudo cat /var/cfengine/ppkeys/localhost.pub"
```
```output
-----BEGIN RSA PUBLIC KEY-----
MIIBCgKCAQEAt93D8fb+M7HGZxsVo+FnOhnLM9E0QCr046N369jOeePY65lPOhAD
nlWlDPJrYqhnobEdnFr/uNp0ydqb1EASe4qjhQUDi1ujz5+T9dTwhZqUfx22RM6D
CLulbdoXwImPOCNi157UBRIwYVJ6527rv0/TlTpS9iUQVStg0YCBEasGRcQfX/bU
DKrL5Ei+ukJtSEx11NlZ9tRYNu22mJYPGGpNJ0FbiHvR+eu7mAuUZ1QeddcuYkGP
H5/eIe0uTGOmFLXb4gUQymNLJUjQqxoO2l6Km4UpGj61871gCiqMGVTvvZWFbo+g
1KR3RS6L/Gqv9U89msZTGQafpjFQyVbYnwIDAQAB
-----END RSA PUBLIC KEY-----
```

It should have the format above, with `BEGIN RSA PUBLIC KEY`, the arbitrary data, and `END RSA PUBLIC KEY`.
When you're scripting / automating the copying of keys, you can add some checks for this.

Download the key:

```command
ssh "$CLIENT_SSH" "sudo cat /var/cfengine/ppkeys/localhost.pub" > client.pub
```

Upload it to the hub:

```command
scp ./client.pub "$HUB_SSH":client.pub
```

And use `cf-key` to trust the key:

```command
ssh "$CLIENT_SSH" "sudo cf-key --trust-key client.pub"
```

### Trusting the hub's key on the client

Now, for the client we need to perform exactly the same steps:

Inspect the key:

```command
ssh "$HUB_SSH" "sudo cat /var/cfengine/ppkeys/localhost.pub"
```
```output
-----BEGIN RSA PUBLIC KEY-----
MIIBCgKCAQEAt8Wti90sRjLiEhLbC5096nEhzV3fU0N4TrxiGPCb26KufavBrXGw
vmzTeJoWnIFFSn7OYU1g59U7s4aViZwqQ647opc0gZo2dVjDTRFW8lB4dmS7SjAe
t8NA3iXQigWY+45TbvPOalNHurhyrJ4g1+0ttdqwk/L1fVkK0u9wmHrgfo+UQR0D
9P96GWnPKyzVp5PdMmfX0Sm6kMBurawRYeiFCq3gqGtkc0rj3FHr1afrM+8egP9D
sWl43NmMlZ8B9Yt2bP0wdNsbXC7vouDZg8sIQVfvcxSkla+kGceGrEmNTDPuGFlx
VknPhmpjMJ7XhvaXXR1btu3/PLjGLDj6SwIDAQAB
-----END RSA PUBLIC KEY-----
```

Download the key:

```command
ssh "$HUB_SSH" "sudo cat /var/cfengine/ppkeys/localhost.pub" > hub.pub
```

Upload it to the client:

```command
scp ./hub.pub "$CLIENT_SSH":hub.pub
```

And use `cf-key` to trust the key:

```command
ssh "$CLIENT_SSH" "sudo cf-key --trust-key hub.pub"
```

### Start CFEngine on the client with a bootstrap command

Now that keys are distributed, trust is established.
We can run the normal bootstrap command with one crucial difference:
`--trust-server no` tells the agent to **not** automatically trust an unknown key on the other end.
This will start the normal CFEngine services (`cf-execd`, `cf-serverd`, etc.):

```
ssh "$CLIENT_SSH" "cf-agent --trust-server no --bootstrap $BOOTSTRAP_IP"
```

When we connect to the hubs IP address, if there is another server answering, a potential [man-in-the-middle attack](https://en.wikipedia.org/wiki/Man-in-the-middle_attack), it will not work.
The agent on the client machine will refuse to communicate with the untrusted server.
This is the main reason (security benefit) of doing mutual authentication and secure key distribution.
