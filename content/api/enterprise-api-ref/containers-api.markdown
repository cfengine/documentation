---
layout: default
title: Container information API
---

Containers API provides access to container inventory data collected from
hosts, including running containers, container images, and container volumes.
It also exposes a per-host summary endpoint with aggregated counts.

## List containers

**URI:** https://hub.cfengine.com/api/inventory/containers

**Method:** GET

**Parameters:**

- **hostkey** _(string)_
  Filter by host key (exact match).
- **owner** _(string)_
  Filter by owner (exact match).
- **name** _(string)_
  Filter by container name (case-insensitive substring match).
- **image** _(string)_
  Filter by image (case-insensitive substring match).
- **state** _(string)_
  Filter by container state (case-insensitive substring match).
- **engine** _(string)_
  Filter by container engine (exact match, e.g. `docker`, `podman`).
- **container_port** _(integer or array of integers)_
  Filter by published container ports. Allowed range: 0–65535. May be
  repeated to match any of several ports.
- **host_port** _(integer or array of integers)_
  Filter by host ports the container is published on. Allowed range:
  0–65535. May be repeated to match any of several ports.
- **host_ip** _(string or array of strings)_
  Filter by the host IP a port is bound to (e.g. `0.0.0.0`). May be repeated.
- **protocol** _(string or array of strings)_
  Filter by port protocol. Allowed values: `tcp`, `udp`, `sctp`
  (case-insensitive). May be repeated.
- **page** _(integer, default: 1)_
  Page number for pagination.
- **per_page** _(integer, default: 20)_
  Number of items per page. Allowed range: 1–100.
- **sort** _(string, default: "started_at")_
  Column to sort by. Allowed values:
  - hostkey
  - owner
  - id
  - name
  - image
  - state
  - engine
  - started_at
  - collected_at
- **order** _(string, default: "desc")_
  Sort direction. Allowed values:
  - asc
  - desc

**Example request (curl):**

```console
curl --user <username>:<password> -X GET https://hub.cfengine.com/api/inventory/containers
```

To filter by ports, repeat a parameter using the `[]` array syntax:

```console
curl --user <username>:<password> -X GET \
  "https://hub.cfengine.com/api/inventory/containers?host_port[]=8080&host_port[]=443&protocol[]=tcp"
```

**Successful response example:**

```
HTTP 200 OK
{
    "data": [
        {
            "hostkey": "SHA=abc123...",
            "owner": "root",
            "id": "9f1c7e2b4a55",
            "name": "web",
            "image": "nginx:1.27",
            "image_id": "sha256:7d3f...",
            "command": "nginx -g 'daemon off;'",
            "state": "running",
            "ports": [
                {
                    "container_port": 80,
                    "host_ip": "0.0.0.0",
                    "host_port": 8080,
                    "protocol": "tcp"
                }
            ],
            "engine": "docker",
            "started_at": "2026-05-20 12:30:00",
            "collected_at": "2026-05-26 09:00:00",
            "details": null
        }
    ],
    "meta": {
        "count": 1,
        "page": 1,
        "timestamp": 1748246400,
        "total": 1
    }
}
```

**Responses:**

| HTTP response code        | Description           |
| ------------------------- | --------------------- |
| 200 OK                    | Containers returned   |
| 400 Bad Request           | Validation error      |
| 401 Unauthorized          | Authorization missing |
| 500 Internal server error | Internal server error |

## List container images

**URI:** https://hub.cfengine.com/api/inventory/container-images

**Method:** GET

**Parameters:**

- **hostkey** _(string)_
  Filter by host key (exact match).
- **owner** _(string)_
  Filter by owner (exact match).
- **repository** _(string)_
  Filter by image repository (case-insensitive substring match).
- **tag** _(string)_
  Filter by image tag (case-insensitive substring match).
- **page** _(integer, default: 1)_
  Page number for pagination.
- **per_page** _(integer, default: 20)_
  Number of items per page. Allowed range: 1–100.
- **sort** _(string, default: "created_at")_
  Column to sort by. Allowed values:
  - hostkey
  - owner
  - id
  - repository
  - tag
  - size_bytes
  - created_at
  - collected_at
- **order** _(string, default: "desc")_
  Sort direction. Allowed values:
  - asc
  - desc

**Example request (curl):**

```console
curl --user <username>:<password> -X GET https://hub.cfengine.com/api/inventory/container-images
```

**Successful response example:**

```
HTTP 200 OK
{
    "data": [
        {
            "hostkey": "SHA=abc123...",
            "owner": "root",
            "id": "sha256:7d3f...",
            "repository": "nginx",
            "tag": "1.27",
            "size_bytes": 142000000,
            "created_at": "2026-05-01 10:00:00",
            "collected_at": "2026-05-26 09:00:00"
        }
    ],
    "meta": {
        "count": 1,
        "page": 1,
        "timestamp": 1748246400,
        "total": 1
    }
}
```

**Responses:**

| HTTP response code        | Description               |
| ------------------------- | ------------------------- |
| 200 OK                    | Container images returned |
| 400 Bad Request           | Validation error          |
| 401 Unauthorized          | Authorization missing     |
| 500 Internal server error | Internal server error     |

## List container volumes

**URI:** https://hub.cfengine.com/api/inventory/container-volumes

**Method:** GET

**Parameters:**

- **hostkey** _(string)_
  Filter by host key (exact match).
- **owner** _(string)_
  Filter by owner (exact match).
- **volume_name** _(string)_
  Filter by volume name (case-insensitive substring match).
- **driver** _(string)_
  Filter by volume driver (case-insensitive substring match).
- **page** _(integer, default: 1)_
  Page number for pagination.
- **per_page** _(integer, default: 20)_
  Number of items per page. Allowed range: 1–100.
- **sort** _(string, default: "created_at")_
  Column to sort by. Allowed values:
  - hostkey
  - owner
  - name
  - driver
  - size_bytes
  - created_at
  - collected_at
- **order** _(string, default: "desc")_
  Sort direction. Allowed values:
  - asc
  - desc

**Example request (curl):**

```console
curl --user <username>:<password> -X GET https://hub.cfengine.com/api/inventory/container-volumes
```

**Successful response example:**

```
HTTP 200 OK
{
    "data": [
        {
            "hostkey": "SHA=abc123...",
            "owner": "root",
            "name": "web-data",
            "driver": "local",
            "size_bytes": 5242880,
            "created_at": "2026-05-15 08:00:00",
            "collected_at": "2026-05-26 09:00:00"
        }
    ],
    "meta": {
        "count": 1,
        "page": 1,
        "timestamp": 1748246400,
        "total": 1
    }
}
```

**Responses:**

| HTTP response code        | Description                |
| ------------------------- | -------------------------- |
| 200 OK                    | Container volumes returned |
| 400 Bad Request           | Validation error           |
| 401 Unauthorized          | Authorization missing      |
| 500 Internal server error | Internal server error      |

## Get containers summary for a host

Returns aggregated container, image, and volume counts for a single host,
along with the list of distinct container engines detected on it.

**URI:** https://hub.cfengine.com/api/inventory/containers/summary/:hostkey

**Method:** GET

**Path parameters:**

- **hostkey** _(string)_
  Host key to compute the summary for. The caller must have access to the
  host.

**Example request (curl):**

```console
curl --user <username>:<password> -X GET https://hub.cfengine.com/api/inventory/containers/summary/SHA=abc123
```

**Successful response example:**

```
HTTP 200 OK
{
    "hostkey": "SHA=abc123...",
    "containers": {
        "running": 3,
        "total": 5
    },
    "images": {
        "named": 8,
        "total": 12
    },
    "volumes": {
        "count": 4,
        "total_size_bytes": 20971520
    },
    "engines": [
        "docker",
        "podman"
    ]
}
```

**Responses:**

| HTTP response code        | Description                        |
| ------------------------- | ---------------------------------- |
| 200 OK                    | Summary returned                   |
| 400 Bad Request           | Invalid host key or host not found |
| 401 Unauthorized          | Authorization missing              |
| 403 Forbidden             | Caller has no access to the host   |
| 500 Internal server error | Internal server error              |

## Permissions

All Containers API endpoints are gated by the same RBAC permission used for
the [Query API](/api/enterprise-api-ref/query/) (`query.post`). The
`/inventory/containers/summary/:hostkey` endpoint additionally requires the
caller to have access to the requested host.
