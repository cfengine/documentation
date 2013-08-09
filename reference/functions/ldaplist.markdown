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

[%CFEngine_function_attributes(uri, dn, filter, record, scope, security)%]

`dn` specifies the distinguished name, an ldap formatted name built from 
components, e.g. "dc=cfengine,dc=com". `filter` is an ldap search, e.g. 
"(sn=User)", and `record` is the name of the single record to be retrieved, 
e.g. `uid`. Which `security` values are supported depends on machine and
server capabilities.

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
