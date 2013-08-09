---
layout: default
title: host2ip
categories: [Reference, Functions, host2ip]
published: true
alias: reference-functions-host2ip.html
tags: [reference, communication functions, functions, host2ip]
---

[%CFEngine_function_prototype(hostname)%]

**Description:** Returns the primary name-service IP address for the named host `hostname`.

Uses whatever configured name service is used by the resolver library to
translate `hostname` into an IP address. It will return an IPv6 address
by preference if such an address exists. This function uses the standard
lookup procedure for a name, so it mimics internal processes and can
therefore be used not only to cache multiple lookups in the configuration, but 
to debug the behavior of the resolver.

[%CFEngine_function_attributes(hostname)%]

**Example:**

```cf3
    bundle server control
    {
      allowconnects         => { escape(host2ip("www.example.com")) };
    }
```

**History:** This function was introduced in CFEngine version 3.0.4
(2010)
