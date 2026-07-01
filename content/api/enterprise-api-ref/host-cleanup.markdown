---
layout: default
title: Host cleanup API
---

The Host cleanup API removes hosts from the hub based on multiple
criteria configured in the hub settings.

## Run hosts cleanup

Runs all enabled cleanup stages sequentially and returns statistics for each stage.

**URI:** https://hub.cfengine.com/api/host-cleanup

**Method:** POST

**Prerequisites:**

Hosts cleanup is configured through the [hub settings][Host cleanup API#Settings]

This endpoint is not available on a [federated reporting][Federated reporting] superhub.

**Example request (curl):**

```console
curl --user <username>:<password> \
  -X POST \
  https://hub.cfengine.com/api/host-cleanup
```

**Example response:**

```
HTTP 200 OK
{
  "deletedHostsCleanup": {
    "found": 0,
    "permanentlyDeleted": 0,
    "failed": 0
  },
  "duplicateHostnameHostsCleanup": {
    "found": 0,
    "softDeleted": 0,
    "permanentlyDeleted": 0,
    "failed": 0
  },
  "duplicateIpHostsCleanup": {
    "found": 1,
    "softDeleted": 1,
    "permanentlyDeleted": 0,
    "failed": 0
  },
  "groupHostsCleanup": {
    "found": 0,
    "softDeleted": 0,
    "permanentlyDeleted": 0,
    "failed": 0
  },
  "InactiveHostsCleanup": {
    "found": 0,
    "softDeleted": 0,
    "permanentlyDeleted": 0,
    "failed": 0
  }
}
```

Each stage runs independently. If a stage fails, an `error` field with the error message
is returned in place of the counters and the remaining stages still run. A maximum of
1000 hosts is processed per stage per call.

**Responses:**

| HTTP response code | Description                                          |
| ------------------ | ---------------------------------------------------- |
| 200 OK             | Cleanup ran; the body contains per-stage statistics. |
| 403 Forbidden      | Endpoint called on a federated reporting superhub.   |

## Settings

The behavior of each stage is controlled by the settings keys, managed
through the [Status and settings REST API][Status and settings REST API#Update settings].
