---
layout: default
title: remotescalar
published: true
tags: [reference, communication functions, functions, remotescalar]
---

**This function is only available in CFEngine Enterprise.**

[%CFEngine_function_prototype(id, server, encrypt)%]

**Description:** Returns a scalar value identified by `id` from a remote CFEngine
`server`. Communication is encrytped depending on ```encrypt```.

If the identifier matches a persistent scalar variable then this will be returned
preferentially. If no such variable is found, then the server will look for a
literal string in a server bundle with a handle that matches the requested object.

The remote system's `cf-serverd` must accept the query for the requested
variable from the host that is requesting it. Access must be granted by making
an `access` promise with `resource_type` set to `literal`.

CFEngine stores the value of this function on the calling host, so that, if the
network is unavailable, the last known value will be used. Hence use of this
function is fault tolerant. Care should be taken in attempting to access
remote variables that are not available, as the repeated connections
needed to resolve the absence of a value can lead to undesirable
behavior. As a general rule, users are recommended to refrain from
relying on the availability of network resources.

[%CFEngine_function_attributes(id, server, encrypt)%]

**Example:**

```cf3
    vars:

     "remote" string => remotescalar("test_scalar","127.0.0.1","yes");
```

```cf3
    bundle server access
    {
    access:
      "value of my test_scalar, can expand variables here - $(sys.host)"
        handle => "test_scalar",
        comment => "Grant access to contents of test_scalar VAR",
        resource_type => "literal",
        admit => { "127.0.0.1" };
    }
```

**Notes:** Note that this function assumes that you have already performed a
successful key exchange between systems, (e.g. using either a remote
copy or `cf-runagent` connection). It contains no mechanism for trust
establishment and will fail if there is no trust relationship
established in advance.

**See also:** `hubknowledge()`, `remoteclassesmatching()`, `hostswithclass()`
