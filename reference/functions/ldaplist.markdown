---
layout: default
title: ldaplist
categories: [Reference, Functions, ldaplist]
published: true
alias: reference-functions-ldaplist.html
tags: [reference, communication functions, functions, ldaplist]
---

**This function is only available in CFEngine Enterprise.**

[%CFEngine_function_prototype(uri, dn, filter, record, scope, security)%]

**Description:** Returns a list with all named values from multiple ldap records.

This function retrieves a single field from all matching LDAP records
identified by the search parameters.

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

   # Get all matching values for "uid" - should be a single record match

  "list" slist =>  ldaplist(
                           "ldap://ldap.example.org",
                           "dc=cfengine,dc=com",
                           "(sn=User)",
                           "uid",
                           "subtree",
                           "none"
                           );
```
