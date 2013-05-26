---
layout: default
title: runagent control promises
categories: [Reference, Components, cf-runagent, runagent control promises]
published: true
alias: reference-components-cfrunagent-control-promises.html
tags: [Components, cf-runagent, control promises]
---

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


## `hosts`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: List of host or IP addresses to attempt connection
with

    body runagent control
    {
    network1::
      hosts => { "host1.example.org", "host2", "host3" };
    
    network2::
      hosts => { "host1.example.com", "host2", "host3" };
    }

**Notes**:

The complete list of contactable hosts. The values may be either
numerical IP addresses or DNS names, optionally suffixed by a ':'
and a port number. If no port number is given, the default CFEngine
port 5308 is assumed.


## `port`

**Type**: int

**Allowed input range**: `1024,99999`

**Default value:** 5308

**Synopsis**: Default port for cfengine server

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

**Notes**:

The standard or registered port number is tcp/5308. CFEngine does
not presently use its registered udp port with the same number, but
this could change in the future.

Changing the standard port number is not recommended practice. You
should not do it without a good reason.


## `force_ipv4`

**Type**: (menu option)

**Allowed input range**:

    true
    false
    yes
    no
    on
    off

**Default value:** false

**Synopsis**: true/false force use of ipv4 in connection

    body copy_from example
    {
    force_ipv4 => "true";
    }

**Notes**:

IPv6 should be harmless to most users unless you have a partially
or misconfigured setup.


## `trustkey`

**Type**: (menu option)

**Allowed input range**:

    true
    false
    yes
    no
    on
    off

**Default value:** false

**Synopsis**: true/false automatically accept all keys on trust
from servers

    body copy_from example
    {
    trustkey => "true";
    }

**Notes**:

If the server's public key has not already been trusted, this
allows us to accept the key in automated key-exchange.

Note that, as a simple security precaution, trustkey should
normally be set to 'false', to avoid key exchange with a server one
is not one hundred percent sure about, though the risks for a
client are rather low. On the server-side however, trust is often
granted to many clients or to a whole network in which possibly
unauthorized parties might be able to obtain an IP address, thus
the trust issue is most important on the server side.

As soon as a public key has been exchanged, the trust option has no
effect. A machine that has been trusted remains trusted until its
key is manually revoked by a system administrator. Keys are stored
in WORKDIR/ppkeys.


## `encrypt`

**Type**: (menu option)

**Allowed input range**:

    true
    false
    yes
    no
    on
    off

**Default value:** false

**Synopsis**: true/false encrypt connections with servers

    body copy_from example
    {
    servers  => { "remote-host.example.org" };
    encrypt => "true";
    }

**Notes**:

Client connections are encrypted with using a Blowfish randomly
generated session key. The intial connection is encrypted using the
public/private keys for the client and server hosts.


ren`

**Type**: (menu option)

**Allowed input range**:

    true
    false
    yes
    no
    on
    off

**Default value:** false

**Synopsis**: true/false parallelize connections to servers

    body runagent control
    {
    background_children => "true";
    }

**Notes**:

Causes the runagent to attempt parallelized connections to the
servers.


## `max_children`

**Type**: int

**Allowed input range**: `0,99999999999`

**Default value:** 50 runagents

**Synopsis**: Maximum number of simultaneous connections to
attempt

    body runagent control
    {
    max_children => "10";
    }
    
    # or
    
    body agent control
    {
    max_children => "10";
    }

**Notes**:

For the run-agent this represents the maximum number of forked
background processes allowed when parallelizing connections to
servers. For the agent it represents the number of background jobs
allowed concurrently. Background jobs often lead to contention of
the disk resources slowing down tasks considerably; there is thus a
law of diminishing returns.


## `output_to_file`

**Type**: (menu option)

**Allowed input range**:

    true
    false
    yes
    no
    on
    off

**Default value:** false

**Synopsis**: true/false whether to send collected output to
file(s)

    body runagent control
    {
    output_to_file => "true";
    }

**Notes**:

Filenames are chosen automatically and placed in the
WORKDIR/outputs/hostname\_runagent.out.


## `output_directory`

**Type**: string

**Allowed input range**: `"?(/.*)`

**Synopsis**: Directory where the output is stored

    body runagent control
    {
    output_directory => "/tmp/run_output";
    }

**Notes**:

*History*: Was introduced in version 3.2.0, Enterprise 2.1.0 (2011)

Defines the location for parallelized output to be saved when
running `cf-runagent` in parallel mode.


## `timeout`

**Type**: int

**Allowed input range**: `1,9999`

**Synopsis**: Connection timeout, sec

    body runagent control
    {
    timeout => "10";
    }

**Notes**:

Timeout in seconds.

