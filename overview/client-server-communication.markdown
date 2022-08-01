---
layout: default
title: Client server communication
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
  executing a `copy_from` files promise using `trustkey=>"true"`.
* **Permission to access something**.
  Your host name or IP address must be mentioned in an `access` promise
  inside a server bundle, made by the file that you are trying to access.

If all of the above criteria are met, connection will be established and data
will be transferred between client and server. The client can only send short
requests, following the CFEngine protocol. The server can return data in a
variety of forms, usually files, but sometimes console output.

## Bootstrapping

[Bootstrap][General Installation#Bootstrap] is the manual first run of cf-agent that establishes
communication with the policy server.
Bootstrapping executes the `failsafe.cf` policy that connects to
the server, establishes trust to the server's key, and that starts the
CFEngine daemon processes `cf-execd`, `cf-serverd` and `cf-monitord`.
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
from hosts within the same `/16` subnet.

After a host has been bootstrapped, the text file `policy_server.dat` in
the CFEngine installation contains the IP address of the policy server.

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
bundle server my_access_rules()
{
  access:
    "/path/file"
      admit   => { "127.0.0.1", "127.0.0.2", "127.0.0.3" },
      deny    => { "192.168.0.0/8" };
}
```

On the client side, i.e. `cf-runagent` and `cf-agent`, there are three issues:

1.  Choosing which server to connect to.
2.  Trusting the key of any previously unknown servers
3.  Choosing whether data transfers should be encrypted (with
    [`encrypt`][files#encrypt]) - not applicable if you are using new [`protocol_version`][Components#protocol_version].

There are two ways of managing trust of server keys by a client. One is an
automated option, setting the option [`trustkey`][files#trustkey] in a `copy_from` files promise, e.g.

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
decision. After the first exchange, trust is no longer needed, because the
keys allow identity to be actually verified.

Even if you leave the trust options switched on, you are not blindly trusting
the hosts you know about. The only potential insecurity lies in any new keys
that you have not thought about. If you use wildcards or IP prefixes in the
trust rules, then other hosts might be able to spoof their way in on trust
because you have left open a hole for them to exploit. That is why it is
recommended to set the system to the state of zero trust
immediately after key transfer, by commenting or emptying out the trust options
(`trustkeysfrom` on the server).

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

CFEngine has 2 communication protocols. `classic` or `1` and `2` or `latest`.
Each protocol provides different encryption options for keeping file contents
private during transfer.

However, the main role of encryption in configuration management is for
authentication. Secrets should not be transferred through policy, encrypted or
not. Policy files should be considered public, and any leakage should not
reveal secret information.

**Note:** Connections from the cf-agent are cached as described in the
documentation for body [`copy_from`][files#copy_from].

### Protocol Classic

Encryption for Enterprise is symmetric AES 256 bit in CBC mode, using
a session key exchanged during the RSA handshake.

In core/community as **outgoing** outlined in the
[body copy_from `encrypt`][files#encrypt] documentation the initial
connection is encrypted using the public/private keys for the client
and server hosts. After the initial connection is established
subsequent connections and data transfer is encrypted by a randomly
generated Blowfish key that is refreshed each session.

With the classic protocol cf-serverd has the ability to enforce that a
file transfer be encrypted by setting the
[`ifencrypted` access attribute][access#ifencrypted]. When ACLs that
require encryption have unencrypted access attempts cf-serverd logs an
error message indicating the file requires encryption. Access to files
that cf-serverd requires to be encrypted can be logged by setting the
[body server control `logencryptedtransfers` attribute][cf-serverd#logencryptedtransfers].

### Protocol 2

3.6 introduced a new protocol option for communication with
cf-serverd. [Protocol 2][Components#protocol_version]
is the default in 3.7+ and uses a TLS session for encryption.

**Note:** When protocol 2 is in use legacy encryption attributes are **noop**.

The following attributes are affected:

- [`encrypt`][files#encrypt] in copy from bodies
- [`ifencrypted`][access#ifencrypted] in in access promises
- [`logencryptedtransfers`][cf-serverd#logencryptedtransfers] in body common
  control

The specific encryption algorithm used depends on the cipher
negotiated between the client and the server. You can control which
ciphers are allowed by cf-serverd for **incoming** connections by
setting the
[body server control `allowciphers` attribute][cf-serverd#allowciphers]. Controlling
which ciphers are allowed to be used in **outgoing** connections is
done by setting
[body common control `tls_ciphers`][Components#tls_ciphers].

Additionally the minimum version of TLS required for **incoming**
connections can be set in
[body server control `allowtlsversion`][cf-serverd#allowtlsversion]
and the minimum version of TLS required for **outgoing** connections
can be set in
[body common control `tls_min_version`][Components#tls_min_version].

There are debug and verbose level logs produced by cf-agent to
indicate when TLS is in use.

The following was captured by running the agent update policy in debug
mode.

`/var/cfenigne/bin/cf-agent -Kdf update.cf`

```
verbose: Connected to host 192.168.56.2 address 192.168.56.2 port 5308
  debug: TLSVerifyCallback: no ssl->peer_cert
  debug: TLSVerifyCallback: no conn_info->key
  debug: This must be the initial TLS handshake, accepting
verbose: TLS version negotiated:  TLSv1.2; Cipher: AES256-GCM-SHA384,TLSv1/SSLv3
verbose: TLS session established, checking trust...
verbose: Received public key compares equal to the one we have stored
verbose: Server is TRUSTED, received key 'SHA=5d20c01e4230aa53863eb36686eaa882094cdbddf53545616dfd588f00cc0659' MATCHES stored one.
  debug: TLSRecvLines(): CFE_v2 cf-serverd 3.7.1.
  debug: TLSRecvLines(): OK WELCOME USERNAME=root
```

cf-serverd emits verbose and debug log messages indicating when TLS is in use.

The following was captured by starting cf-serverd in the foreground
with debug mode.

`/var/cfenigne/bin/cf-serverd -Fd`

```
verbose: New connection (from 192.168.56.3, sd 7), spawning new thread...
verbose: CollectCallHasPending: false
  debug: Waiting at incoming select...
   info: 192.168.56.3> Accepting connection
verbose: 192.168.56.3> Setting socket timeout to 600 seconds.
verbose: 192.168.56.3> Peeked nothing important in TCP stream, considering the protocol as TLS
  debug: 192.168.56.3> Peeked data: ....2......ak.
  debug: 192.168.56.3> TLSVerifyCallback: no ssl->peer_cert
  debug: 192.168.56.3> TLSVerifyCallback: no conn_info->key
  debug: 192.168.56.3> This must be the initial TLS handshake, accepting
verbose: 192.168.56.3> TLS version negotiated:  TLSv1.2; Cipher: AES256-GCM-SHA384,TLSv1/SSLv3
verbose: 192.168.56.3> TLS session established, checking trust...
  debug: 192.168.56.3> TLSRecvLines(): CFE_v2 cf-agent 3.7.1.
  debug: 192.168.56.3> TLSRecvLines(): IDENTITY USERNAME=root.
verbose: 192.168.56.3> Setting IDENTITY: USERNAME=root
verbose: 192.168.56.3> Received public key compares equal to the one we have stored
verbose: 192.168.56.3> SHA=4f25279831eeaf579d2e3451345854a93fdefc856ad741bd59515b859fb84dea: Client is TRUSTED, public key MATCHES stored one.
```

## Troubleshooting

When setting up `cf-serverd`, you might see the error message

      Unspecified server refusal

This means that `cf-serverd` is unable or is unwilling to authenticate the
connection from your client machine. The message is deliberately non-specific
so that anyone attempting to attack or exploit the service will not be given
information which might be useful to them.

<!-- **TODO: how/where to check the server log?** -->

There is a simple checklist for curing this problem:

1. Make sure that you have granted access to the client's address in the
   [`server control`][cf-serverd#Control Promises] body.
2. Make sure the connecting client is granted access to the requested resources
   (files usually) in the `access_rules` promise bundle.
3. See the verbose log of the server for the exact error message, since the
   client always gets the "Unspecified server refusal" reply from the server.
   To run the server in verbose, kill cf-serverd on the policy hub and run:
    $ cf-serverd -v
   and then manually run `cf-agent` on the client.
4. In the unlikely case that you still get no indication of the denial, try
   increasing the agent run verbosity. `cf-agent -I` for info-level messages
   or even `cf-agent -v` for verbose.
