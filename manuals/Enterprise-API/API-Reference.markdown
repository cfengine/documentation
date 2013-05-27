layout: default
title: 
categories: [Enterprise 3.0 API,]
published: true
alias: SQL-Queries.html
tags: [Enterprise 3.0 API,]
---
### 1.8 API Reference

-   [/api](/manuals/Enterprise-3-0-API#g_t_002fapi)
-   [/api/settings](/manuals/Enterprise-3-0-API#g_t_002fapi_002fsettings)
-   [/api/user](/manuals/Enterprise-3-0-API#g_t_002fapi_002fuser)
-   [/api/user/id](/manuals/Enterprise-3-0-API#g_t_002fapi_002fuser_002fid)
-   [/api/role](/manuals/Enterprise-3-0-API#g_t_002fapi_002frole)
-   [/api/role/id](/manuals/Enterprise-3-0-API#g_t_002fapi_002frole_002fid)
-   [/api/host](/manuals/Enterprise-3-0-API#g_t_002fapi_002fhost)
-   [/api/host/host-id](/manuals/Enterprise-3-0-API#g_t_002fapi_002fhost_002fhost_002did)
-   [/api/host/host-id/context](/manuals/Enterprise-3-0-API#g_t_002fapi_002fhost_002fhost_002did_002fcontext)
-   [/api/host/host-id/context/context-id](/manuals/Enterprise-3-0-API#g_t_002fapi_002fhost_002fhost_002did_002fcontext_002fcontext_002did)
-   [/api/host/host-id/vital](/manuals/Enterprise-3-0-API#g_t_002fapi_002fhost_002fhost_002did_002fvital)
-   [/api/promise](/manuals/Enterprise-3-0-API#g_t_002fapi_002fpromise)
-   [/api/promise/promise-id](/manuals/Enterprise-3-0-API#g_t_002fapi_002fpromise_002fpromise_002did)
-   [/api/query](/manuals/Enterprise-3-0-API#g_t_002fapi_002fquery)
-   [/api/query/async](/manuals/Enterprise-3-0-API#g_t_002fapi_002fquery_002fasync)
-   [/api/query/async/async-query-id](/manuals/Enterprise-3-0-API#g_t_002fapi_002fquery_002fasync_002fasync_002dquery_002did)

* * * * *

Next: [/api/settings](/manuals/Enterprise-3-0-API#g_t_002fapi_002fsettings),
Previous: [API Reference](/manuals/Enterprise-3-0-API#API-Reference),
Up: [API Reference](/manuals/Enterprise-3-0-API#API-Reference)

#### 1.8.1 /api

*Supported Operations*:  
**GET**

*Fields*:

-   **apiName** *(string)* Human-friendly API name.
-   **apiVersion** *(string)* API version string.
-   **enterpriseVersion** *(string)* Version of the CFEngine Enterprise
    build.
-   **coreVersion** *(string)* The version of CFEngine Core (Community)
    the Enterprise version was built against.
-   **databaseHostname** *(string)* Hostname (or IP) of the database the
    API is connected to.
-   **databasePort** *(integer)* Port number of the database the API is
    connected to.
-   **authenticated** *("internal", "external")*, Whether the request
    was authenticated using the internal users table or an external
    source.
-   **license.expires** *(integer)* Time when the license expires.
-   **license.installTime** *(integer)* Time when the license was
    installed.
-   **license.owner** *(string)* The name of the license owner.
-   **license.granted** *(integer)* Host number capacity granted by the
    license.
-   **license.licenseUsage.lastMeasured** *(integer)* Time when license
    usage was last updated.
-   **license.licenseUsage.samples** *(integer)* Number of samples
    collected for license usage.
-   **license.licenseUsage.minObservedLevel** *(integer)* Minimum number
    of observed host licenses in use.
-   **license.licenseUsage.minObservedLevel** *(integer)* Maximum number
    of observed host licenses in use.
-   **license.licenseUsage.meanUsage** *(integer)* Average number of
    observed host licenses in use.
-   **license.licenseUsage.meanCumulativeUtilization** *(integer)* (not
    sure)
-   **license.licenseUsage.usedToday** *(integer)* Total number of host
    licenses observed used today.

* * * * *

Next: [/api/user](/manuals/Enterprise-3-0-API#g_t_002fapi_002fuser),
Previous: [/api](/manuals/Enterprise-3-0-API#g_t_002fapi), Up: [API
Reference](/manuals/Enterprise-3-0-API#API-Reference)

#### 1.8.2 /api/settings

*Supported Operations*:  
**GET**, **POST**

*Fields*:

-   **rbacEnabled** *(boolean)* Whether RBAC is applied to requests.
-   **ldapEnabled** *(boolean)* Whether external authentication is
    activated.
-   **activeDirectoryDomain** *(string)* AD domain to use if AD is
    enabled in **ldapMode**.
-   **ldapBaseDN** *(string)* LDAP BaseDN to use for external LDAP
    requests.
-   **ldapEncryption** *("plain", "ssl", "tls")* Type of LDAP binding to
    establish to external LDAP server. (Default: "plain").
-   **ldapHost** *(string)* Hostname of external LDAP server.
-   **ldapMode** *("standard", "activeDirectory")* Type of LDAP server
    to use. "standard" is effectively OpenLDAP. (Default: "standard").
-   **ldapLoginAttribute** *(string)* LDAP attribute to use for
    usernames. (default: "uid").
-   **ldapUsername** *(string)* LDAP username.
-   **ldapPassword** *(string)* LDAP password.
-   **ldapUsersDirectory** *(string)* Attribute and value to qualify the
    directory in which to look up users, e.g. "ou=people".
-   **ldapPort** *(integer)* Port for external LDAP connections not
    using SSL. (default 389).
-   **ldapPort** *(integer)* Port for external LDAP connections using
    SSL. (default 636).
-   **blueHostHorizon** *(integer)* Time interval (seconds) for when to
    consider a host unreachable. (default 900).
-   **logLevel** *("emergency", "alert", "critical", "error", "warning",
    "notice", "info", "debug")* Syslog filter specifying the severity
    level at which messages produced by the API should be emitted to
    syslog and apache.log. (default: error).

* * * * *

Next: [/api/user/id](/manuals/Enterprise-3-0-API#g_t_002fapi_002fuser_002fid),
Previous: [/api/settings](/manuals/Enterprise-3-0-API#g_t_002fapi_002fsettings),
Up: [API Reference](/manuals/Enterprise-3-0-API#API-Reference)

#### 1.8.3 /api/user

*Supported Operations*:  
**GET**

*Query Parameters*:

-   **id** *(regex string)* Regular expression for filtering usernames.
-   **external** *("true", "false")* Returns only internal users (false)
    or only external (true), or all if not specified.

* * * * *

Next: [/api/role](/manuals/Enterprise-3-0-API#g_t_002fapi_002frole),
Previous: [/api/user](/manuals/Enterprise-3-0-API#g_t_002fapi_002fuser),
Up: [API Reference](/manuals/Enterprise-3-0-API#API-Reference)

#### 1.8.4 /api/user/:id

*Supported Operations*:  
**GET**, **PUT**, **POST**, **DELETE**

*Fields*:

-   **id** *(string)* ID of a user.
-   **password** *(string)* Password of a user. (Never returned from
    API).
-   **email** *(string)* Email address associated with user.
-   **roles** *(array of strings)* Set of IDs of roles a user is in.
    (Default: empty)
-   **external** *(boolean)* Whether or not the user was found
    externally (LDAP).

* * * * *

Next: [/api/role/id](/manuals/Enterprise-3-0-API#g_t_002fapi_002frole_002fid),
Previous: [/api/user/id](/manuals/Enterprise-3-0-API#g_t_002fapi_002fuser_002fid),
Up: [API Reference](/manuals/Enterprise-3-0-API#API-Reference)

#### 1.8.5 /api/role

*Supported Operations*:  
**GET**

* * * * *

Next: [/api/host](/manuals/Enterprise-3-0-API#g_t_002fapi_002fhost),
Previous: [/api/role](/manuals/Enterprise-3-0-API#g_t_002fapi_002frole),
Up: [API Reference](/manuals/Enterprise-3-0-API#API-Reference)

#### 1.8.6 /api/role/:id

*Supported Operations*:  
**GET**, **PUT**, **POST**, **DELETE**

*Fields*:

-   **id** *(string)* ID of a role.
-   **description** *(string)* Arbitrary text describing the role
-   **includeContext** *(comma delimited string of regular expression
    strings)* Includes hosts visible to the users in the role.
-   **excludeContext** *(comma delimited string of regular expression
    strings)* Excludes bundles visible to the users in the role.
-   **includeBundles** *(comma delimited string of regular expression
    strings)* Includes bundles visible to the users in the role.
-   **excludeBundles** *(comma delimited string of regular expression
    strings)* Excludes bundles visible to the users in the role.

* * * * *

Next: [/api/host/host-id](/manuals/Enterprise-3-0-API#g_t_002fapi_002fhost_002fhost_002did),
Previous: [/api/role/id](/manuals/Enterprise-3-0-API#g_t_002fapi_002frole_002fid),
Up: [API Reference](/manuals/Enterprise-3-0-API#API-Reference)

#### 1.8.7 /api/host

*Supported Operations*:  
**GET**

*Query Parameters*:

-   **include-context** *(comma delimited string of regular expression
    strings)* Includes hosts having context matching the expression.
-   **exclude-context** *(comma delimited string of regular expression
    strings)* Excludes hosts having context matching the expression.

* * * * *

Next: [/api/host/host-id/context](/manuals/Enterprise-3-0-API#g_t_002fapi_002fhost_002fhost_002did_002fcontext),
Previous: [/api/host](/manuals/Enterprise-3-0-API#g_t_002fapi_002fhost),
Up: [API Reference](/manuals/Enterprise-3-0-API#API-Reference)

#### 1.8.8 /api/host/:host-id

-   **id** *(string)* ID of a host.
-   **hostname** *(string)* Hostname of a host.
-   **ip** *(string)* IP address of a host.

* * * * *

Next: [/api/host/host-id/context/context-id](/manuals/Enterprise-3-0-API#g_t_002fapi_002fhost_002fhost_002did_002fcontext_002fcontext_002did),
Previous: [/api/host/host-id](/manuals/Enterprise-3-0-API#g_t_002fapi_002fhost_002fhost_002did),
Up: [API Reference](/manuals/Enterprise-3-0-API#API-Reference)

#### 1.8.9 /api/host/:host-id/context

*Supported Operations*:  
**GET**

* * * * *

Next: [/api/host/host-id/vital](/manuals/Enterprise-3-0-API#g_t_002fapi_002fhost_002fhost_002did_002fvital),
Previous: [/api/host/host-id/context](/manuals/Enterprise-3-0-API#g_t_002fapi_002fhost_002fhost_002did_002fcontext),
Up: [API Reference](/manuals/Enterprise-3-0-API#API-Reference)

#### 1.8.10 /api/host/:host-id/context/:context-id

*Supported Operations*:  
**GET**

*Fields*:

-   **id** *(string)* ID of a context (class name)
-   **mean** *(real)* Occurrence probability of the context in an agent
    run.
-   **stdv** *(real)* Standard deviation of occurrence probability.
-   **timestamp** *(integer*) Last time context was activated on agent.

* * * * *

Next: [/api/promise](/manuals/Enterprise-3-0-API#g_t_002fapi_002fpromise),
Previous: [/api/host/host-id/context/context-id](/manuals/Enterprise-3-0-API#g_t_002fapi_002fhost_002fhost_002did_002fcontext_002fcontext_002did),
Up: [API Reference](/manuals/Enterprise-3-0-API#API-Reference)

#### 1.8.11 /api/host/:host-id/vital

*Supported Operations*:  
**GET**

##### 1.8.11.1 /api/host/:host-id/vital/:vital-id

*Supported Operations*:  
**GET**

*Query Parameters*:

-   **from** *(integer)* Timestamp marking the start of the interval for
    which to fetch data. Data is only available going back one week.
-   **to** *(integer)* End of data interval to be fetched.

<!-- -->

*Fields*:

-   **id** *(string)* ID of vital sign.
-   **description** *(string)* Description of vital sign.
-   **units** *(string)* Measurement unit of vital sign.
-   **timestamp** *(integer)* Timestamp of the last received data point.
-   **values** *(array of [ t, y ], where t is the sample timestamp)*
    Vital sign data.

* * * * *

Next: [/api/promise/promise-id](/manuals/Enterprise-3-0-API#g_t_002fapi_002fpromise_002fpromise_002did),
Previous: [/api/host/host-id/vital](/manuals/Enterprise-3-0-API#g_t_002fapi_002fhost_002fhost_002did_002fvital),
Up: [API Reference](/manuals/Enterprise-3-0-API#API-Reference)

#### 1.8.12 /api/promise

*Supported Operations*:  
**GET**

* * * * *

Next: [/api/query](/manuals/Enterprise-3-0-API#g_t_002fapi_002fquery),
Previous: [/api/promise](/manuals/Enterprise-3-0-API#g_t_002fapi_002fpromise),
Up: [API Reference](/manuals/Enterprise-3-0-API#API-Reference)

#### 1.8.13 /api/promise/:promise-id

*Supported Operations*:  
**GET**

*Fields*:

-   **id** *(string)* Promise handle.
-   **type** *(string)* Promise type.
-   **promiser** *(string)* Promiser of the promise.
-   **promisees** *(array of strings)* A list of promisees of the
    promise.
-   **bundle** *(string)* The bundle this promise belongs to
-   **comment** *(string)* Associated comment for the promise.

* * * * *

Next: [/api/query/async](/manuals/Enterprise-3-0-API#g_t_002fapi_002fquery_002fasync),
Previous: [/api/promise/promise-id](/manuals/Enterprise-3-0-API#g_t_002fapi_002fpromise_002fpromise_002did),
Up: [API Reference](/manuals/Enterprise-3-0-API#API-Reference)

#### 1.8.14 /api/query

*Supported Operations*:  
**POST**

*Fields*:

-   **query** *(string)* SQL query string.
-   **sortColumn** *(string)* Column on which to sort results. This is
    applied to the result of the SQL query and can be considered post
    processing. The Mission Portal uses this to sort cached reports.
-   **sortDescending** *(bool)* Apply post-sorting descendingly.
-   **skip** *(integer)* Number of results to skip for the processed
    query. The Mission Portal uses this for pagination on cached
    results.
-   **limit** *(integer)* Limit the number of results in the processed
    query.

* * * * *

Next: [/api/query/async/async-query-id](/manuals/Enterprise-3-0-API#g_t_002fapi_002fquery_002fasync_002fasync_002dquery_002did),
Previous: [/api/query](/manuals/Enterprise-3-0-API#g_t_002fapi_002fquery),
Up: [API Reference](/manuals/Enterprise-3-0-API#API-Reference)

#### 1.8.15 /api/query/async

*Supported Operations*:  
**POST**

*Fields*:

-   **query** *(string)* SQL query string.
-   **id** *(string)* ID of the query job.
-   **error** *(string)* Error if anything went wrong.

* * * * *

Previous: [/api/query/async](/manuals/Enterprise-3-0-API#g_t_002fapi_002fquery_002fasync),
Up: [API Reference](/manuals/Enterprise-3-0-API#API-Reference)

#### 1.8.16 /api/query/async/:async-query-id

*Supported Operations*:  
**GET**, **DELETE**

*Fields*:

-   **id** *(string)* ID of the query job.
-   **percentageComplete** *(integer)* Processing status for the query.
-   **href** *(string)* Download link for the finished report.
-   **error** *(string)* Error if anything went wrong.

Table of Contents
-----------------

-   [CFEngine Enterprise 3.0 API](/manuals/Enterprise-3-0-API#Top)
-   [1 REST API](/manuals/Enterprise-3-0-API#REST-API)
    -   [1.1 Basic Properties of the
        API](/manuals/Enterprise-3-0-API#Basic-Properties-of-the-API)
        -   [1.1.1 HTTP +
            JSON](/manuals/Enterprise-3-0-API#HTTP-_002b-JSON)
        -   [1.1.2 Requests](/manuals/Enterprise-3-0-API#Requests)
        -   [1.1.3 Responses](/manuals/Enterprise-3-0-API#Responses)
        -   [1.1.4 Pagination](/manuals/Enterprise-3-0-API#Pagination)
        -   [1.1.5 Time](/manuals/Enterprise-3-0-API#Time)
        -   [1.1.6
            Authentication](/manuals/Enterprise-3-0-API#Authentication)
        -   [1.1.7
            Authorization](/manuals/Enterprise-3-0-API#Authorization)

    -   [1.2 Differences between the CFEngine Nova 2.2 REST API and the
        CFEngine Enterprise 3.0
        API](/manuals/Enterprise-3-0-API#Differences-between-the-CFEngine-Nova-2_002e2-REST-API-and-the-CFEngine-Enterprise-3_002e0-API)
        -   [1.2.1 Read vs.
            Read/Write](/manuals/Enterprise-3-0-API#Read-vs_002e-Read_002fWrite)
        -   [1.2.2 Built-in Reports vs. Reporting
            Engine](/manuals/Enterprise-3-0-API#Built_002din-Reports-vs_002e-Reporting-Engine)
        -   [1.2.3
            Content-Type](/manuals/Enterprise-3-0-API#Content_002dType)
        -   [1.2.4 New Users](/manuals/Enterprise-3-0-API#New-Users)
        -   [1.2.5 Base Path](/manuals/Enterprise-3-0-API#Base-Path)
        -   [1.2.6 Still
            available](/manuals/Enterprise-3-0-API#Still-available)
        -   [1.2.7 Mission
            Portal](/manuals/Enterprise-3-0-API#Mission-Portal)

    -   [1.3 Checking
        Status](/manuals/Enterprise-3-0-API#Checking-Status)
    -   [1.4 Managing
        Settings](/manuals/Enterprise-3-0-API#Managing-Settings)
        -   [1.4.1 Viewing
            settings](/manuals/Enterprise-3-0-API#Viewing-settings)
        -   [1.4.2 Example: Configuring
            LDAP](/manuals/Enterprise-3-0-API#Example-_002d-Configuring-LDAP)
        -   [1.4.3 Example: Configuring Active
            Directory](/manuals/Enterprise-3-0-API#Example-_002d-Configuring-Active-Directory)
        -   [1.4.4 Example: Changing The Log
            Level](/manuals/Enterprise-3-0-API#Example-_002d-Changing-The-Log-Level)

    -   [1.5 Managing Users and
        Roles](/manuals/Enterprise-3-0-API#Managing-Users-and-Roles)
        -   [1.5.1 Example: Listing
            Users](/manuals/Enterprise-3-0-API#Example-_002d-Listing-Users)
        -   [1.5.2 Example: Creating a New
            User](/manuals/Enterprise-3-0-API#Example-_002d-Creating-a-New-User)
        -   [1.5.3 Example: Updating an Existing
            User](/manuals/Enterprise-3-0-API#Example-_002d-Updating-an-Existing-User)
        -   [1.5.4 Example: Retrieving a
            User](/manuals/Enterprise-3-0-API#Example-_002d-Retrieving-a-User)
        -   [1.5.5 Example: Adding a User to a
            Role](/manuals/Enterprise-3-0-API#Example-_002d-Adding-a-User-to-a-Role)
        -   [1.5.6 Example: Deleting a
            User](/manuals/Enterprise-3-0-API#Example-_002d-Deleting-a-User)
        -   [1.5.7 Example: Creating a New
            Role](/manuals/Enterprise-3-0-API#Example-_002d-Creating-a-New-Role)

    -   [1.6 Browsing Host
        Information](/manuals/Enterprise-3-0-API#Browsing-Host-Information)
        -   [1.6.1 Example: Listing Hosts With A Given
            Context](/manuals/Enterprise-3-0-API#Example-_002d-Listing-Hosts-With-A-Given-Context)
        -   [1.6.2 Example: Looking Up Hosts By
            Hostname](/manuals/Enterprise-3-0-API#Example-_002d-Looking-Up-Hosts-By-Hostname)
        -   [1.6.3 Example: Looking Up Hosts By
            IP](/manuals/Enterprise-3-0-API#Example-_002d-Looking-Up-Hosts-By-IP)
        -   [1.6.4 Example: Removing Host
            Data](/manuals/Enterprise-3-0-API#Example-_002d-Removing-Host-Data)
        -   [1.6.5 Example: Listing Available Vital Signs For A
            Host](/manuals/Enterprise-3-0-API#Example-_002d-Listing-Available-Vital-Signs-For-A-Host)
        -   [1.6.6 Example: Retrieving Vital Sign
            Data](/manuals/Enterprise-3-0-API#Example-_002d-Retrieving-Vital-Sign-Data)

    -   [1.7 SQL Queries](/manuals/Enterprise-3-0-API#SQL-Queries)
        -   [1.7.1 Synchronous
            Queries](/manuals/Enterprise-3-0-API#Synchronous-Queries)
            -   [1.7.1.1 Example: Listing Hostname and IP for Ubuntu
                Hosts](/manuals/Enterprise-3-0-API#Synchronous-Queries)

        -   [1.7.2 Asynchronous
            Queries](/manuals/Enterprise-3-0-API#Asynchronous-Queries)
            -   [1.7.2.1 Issuing The
                Query](/manuals/Enterprise-3-0-API#Asynchronous-Queries)
            -   [1.7.2.2 Checking
                Status](/manuals/Enterprise-3-0-API#Asynchronous-Queries)
            -   [1.7.2.3 Getting The Completed
                Report](/manuals/Enterprise-3-0-API#Asynchronous-Queries)

        -   [1.7.3 Subscribed
            Queries](/manuals/Enterprise-3-0-API#Subscribed-Queries)
            -   [1.7.3.1 Example: Creating A Subscribed
                Query](/manuals/Enterprise-3-0-API#Subscribed-Queries)
            -   [1.7.3.2 Example: Listing Report
                Subscriptions](/manuals/Enterprise-3-0-API#Subscribed-Queries)
            -   [1.7.3.3 Example: Removing A Report
                Subscription](/manuals/Enterprise-3-0-API#Subscribed-Queries)

    -   [1.8 API Reference](/manuals/Enterprise-3-0-API#API-Reference)
        -   [1.8.1 /api](/manuals/Enterprise-3-0-API#_002fapi)
        -   [1.8.2
            /api/settings](/manuals/Enterprise-3-0-API#_002fapi_002fsettings)
        -   [1.8.3
            /api/user](/manuals/Enterprise-3-0-API#_002fapi_002fuser)
        -   [1.8.4
            /api/user/:id](/manuals/Enterprise-3-0-API#_002fapi_002fuser_002fid)
        -   [1.8.5
            /api/role](/manuals/Enterprise-3-0-API#_002fapi_002frole)
        -   [1.8.6
            /api/role/:id](/manuals/Enterprise-3-0-API#_002fapi_002frole_002fid)
        -   [1.8.7
            /api/host](/manuals/Enterprise-3-0-API#_002fapi_002fhost)
        -   [1.8.8
            /api/host/:host-id](/manuals/Enterprise-3-0-API#_002fapi_002fhost_002fhost_002did)
        -   [1.8.9
            /api/host/:host-id/context](/manuals/Enterprise-3-0-API#_002fapi_002fhost_002fhost_002did_002fcontext)
        -   [1.8.10
            /api/host/:host-id/context/:context-id](/manuals/Enterprise-3-0-API#_002fapi_002fhost_002fhost_002did_002fcontext_002fcontext_002did)
        -   [1.8.11
            /api/host/:host-id/vital](/manuals/Enterprise-3-0-API#_002fapi_002fhost_002fhost_002did_002fvital)
            -   [1.8.11.1
                /api/host/:host-id/vital/:vital-id](/manuals/Enterprise-3-0-API#_002fapi_002fhost_002fhost_002did_002fvital)

        -   [1.8.12
            /api/promise](/manuals/Enterprise-3-0-API#_002fapi_002fpromise)
        -   [1.8.13
            /api/promise/:promise-id](/manuals/Enterprise-3-0-API#_002fapi_002fpromise_002fpromise_002did)
        -   [1.8.14
            /api/query](/manuals/Enterprise-3-0-API#_002fapi_002fquery)
        -   [1.8.15
            /api/query/async](/manuals/Enterprise-3-0-API#_002fapi_002fquery_002fasync)
        -   [1.8.16
            /api/query/async/:async-query-id](/manuals/Enterprise-3-0-API#_002fapi_002fquery_002fasync_002fasync_002dquery_002did)

