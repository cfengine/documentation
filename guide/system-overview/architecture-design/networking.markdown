---
layout: default
title: Networking
published: true
sorting: 10
tags: [overviews, troubleshooting, connectivity, network, server, access, remote, keys, encryption, security]
---

Starting [`cf-serverd`][cf-serverd], sets up a line of communication between 
hosts. This daemon authenticates requests from the network and processes them 
according to rules specified in the server control body and server bundles 
containing access promises. The server can allow the network to access files, 
or to execute CFEngine.

The only contact [`cf-agent`][cf-agent] makes to the server is via remote copy 
requests. It does not and cannot grant any access to a system from the 
network. It is only able request access to files on the remote server.

Lastly, [`cf-runagent`][cf-runagent] can be used to run `cf-agent` on a number 
of remote hosts.

Unlike other approaches to automation, CFEngine does not rely on SSH key 
authentication and configuring trust, the communication between hosts is very 
structured and also able to react to availability issues. This means that you 
don't have to arrange risk login credentials to get CFEngine to work. If large 
portions of your network stop working, individual host in the CFEngine system
understand how to keep on running and delivering promises.

If the network is not working, CFEngine agents skip new promises and continue 
with what they already have. CFEngine was specifically designed be resilient 
against connectivity issues network failure may be in question. CFEngine is
fault tolerant and opportunistic.

## Server Connection

In order to connect to the CFEngine server you need:

* A public-private key pair

To create a key pair, run [`cf-key`][cf-key].

* An IP (v4 or v6) address.

You must be online with a configured network address. 

* Permission to connect to the server

The server control body must grant access to your computer and public key by 
name or IP address, by listing it in one of the lists (see below).

* Mutual trust

Your public key must be trusted by the server, and you must trust the server's 
public key. By mutually trusting each others' keys, client and server agree to 
use that key as a sufficient identifier for the computer. 

* Permission to access something

Your host name or IP address must be mentioned in an [`access` promise][access]
inside a server bundle, made by the file that you are trying to access.

If all of the above criteria are met, connection will be established and data 
will be transferred between client and server. The client can only send short 
requests, following the CFEngine protocol. The server can return data in a 
variety of forms, usually files, but sometimes console output.

### Bootstrapping

Bootstrapping establishes a connection between host and policy server, and
executes the policy that starts the CFEngine daemon processes 
[`cf-execd`][cf-execd], [`cf-serverd`][cf-serverd] and 
[`cf-monitord`][cf-monitord]. The host that other hosts are bootstrapped to
automatically assumes the role of policy server.

You should bootstrap the policy server first to itself:

    $ /var/cfengine/bin/cf-agent --bootstrap [public IP of localhost]

Then execute the same step on all hosts that should pull policy from that
server. CFEngine will create keys if there are none present, and exchange 
those to establish trust.

CFEngine will output diagnostic information upon bootstrap. In case of error, 
investigate the [`access` promises][access] the server is making. Note that 
by default, CFEngine's server daemon `cf-serverd` trust incoming connections 
from hosts within the same subnet.

## Key exchange

The key exchange model used by CFEngine is based on that used by OpenSSH. It 
is a peer to peer exchange model, not a central certificate authority model. 
This means that there are no scalability bottlenecks (at least by design, 
though you might introduce your own if you go for an overly centralized 
architecture).

Key exchange is handled automatically by CFEngine and all you need to do is to 
decide which keys to trust. The server `cf-serverd` blocks the acceptance of 
unknown keys by default. In order to accept such a new key, the IP address of 
the presumed client must be listed in the `trustkeysfrom` stanza of a `server` 
bundle (these bundles can be placed in any file). Once a key has been 
accepted, it will never be replaced with a new key, thus no more trust is 
offered or required.

Once you have arranged for the right to connect to the server, you must decide 
which hosts will have access to which files. This is done with [`access` 
promises][access].

```cf3
    bundle server access_rules()
    
    {
    access:
    
      "/path/file"
    
        admit   => { "127.0.0.1", "127.0.0.2", "127.0.0.3" },
        deny    => { "192\..*" };
    }
```

On the client side, i.e. [`cf-runagent`][cf-runagent] and 
[`cf-agent`][cf-agent], there are three issues:

1.  Choosing which server to connect to.
2.  Trusting the identity of any previously unknown servers, i.e.
    trusting the server's public key to be its and no one else's. (The
    issues here are the same as for the server.)
3.  Choosing whether data transfers should be encrypted (with
    `encrypt`).

There are two ways of managing trust of server keys by a client. One is an 
automated option, setting the option `trustkey` in a `copy_from` stanza, e.g.

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

