---
layout: default
title: LDAP authentication API
published: true
tags: [reference, enterprise, API, authenticating, LDAP]
---

LDAP authentication API allows to check ldap user credentials and change LDAP settings.

## Login

**URI:** https://hub.cfengine.com/ldap/login

**Method:** POST

**Parameters:**

* **username** *(string)*
    Username from LDAP
* **password** *(string)*
    User password

**Example response:**

```
HTTP 200 Ok
{
    "success": true,
    "message": "You are successfully authenticated"
}
```

## Get settings

**URI:** https://hub.cfengine.com/ldap/settings

**Method:** GET

**Headers:**

* **Authorization: api_token** *(string)*
    Set token to access api. To get the token please look at - ```/var/cfengine/httpd/htdocs/ldap/config/settings.php```

**Example response:**

```
HTTP 200 Ok
{
    "success": true,
    "data": {
        "domain_controller": "local.loc",
        "base_dn": "DC=local,DC=loc",
        "login_attribute": "cn",
        "port": 365,
        "use_ssl": false,
        "use_tls": false,
        "timeout": 5,
        "admin_username": "cn=admin,DC=local,DC=loc",
        "admin_password": "Password is set"
    }
}
```

**Output:**

* **domain_controller**
    The domain controllers option is   server name located on your network that serve Active Directory.
* **base_dn**
    The base distinguished name is the base distinguished name you'd like to perform operations on. An example base DN would be DC=corp,DC=acme,DC=org.
* **login_attribute**
    Login attribute like cn or uid
* **group_attribute**
    Group attribute (e.g. memberOf in Active Directory). Required for [LDAP roles syncing][Settings#LDAP groups syncing] with internal roles.
* **port**
    The port option is used for authenticating and binding to your AD server. The default ports are already used for non SSL and SSL connections (389 and 636).
* **use_ssl**
    Use ssl for connection
* **use_tls**
    Use tls for connection
* **timeout**
    The timeout option allows you to configure the amount of seconds to wait until your application receives a response from your LDAP server.
* **admin_username**
    LDAP admin distinguished name. Emp.: cn=admin,dc=jumpcloud,dc=com
* **admin_password**
    LDAP admin password.

## Update settings

**URI:** https://hub.cfengine.com/ldap/settings

**Method:** PATCH

Note that the PATCH HTTP method only requires partial JSON for an update. Such as {"port":3269} instead of the entire set of parameters.

**Headers:**

* **Authorization: api_token** *(string)*
    Set token to access api. To get the token please look at - ```/var/cfengine/httpd/htdocs/ldap/config/settings.php```

* **Content-Type: application/json** *(string)*
    Content-Type must be application/json for the API to parse JSON provided.

**Parameters:**

* **domain_controller** *(string)*
    The domain controllers option is   server name located on your network that serve Active Directory.
* **base_dn** *(string)*
    The base distinguished name is the base distinguished name you'd like to perform operations on. An example base DN would be DC=corp,DC=acme,DC=org.
* **login_attribute**  *(string)*
    Login attribute like cn or uid
* **port** *(integer)*
    The port option is used for authenticating and binding to your AD server. The default ports are already used for non SSL and SSL connections (389 and 636).  Optional parameter.
* **use_ssl** *(boolean)*
    Use ssl for connection.  Optional parameter.
* **use_tls** *(boolean)*
    Use tls for connection.  Optional parameter.
* **timeout** *(integer)*
    The timeout option allows you to configure the amount of seconds to wait until your application receives a response from your LDAP server.  Optional parameter.
* **admin_username**
        LDAP admin distinguished name. Emp.: cn=admin,dc=jumpcloud,dc=com
* **admin_password**
        LDAP admin password.

**Example response:**

```
HTTP 200 Ok
{
    "success": true,
    "message": "Settings successfully saved."
}
```
