---
layout: default
title: network_connections
published: true
tags: [reference, network functions, functions, network_connections, network, connections, inet, inet6, tcp, tcp6, udp, udp6]
---

[%CFEngine_function_prototype(regex)%]

**Description:** Return the list of current network connections.

[%CFEngine_function_attributes(regex)%]

The returned data container has four keys:

* `tcp` has all the TCP connections over IPv4
* `tcp6` has all the TCP connections over IPv6
* `udp` has all the UDP connections over IPv4
* `udp6` has all the UDP connections over IPv6

Under each key, there's an array of connection objects that all look like this:

```
      {
        "local": {
          "address": "...source address...",
          "port": "...source port..."
        },
        "remote": {
          "address": "...remote address...",
          "port": "...remote port..."
        },
        "state": "...connection state..."
      }
```

The address will be either IPv4 or IPv6 as appropriate. The port will
be an integer stored as a string. The state will be a string like
`UNKNOWN`.

**Note:** This function is supported on Linux.

On Linux, usually a state of `UNKNOWN` and a remote address `0.0.0.0`
or `0:0:0:0:0:0:0:0` with port `0` mean this is a listening IPv4 and
IPv6 server. In addition, usually a local address of `0.0.0.0` or
`0:0:0:0:0:0:0:0` means the server is listening on every IPv4 or IPv6
interface, while `127.0.0.1` (the IPv4 localhost address) or
`0:100:0:0:0:0:0:0` means the server is only listening to connections
coming from the same machine.

A state of `ESTABLISHED` usually means you're looking at a live
connection.

On Linux, all the data is collected from the files `/proc/net/tcp`,
`/proc/net/tcp6`, `/proc/net/udp`, and `/proc/net/udp6`.

**Example:**

```cf3
    vars:
      "connections" data => network_connections();
```

Output:

The SSH daemon:

```
   {
     "tcp": [
      {
        "local": {
          "address": "0.0.0.0",
          "port": "22"
        },
        "remote": {
          "address": "0.0.0.0",
          "port": "0"
        },
        "state": "UNKNOWN"
      }
    ]
   }
```

The printer daemon listening only to local IPv6 connections on port `631`:

```
    "tcp6": [
      {
        "local": {
          "address": "0:100:0:0:0:0:0:0",
          "port": "631"
        },
        "remote": {
          "address": "0:0:0:0:0:0:0:0",
          "port": "0"
        },
        "state": "UNKNOWN"
      }
   ]
```

An established connection on port 2200:

```
     "tcp": [
      {
        "local": {
          "address": "192.168.1.33",
          "port": "2200"
        },
        "remote": {
          "address": "1.2.3.4",
          "port": "8533"
        },
        "state": "ESTABLISHED"
      }
    ]
```

**History:** Introduced in CFEngine 3.9

**See also:** `sys.inet`, `sys.inet6`.
