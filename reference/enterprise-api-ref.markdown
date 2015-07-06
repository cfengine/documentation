---
layout: default
title:  Enterprise API Reference
published: true
sorting: 70
tags: [reference, enterprise, REST, API, reporting, sql]
---

The Enterprise API is a conventional REST API in the sense that it has a
number of URI resources that support one or more GET, PUT, POST, or
DELETE operations. While reporting is done using SQL, this query is
always wrapped in a JSON request.

## Requests

**GET** requests are one of **listing** or **getting**. **Listing** resources 
means that a number of results will be returned, but each entry may contain 
limited information. An example of a **listing** query is `/api/user` to list 
users. Notice that URI components are always non-plural. An exception to this 
is `/api/settings`, which returns the singleton resource for settings. 
**Getting** a resource specifies an individual resource to return, e.g. 
`/api/user/homer`.

**PUT** request typically create a new resource, e.g. a user.

**POST** requests typically updates an existing resource. **DELETE** requests are also supported in some cases.

### Pagination

Pagination is handled by `page` and `count` query parameters to a **GET** request, e.g. `/api/user?page=5&count=30` to get the 5th page of pages with 30 entries each. The default `page` is 1 and the default `count` is 50 if these are not specified explicitly.

## Responses

Enterprise API responses are always of the following format, consisting of a 
'meta' object and a 'data' array.

```json
    {
      "meta": {
        "page": 1,
        "count": 1,
        "total": 1,
        "timestamp": 1350922925
      },
      "data": [
         ... 
      ]
    }
```

`page` refers to the current page number of the request. `count` is the number of results in the current page, equaling the length of the `data` array. `total` is the number of results in all available pages combined. `timestamp` is the time the request was processed by the API. The `data` array is resource dependent, but will always contain objects. Response objects typically do not contain error codes.

If the response is not `200 OK`, the appropriate HTTP error code returned along with a (possibly non-JSON) payload.

All timestamps are reported in *Unix Time*, i.e. seconds since 1970.

## Authentication

The API supports both internal and external authentication. The internal users 
table will always be consulted first, followed by an external source specified 
in the settings. External sources are *OpenLDAP* or *Active Directory* servers 
configurable through `POST /api/settings`.


## Authorization

Some resources require that the request user is a member of the *admin* role. Roles are managed with `/api/role`. Role Based Access Control (RBAC) is configurable through the settings. Users typically have permission to access their own resources, e.g. their own scheduled reports.

