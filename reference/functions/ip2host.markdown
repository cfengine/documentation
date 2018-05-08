---
layout: default
title: ip2host
published: true
tags: [reference, communication functions, functions, ip2host, cached function]
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

[%CFEngine_include_snippet(ip2host.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(ip2host.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**See Also:** `host2ip()`, `iprange()`, `isipinsubnet()`

**History:** Was introduced in version 3.1.3, Nova 2.0.2 (2010)
