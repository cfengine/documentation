---
layout: default
title: Networking
published: true
sorting: 30
tags: [overviews, troubleshooting, connectivity, network, server, access, remote, keys, encryption, security]
---

Starting `cf-serverd` sets up a line of communication between 
hosts. This daemon authenticates requests from the network and processes them 
according to rules specified in the
[`server control`][cf-serverd#Control Promises] body and server bundles 
containing `access` promises.

The server can allow the network to access files or to execute CFEngine:

* The only contact [`cf-agent`][cf-agent] makes to the server is via remote copy 
  requests. It does not and cannot grant any access to a system from the 
  network. It is only able to request access to files on the remote server.

* [`cf-runagent`][cf-runagent] can be used to run `cf-agent` on a number 
  of remote hosts.

Unlike other approaches to automation, CFEngine does not rely on SSH key 
authentication and configuring trust, the communication between hosts is very 
structured and also able to react to availability issues. This means that you 
don't have to arrange login credentials to get CFEngine to work. If large 
portions of your network stop working, then CFEngine on each individual host
understands how to keep on running and delivering promises.

In particular, if the network is not working,
CFEngine agents skip downloading new promises and continue 
with what they already have. CFEngine was specifically designed to be resilient 
against connectivity issues network failure may be in question. CFEngine is
fault tolerant and opportunistic.

## Connecting to server

In order to connect to the CFEngine server you need:

* **A public-private key pair**. It is automatically generated during package
  installation or during bootstrap. To manually create a key pair,
  run `cf-key`.
* **Network connectivity** with an IPv4 or IPv6 address.
* **Permission to connect** to the server.
  The [`server control`][cf-serverd#Control Promises] body must grant access
  to your computer and public key by name or IP address, by listing it in
  the appropriate access lists (see below).
* **Mutual key trust**.
  Your public key must be trusted by the server, and you must trust the server's 
  public key. The first part is established by having the
  [`trustkeysfrom`][cf-serverd#trustkeysfrom] setting open on the server for the first
  connection of the agent. It should be closed later to avoid trusting new agents.
  The second part is established by bootstrapping the agent to the hub, or by
  executing a `copy_from` files promise using ```trustkey=>"true"```.
* **Permission to access something**.
  Your host name or IP address must be mentioned in an `access` promise
  inside a server bundle, made by the file that you are trying to access.

If all of the above criteria are met, connection will be established and data 
will be transferred between client and server. The client can only send short 
requests, following the CFEngine protocol. The server can return data in a 
variety of forms, usually files, but sometimes console output.

## Bootstrapping

Bootstrapping executes the policy (```failsafe.cf```) that connects to 
the server and establishes trust to the server's key, and that starts the 
CFEngine daemon processes cf-execd`, `cf-serverd` and `cf-monitord`.
The host that other hosts are bootstrapped to
automatically assumes the role of policy server.

You should bootstrap the policy server first to itself:

    $ /var/cfengine/bin/cf-agent --bootstrap [public IP of localhost]

Then execute the same step (using the exact same IP) 
on all hosts that should pull policy from that server. 
CFEngine will create keys if there are none present, and exchange 
those to establish trust.

CFEngine will output diagnostic information upon bootstrap. In case of error, 
investigate the `access` promises the server is making (run `cf-serverd` in
verbose mode on the policy hub for more informative messages). Note that 
by default, CFEngine's server daemon `cf-serverd` trusts incoming connections 
from hosts within the same ```/16``` subnet.

## Key exchange

The key exchange model used by CFEngine is based on that used by OpenSSH. It 
is a peer to peer exchange model, not a central certificate authority model. 
This means that there are no scalability bottlenecks (at least by design, 
though you might introduce your own if you go for an overly centralized 
architecture).

Key exchange is handled automatically by CFEngine and all you need to do is to 
decide which keys to trust. The server (`cf-serverd`) trusts new keys only
from addresses in `trustkeysfrom`. Once a key has been 
accepted you should close down `trustkeysfrom` list. Then, even if a malicious peer
is spoofing an allowed IP address, its unknown key will be denied.

Once you have arranged for the right to connect to the server, you must decide 
which hosts will have access to which files. This is done with `access` promises.

```cf3
    bundle server access_rules()
    
    {
    access:
    
      "/path/file"
    
        admit   => { "127.0.0.1", "127.0.0.2", "127.0.0.3" },
        deny    => { "192\..*" };
    }
```

On the client side, i.e. `cf-runagent and `cf-agent, there are three issues:

1.  Choosing which server to connect to.
2.  Trusting the key of any previously unknown servers
3.  Choosing whether data transfers should be encrypted (with
    `encrypt`) - not applicable if you are using new `protocol_version`.

There are two ways of managing trust of server keys by a client. One is an 
automated option, setting the option `trustkey` in a `copy_from` files promise, e.g.

```cf3
    body copy_from example
    {
      # .. other settings ..
      trustkey => "true";
    }
```

Another way is to run `cf-runagent` in interactive mode. When you run 
`cf-runagent`, unknown server keys are offered to you interactively (as with 
`ssh`) for you to accept or deny manually:

     $ WARNING - You do not have a public key from host ubik.iu.hio.no = 128.39.74.25
     $ Do you want to accept one on trust? (yes/no)
     -->

Once public keys have been exchanged from client to server and from server to 
client, the issue of trust is solved according to public key authentication 
schemes. You only need to worry about trust when one side of a connection has 
never seen the other side before.

### Time windows (races)

All security is based on a moment of trust that is granted by a user at some 
point in time – and is assumed thereafter (once given, hard to rescind). 
Cryptographic key methods only remove the need for a repeat of the trust 
decision. After the first exchange, trust is no longer needed, because they 
keys allow identity to be actually verified.

Even if you leave the trust options switched on, you are not blindly trusting 
the hosts you know about. The only potential insecurity lies in any new keys 
that you have not thought about. If you use wildcards or IP prefixes in the 
trust rules, then other hosts might be able to spoof their way in on trust 
because you have left open a hole for them to exploit. That is why it is 
recommended to return the system to the default state of zero trust 
immediately after key transfer, by commenting out the trust options.

It is possible, though somewhat laborious, to transfer the keys out of band, 
by copying `/var/cfengine/ppkeys/localhost.pub` to 
`/var/cfengine/ppkeys/user-aaa.bbb.ccc.mmm` (assuming IPv4) on another host. 
e.g.

         localhost.pub -> root-128.39.74.71.pub

<!--**TODO: update with new key file name format** -->

### Other users than root

CFEngine normally runs as user "root" (except on Windows which does
not normally have a root user), i.e. a privileged administrator. If
other users are to be granted access to the system, they must also
generate a key and go through the same process. In addition, the
users must be added to the server configuration file.


## Encryption

CFEngine provides encryption for keeping file contents private during transfer. It is assumed that users will use this judiciously. There is nothing to be gained by encrypting the transfer of public files – overt use of encryption just contributes to global warming, burning unnecessary CPU cycles without offering any security.

The main role for encryption in configuration management is for authentication. CFEngine always uses encryption during authentication, so none of the encryption settings affect the security of authentication.


## Troubleshooting

When setting up `cf-serverd`, you might see the error message

      Unspecified server refusal

This means that `cf-serverd` is unable or is unwilling to authenticate the 
connection from your client machine. The message is deliberately non-specific 
so that anyone attempting to attack or exploit the service will not be given 
information which might be useful to them.

<!-- **TODO: how/where to check the server log?** -->

There is a simple checklist for curing this problem:

1.  Make sure that the domain variable is set in the configuration
    files read by both client and server; alternatively use
    `skipidentify` to decouple DNS from the the
    authentication.
2.  Make sure that you have granted access to your client in the
    server body

```cf3                  
    body server control
    {
        allowconnects         => { "127.0.0.1" , "::1" ...etc };
        allowallconnects      => { "127.0.0.1" , "::1" ...etc };
        trustkeysfrom         => { "127.0.0.1" , "::1" ...etc };
    }
```                  

3.  Make sure you have created valid keys for the hosts using
    `cf-key`.
4.  If you are using secure copy, make sure that you have created a
    key file and that you have distributed and installed it to all
    participating hosts in your cluster.

Always remember that you can run CFEngine in verbose or debugging modes to see 
how the authentication takes place:

    $ cf-agent -v
    $ cf-serverd -v

`cf-agent` reports that access is denied regardless of the nature
of the error, to avoid giving away information which might be used
by an attacker. To find out the real reason for a denial, use
verbose ‘-v’ or even debugging mode ‘-d2’.

