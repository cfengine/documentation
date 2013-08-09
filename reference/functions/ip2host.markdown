---
layout: default
title: ip2host
categories: [Reference, Functions, ip2host]
published: true
alias: reference-functions-ip2host.html
tags: [reference, communication functions, functions, ip2host]
---

[%CFEngine_function_prototype(ip)%]

**Description:** Returns the primary name-service host name for the IP address 
`ip`.

Uses whatever configured name service is used by the resolver library to
translate an IP address to a hostname. IPv6 addresses will also resolve,
if supported by the resolver library.

Note that DNS lookups may take time and thus cause CFEngine agents to
wait for responses, slowing their progress significantly.

[%CFEngine_function_attributes(ip)%]

**Example:**

```cf3
bundle agent reverse_lookup
{
vars:
 "local4" string => ip2host("127.0.0.1");
 "local6" string => ip2host("::1");


reports:
  "local4 is $(local4)";
  "local6 is $(local6)";
}
```

**History:** Was introduced in version 3.1.3, Nova 2.0.2 (2010)
