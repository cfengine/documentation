---
layout: default
title: regldap
categories: [Reference, Functions, regldap]
published: true
alias: reference-functions-regldap.html
tags: [reference, communication functions, functions, regldap]
---

**This function is only available in CFEngine Enterprise.**

[%CFEngine_function_prototype(uri, dn, filter, record, scope, regex, security)%]

**Description:** Returns whether the regular expression `regex` matches a 
value item in the LDAP search.

This function retrieves a single field from all matching LDAP records
identified by the search parameters and compares it to the regular
expression `regex`.

[%CFEngine_function_attributes(uri, dn, filter, record, scope, regex, security)%]

`dn` specifies the distinguished name, an ldap formatted name built from 
components, e.g. "dc=cfengine,dc=com". `filter` is an ldap search, e.g. 
"(sn=User)", and `record` is the name of the single record to be retrieved
and matched against `regex`, e.g. `uid`. Which `security` values are supported 
depends on machine and server capabilities.

**Example:**

```cf3
classes:

   "found" expression => regldap(
                                "ldap://ldap.example.org",
                                "dc=cfengine,dc=com",
                                "(sn=User)",
                                "uid",
                                "subtree",
                                "jon.*",
                                "none"
                                );
```
