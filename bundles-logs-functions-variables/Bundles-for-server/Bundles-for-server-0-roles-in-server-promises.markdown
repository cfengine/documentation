---
layout: default
title: roles-in-server-promises
categories: [Bundles-for-server,roles-in-server-promises]
published: true
alias: Bundles-for-server-roles-in-server-promises.html
tags: [Bundles-for-server,roles-in-server-promises]
---

### `roles` promises in server

\

Roles promises are server-side decisions about which users are allowed
to define soft-classes on the server's system during remote invocation
of `cf-agent`. This implements a form of Role Based Access Control
(RBAC) for pre-assigned class-promise bindings. The user names cited
must be attached to trusted public keys in order to be accepted. The
regular expression is anchored, meaning it must match the entire name
(see [Anchored vs. unanchored regular
expressions](#Anchored-vs_002e-unanchored-regular-expressions)).

~~~~ {.smallexample}
     
      roles:
     
        "regex"
     
           authorize = { "usernames", ... };
     
~~~~

*It is worth re-iterating here that it is not possible to send commands
or modify promise definitions by remote access. At best users may try to
send classes when using*`cf-runagent`*in order to activate sleeping
promises. This mechanism limits their ability to do this*.

\

~~~~ {.verbatim}
bundle server access_rules()

{
roles:

  # Allow mark

  "Myclass_.*"  authorize => { "mark" };
}
~~~~

\

In this example user mark is granted permission to remotely activate
classes matching the regular expression when Mark\_.\* using the
`cf-runagent` to activate CFEngine. In this way one can implement a form
of Role Based Access Control (RBAC), provided users do not have
privileged access on the host directly.

-   [authorize in roles](#authorize-in-roles)

#### `authorize`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: List of public-key user names that are allowed to activate
the promised class during remote agent activation

**Example**:\
 \

~~~~ {.verbatim}
roles:

  ".*"  authorize => { "mark", "marks_friend" };
~~~~

**Notes**:\
 \

Part of Role Based Access Control (RBAC) in CFEngine. The users listed
in this section are granted access to set certain classes by using the
remote `cf-runagent`. The user-names will refer to public key identities
already trusted on the system.
