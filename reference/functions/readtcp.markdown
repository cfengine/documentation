---
layout: default
title: readtcp
categories: [Reference, Functions, readtcp]
published: true
alias: reference-functions-readtcp.html
tags: [reference, communication functions, functions, readtcp]
---

[%CFEngine_function_prototype(hostnameip, port, sendstring, maxbytes)%]

**Description:** Connects to tcp `port` of `hostnameip`, sends `sendstring`,
reads at most `maxbytes` from the response and returns those.

If the send string is empty, no data are sent or received from the
socket. Then the function only tests whether the TCP port is alive and
returns an empty string.

Not all Unix TCP read operations respond to signals for interruption, so 
poorly formed requests can block the `cf-agent` process. Always test TCP 
connections fully before deploying.

[%CFEngine_function_attributes(host, port, sendstring, maxbytes)%]

**Example:**

```cf3
    bundle agent example
    {     
    vars:

      "my80" string => readtcp("research.iu.hio.no","80","GET /index.php HTTP/1.1$(const.r)$(const.n)Host: research.iu.hio.no$(const.r)$(const.n)$(const.r)$(const.n)",20);

    classes:

      "server_ok" expression => regcmp("[^\n]*200 OK.*\n.*","$(my80)");

    reports:

      server_ok::

        "Server is alive";

      !server_ok::

        "Server is not responding - got $(my80)";
    }
```

**Notes:** Note that on some systems the timeout mechanism does not seem to
successfully interrupt the waiting system calls so this might hang if you send 
an incorrect query string. This should not happen, but the cause has yet to be 
diagnosed.

