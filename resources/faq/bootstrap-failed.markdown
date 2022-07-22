---
layout: default
title: Bootstrapping
published: true
tags: [faq]
---

## Why did bootstrap fail?

When I bootstrap a host, I get errors:

- `No suitable server found for '<path>'`
- `No suitable server responded to hail`
- `Authentication dialogue with '<IP>' failed`
- `Protocol transaction broken off (1). (ReceiveTransaction: Connection reset by peer)`
- `Couldn't receive. (recv: Connection reset by peer)`
- `Failed to establish TLS connection: underlying network error ()`
- `Failed to establish TLS connection: underlying network error (Connection reset by peer)`

These types of errors typically indicate a problem with access.

To troubleshoot these types of errors review `cf-serverd` summary of access promises. `allowconnects` in `body server control` and `trustkeysfrom` in `body server control` should also be reviewed.

### `cf-serverd` summary of access promises

cf-serverd provides a summary of access promises in *verbose* logs. Use this to see if `cf-serverd` is allowing access to the client.

Run cf-serverd with verbose logging and inspect the summary of access promises:

```console
cf-serverd -v | awk '/=== BEGIN summary of access promises ===/,/=== END summary of access promises ===/'
```

Example Output:

```
verbose:  === BEGIN summary of access promises ===
verbose: Host IPs allowed connection access (allowconnects):
verbose:       IP: 192.168.56.2/16
verbose:       IP: ::1
verbose:       IP: 127.0.0.1
verbose: Host IPs denied connection access (denyconnects):
verbose: Host IPs allowed multiple connection access (allowallconnects):
verbose:       IP: 192.168.56.2/16
verbose:       IP: ::1
verbose:       IP: 127.0.0.1
verbose: Host IPs whose keys we shall establish trust to (trustkeysfrom):
verbose:       IP: 0.0.0.0/0
verbose: Host IPs allowed legacy connections (allowlegacyconnects):
verbose: Users from whom we accept cf-runagent connections (allowusers):
verbose: Access control lists:
verbose:       Path: /usr/bin/bash
verbose:               admit_ips: 192.168.56.2
verbose:       Path: /var/cfengine/bin/
verbose:               admit_ips: 192.168.56.2/16
verbose:       Path: /var/cfengine/cmdb/$(connection.key)/
verbose:               admit_keys: $(connection.key)
verbose:       Path: /var/cfengine/data/
verbose:               admit_ips: 192.168.56.2/16
verbose:       Path: /var/cfengine/master_software_updates/
verbose:               admit_ips: 192.168.56.2/16
verbose:       Path: /var/cfengine/masterfiles/
verbose:               admit_ips: 192.168.56.2/16
verbose:       Path: /var/cfengine/masterfiles/.no-distrib/
verbose:               deny_ips: 0.0.0.0/0
verbose:       Path: /var/cfengine/modules/
verbose:               admit_ips: 192.168.56.2/16
verbose:       Query: collect_calls
verbose:               admit_ips: 192.168.56.2/16
verbose:       Query: delta
verbose:               admit_ips: 127.0.0.1
verbose:               admit_ips: 192.168.56.2
verbose:               admit_ips: ::1
verbose:       Query: full
verbose:               admit_ips: 127.0.0.1
verbose:               admit_ips: 192.168.56.2
verbose:               admit_ips: ::1
verbose:       Query: rebase
verbose:               admit_ips: 127.0.0.1
verbose:               admit_ips: 192.168.56.2
verbose:               admit_ips: ::1
verbose:       Role: .*
verbose: Access control lists for the classic network protocol:
verbose:       Path: /var/cfengine/masterfiles
verbose:               admit: 192.168.56.2/16
verbose:       Path: /var/cfengine/bin
verbose:               admit: 192.168.56.2/16
verbose:       Path: /var/cfengine/data
verbose:               admit: 192.168.56.2/16
verbose:       Path: /var/cfengine/modules
verbose:               admit: 192.168.56.2/16
verbose:       Path: /var/cfengine/master_software_updates
verbose:               admit: 192.168.56.2/16
verbose:       Path: /usr/bin/bash
verbose:               admit: 192.168.56.2
verbose:       Path: /var/cfengine/masterfiles/.no-distrib
verbose:               deny: 0.0.0.0/0
verbose: Object: collect_calls
verbose: Admit '192.168.56.2/16' root=
verbose: Object: delta
verbose: Admit '192.168.56.2' root=
verbose: Admit '::1' root=
verbose: Admit '127.0.0.1' root=
verbose: Object: rebase
verbose: Admit '192.168.56.2' root=
verbose: Admit '::1' root=
verbose: Admit '127.0.0.1' root=
verbose: Object: full
verbose: Admit '192.168.56.2' root=
verbose: Admit '::1' root=
verbose: Admit '127.0.0.1' root=
verbose: Object collect_calls
verbose: Object delta
verbose: Object rebase
verbose: Object full
verbose:  === END summary of access promises ===
```

**Notes:**

* If the summary of access promises looks correct, it may be that `cf-serverd` has not reloaded with a new access rule.

    Try stopping `cf-serverd` and starting it in the foreground with verbose logging (`cf-serverd --no-fork --log-level verbose`) and look for logs related to the client that was failing.

### `allowconnects` in `body server control`

In order for a host to communicate it must be within an IP range that is allowed to connect to the server.

`cf-serverd` logs errors when a host not in allow connects tries to communicate.

* `Remote host '<ip>' not in allowconnects, denying connection`

**Notes:**

* `def.acl` in the Masterfiles Policy Framework is included in this list by default.

See also: [`def.acl`][Masterfiles Policy Framework#acl], [`def.trustkeysfrom`][Masterfiles Policy Framework#trustkeysfrom]

### `trustkeysfrom` in `body server control`

This defines networks from which a host will automatically trust hosts. If you do not use automatic trust establishment you must arrange trust separately. The [Secure Bootstrap guide][Secure Bootstrap] details a step-by-step procedure to securely bootstrap hosts.

`cf-serverd` logs verbose and notice messages relating to un-trusted clients trying to connect:

* `notice: 192.168.56.4>    TRUST FAILED, peer presented an untrusted key, dropping connection!`
* `verbose: 192.168.56.4>    Did not find new key format '/var/cfengine/ppkeys/root-SHA=85f8a23d6738599e03951e6930e661bcd9bb3ae12f32486c9795cc9baa7d5b4e.pub'`
* `verbose: 192.168.56.4>    Trying old style '/var/cfengine/ppkeys/root-192.168.56.4.pub'`
* `verbose: 192.168.56.4>    Received key 'SHA=85f8a23d6738599e03951e6930e661bcd9bb3ae12f32486c9795cc9baa7d5b4e' not found in ppkeys`

See also: [`def.acl`][Masterfiles Policy Framework#acl], [`def.trustkeysfrom`][Masterfiles Policy Framework#trustkeysfrom]
