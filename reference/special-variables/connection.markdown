---
layout: default
title: connection
published: true
tags: [reference, variables, connection]
---

The context `connection` is used by the `shortcut` attribute in `access`
promises to access information about the remote agent requesting access.

```cf3
access:
    "/var/cfengine/cmdb/$(connection.key).json"
      shortcut   => "me.json",
      admit_keys => { "$(connection.key)" };
```

**Note:** The usage of the `connection` variables is strictly limited to
literal strings within the `promiser` and admit/deny lists of `access` promise
types; they cannot be passed into functions or stored in other variables. These
variables can only be used with incoming connections that use
[`protocol_version`][Components#protocol_version] >=2 ( or "latest" ).

### connection.key

This variable contains the public key sha of the connecting client in the form 'SHA=...'.

```cf3
access:
    "/var/cfengine/cmdb/$(connection.key).json"
      shortcut   => "me.json",
      admit_keys => { "$(connection.key)" };
```


### connection.ip

This variable contains the IP address of the connecting remote agent.

```cf3
access:
    "/var/cfengine/cmdb/$(connection.ip).json"
      shortcut   => "myip.json",
      admit_keys => { "$(connection.key)" };
```


### connection.hostname

This variable contains the hostname of the connecting client as determined by a
reverse DNS lookup from `cf-serverd`.

```cf3
access:
    "/var/cfengine/cmdb/$(connection.hostname).json"
      shortcut   => "myhostname.json",
      admit_keys => { "$(connection.key)" };
```

**Note:** Reverse lookups are only performed when necessary. To avoid the
performance impact of reverse dns lookups for each connection avoid using
`admit_hostnames`, using hostnames in your `admit` rules, and these
`connection` variables.

