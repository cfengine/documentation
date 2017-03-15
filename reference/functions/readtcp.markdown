---
layout: default
title: readtcp
published: true
tags: [reference, communication functions, functions, readtcp, cached function]
---

[%CFEngine_function_prototype(hostnameip, port, sendstring, maxbytes)%]

**Description:** Connects to tcp ```port``` of `hostnameip`, sends `sendstring`,
reads at most `maxbytes` from the response and returns those.

If the send string is empty, no data are sent or received from the
socket. Then the function only tests whether the TCP port is alive and
returns an empty string.

Not all Unix TCP read operations respond to signals for interruption, so
poorly formed requests can block the `cf-agent` process. Always test TCP
connections fully before deploying.

[%CFEngine_function_attributes(host, port, sendstring, maxbytes)%]

**Example:**

[%CFEngine_include_snippet(readtcp.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

```
R: Server is alive
```

**Notes:** Note that on some systems the timeout mechanism does not seem to
successfully interrupt the waiting system calls so this might hang if you send
an incorrect query string. This should not happen, but the cause has yet to be
diagnosed.

