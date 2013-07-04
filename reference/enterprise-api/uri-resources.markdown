---
layout: default
title:  URI Resources
categories: [Reference, Enterprise API, URI Resources]
published: true
alias: reference-enterprise-api-uri-resources.html
tags: [reference, enterprise, REST, API, reporting, sql, URI]
---

### /api

**Supported Operations**: `GET`

**Fields**:

-   `apiName` *(string)* Human-friendly API name.
-   `apiVersion` *(string)* API version string.
-   `enterpriseVersion` *(string)* Version of the CFEngine Enterprise
    build.
-   `coreVersion` *(string)* The version of CFEngine Core (Community)
    the Enterprise version was built against.
-   `databaseHostname` *(string)* Hostname (or IP) of the database the
    API is connected to.
-   `databasePort` *(integer)* Port number of the database the API is
    connected to.
-   `authenticated` *("internal", "external")*, Whether the request
    was authenticated using the internal users table or an external
    source.
-   `license.expires` *(integer)* Time when the license expires.
-   `license.installTime` *(integer)* Time when the license was
    installed.
-   `license.owner` *(string)* The name of the license owner.
-   `license.granted` *(integer)* Host number capacity granted by the
    license.
-   `license.licenseUsage.lastMeasured` *(integer)* Time when license
    usage was last updated.
-   `license.licenseUsage.samples` *(integer)* Number of samples
    collected for license usage.
-   `license.licenseUsage.minObservedLevel` *(integer)* Minimum number
    of observed host licenses in use.
-   `license.licenseUsage.minObservedLevel` *(integer)* Maximum number
    of observed host licenses in use.
-   `license.licenseUsage.meanUsage` *(integer)* Average number of
    observed host licenses in use.
-   `license.licenseUsage.meanCumulativeUtilization` *(integer)* (not
    sure)
-   `license.licenseUsage.usedToday` *(integer)* Total number of host
    licenses observed used today.


### /api/settings

**Supported Operations**: `GET`, `POST`

**Fields**:

-   `rbacEnabled` *(boolean)* Whether RBAC is applied to requests.
-   `ldapEnabled` *(boolean)* Whether external authentication is
    activated.
-   `activeDirectoryDomain` *(string)* AD domain to use if AD is
    enabled in `ldapMode`.
-   `ldapBaseDN` *(string)* LDAP BaseDN to use for external LDAP
    requests.
-   `ldapEncryption` *("plain", "ssl", "tls")* Type of LDAP binding to
    establish to external LDAP server. (Default: "plain").
-   `ldapHost` *(string)* Hostname of external LDAP server.
-   `ldapMode` *("standard", "activeDirectory")* Type of LDAP server
    to use. "standard" is effectively OpenLDAP. (Default: "standard").
-   `ldapLoginAttribute` *(string)* LDAP attribute to use for
    usernames. (default: "uid").
-   `ldapUsername` *(string)* LDAP username.
-   `ldapPassword` *(string)* LDAP password.
-   `ldapUsersDirectory` *(string)* Attribute and value to qualify the
    directory in which to look up users, e.g. "ou=people".
-   `ldapPort` *(integer)* Port for external LDAP connections not
    using SSL. (default 389).
-   `ldapPort` *(integer)* Port for external LDAP connections using
    SSL. (default 636).
-   `blueHostHorizon` *(integer)* Time interval (seconds) for when to
    consider a host unreachable. (default 900).
-   `logLevel` *("emergency", "alert", "critical", "error", "warning",
    "notice", "info", "debug")* Syslog filter specifying the severity
    level at which messages produced by the API should be emitted to
    syslog and apache.log. (default: error).


### /api/user

**Supported Operations**: `GET`  

**Query Parameters**:

-   `id` *(regex string)* Regular expression for filtering usernames.
-   `external` *("true", "false")* Returns only internal users (false)
    or only external (true), or all if not specified.

### /api/user/:id

**Supported Operations**: `GET`, `PUT`, `POST`, `DELETE`

**Fields**:

-   `id` *(string)* ID of a user.
-   `password` *(string)* Password of a user. (Never returned from
    API).
-   `email` *(string)* Email address associated with user.
-   `roles` *(array of strings)* Set of IDs of roles a user is in.
    (Default: empty)
-   `external` *(boolean)* Whether or not the user was found
    externally (LDAP).


### /api/role

**Supported Operations**: `GET`


### /api/role/:id

**Supported Operations**: `GET`, `PUT`, `POST`, `DELETE`

**Fields**:

-   `id` *(string)* ID of a role.
-   `description` *(string)* Arbitrary text describing the role
-   `includeContext` *(comma delimited string of regular expression
    strings)* Includes hosts visible to the users in the role.
-   `excludeContext` *(comma delimited string of regular expression
    strings)* Excludes bundles visible to the users in the role.
-   `includeBundles` *(comma delimited string of regular expression
    strings)* Includes bundles visible to the users in the role.
-   `excludeBundles` *(comma delimited string of regular expression
    strings)* Excludes bundles visible to the users in the role.


### /api/host

**Supported Operations**: `GET`

*Query Parameters*:

-   `include-context` *(comma delimited string of regular expression
    strings)* Includes hosts having context matching the expression.
-   `exclude-context` *(comma delimited string of regular expression
    strings)* Excludes hosts having context matching the expression.


### /api/host/:host-id

-   `id` *(string)* ID of a host.
-   `hostname` *(string)* Hostname of a host.
-   `ip` *(string)* IP address of a host.

#### /api/host/:host-id/vital/:vital-id

**Supported Operations**: `GET`

*Query Parameters*:

-   `from` *(integer)* Timestamp marking the start of the interval for
    which to fetch data. Data is only available going back one week.
-   `to` *(integer)* End of data interval to be fetched.

**Fields**:

-   `id` *(string)* ID of vital sign.
-   `description` *(string)* Description of vital sign.
-   `units` *(string)* Measurement unit of vital sign.
-   `timestamp` *(integer)* Timestamp of the last received data point.
-   `values` *(array of [ t, y ], where t is the sample timestamp)*
    Vital sign data.

### /api/query

**Supported Operations**:  
`POST`

**Fields**:

-   `query` *(string)* SQL query string.
-   `sortColumn` *(string)* Column on which to sort results. This is
    applied to the result of the SQL query and can be considered post
    processing. The Mission Portal uses this to sort cached reports.
-   `sortDescending` *(boolean)* Apply post-sorting in descending order.
-   `skip` *(integer)* Number of results to skip for the processed
    query. The Mission Portal uses this for pagination on cached
    results.
-   `limit` *(integer)* Limit the number of results in the processed
    query.
-   `disableCache` *(boolean)* Don't use cached data


### /api/query/async

**Supported Operations**: `POST`

**Fields**:

-   `query` *(string)* SQL query string.
-   `id` *(string)* ID of the query job.
-   `error` *(string)* Error if anything went wrong.


### /api/query/async/:async-query-id

**Supported Operations**: `GET`, `DELETE`

**Fields**:

-   `id` *(string)* ID of the query job.
-   `percentageComplete` *(integer)* Processing status for the query.
-   `href` *(string)* Download link for the finished report.
-   `error` *(string)* Error if anything went wrong.
