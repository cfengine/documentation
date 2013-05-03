---
layout: default
title: Function-hostsseen
categories: [Special-functions,Function-hostsseen]
published: true
alias: Special-functions-Function-hostsseen.html
tags: [Special-functions,Function-hostsseen]
---

### Function hostsseen

**Synopsis**: hostsseen(arg1,arg2,arg3) returns type **slist**

\
 *arg1* : Horizon since last seen in hours, *in the range* 0,99999999999
\
 *arg2* : Complements for selection policy, *in the range*
lastseen,notseen \
 *arg3* : Type of return value desired, *in the range* name,address \

Extract the list of hosts last seen/not seen within the last arg1 hours

**Example**:\
 \

~~~~ {.verbatim}
bundle agent test

{
vars:

  "myhosts" slist => { hostsseen("inf","lastseen","address") };

reports:

  cfengine_3::

    "Found client/peer: $(myhosts)";

}
~~~~

**Notes**:\
 \

Finds a list of hosts seen by a CFEngine remote connection on the
current host within the number of hours specified by argument 1.
Argument 2 may be lastseen or notseen, the latter being all hosts not
observed to have connected within the specified time. Argument 3 may be
address or name, to return IP address or hostname form.
