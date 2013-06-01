---
layout: default
title: ldapvalue
categories: [Reference, Functions, ldapvalue]
published: true
alias: reference-functions-ldapvalue.html
tags: [reference, functions, ldapvalue]
---

**This function is only available in CFEngine Enterprise.**

**Prototype**: `ldapvalue(arg1, arg2, arg3, arg4,arg5, arg6)`

**Return type**:

`string`

* `arg1` : URI, *in the range* .\*
* `arg2` : Distinguished name, *in the range* .\*
* `arg3` : Filter, *in the range* .\*
* `arg4` : Record name, *in the range* .\*
* `arg5` : Search scope policy, *in the range* subtree,onelevel,base   
* `arg6` : Security level, *in the range* none,ssl,sasl   

Extract the first matching named value from ldap

**Example**:

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

**Notes**:
```cf3
     
     (string) ldapvalue(uri,dn,filter,name,scope,security)
     
```

This function retrieves a single field from a single LDAP record
identified by the search parameters. The first matching value it taken.

**ARGUMENTS**:

uri

String value of the ldap server. e.g. `"ldap://ldap.cfengine.com.no"`   

dn

Distinguished name, an ldap formatted name built from components, e.g.
"dc=cfengine,dc=com".   

filter

String filter criterion, in ldap search, e.g. "(sn=User)".   

name

String value, the name of a single record to be retrieved, e.g. `uid`.

scope

Menu option, the type of ldap search, from the specified root. May take
values:

```cf3
              subtree
              onelevel
              base
```
