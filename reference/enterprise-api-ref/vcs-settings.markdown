---
layout: default
title: VCS settings API
published: true
tags: [reference, enterprise, API, settings, VCS]
---
VCS API for managing version control repository settings.

## Get VCS settings
   

**URI:** https://hub.cfengine.com/api/vcs/settings

**Method:** GET

**Example request (curl):**

```
curl -k --user <username>:<password> \
  -X GET \
  https://hub.cfengine.com/api/vcs/settings 
'
```

**Example response:**

```
{
    "meta": {
        "page": 1,
        "count": 10,
        "total": 1,
        "timestamp": 1535717855
    },
    "data": {
        "GIT_URL": "https://github.com/cfengine/masterfiles.git",
        "GIT_REFSPEC": "master",
        "GIT_USERNAME": "username",
        "GIT_PASSWORD": "passwordOrToken",
        "GIT_WORKING_BRANCH": "CF_WORKING_BRANCH",
        "PKEY": "/opt/cfengine/userworkdir/admin/.ssh/id_rsa.pvt",
        "SCRIPT_DIR": "/var/cfengine/httpd/htdocs/api/dc-scripts",
        "VCS_TYPE": "GIT"
    }
}
```

## Change VCS settings

**URI:** https://hub.cfengine.com/api/vcs/settings

**Method:** POST

**Parameters:**

* **vscType** *(string)*
  VCS type. Allowed values: `GIT`, `GIT_CFBS`. Default value: `GIT`
* **gitServer** *(string)*
    Git repository URL `Emp: https://github.com/cfengine/masterfiles.git`. Required parameter.
* **gitRefspec** *(string)*
    The Git refspec to checkout. It can be a branch name, a tag name, a commit hash or a partial hash. Required parameter.
* **gitUsername** *(string)*
    Git username for authentication, not needed for public repositories.
* **gitPassword** *(string)*
    Git password or token for authentication, not needed for public repositories.
* **gitPrivateKey** *(string)*
    Git private key raw content for authentication.
 
**Example request (curl):**
 
```
curl -k --user <username>:<password> \
  -X POST \
  https://hub.cfengine.com/api/vcs/settings \
  -H 'content-type: application/json' \
  -d '{
        "gitServer":"https://github.com/cfengine/masterfiles.git",
        "gitRefspec":"master",
        "gitUsername":"gituser",
        "gitPassword":"passwordOrToken",
        "gitPrivateKey" "Private key raw content"
      }
'
```

**Example response:**

```
 {
     "gitServer": "https://github.com/cfengine/masterfiles.git",
     "gitRefspec": "master",
     "gitUsername": "gituser",
     "gitPassword": "passwordOrToken",
     "gitPrivateKey": "/opt/cfengine/userworkdir/admin/.ssh/id_rsa.pvt"
 }
```

## History

* `vscType` parameter added in 3.19.0, 3.18.1
