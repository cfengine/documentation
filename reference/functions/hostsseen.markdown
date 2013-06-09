---
layout: default
title: hostsseen
categories: [Reference, Functions, hostsseen]
published: true
alias: reference-functions-hostsseen.html
tags: [reference, functions, hostsseen]
---

**Prototype**: `hostsseen(horizon, seen, field)`

**Return type**: `slist`

**Description**: Returns a list with the information `field` of hosts that were seen or not seen within the last `horizon` hours.

Finds a list of hosts seen by a CFEngine remote connection on the current host 
within the number of hours specified in `horizon`. The argument `seen` may be 
lastseen or notseen, the latter selecting all hosts not observed to have 
connected within the specified time.

**Arguments**:

* `horizon` : Horizon since last seen in hours, in the range `0,99999999999`
* `seen` : Selection criteria, one of
    * lastseen
    * notseen   
* `field` : Type of return value desired, one of
    * name
    * address   

**Example**:

```cf3
bundle agent test
{
vars:

  "myhosts" slist => { hostsseen("inf","lastseen","address") };

reports:

  cfengine_3::

    "Found client/peer: $(myhosts)";

}
```
