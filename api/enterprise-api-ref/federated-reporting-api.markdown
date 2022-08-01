---
layout: default
title: Federated reporting configuration API
published: true
tags: [reference, enterprise, API, reporting]
---

This API is used for configuring hubs so that a single hub can be used to report on any host connected to participating feeder hubs.

# Remote hubs

Federated reporting must be enabled before it is possible to use the remote hubs API, please
see the `Enable hub for Federated Reporting` section below.

## Remote hubs list

**URI:** https://hub.cfengine.com/api/fr/remote-hub

**Method:** GET

**Example response:**

```
HTTP 200 OK
{
    "id-1": {
        "id": 1,
        "hostkey": "SHA=2d67a6840878de...",
        "api_url": "https://172.28.128.5",
        "ui_name": "ubuntu-xenial",
        "role": "feeder",
        "target_state": "on",
        "transport": {
            "mode": "pull_over_rsync",
            "ssh_user": "cfdrop",
            "ssh_host": "172.28.128.5",
            "ssh_pubkey": "",
            "ssh_fingerprint": ""
        }
    },
    "id-2": {
        "id": 2,
        "hostkey": "SHA=wefweg34tgfds...",
        "api_url": "https://172.28.128.6",
        "ui_name": "ubuntu-beaver",
        "role": "feeder",
        "target_state": "on",
        "transport": {
            "mode": "pull_over_rsync",
            "ssh_user": "cfdrop",
            "ssh_host": "superhub",
            "ssh_pubkey": "pubkey cfdrop",
            "ssh_fingerprint": null
        }
    }
}
```

## Get remote hub

**URI:** https://hub.cfengine.com/api/fr/remote-hub/:remote_hub_id

**Method:** GET

**Parameters:**

* **remote_hub_id** *(number)*
    Remote hub id

**Example response:**

```
HTTP 200 OK
{
    "id": 1,
    "hostkey": "SHA=2d67a6840878de098abbef1172f103a6febbfb5d00b8ace31ca3d46a9d22930d",
    "api_url": "https://172.28.128.5",
    "ui_name": "ubuntu-xenial",
    "role": "feeder",
    "target_state": "on",
    "transport": {
        "mode": "pull_over_rsync",
        "ssh_user": "cfdrop",
        "ssh_host": "172.28.128.5",
        "ssh_pubkey": "",
        "ssh_fingerprint": ""
    }
}
```

## Add remote hub

**URI:** https://hub.cfengine.com/api/fr/remote-hub

**Method:** POST

**Parameters:**

* **ui_name** *(string)*
    Remote hub name
* **hostkey** *(string)*
    Remote hub hostkey
* **role** *(string)*
    Remote hub role. Allowed values: `feeder`, `superhub`
* **target_state** *(string)*
    Target state of remote hub. Allowed values: `on`, `paused`
* **transport** *(json)*
    Transport data. Emp `{ "mode": "pull_over_rsync", "ssh_user": "cfdrop", "ssh_host": "172.28.128.5", "ssh_pubkey": "", "ssh_fingerprint": ""}`

**Example response:**

```
HTTP 201 CREATED
```

## Update remote hub

**URI:** https://hub.cfengine.com/api/fr/remote-hub/:remote_hub_id

**Method:** PUT

**Parameters:**

* **remote_hub_id** *(number)*
    Remote hub id
* **ui_name** *(string)*
    Remote hub name
* **hostkey** *(string)*
    Remote hub hostkey
* **role** *(string)*
    Remote hub role. Allowed values: `feeder`, `superhub`
* **target_state** *(string)*
    Target state of remote hub. Allowed values: `on`, `paused`
* **transport** *(json)*
    Transport data. Emp `{ "mode": "pull_over_rsync", "ssh_user": "cfdrop", "ssh_host": "172.28.128.5", "ssh_pubkey": "", "ssh_fingerprint": ""}`

**Example response:**

```
HTTP 202 ACCEPTED
```

## Delete remote hub

**URI:** https://hub.cfengine.com/api/fr/remote-hub/:remote_hub_id

**Method:** DELETE

**Parameters:**

* **remote_hub_id** *(number)*
    Remote hub id

**Example response:**

```
HTTP 202 ACCEPTED
```

# Enable hub for Federated Reporting

## Enable hub as a Superhub

**URI:** https://hub.cfengine.com/api/fr/setup-hub/superhub

**Method:** POST

**Example response:**

```
HTTP 202 ACCEPTED
```


## Enable hub as a Feeder

**URI:** https://hub.cfengine.com/api/fr/setup-hub/feeder

**Method:** POST

**Example response:**

```
HTTP 202 ACCEPTED
```

## Hub status

**URI:** https://hub.cfengine.com/api/fr/hub-status

**Method:** GET

**Example response:**

```
{
    "configured": true,
    "role": "feeder",
    "enable_request_sent": true,
    "transport_ssh_public_key": "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIFpTZhfubmkXONNReTAXA9v2eYo3xQ4GKcsB3J7i5arw root@ubuntu-xenial",
    "ssh_fingerprint": false,
    "target_state": "on"
}
```

# Federation config

Federated reporting must be enabled before generating or removing federation configuration, please
see `Enable hub for Federated Reporting` section above. Otherwise an error will be thrown and 
config file will not be created/deleted.

## Generate federation config
 
**URI:** https://hub.cfengine.com/api/fr/federation-config

**Method:** POST

**Example response:**

```
HTTP 202 ACCEPTED
```

## Delete federation config
 
**URI:** https://hub.cfengine.com/api/fr/federation-config

**Method:** DELETE

**Example response:**

```
HTTP 202 ACCEPTED
```
