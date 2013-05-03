---
layout: default
title: Function-readtcp
categories: [Special-functions,Function-readtcp]
published: true
alias: Special-functions-Function-readtcp.html
tags: [Special-functions,Function-readtcp]
---

### Function readtcp

**Synopsis**: readtcp(arg1,arg2,arg3,arg4) returns type **string**

\
 *arg1* : Host name or IP address of server socket, *in the range* .\* \
 *arg2* : Port number, *in the range* 0,99999999999 \
 *arg3* : Protocol query string, *in the range* .\* \
 *arg4* : Maximum number of bytes to read, *in the range* 0,99999999999
\

Connect to tcp port, send string and assign result to variable

**Example**:\
 \

~~~~ {.verbatim}
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
~~~~

hostnameip

The host name or IP address of a tcp socket. \

port

The port number to connect to. \

sendstring

A string to send to the TCP port to elicit a response \

maxbytes

The maximum number of bytes to read in response.

Important note: not all Unix TCP read operations respond to signals for
interruption so poorly formed requests can hang. Always test TCP
connections fully before deploying.

**Notes**:\
 \

If the send string is empty, no data are sent or received from the
socket. Then the function only tests whether the TCP port is alive and
returns an empty variable.

Note that on some systems the timeout mechanism does not seem to
successfully interrupt the waiting system calls so this might hang if
you send a query string that is incorrect. This should not happen, but
the cause has yet to be diagnosed.
