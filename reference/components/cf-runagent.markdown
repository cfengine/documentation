---
layout: default
title: cf-runagent
published: true
sorting: 70
tags: [Components, cf-runagent]
keywords: [runagent]
---

`cf-runagent` connects to a list of running instances of
`cf-serverd`. It allows foregoing the usual `cf-execd` schedule to activate `cf-agent`.
Additionally, a user may send [classes][Classes and Decisions] to be defined
on the remote host. Two kinds of classes may be sent: classes to decide on
which hosts `cf-agent` will be started, and classes that the user requests
`cf-agent` should define on execution. The latter type is regulated by
`cf-serverd`'s [role based access control][roles].

## Command reference ##

[%CFEngine_include_snippet(cf-runagent.help, [\s]*--[a-z], ^$)%]

**See also:** [bundle resource_type in server access promises][access#resource_type], [cfruncommand in body server control][cf-serverd#cfruncommand]

## Control Promises

Settings describing the details of the fixed behavioral promises made by
`cf-runagent`. The most important parameter here is the list of hosts that the
agent will poll for connections. This is easily read in from a file list,
however when doing so always have a stable input source that does not depend
on the network (including a database or directory service) in any way:
introducing such dependencies makes configuration brittle.

```cf3
body runagent control
{
    # default port is 5308
    hosts => { "127.0.0.1:5308", "eternity.iu.hio.no:80", "slogans.iu.hio.no" };

    #output_to_file => "true";
}
```

### hosts

**Description:** List of host or IP addresses to attempt connection
with

The complete list of contactable hosts. The values may be either
numerical IP addresses or DNS names, optionally suffixed by a ':'
and a port number. If no port number is given, the default CFEngine
port 5308 is assumed.

**Type:** `slist`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
body runagent control
{
  network1::
    hosts => { "host1.example.org", "host2", "host3" };

  network2::
    hosts => { "host1.example.com", "host2", "host3" };
}
```

### port

**Description:** Default port for CFEngine server

**Type:** `int`

**Allowed input range:** `1,65535`

**Default value:** 5308

**Example:**

```cf3
body hub control
{
  port => "5308";
}

body server control
{
  specialhost::
   port => "5308";

  !specialhost::
   port => "5308";
}
```

**Notes:**

The standard or registered port number is tcp/5308. CFEngine does
not presently use its registered udp port with the same number, but
this could change in the future.

Changing the standard port number is not recommended practice. You
should not do it without a good reason.


### force_ipv4

**Description:** true/false force use of ipv4 in connection

**Type:** [`boolean`][boolean]

**Default value:** false

**Example:**

```cf3
body copy_from example
{
  force_ipv4 => "true";
}
```

**Notes:**
IPv6 should be harmless to most users unless you have a partially
or misconfigured setup.

### trustkey

**Description:** true/false automatically accept all keys on trust
from servers

If the server's public key has not already been trusted, this
allows us to accept the key in automated key-exchange.

Note that, as a simple security precaution, `trustkey` should
normally be set to 'false', to avoid key exchange with a server one
is not one hundred percent sure about, though the risks for a
client are rather low. On the server-side however, trust is often
granted to many clients or to a whole network in which possibly
unauthorized parties might be able to obtain an IP address, thus
the trust issue is most important on the server side.

As soon as a public key has been exchanged, the trust option has no
effect. A machine that has been trusted remains trusted until its
key is manually revoked by a system administrator. Keys are stored
in `WORKDIR/ppkeys`.

**Type:** [`boolean`][boolean]

**Default value:** false

**Example:**

```cf3
body copy_from example
{
  trustkey => "true";
}
```

### encrypt

**Description:** true/false encrypt connections with servers

Client connections are encrypted with using a Blowfish randomly
generated session key. The initial connection is encrypted using the
public/private keys for the client and server hosts.

**Type:** [`boolean`][boolean]

**Default value:** false

**Example:**

```cf3
body copy_from example
{
  servers  => { "remote-host.example.org" };
  encrypt => "true";
}
````

### background_children

**Description:** true/false parallelize connections to servers

Causes `cf-runagent` to attempt parallelized connections to the
servers.

**Type:** [`boolean`][boolean]

**Default value:** false

**Example:**

```cf3
body runagent control
{
  background_children => "true";
}
```

### max_children

**Description:** Maximum number of simultaneous connections to
attempt

For the run-agent this represents the maximum number of forked
background processes allowed when parallelizing connections to
servers. For the agent it represents the number of background jobs
allowed concurrently. Background jobs often lead to contention of
the disk resources slowing down tasks considerably; there is thus a
law of diminishing returns.

**Type:** `int`

**Allowed input range:** `0,99999999999`

**Default value:** 50 runagents

**Example:**

```cf3
body runagent control
{
  max_children => "10";
}
```

### output_to_file

**Description:** true/false whether to send collected output to
file(s)

Filenames are chosen automatically and placed in the
`WORKDIR/outputs/hostname_runagent.out`.

**Type:** [`boolean`][boolean]

**Default value:** false

**Example:**

```cf3
body runagent control
{
  output_to_file => "true";
}
```

### output_directory

**Description:** Directory where the output is stored

Defines the location for parallelized output to be saved when
running `cf-runagent` in parallel mode.

**Type:** `string`

**Allowed input range:** `"?(/.*)`

**Example:**

```cf3
body runagent control
{
  output_directory => "/tmp/run_output";
}
```

**History:** Was introduced in version 3.2.0, Enterprise 2.1.0 (2011)

### timeout

**Description:** Connection timeout in seconds

**Type:** `int`

**Allowed input range:** `1,9999`

**Examples**:

```cf3
body runagent control
{
  timeout => "10";
}
```

**See also:** [body `copy_from` timeout][files#timeout], [agent `default_timeout`][cf-agent#default_timeout]

## Sockets

`cf-runagent` can be triggered by writing a hostname or IP into a socket provided by `cf-execd`.

**Notes:**

* Unlike execution triggered with the `cf-runagent` binary, there is currently no capability to define additional options like defining additional classes, or the remote bundlesequence.

**Example:**

```console
echo 'host001' > /var/cfengine/state/cf-execd.sockets/cf-runagent.socket
```

**See also:** [`cf-execd`][cf-execd], [`runagent_socket_allow_users`][cf-execd#runagent_socket_allow_users]

**History:**

* 3.18.0 Added socket for triggering `cf-runagent` by hostname or IP.
