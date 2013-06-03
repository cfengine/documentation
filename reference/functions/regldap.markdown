---
layout: default
title: regldap
categories: [Reference, Functions, regldap]
published: true
alias: reference-functions-regldap.html
tags: [reference, functions, regldap]
---

**This function is only available in CFEngine Enterprise.**

**Prototype**: `regldap(uri, dn, filter, record, scope, regex, security)`

**Return type**: `class`

**Description**: Returns whether the regular expression `regex` matches a 
value item in the LDAP search.

This function retrieves a single field from all matching LDAP records
identified by the search parameters and compares it to the regular
expression `regex`.

**Arguments**:

* `uri` : URI, *in the range* .\*

String value of the ldap server. e.g. `"ldap://ldap.cfengine.com.no"`   

* `dn` : Distinguished name, *in the range* .\*

Distinguished name, an ldap formatted name built from components, e.g.
"dc=cfengine,dc=com".   

* `filter` : Filter, *in the range* .\*

String filter criterion, in ldap search, e.g. "(sn=User)".   

* `record` : Record name, *in the range* .\*

String value with the name of the single record to be retrieved, e.g. `uid`.

* `scope` : Search scope policy, one of
    * subtree
    * onelevel
    * base

* `arg6` : Regex to match results, *in the range* .\*

* `security` : Security level, one of
    * none
    * ssl
    * sasl

Menu option indicating the encryption and authentication settings for
communication with the LDAP server. These features might be subject to
machine and server capabilities.

**Example**:

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
