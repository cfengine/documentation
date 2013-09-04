---
layout: default
title: ldapvalue
categories: [Reference, Functions, ldapvalue]
published: true
alias: reference-functions-ldapvalue.html
tags: [reference, communication functions, functions, ldap]
---

**This function is only available in CFEngine Enterprise.**

**Prototype:** `ldapvalue(uri, dn, filter, record, scope, security)`

**Return type:** `string`

**Description:** Returns the first matching named value from ldap.

This function retrieves a single field from a single LDAP record
identified by the search parameters. The first matching value it taken.

**Arguments**:

* `uri` : URI, in the range `.*`

String value of the ldap server. e.g. `"ldap://ldap.cfengine.com.no"`   

* `dn` : Distinguished name, in the range `.*`

Distinguished name, an ldap formatted name built from components, e.g.
"dc=cfengine,dc=com".   

* `filter` : Filter, in the range `.*`

String filter criterion, in ldap search, e.g. "(sn=User)".   

* `record` : Record name, in the range `.*`

String value with the name of the single record to be retrieved, e.g. `uid`.

* `scope` : Search scope policy, one of
    * subtree
    * onelevel
    * base

* `security` : Security level, one of
    * none
    * ssl
    * sasl

Menu option indicating the encryption and authentication settings for
communication with the LDAP server. These features might be subject to
machine and server capabilities.

**Example:**

```cf3
vars:

   # Get the first matching value for "uid" in schema

  "value" string => ldapvalue(
                             "ldap://ldap.example.org", 
                             "dc=cfengine,dc=com",
                             "(sn=User)",
                             "uid",
                             "subtree",
                             "none"
                             );
```

