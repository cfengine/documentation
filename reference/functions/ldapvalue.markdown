---
layout: default
title: ldapvalue
categories: [Reference, Functions, ldapvalue]
published: true
alias: reference-functions-ldapvalue.html
tags: [reference, communication functions, functions, ldapvalue]
---

**This function is only available in CFEngine Enterprise.**

[%CFEngine_function_prototype(uri, dn, filter, record, scope, security)%]

**Description:** Returns the first matching named value from ldap.

This function retrieves a single field from a single LDAP record
identified by the search parameters. The first matching value it taken.

[%CFEngine_function_attributes(uri, dn, filter, record, scope, security)%]

`dn` specifies the distinguished name, an ldap formatted name built from 
components, e.g. "dc=cfengine,dc=com". `filter` is an ldap search, e.g. 
"(sn=User)", and `record` is the name of the single record to be retrieved, 
e.g. `uid`. Which `security` values are supported depends on machine and
server capabilities.

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

