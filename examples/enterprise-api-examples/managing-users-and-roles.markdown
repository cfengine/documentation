---
layout: default
title:  Managing Users and Roles
published: true
sorting: 40
tags: [examples, enterprise, rest, api, reporting, users, roles]
---

Users and Roles determine who has access to what data from the API.
Roles are defined by regular expressions that determine which hosts the
user can see, and what policy outcomes are restricted.


## Example: Listing Users

**Request**

    curl --user admin:admin http://test.cfengine.com/api/user

**Response**

    {
      "meta": {
        "page": 1,
        "count": 2,
        "total": 2,
        "timestamp": 1350994249
      },
      "data": [
        {
          "id": "calvin",
          "external": true,
          "roles": [
            "Huguenots", "Marketing"
          ]
        },
        {
          "id": "quinester",
          "name": "Willard Van Orman Quine",
          "email": "noreply@@aol.com",
          "external": false,
          "roles": [
            "admin"
          ]
        }
      ]
    }


## Example: Creating a New User

All users will be created for the internal user table. The API will never
attempt to write to an external LDAP server.

**Request**

    curl --user admin:admin http://test.cfengine.com/api/user/snookie -X PUT -d
    {
      "email": "snookie@mtv.com",
      "roles": [
        "HR"
      ]
    }

**Response**

    201 Created
    }


## Example: Updating an Existing User

Both internal and external users may be updated. When updating an external
users, the API will essentially annotate metadata for the user, it will never
write to LDAP. Consequently, passwords may only be updated for internal users.
Users may only update their own records, as authenticated by their user
credentials.

**Request**

    curl --user admin:admin http://test.cfengine.com/api/user/calvin -X POST -d '{ "name": "Calvin" }'

**Response**

    204 No Content

## Example: Retrieving a User

It is possible to retrieve data on a single user instead of listing
everything. The following query is similar to issuing `GET
/api/user?id=calvin`, with the exception that the previous query accepts
a regular expression for `id`.

**Request**

    curl --user admin:admin http://test.cfengine.com/api/user/calvin

**Response**

    {
      "meta": {
        "page": 1,
        "count": 1,
        "total": 1,
        "timestamp": 1350994249
      },
      "data": [
        {
          "id": "calvin",
          "name": "Calvin",
          "external": true,
          "roles": [
            "Huguenots", "Marketing"
          ]
        },
      ]
    }

## Example: Adding a User to a Role

Adding a user to a role is just an update operation on the user. The full
role-set is updated, so if you are only appending a role, you may want to
fetch the user data first, append the role and then update. The same approach
is used to remove a user from a role.

**Request**

    curl --user admin:admin http://test.cfengine.com/api/user/snookie -X POST -d
    {
      "roles": [
        "HR", "gcc-contrib"
      ]
    }

**Response**

    204 No Content
    }


## Example: Deleting a User

Users can only be deleted from the internal users table.

**Request**

    curl --user admin:admin http://test.cfengine.com/api/user/snookie -X DELETE

**Response**

    204 No Content
