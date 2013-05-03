---
layout: default
title: Function-host2ip
categories: [Special-functions,Function-host2ip]
published: true
alias: Special-functions-Function-host2ip.html
tags: [Special-functions,Function-host2ip]
---

### Function host2ip

**Synopsis**: host2ip(arg1) returns type **string**

\
 *arg1* : Host name in ascii, *in the range* .\* \

Returns the primary name-service IP address for the named host

**Example**:\
 \

~~~~ {.verbatim}
bundle server control
{
allowconnects         => { escape(host2ip("www.example.com")) };
}
~~~~

**Notes**:\
 \

Uses whatever configured name service is used by the resolver library to
translate a hostname into an IP address. It will return an IPv6 address
by preference if such an address exists. This function uses the standard
lookup procedure for a name, so it mimics internal processes and can
therefore be used not only to cache multiple lookups in the
configuration, but to debug the behaviour of the resolver.

**History**: This function was introduced in CFEngine version 3.0.4
(2010)
