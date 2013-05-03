---
layout: default
title: Function-remotescalar
categories: [Special-functions,Function-remotescalar]
published: true
alias: Special-functions-Function-remotescalar.html
tags: [Special-functions,Function-remotescalar]
---

### Function remotescalar

**Synopsis**: remotescalar(arg1,arg2,arg3) returns type **string**

\
 *arg1* : Variable identifier, *in the range*
[a-zA-Z0-9\_\$(){}\\[\\].:]+ \
 *arg2* : Hostname or IP address of server, *in the range* .\* \
 *arg3* : Use enryption, *in the range* true,false,yes,no,on,off \

Read a scalar value from a remote cfengine server

**Example**:\
 \

~~~~ {.verbatim}
vars:

 "remote" string => remotescalar("test_scalar","127.0.0.1","yes");
~~~~

**Notes**:\
 \
 The remote system's cf-serverd must accept the query for the requested
variable from the host that is requesting it. An example of this
configuration follows.

This function asks for an identifier. It is up to the server to
interpret what this means and to return a value of its choosing. If the
identifier matches a persistent scalar variable then this will be
returned preferentially. If no such variable is found, then the server
will look for a literal string in a server bundle with a handle that
matches the requested object.

~~~~ {.verbatim}
bundle server access
{
access:
  "value of my test_scalar, can expand variables here - $(sys.host)"
    handle => "test_scalar",
    comment => "Grant access to contents of test_scalar VAR",
    resource_type => "literal",
    admit => { "127.0.0.1" };
}
~~~~

CFEngine caches the value of this variable, so that, if the network is
unavailable, the last known value will be used. Hence use of this
function is fault tolerant. Care should be taken in attempting to access
remote variables that are not available, as the repeated connections
needed to resolve the absence of a value can lead to undesirable
behaviour. As a general rule, users are recommended to refrain from
relying on the availability of network resources.

~~~~ {.example}
     
     (string) remotescalar(resource handle,host/IP address,encrypt);
     
~~~~

This function downloads a string from a remote server, using the promise
handle as a variable identifier. Availability: Enterprise editions of
CFEngine only.

**ARGUMENTS**:

resource handle

The name of the promise on the server side \

host or IP address

The location of the server on which the resource resides. \

encrypt

Whether to encrypt the connection to the server.

~~~~ {.smallexample}
               true
               yes
               false
               no
~~~~

Note that this function assumes that you have already performed a
successful key exchange between systems, (e.g. using either a remote
copy or `cf-runagent` connection). It contains no mechanism for trust
establishment and will fail if there is no trust relationship
established in advance.
