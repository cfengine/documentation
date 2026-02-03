---
layout: default
title: control_server
aliases:
  - "/reference-special-variables-default:control_server.html"
---

Variables in the `default:control_server` context are automatically created from attributes defined in `body server control` following the pattern `default:default:control_server.<attribute>`.

### default:control_server.allowallconnects

Defines a list of IP addresses or subnets that are allowed to have more than one connection to cf-serverd simultaneously.

**See also:** [allowallconnects in body server control][cf-serverd#Control promises]

### default:control_server.allowconnects

Defines a list of IP addresses or subnets which restricts hosts that are allowed to connect to cf-serverd. This is the first layer of access control in cf-serverd.

**See also:** [allowconnects in body server control][cf-serverd#Control promises]

### default:control_server.allowciphers

Specifies the ciphers that cf-serverd is allowed to use for better security.

**See also:** [allowciphers in body server control][cf-serverd#Control promises]

### default:control_server.allowlegacyconnects

Defines a list of networks that are allowed to connect using the classic/legacy protocol (for clients using protocol versions prior to 3.7.0).

**See also:** [allowlegacyconnects in body server control][cf-serverd#Control promises]

### default:control_server.allowtlsversion

Specifies the minimum TLS version that cf-serverd will accept for connections.

**See also:** [allowtlsversion in body server control][cf-serverd#Control promises]

### default:control_server.call_collect_interval

Configures the interval (in minutes) at which agents will try to report their data to the hub in client initiated reporting mode.

**See also:** [call_collect_interval in body server control][cf-serverd#Control promises]

### default:control_server.collect_window

Controls how long (in seconds) cf-serverd holds an open connection for client initiated reporting. After this time, the connection is closed.

**See also:** [collect_window in body server control][cf-serverd#Control promises]

### default:control_server.maxconnections

Configures the maximum number of connections allowed by cf-serverd. Should be set greater than the number of hosts bootstrapped.

**See also:** [maxconnections in body server control][cf-serverd#Control promises]

### default:control_server.port

Defines the port on which cf-serverd listens for connections.

**See also:** [port in body server control][cf-serverd#Control promises]

### default:control_server.allowusers

Contains a list of usernames who may execute requests from this server.

**See also:** [`allowusers` in `body server control`][cf-serverd#allowusers]

### default:control_server.auditing

A true/false flag to determine whether connections to cf-serverd will be audited. Type: option (boolean). Allowed values: true,false,yes,no,on,off.

**See also:** [`auditing` in `body server control`][cf-serverd#auditing]

### default:control_server.bindtointerface

IP of the interface to which the server should bind on multi-homed hosts. Type: string. Allowed range: (empty).

**See also:** [`bindtointerface` in `body server control`][cf-serverd#bindtointerface]

### default:control_server.cfruncommand

Specifies the command used by cf-runagent to execute cf-agent. Type: string. Allowed range: .+.

**See also:** [`cfruncommand` in `body server control`][cf-serverd#cfruncommand]

### default:control_server.denybadclocks

Controls whether hosts with clocks that are out of sync may connect to the server. Type: option (boolean). Allowed values: true,false,yes,no,on,off.

**See also:** [`denybadclocks` in `body server control`][cf-serverd#denybadclocks]

### default:control_server.denyconnects

Contains a list of IP addresses or subnets that are not allowed to connect to cf-serverd. Type: slist. Allowed range: (empty).

**See also:** [`denyconnects` in `body server control`][cf-serverd#denyconnects]

### default:control_server.dynamicaddresses

Contains IP addresses which should be allowed to re-connect from different IP addresses. Type: slist. Allowed range: (empty).

**See also:** [`dynamicaddresses` in `body server control`][cf-serverd#dynamicaddresses]

### default:control_server.hostnamekeys

Determines whether to label ppkeys by hostname not IP address. This represents a server side choice to base key associations on host names rather than IP address. Type: option (boolean). Allowed values: true,false,yes,no,on,off.

**See also:** [`hostnamekeys` in `body server control`][cf-serverd#hostnamekeys]

### default:control_server.listen

Enables server daemon to listen on defined port. Type: option (boolean). Allowed values: true,false,yes,no,on,off.

**See also:** [`listen` in `body server control`][cf-serverd#listen]

### default:control_server.logallconnections

Controls whether to log all connections to cf-serverd. Type: option (boolean). Allowed values: true,false,yes,no,on,off.

**See also:** [`logallconnections` in `body server control`][cf-serverd#logallconnections]

### default:control_server.logencryptedtransfers

Controls whether to log encrypted file transfers. Type: option (boolean). Allowed values: true,false,yes,no,on,off.

**See also:** [`logencryptedtransfers` in `body server control`][cf-serverd#logencryptedtransfers]

### default:control_server.serverfacility

Controls the syslog facility used by `cf-serverd`. Valid values are `LOG_USER`, `LOG_DAEMON`, `LOG_LOCAL0` through `LOG_LOCAL7`.

**See also:** [`serverfacility` in `body server control`][cf-serverd#serverfacility]

### default:control_server.skipverify

Contains a list of IP addresses or subnets from which to skip verification of source IP address. Type: slist. Allowed range: (empty).

**See also:** [`skipverify` in `body server control`][cf-serverd#skipverify]

### default:control_server.trustkeysfrom

Contains a list of IP addresses or subnets from which keys will be trusted automatically. Type: slist. Allowed range: (empty).

**See also:** [`trustkeysfrom` in `body server control`][cf-serverd#trustkeysfrom]
