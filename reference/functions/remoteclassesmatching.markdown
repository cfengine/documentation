---
layout: default
title: remoteclassesmatching
categories: [Reference, Functions, remoteclassesmatching]
published: true
alias: reference-functions-remoteclassesmatching.html
tags: [reference, functions, remoteclassesmatching]
---

**This function is only available in CFEngine Enterprise.**

**Prototype**: `remoteclassesmatching(regex, server, encrypt, prefix)`

**Return type**: `class`

**Description**: Read persistent classes matching regular expression `regex`
from a remote CFEngine server `server` and add them into local context with 
`prefix`.

The return value is true (sets the class) if communication with the server was 
successful and classes were populated in the current bundle.

This function contacts a remote `cf-serverd` and requests access to defined 
*persistent classes* on that system. Access must be granted by making an 
`access` promise with `resource_type` set to `context`.

**Arguments**:

* `regex` : Regular expression, in the range `.*`

This should match a list of *persistent* classes of be returned from the
server, if the server has granted access to them.

* `server` : Server name or address, in the range `.*`

The name or IP address of the remote server.

* `encrypt` : Boolean

Use encryption.

* `prefix` : Return class prefix, in the range
`[a-zA-Z0-9_$(){}\[\].:]+`

A string to be added to the returned classes. If the server defines a 
persistent class `alpha`, then this would generate a private class in the 
current bundle called `prefix_alpha`.

**Example**:

```cf3
   "succeeded" expression => remoteclassesmatching("regex","server","yes","myprefix");
```

**Notes**: Note that this function assumes that you have already performed a
successful key exchange between systems, (e.g. using either a remote
copy or `cf-runagent` connection). It contains no mechanism for trust
establishment and will fail if there is no trust relationship
pre-established.
