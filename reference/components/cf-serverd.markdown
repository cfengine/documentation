---
layout: default
title: cf-serverd
published: true
sorting: 20
tags: [Components, cf-serverd]
keywords: [server]
---

`cf-serverd` is a socket listening daemon providing two services: it acts as a
file server for remote file copying and it allows an authorized
`cf-runagent` to start a `cf-agent` run. `cf-agent`
typically connects to a `cf-serverd` instance to request updated policy code,
but may also request additional files for download. `cf-serverd`  employs
[role based access control][roles] (defined in policy code) to authorize
requests.

`cf-serverd` keeps the promises made in `common` and `server` bundles, and is
affected by `common` and `server` control bodies.

**Notes:**

* This daemon reloads it's config when the SIGHUP signal is received.
* If `enable_report_dumps` exists in `WORKDIR` (`/var/cfengine/enable_report_dumps`) `cf-serverd` will log reports provided to `cf-hub` to `WORKDIR/diagnostics/report_dump` (`/var/cfengine/diagnostics/report_dumps`). This data is useful when troubleshooting reporting issues with CFEngine Enterprise.
* `cf-serverd` always considers the class ```server``` to be defined.

**History:**

- SIGHUP behavior added in 3.7.0
- `enable_report_dumps` added in 3.16.0

## Command reference ##

[%CFEngine_include_snippet(cf-serverd.help, [\s]*--[a-z], ^$)%]

## Control Promises

Settings describing the details of the fixed behavioral promises made by
`cf-serverd`. Server controls are mainly about determining access policy for
the connection protocol: i.e. access to the server itself. Access to specific
files must be granted in addition.

```cf3
    body server control
    {
        allowconnects         => { "127.0.0.1" , "::1" };
        allowallconnects      => { "127.0.0.1" , "::1" };

        # Uncomment me under controlled circumstances
        #trustkeysfrom         => { "127.0.0.1" , "::1" };
    }
```


### allowconnects

**Description:** List of IP addresses that may connect to the
server port. They are denoted in either IP or subnet form. For
compatibility reasons, regular expressions are also accepted.

This is the first line of defence; clients who are not
in this list may not connect or send any data to the server.

See also the warning about regular expressions in
[`allowallconnects`][cf-serverd#allowallconnects].

**Type:** `slist`

**Allowed input range:** (arbitrary string)

**Examples**:

```cf3
    allowconnects => {
         "127.0.0.1",
         "::1",
         "200.1.10.0/24",
         "200\.1\.10\..*",
         };
```


### allowallconnects

**Description:** List of IP addresses that may have more than one
connection to the server port. They are denoted in either IP or subnet
form. For compatibility reasons, regular expressions are also accepted.

The clients that are not listed here may have only one open connection
at the time with the server.

Note that `127.0.0.1` is a regular expression (i.e., "127 any
character 0 any character 0 any character 1"), but this will only
match the IP address `127.0.0.1`. Take care with IP addresses and
domain names, as the hostname regular expression `www.domain.com`
will potentially match more than one hostname (e.g.,
`wwwxdomain.com`, in addition to the desired hostname
`www.domain.com`).

**Type:** `slist`

**Allowed input range:** (arbitrary string)

**Examples**:

```cf3
    allowallconnects      => {
         "127.0.0.1",
         "::1",
         "200.1.10.0/24",
         "200\.1\.10\..*",
         };
```


### allowlegacyconnects

**Description:** List of hosts from which the server accepts connections
that are not using the latest protocol.

To define subnets or address ranges, use CIDR notation:

```cf3
    allowlegacyconnects =>  { "192.168.1.0/24", "192.168.2.123" }
```

In CFEngine <= 3.8, absence of this attribute means that connections from all hosts are accepted,
for compatibility with pre-3.6 CFEngine versions.

Set this attribute to an empty list to not allow any incoming connections
using legacy protocol versions:

```cf3
    allowlegacyconnects => { }
```

In CFEngine >= 3.9, legacy protocol is disallowed by default, and you have to
specify a list of hosts allowed to use the legacy protocol.

[%CFEngine_promise_attribute()%]

**See also:** [`protocol_version`][Components#protocol_version]


### allowciphers

**Description:** List of TLS ciphers the server accepts for **incoming** connections.
For a list of possible ciphers, see man page for "openssl ciphers".

[%CFEngine_promise_attribute(AES256-GCM-SHA384:AES256-SHA)%]

**Example:**

```cf3
body server control
{
      # Only this non-default cipher is to be accepted
      allowciphers    => "RC4-MD5";
}
```

**Note:** When used with
[`protocol_version`][Components#protocol_version] 1 (classic protocol),
this does not do anything as the classic protocol does not support TLS ciphers.

**See also:**
[`protocol_version`][Components#protocol_version],
[`tls_ciphers`][Components#tls_ciphers],
[`tls_min_version`][Components#tls_min_version],
[`allowtlsversion`][cf-serverd#allowtlsversion],
[`encrypt`][files#encrypt],
[`logencryptedtransfers`][cf-serverd#logencryptedtransfers],
[`ifencrypted`][access#ifencrypted]

**History:** Introduced in CFEngine 3.6.0


### allowtlsversion

**Description:** Minimum TLS version allowed for **incoming** connections.

[%CFEngine_promise_attribute(1.0)%]

**Example:**

```cf3
body server control
{
      # Allow only TLSv1.1 or higher
      allowtlsversion => "1.1";
}
```

**Note:** When used with
[`protocol_version`][Components#protocol_version] 1 (classic protocol),
this attribute does not do anything.

**See also:**
[`protocol_version`][Components#protocol_version],
[`tls_ciphers`][Components#tls_ciphers],
[`tls_min_version`][Components#tls_min_version],
[`allowciphers`][cf-serverd#allowciphers],
[`encrypt`][files#encrypt],
[`logencryptedtransfers`][cf-serverd#logencryptedtransfers],
[`ifencrypted`][access#ifencrypted]

**History:** Introduced in CFEngine 3.7.0


### allowusers

**Description:** List of usernames who may execute requests from this
server

The usernames listed in this list are those asserted as public key
identities during client-server connections. These may or may not
correspond to system identities on the server-side system.

**Type:** `slist`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
    allowusers => { "cfengine", "root" };
```


### bindtointerface

**Description:** IP of the interface to which the server should bind
on multi-homed hosts

On multi-homed hosts, the server and client can bind to a specific
interface for server traffic. The IP address of the interface must
be given as the argument, not the device name.

**Type:** `string`

**Allowed input range:** (arbitrary string)

```cf3
    bindtointerface => "192.168.1.1";
```

To bind to all interfaces, including IPV6:

```cf3
    bindtointerface => "::";
```

Note that a bug in netstat will not correctly report that cf-serverd is
listening on both IPV4 and IPV6 interfaces. A test with netcat (nc) will
confirm.

```cf3
   # nc -v -4 172.16.100.1 5308
   Connection to 172.16.100.1 5308 port [tcp/cfengine] succeeded!
   ^C
   # nc -v -6 fe80:470:1d:a2f::2 5308
   Connection to fe80:470:1d:a2f::2 5308 port [tcp/cfengine] succeeded!
   ^C
```


### cfruncommand

**Description:** Path to the cf-agent command or cf-execd wrapper for
remote execution

It is normal for this to point to the location of `cf-agent` but it
could also point to the `cf-execd`, or even another program or
shell command at your own risk.

**Type:** `string`

**Allowed input range:** `.+`


```cf3
    body server control
    {
    cfruncommand => "/var/cfengine/bin/cf-agent";
    }
```

**See also:** [cf-runagent][cf-runagent], [bundle resource_type in server access promises][access#resource_type]

### call_collect_interval

**CFEngine Enterprise only.**

**Description:** The interval in minutes in between collect calls to
the CFEngine Server offering a tunnel for report collection.

If option time is set, it causes the server daemon to peer with a
policy hub by attempting a connection at regular intervals of the
value of the parameter in minutes.

This feature is designed to allow Enterprise report collection from
hosts that are not directly addressable from a hub data-aggregation
process. For example, if some of the clients of a policy hub are
behind NAT or firewall then the hub possibly is not able to
open a connection to port 5308 of the client. The solution is to
enable `call_collect_interval` on the client's cf-serverd.
**Note:** also remember to admit the client's IP on the hub's
`collect_calls` ACL (see `resource_type` in
bundle server `access_rules`).

If this option is set, the client's `cf-serverd` will "peer" with
the server daemon on a policy hub. This means that, `cf-serverd` on
an unreachable (e.g. NATed) host will attempt to report in to the
`cf-serverd` on its assigned policy hub and offer it a short time
window in which to download reports over the established
connection. The effect is to establish a temporary secure tunnel
between hosts, initiated from the satellite host end. The
connection is made in such a way that host autonomy is not
compromised. Either hub may refuse or decline to play their role at
any time, in the usual way (avoiding DOS attacks). Normal access
controls must be set for communication in both directions.

Collect calling cannot be as efficient as data collection by the
`cf-hub`, as the hub is not able to load balance. Hosts that use this
approach should exclude themselves from the cf-hub data
collection.

The sequence of events is this:

-   The host's `cf-serverd` connects to its registered CFEngine Server
-   The host identifies itself to authentication and access
    control and sends a collect-call pull-request to the server
-   The server might honor this, if the access control grants access.
-   If access is granted, the server has `collect_window` seconds to
    initiate a query to the host for its reports.
-   The server identifies itself to authentication and access
    control and sends a query request to the host to collect the
    reports.
-   When finished, the host closes the tunnel.

**Type:** `int`

**Allowed input range:** `0,99999999999`

**Example:**

    call_collect_interval => "5";

The full configuration to enable client initiated reporting would look something like this:

```cf3
#########################################################
# Server config
#########################################################

body server control
{
  allowconnects         => { "10.10.10.0/24" , "::1" };
  allowallconnects      => { "10.10.10.0/24" , "::1" };
  trustkeysfrom         => { "10.10.10.0/24" , "::1" };

  call_collect_interval => "5";
}

#########################################################

bundle server my_access_rules()
{
  access:

    policy_server::

     "collect_calls"
         resource_type => "query",
               admit   => { "10.10.10.10" },
               comment => "The policy server must admit queries for collect_calls (client initated reporting).";

    satellite_hosts::

      "delta"
               comment => "Grant access to cfengine hub to collect report deltas",
         resource_type => "query",
               admit   => { "policy_hub" };

      "full"
              comment => "Grant access to cfengine hub to collect full report dump",
        resource_type => "query",
              admit   => { "policy_hub"  };
}
```

**Note:** In the [Masterfiles Policy Framework][Masterfiles Policy Framework], `body server control` and default access rules are found in `controls/cf_serverd.cf`.

**History:** Was introduced in Enterprise 3.0.0 (2012)


### collect_window

**CFEngine Enterprise only.**

**Description:** A time in seconds that a collect-call tunnel remains
open to a hub to attempt a report transfer before it is closed

**Type:** `int`

**Allowed input range:** `0,99999999999`

    collect_window => "15";

**Default value:** 30.

**History:** Was introduced in Enterprise 3.0.0 (2012)


### denybadclocks

**Description:** true/false accept connections from hosts with clocks
that are out of sync

A possible form of attack on the fileserver is to request files
based on time by setting the clocks incorrectly. This option
prevents connections from clients whose clocks are drifting too far
from the server clock (where "too far" is currently defined as
"more than an hour off"). This serves as a warning about clock
asynchronization and also a protection against Denial of Service
attempts based on clock corruption.

**Type:** [`boolean`][boolean]

**Default value:** true

**Example:**

```cf3
    body server control
    {
    denybadclocks => "true";
    }
```


### denyconnects

**Description:** List of IPs that may NOT connect to the
server port

Hosts or IP addresses that are explicitly denied access. This
should only be used in special circumstances. One should never
grant generic access to everything and then deny special cases.
Since the default server behavior is to grant no access to
anything, this list is unnecessary unless you have already granted
access to some set of hosts using a generic pattern, to which you
intend to make an exception.

See also the warning about regular expressions in
[`allowallconnects`][cf-serverd#allowallconnects].

**Type:** `slist`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
    body server control
    {
    denyconnects => { "badhost\.domain\.evil", "host3\.domain\.com" };
    }
```


### logallconnections

**Deprecated: This attribute was deprecated in 3.7.0.**

### logencryptedtransfers

**Description:** true/false log all successful transfers required to
be encrypted. Only applies to classic protocol connections
(because the new protocol uses TLS which enforces encryption for everything).

If true the server will log all transfers of files which the server
requires to encrypted in order to grant access (see `ifencrypted`)
to syslog. These files are deemed to be particularly sensitive.

**Type:** [`boolean`][boolean]

**Default value:** false

**Example:**

```cf3
    body server control
    {
    logencryptedtransfers => "true";
    }
```

**See also:** [`ifencrypted`][access#ifencrypted], [`encrypt`][files#encrypt], [`tls_ciphers`][Components#tls_ciphers], [`tls_min_version`][Components#tls_min_version], [`allowciphers`][cf-serverd#allowciphers], [`allowtlsversion`][cf-serverd#allowtlsversion], [`protocol_version`][Components#protocol_version]


### maxconnections

**Description:** Maximum number of concurrent connections the server
  will accept. Recommended value for a hub is **two times the total
  number of hosts bootstrapped to this hub**.

**Type:** `int`

**Allowed input range:** `0,99999999999`

**Default value:** 30

**Example:**

```cf3
    # client side

    body agent control
    {
    maxconnections => "1000";
    }

    # server side

    body server control
    {
    maxconnections => "1000";
    }
```


### port

**Description:** Default port for the CFEngine server

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

### serverfacility

**Description:** Menu option for syslog facility level

**Type:** (menu option)

**Allowed input range:**

    LOG_USER
    LOG_DAEMON
    LOG_LOCAL0
    LOG_LOCAL1
    LOG_LOCAL2
    LOG_LOCAL3
    LOG_LOCAL4
    LOG_LOCAL5
    LOG_LOCAL6
    LOG_LOCAL7

See syslog notes.

**Default value:** `LOG_USER`

**Example:**

```cf3
    body server control
    {
    serverfacility => "LOG_USER";
    }
```


### skipverify

**Description:** This option is obsolete, does nothing and is retained
for backward compatibility.

**Type:** `slist`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
    body server control
    {
    skipverify => { "special_host.*", "192.168\..*" };
    }
```


### trustkeysfrom

**Description:** List of IPs from whom the server will accept and trust
new (untrusted) public keys.  They are denoted in either IP or subnet
form. For compatibility reasons, regular expressions are also
accepted.

The new accepted public keys are written to the `ppkeys`
directory, and a message is logged:

```
192.168.122.254> Trusting new key: MD5=0d5603d68dd62d35bab2150e35d055ae
```

**NOTE:** `trustkeysfrom` should normally be an empty list except in
controlled circumstances, for example when the network is being set up
and keys are to be exchanged for the first time.

See also the warning about regular expressions in
[`allowallconnects`][cf-serverd#allowallconnects].

**Type:** `slist`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
    body server control
    {
    trustkeysfrom => { "10.0.1.1", "192.168.0.0/16"};
    }
```


### listen

**Description:** true/false enable server daemon to listen on defined
port

This attribute allows to disable `cf-serverd` from listening on any
port. Should be used in conjunction with `call_collect_interval`.

This setting only applies to CFEngine clients, the policy hub will
not be affected. Changing this setting requires a restart of
`cf-serverd` for the change to take effect.

**Type:** [`boolean`][boolean]

**Default value:** true

**Example:**

```cf3
    body server control
    {

      listening_host_context::
        listen => "true";

      !listening_host_context::
        listen => "false";
    }
```

**History:** Was introduced in 3.4.0, Enterprise 3.0 (2012)


## Deprecated attributes in body server control

The following attributes were functional in previous versions
of CFEngine, but today they are deprecated, either because
their functionality is being handled trasparently or because
it doesn't apply to current CFEngine version.

* ```auditing```
* ```dynamicaddresses```
* ```hostnamekeys```
* ```keycacheTTL```
