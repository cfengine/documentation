---
layout: default
title: Variables
categories: [Manuals, Troubleshooting, Remote Access]
published: true
alias: manuals-concept-variables.html
tags: [manuals, concepts, variables]
---


-   [Server connection](#Server-connection)
-   [Key exchange](#Key-exchange)
-   [Time windows](/manuals/cf3-Reference#Time-windows)
-   [Other users than root](/manuals/cf3-Reference#Other-users-than-root)
-   [Encryption](/manuals/cf3-Reference#Encryption)


### Server connection

When setting up `cf-serverd`, you might see the error message

      Unspecified server refusal

This means that `cf-serverd` is unable or is unwilling to
authenticate the connection from your client machine. The message
is generic: it is deliberately non-specific so that anyone
attempting to attack or exploit the service will not be given
information which might be useful to them. There is a simple
checklist for curing this problem:

1.  Make sure that the domain variable is set in the configuration
    files read by both client and server; alternatively use
    `skipidentify` and `skipverify` to decouple DNS from the the
    authentication.
2.  Make sure that you have granted access to your client in the
    server body
                  
                  body server control
                  {
                  allowconnects         => { "127.0.0.1" , "::1" ...etc };
                  allowallconnects      => { "127.0.0.1" , "::1" ...etc };
                  trustkeysfrom         => { "127.0.0.1" , "::1" ...etc };
                  }
                  

3.  Make sure you have created valid keys for the hosts using
    `cf-key`.
4.  If you are using secure copy, make sure that you have created a
    key file and that you have distributed and installed it to all
    participating hosts in your cluster.

Always remember that you can run CFEngine in verbose or debugging
modes to see how the authentication takes place:

    cf-agent -v
    cf-serverd -v

`cf-agent` reports that access is denied regardless of the nature
of the error, to avoid giving away information which might be used
by an attacker. To find out the real reason for a denial, use
verbose ‘-v’ or even debugging mode ‘-d2’.




### Key exchange

The key exchange model used by CFEngine is based on that used by
OpenSSH. It is a peer to peer exchange model, not a central
certificate authority model. This means that there are no
scalability bottlenecks (at least by design, though you might
introduce your own if you go for an overly centralized
architecture).

The problem of key distribution is the conundrum of every public
key infrastructure. Key exchange is handled automatically by
CFEngine and all you need to do is to decide which keys to trust.

When public keys are offered to a server, they could be accepted
automatically on trust because no one is available to make a
decision about them. This would lead to a race to be the first to
submit a key claiming identity.

Even with DNS checks for correct name/IP address correlation
(turned off with `skipverify`), it might be possible to submit a
false key to a server.

The server `cf-serverd` blocks the acceptance of unknown keys by
default. In order to accept such a new key, the IP address of the
presumed client must be listed in the `trustkeysfrom` stanza of a
`server` bundle (these bundles can be placed in any file). Once a
key has been accepted, it will never be replaced with a new key,
thus no more trust is offered or required.

Once you have arranged for the right to connect to the server, you
must decide which hosts will have access to which files. This is
done with `access` rules.

    bundle server access_rules()
    
    {
    access:
    
      "/path/file"
    
        admit   => { "127.0.0.1", "127.0.0.2", "127.0.0.3" },
        deny    => { "192\..*" };
    }

On the client side, i.e. `cf-runagent` and `cf-agent`, there are
three issues:

1.  Choosing which server to connect to.
2.  Trusting the identity of any previously unknown servers, i.e.
    trusting the server's public key to be its and no one else's. (The
    issues here are the same as for the server.)
3.  Choosing whether data transfers should be encrypted (with
    `encrypt`).

Because there are two clients for connecting to `cf-serverd`
(`cf-agent` and `cf-runagent`), there are also two ways of managing
trust of server keys by a client. One is an automated option,
setting the option `trustkey` in a `copy_from` stanza, e.g.

    body copy_from example
         {
         # .. other settings ..
    
         trustkey => "true";
         }

Another way is to run `cf-runagent` in interactive mode. When you
run `cf-runagent`, unknown server keys are offered to you
interactively (as with `ssh`) for you to accept or deny manually:

         
         WARNING - You do not have a public key from host ubik.iu.hio.no = 128.39.74.25
                   Do you want to accept one on trust? (yes/no)
         -->
         




### Time windows (races)

Once public keys have been exchanged from client to server and from
server to client, the issue of trust is solved according to public
key authentication schemes. You only need to worry about trust when
one side of a connection has never seen the other side before.

Often you will have a central server and many client satellites.
Then the best way to transfer all the keys is to set the `trustkey`
flags on server and clients sides to coincide with a time at which
you know that `cf-agent` will be run, and when a spoofer is
unlikely to be able to interfere.

This is a once-only task, and the chance of an attacker being able
to spoof a key-transfer is small. It would require skill and
inside-information about the exchange procedure, which would tend
to imply that the trust model was already broken.

Another approach would be to run `cf-runagent` against all the
hosts in the group from the central server and accept the keys one
by one, by hand, though there is little to be gained from this.

Trusting a host for key exchange is unavoidable. There is no clever
way to avoid it. Even transferring the files manually by diskette,
and examining every serial number of the computers you have, the
host has to trust the information you are giving it. It is all
based on assertion. You can make it almost impossible for keys to
be faked or attacked, but you cannot make it absolutely impossible.
Security is about managing reasonable levels of risk, not about
magic.

All security is based on a moment of trust, that is granted by a
user at some point in time – and is assumed thereafter (once given,
hard to rescind). Cryptographic key methods only remove the need
for a repeat of the trust decision. After the first exchange, trust
is no longer needed, because they keys allow identity to be
actually verified.

Even if you leave the trust options switched on, you are not
blindly trusting the hosts you know about. The only potential
insecurity lies in any new keys that you have not thought about. If
you use wildcards or IP prefixes in the trust rules, then other
hosts might be able to spoof their way in on trust because you have
left open a hole for them to exploit. That is why it is recommended
to return the system to the default state of zero trust immediately
after key transfer, by commenting out the trust options.

It is possible, though somewhat laborious to transfer the keys out
of band, by copying /var/cfengine/ppkeys/localhost.pub to
`/var/cfengine/ppkeys/user-aaa.bbb.ccc.mmm` (assuming IPv4) on
another host. e.g.

         
         localhost.pub -> root-128.39.74.71.pub
         

This would be a silly way to transfer keys between nearby hosts
that you control yourself, but if transferring to long distance,
remote hosts it might be an easier way to manage trust.




### Other users than root

CFEngine normally runs as user "root" (except on Windows which does
not normally have a root user), i.e. a privileged administrator. If
other users are to be granted access to the system, they must also
generate a key and go through the same process. In addition, the
users must be added to the server configuration file.




### Encryption

CFEngine provides encryption for keeping file contents private
during transfer. It is assumed that users will use this
judiciously. There is nothing to be gained by encrypting the
transfer of public files – overt use of encryption just contributes
to global warming, burning unnecessary CPU cycles without offering
any security.

The main role for encryption in configuration management is for
authentication. CFEngine always uses encryption during
authentication, so none of the encryption settings affect the
security of authentication.

