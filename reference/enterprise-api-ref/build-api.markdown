---
layout: default
title: Build API
published: true
tags: [reference, enterprise, API, build, modules]
---

The Build API enables you to configure modules easily to your projects.

# Projects API

## Create project

**URI:** https://hub.cfengine.com/build/projects

**Method:** POST

**Parameters:**
* **repositoryUrl** *(string)*
  Git repository URL. Project will be synchronized with this repository. Supported protocols: `http`, `ssh`, `git`. Required. 

* **branch** *(string)*
  Repository branch. Required.

* **name** *(string)*
  Project name.

* **authenticationType** *(string)*
  Authentication type that will be used to get access to the repository. Allowed values: `password`, `ssh_key`. Required.

* **username** *(string)*
  Username for authentication to the repository. Required when authentication type is `password`.

* **password** *(string)*
  Password for authentication to the repository. Required when authentication type is `password`.

* **sshPrivateKey** *(string)*
  SSH private key for authentication to the repository.

**Example request (curl):**

```console
curl -k --user <username>:<password> \
  -X POST \
  https://hub.cfengine.com/api/build/projects \
  -H 'content-type: application/json' \
  -d '
  {
  "repositoryUrl": "https://github.com/username/repository.git",
  "branch": "master",
  "authenticationType": "password",
  "password" : "git_token_or_password",
  "username" : "git_username",
  "name": "Production"
  }'
```

**Successful response example:**

```
HTTP 200 Ok
{
    "id": "8"
}
```

**Responses:**

| HTTP response code | Description |
|--------|-------------|
| 200 OK | Project successfully created |
| 422 Unprocessable entity | Validation error occurred |
| 409 Conflict | Project with the same repository url and branch already exists |
| 500 Internal server error | Internal server error |


## Update project

**URI:** https://hub.cfengine.com/build/projects/:id

**Method:** PATCH

**Parameters:**
* **id** *(integer)*
  Project's ID

* **repositoryUrl** *(string)*
  Git repository URL. Project will be synchronized with this repository. Supported protocols: `http`, `ssh`, `git`.

* **branch** *(string)*
  Repository branch.

* **name** *(string)*
  Project name.

* **authenticationType** *(string)*
  Authentication type that will be used to get access to the repository. Allowed values: `password`, `ssh_key`.

* **username** *(string)*
  Username for authentication to the repository.

* **password** *(string)*
  Password for authentication to the repository.

* **sshPrivateKey** *(string)*
  SSH private key for authentication to the repository.

**Example request (curl):**

```console
curl -k --user <username>:<password> \
  -X PATCH \
  https://hub.cfengine.com/api/build/projects/2 \
  -H 'content-type: application/json' \
  -d '
  {
  "branch": "staging",
  }'
```

**Successful response example:**

```
HTTP 204 No content
```

**Responses:**

| HTTP response code | Description |
|--------|-------------|
| 204 No content | Project successfully updated |
| 404 Not found | Project does not found |
| 422 Unprocessable entity | Validation error occurred |
| 409 Conflict | Project with the same repository url and branch already exists |
| 500 Internal server error | Internal server error |

## Get project

**URI:** https://hub.cfengine.com/build/projects/:id

**Method:** GET

**Parameters:**

* **id** *(integer)*
  Project's ID

**Example request (curl):**

```console
curl -k --user <username>:<password> \
  -X GET \
  https://hub.cfengine.com/api/build/projects/2 
```

**Successful response example:**

```
HTTP 200 OK
{
    "id": 2,
    "repository_url": "https://github.com/username/repository.git",
    "branch": "master",
    "name": "Production",
    "authentication_type": "password",
    "username": "admin",
    "is_empty": false,
    "created_at": "2022-03-17 14:01:56.23852+00",
    "password": "set",
    "ssh_private_key": "not set"
}
```

API does not return password or ssh private key, but returns `set` or `not set`.

**Responses:**

| HTTP response code | Description |
|--------|-------------|
| 200 Ok | Successful response  |
| 404 Not found | Project does not found |
| 500 Internal server error | Internal server error |

## Get projects list

**URI:** https://hub.cfengine.com/build/projects

**Method:** GET

**Parameters:**

* **id** *(integer)*
  Project's ID

**Example request (curl):**

```console
curl -k --user <username>:<password> \
  -X GET \
  https://hub.cfengine.com/api/build/projects
```

**Successful response example:**

```
HTTP 200 OK
{
    "data": [
        {
            "id": 3,
            "repository_url": "https://github.com/build/modules.git",
            "branch": "master",
            "name": null,
            "authentication_type": "password",
            "username": "admin",
            "is_empty": false,
            "created_at": "2022-03-17 13:13:21.107899+00",
            "password": "set",
            "ssh_private_key": "not set"
        },
        {
            "id": 4,
            "repository_url": "https://github.com/build/modules.git",
            "branch": "production",
            "name": null,
            "authentication_type": "password",
            "username": "admin",
            "is_empty": false,
            "created_at": "2022-03-17 13:13:23.333539+00",
            "password": "set",
            "ssh_private_key": "not set"
        }
    ],
    "meta": {
        "count": 2,
        "page": 1,
        "timestamp": 1647596804,
        "total": 2
    }
}
```

API does not return password or ssh private key, but returns `set` or `not set`.

**Responses:**

| HTTP response code | Description |
|--------|-------------|
| 200 Ok | Successful response  |
| 404 Not found | Project does not found |
| 500 Internal server error | Internal server error |

## Delete project

**URI:** https://hub.cfengine.com/build/projects/:id

**Method:** DELETE

**Parameters:**

* **id** *(integer)*
  Project's ID

**Example request (curl):**

```console
curl -k --user <username>:<password> \
  -X DELETE \
  https://hub.cfengine.com/api/build/projects/2 
```

**Successful response example:**

```
HTTP 204 No content
```

API does not return password or ssh private key, but returns `set` or `not set`.

**Responses:**

| HTTP response code | Description |
|--------|-------------|
| 204 No content | Project successfully deleted |
| 404 Not found | Project does not found |
| 500 Internal server error | Internal server error |
