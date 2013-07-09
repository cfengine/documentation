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

**Arguments**:

* `array` : Array name, in the range `.*`

String name of the array to populate with the result of the search   

* `uri` : URI, in the range `.*`

String value of the ldap server. e.g. `"ldap://ldap.cfengine.com.no"`   

* `dn` : Distinguished name, in the range `.*`

Distinguished name, an ldap formatted name built from components, e.g.
"dc=cfengine,dc=com".   

* `filter` : Filter, in the range `.*`

String filter criterion, in ldap search, e.g. "(sn=User)".   

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
classes:

   "gotdata" expression => ldaparray(
                                    "myarray",
                                    "ldap://ldap.example.org",
                                    "dc=cfengine,dc=com",
                                    "(uid=mark)",
                                    "subtree",
                                    "none");
```
