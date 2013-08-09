---
layout: default
title: ldaparray
categories: [Reference, Functions, ldaparray]
published: true
alias: reference-functions-ldaparray.html
tags: [reference, communication functions, functions, ldaparray]
---

**This function is only available in CFEngine Enterprise.**

[%CFEngine_function_prototype(array, uri, dn, filter, scope, security)%]

**Description:** Fills `array` with the entire LDAP record, and returns 
whether there was a match for the search.

This function retrieves an entire record with all elements and populates
an associative array with the entries. It returns a class that is true
if there was a match for the search, and false if nothing was retrieved.

[%CFEngine_function_attributes(array, uri, dn, filter, scope, security)%]

`dn` specifies the distinguished name, an ldap formatted name built from 
components, e.g. "dc=cfengine,dc=com". `filter` is an ldap search, e.g. 
"(sn=User)". Which `security` values are supported depends on machine and
server capabilities.

**Example:**

```cf3
classes:

   "gotdata" expression => ldaparray(
                                    "myarray",
                                    "ldap://ldap.example.org",
                                    "dc=cfengine,dc=com",
                                    "(uid=mark)",
                                    "subtree",
                                    "none");
```
