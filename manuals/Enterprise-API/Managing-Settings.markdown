layout: default
title:  Managing Settings
categories: [Enterprise 3.0 API, Managing Settings]
published: true
alias: Managing-Settings.html
tags: [Enterprise 3.0 API, Managing Settings]
---
### 1.4 Managing Settings

-   [Viewing settings](/manuals/Enterprise-3-0-API#Viewing-settings)
-   [Example - Configuring
    LDAP](/manuals/Enterprise-3-0-API#Example-_002d-Configuring-LDAP)
-   [Example - Configuring Active
    Directory](/manuals/Enterprise-3-0-API#Example-_002d-Configuring-Active-Directory)
-   [Example - Changing The Log
    Level](/manuals/Enterprise-3-0-API#Example-_002d-Changing-The-Log-Level)

Most of the settings configurable in the API relate to LDAP
authentication of users. Settings support two operations, **GET** (view
settings) and **POST** (update settings). When settings are updated,
they are sanity checked individually and as a whole. All or no settings
will be updated for a request.

* * * * *

Next: [Example - Configuring
LDAP](/manuals/Enterprise-3-0-API#Example-_002d-Configuring-LDAP),
Previous: [Managing
Settings](/manuals/Enterprise-3-0-API#Managing-Settings), Up: [Managing
Settings](/manuals/Enterprise-3-0-API#Managing-Settings)

#### 1.4.1 Viewing settings

**Request**

    curl --user admin:admin http://test.cfengine.com/api/settings

**Response**

    {
      "meta": {
        "page": 1,
        "count": 1,
        "total": 1,
        "timestamp": 1350992335
      },
      "data": [
        {
          "rbacEnabled": true,
          "ldapEnabled": false,
          "ldapActiveDirectoryDomain": "ad.cfengine.com",
          "ldapBaseDN": "DC=ad,DC=cfengine,DC=com",
          "ldapEncryption": "plain",
          "ldapHost": "ldap-server.cfengine.com",
          "ldapLoginAttribute": "sAMAccountName",
          "ldapMode": "activeDirectory",
          "ldapPassword": "password",
          "ldapPort": 389,
          "ldapPortSSL": 636,
          "ldapUsername": "test",
          "ldapUsersDirectory": "CN=Users",
          "blueHostHorizon": 900,
          "logLevel": "error"
        }
      ]
    }

* * * * *

Next: [Example - Configuring Active
Directory](/manuals/Enterprise-3-0-API#Example-_002d-Configuring-Active-Directory),
Previous: [Viewing
settings](/manuals/Enterprise-3-0-API#Viewing-settings), Up: [Managing
Settings](/manuals/Enterprise-3-0-API#Managing-Settings)

#### 1.4.2 Example: Configuring LDAP

The setting **ldapEnabled** turns external authentication on or off.
When turned on, the API will check to see that the other LDAP related
settings make sense, and attempt to authenticate using the configured
credentials. If it is not successful in doing this, no settings will be
changed. The API will notify you with a return code an a message
describing the error.

**Request**

    curl --user admin:admin http://test.cfengine.com/api/settings -X POST -d
    {
      "ldapEnabled": true,
      "ldapActiveDirectoryDomain": "ad.cfengine.com",
      "ldapBaseDN": "DC=ad,DC=example,DC=com",
      "ldapEncryption": "ssl",
      "ldapHost": "ldap-server.cfengine.com",
      "ldapLoginAttribute": "sAMAccountName",
      "ldapMode": "standard",
      "ldapPassword": "password",
      "ldapUsername": "test",
      "ldapUsersDirectory": "ou",
    }

**Response**

    204 No Content

* * * * *

Next: [Example - Changing The Log
Level](/manuals/Enterprise-3-0-API#Example-_002d-Changing-The-Log-Level),
Previous: [Example - Configuring
LDAP](/manuals/Enterprise-3-0-API#Example-_002d-Configuring-LDAP),
Up: [Managing Settings](/manuals/Enterprise-3-0-API#Managing-Settings)

#### 1.4.3 Example: Configuring Active Directory

Active Directory is configured in much the same way as OpenLDAP, but the
additional field **ldapActiveDirectoryDomain** is required. **ldapMode**
is also changed from *standard* to *activeDirectory*.

**Request**

    curl --user admin:admin http://test.cfengine.com/api/settings -X POST -d
    {
      "ldapEnabled": true,
      "ldapBaseDN": "DC=example,DC=com",
      "ldapEncryption": "plain",
      "ldapHost": "ad-server.cfengine.com",
      "ldapLoginAttribute": "uid",
      "ldapMode": "activeDirectory",
      "ldapPassword": "password",
      "ldapUsername": "test",
      "ldapUsersDirectory": "CN=Users",
    }

**Response**

    204 No Content

* * * * *

Previous: [Example - Configuring Active
Directory](/manuals/Enterprise-3-0-API#Example-_002d-Configuring-Active-Directory),
Up: [Managing Settings](/manuals/Enterprise-3-0-API#Managing-Settings)

#### 1.4.4 Example: Changing The Log Level

The API uses standard Unix syslog to log a number of events.
Additionally, log events are sent to stderr, which means they may also
end up in your Apache log. Log events are filtered based on the log
level in settings. Suppose you wanted to have greater visibility into
the processing done at the backend. The standard log level is *error*.
Changing it to *info* is done as follows.

**Request**

    curl --user admin:admin http://test.cfengine.com/api/settings -X POST -d
    {
      "logLevel": "info"
    }

**Response**

    204 No Content

* * * * *

Next: [Browsing Host
Information](/manuals/Enterprise-3-0-API#Browsing-Host-Information),
Previous: [Managing
Settings](/manuals/Enterprise-3-0-API#Managing-Settings), Up: [REST
API](/manuals/Enterprise-3-0-API#REST-API)

