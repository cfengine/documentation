---
layout: default
title: Function-remoteclassesmatching
categories: [Special-functions,Function-remoteclassesmatching]
published: true
alias: Special-functions-Function-remoteclassesmatching.html
tags: [Special-functions,Function-remoteclassesmatching]
---

### Function remoteclassesmatching

**Synopsis**: remoteclassesmatching(arg1,arg2,arg3,arg4) returns type
**class**

\
 *arg1* : Regular expression, *in the range* .\* \
 *arg2* : Server name or address, *in the range* .\* \
 *arg3* : Use encryption, *in the range* true,false,yes,no,on,off \
 *arg4* : Return class prefix, *in the range*
[a-zA-Z0-9\_\$(){}\\[\\].:]+ \

Read persistent classes matching a regular expression from a remote
cfengine server and add them into local context with prefix

**Example**:\
 \

~~~~ {.verbatim}
 "succeeded" expression => remoteclassesmatching("regex","server","yes","myprefix");
~~~~

**Notes**:\
 \
 This function is only available in Enterprise versions of CFEngine
(Nova, Enterprise, etc).

This function contacts a remote `cf-serverd` and requests access to
defined *persistent classes* on that system. These must be granted
access to by making an `access` promise with `resource_type` set to
`context`.

The return value is true (sets the class) if communication with the
server was successful and classes are populated in the current bundle
with a prefix of your choosing. The arguments are:

*Regular expression*

This should match a list of *persistent* classes of be returned from the
server, if the server has granted access to them. \

*Server*

The name or IP address of the remote server. \

*Encryption*

Boolean value, whether or not to encrypt communication. \

*Prefix*

A string to be added to the returned classes. For example, if the server
defines a persistent class alpha, then this would generate a private
class in the current bundle called myprefix\_alpha.

Note that this function assumes that you have already performed a
successful key exchange between systems, (e.g. using either a remote
copy or `cf-runagent` connection). It contains no mechanism for trust
establishment and will fail if there is no trust relationship
pre-established.
