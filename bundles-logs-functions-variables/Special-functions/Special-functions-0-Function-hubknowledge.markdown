---
layout: default
title: Function-hubknowledge
categories: [Special-functions,Function-hubknowledge]
published: true
alias: Special-functions-Function-hubknowledge.html
tags: [Special-functions,Function-hubknowledge]
---

### Function hubknowledge

**Synopsis**: hubknowledge(arg1) returns type **string**

\
 *arg1* : Variable identifier, *in the range*
[a-zA-Z0-9\_\$(){}\\[\\].:]+ \

Read global knowledge from the hub host by id (commercial extension)

**Example**:\
 \

~~~~ {.verbatim}
vars:

  guard::

   "global_number" string => hubknowledge("number_variable");
~~~~

**Notes**:\
 \

This function is only available in commercial releases of CFEngine. It
is intended for use in distributed orchestration. It is recommended that
you use this function sparingly with *guards*, as it contributes to
network traffic and depends on the network for its function. Unlike
`remotescalar()`, the value of hub-knowledge is not cached.

This function behaves is essentially similar to the `remotescalar`
function, except that it always gets its information from the policy
server hub by an encrypted connection. It is designed for spreading
globally calibrated information about a CFEngine swarm back to the
client machines. The data available through this channel are generated
automatically by discovery, unlike `remotescalar` which accesses user
defined data.

This function asks for an identifier. It is up to the server to
interpret what this means and to return a value of its choosing. If the
identifier matches a persistent scalar variable (such as is used to
count distributed processes in CFEngine Enterprise) then this will be
returned preferentially. If no such variable is found, then the server
will look for a literal string in a server bundle with a handle that
matches the requested object.
