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
  -d '{"hostkey": "SHA=hostkey"}'
```

**Example response:**

```
HTTP 202 Accepted
```
