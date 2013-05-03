---
layout: default
title: Function-ip2host
categories: [Special-functions,Function-ip2host]
published: true
alias: Special-functions-Function-ip2host.html
tags: [Special-functions,Function-ip2host]
---

### Function ip2host

**Synopsis**: ip2host(arg1) returns type **string**

\
 *arg1* : IP address (IPv4 or IPv6), *in the range* .\* \

Returns the primary name-service host name for the IP address

**Example**:\
 \

~~~~ {.verbatim}
bundle agent reverse_lookup
{
vars:
 "local4" string => ip2host("127.0.0.1");
 "local6" string => ip2host("::1");


reports:
cfengine_3::
  "local4 is $(local4)";
  "local6 is $(local6)";
}
~~~~

**Notes**:\
 \

Uses whatever configured name service is used by the resolver library to
translate an IP address to a hostname. IPv6 addresses will also resolve,
if supported by the resolver library.

Note that DNS lookups may take time and thus cause CFEngine agents to
wait for responses, slowing their progress significantly.

*History*: Was introduced in version 3.1.3, Nova 2.0.2 (2010)
