---
layout: default
title: isipinsubnet
published: true
tags: [reference, communication functions, functions, subnet, networking, IPv4, IP, isipinsubnet]
---

[%CFEngine_function_prototype(range, ip_address1, ip_address2, ...)%]

**Description:** Returns whether the given `range` contains any of the following IP addresses.

[%CFEngine_function_attributes(range, ip_address1, ip_address2, ...)%]

**Example:**

Run:

[%CFEngine_include_snippet(isipinsubnet.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(isipinsubnet.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**See Also:** [iprange][iprange()], [host2ip][host2ip()], [ip2host][ip2host()]

**History:** Was introduced in CFEngine 3.10.
