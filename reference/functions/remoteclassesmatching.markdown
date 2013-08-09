---
layout: default
title: remoteclassesmatching
categories: [Reference, Functions, remoteclassesmatching]
published: true
alias: reference-functions-remoteclassesmatching.html
tags: [reference, communication functions, functions, remoteclassesmatching]
---

**This function is only available in CFEngine Enterprise.**

[%CFEngine_function_prototype(regex, server, encrypt, prefix)%]

**Description:** Reads persistent classes matching regular expression `regex`
from a remote CFEngine server `server` and adds them into local context with 
prefix `prefix`.

The return value is true (sets the class) if communication with the server was 
successful and classes were populated in the current bundle.

This function contacts a remote `cf-serverd` and requests access to defined 
*persistent classes* on that system. Access must be granted by making an 
`access` promise with `resource_type` set to `context`.

[%CFEngine_function_attributes(regex, server, encrypt, prefix)%]

**Example:**

```cf3
   "succeeded" expression => remoteclassesmatching("regex","server","yes","myprefix");
```

**Notes:** Note that this function assumes that you have already performed a
successful key exchange between systems, (e.g. using either a remote
copy or `cf-runagent` connection). It contains no mechanism for trust
establishment and will fail if there is no trust relationship
pre-established.
