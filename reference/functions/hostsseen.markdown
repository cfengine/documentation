---
layout: default
title: hostsseen
categories: [Reference, Functions, hostsseen]
published: true
alias: reference-functions-hostsseen.html
tags: [reference, communication functions, functions, hostsseen]
---

[%CFEngine_function_prototype(horizon, seen, field)%]

**Description:** Returns a list with the information `field` of hosts that were seen or not seen within the last `horizon` hours.

Finds a list of hosts seen by a CFEngine remote connection on the current host 
within the number of hours specified in `horizon`. The argument `seen` may be 
lastseen or notseen, the latter selecting all hosts not observed to have 
connected within the specified time.

[%CFEngine_function_attributes(horizon, seen, field)%]

**Example:**

```cf3
bundle agent test
{
vars:

  "myhosts" slist => { hostsseen("inf","lastseen","address") };

reports:
  "Found client/peer: $(myhosts)";
}
```
