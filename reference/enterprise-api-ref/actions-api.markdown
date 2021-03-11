---
layout: default
title: Actions API
published: true
tags: [reference, enterprise, API, report collection]
---

Actions API enables you to perform specific actions such a requesting report collection.

## Report collection

You can trigger a delta report collection in order to have fresh host data.

**URI:** https://hub.cfengine.com/api/actions/report_collection

**Method:** POST

**Parameters:**

* **hostkey** *(string)*
    Unique host identifier
    
**Example request (curl):**
 
```
curl -k --user <username>:<password> \
  -X POST \
  https://hub.cfengine.com/api/actions/report_collection \
  -H 'content-type: application/json' \
  -d '{"hostkey": "SHA=f329165d27a4484c626eb888e0ce3b1c6da6317177851fc999c2b1b1c159b4e8"}'
```

**Example response:**

```
HTTP 202 Accepted
```

## Trigger agent run

You can trigger an agent run for an individual host.

**URI:** https://hub.cfengine.com/api/actions/agent_run

**Method:** POST

**Parameters:**

* **hostkey** *(string)*
  Unique host identifier

**Example request (curl):**

```
curl -k --user <username>:<password> \
  -X POST \
  https://hub.cfengine.com/api/actions/agent_run \
  -H 'content-type: application/json' \
  -d '{"hostkey": "SHA=f329165d27a4484c626eb888e0ce3b1c6da6317177851fc999c2b1b1c159b4e8"}'
```

**Example response:**

```
HTTP 202 Accepted

{
    "output": "  notice: Waiting for child processes to finish\n172.28.128.15> cf-serverd executing cfruncommand: /bin/sh -c '
     \"/var/cfengine/bin/cf-agent\" -I -D cf_runagent_initiated -f /var/cfengine/inputs/update.cf  ;
     \"/var/cfengine/bin/cf-agent\" -I -D cf_runagent_initiated\n",
    "exit_code": 0
}
```
