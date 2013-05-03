---
layout: default
title: Function-ldapvalue
categories: [Special-functions,Function-ldapvalue]
published: true
alias: Special-functions-Function-ldapvalue.html
tags: [Special-functions,Function-ldapvalue]
---

### Function ldapvalue

**Synopsis**: ldapvalue(arg1,arg2,arg3,arg4,arg5,arg6) returns type
**string**

\
 *arg1* : URI, *in the range* .\* \
 *arg2* : Distinguished name, *in the range* .\* \
 *arg3* : Filter, *in the range* .\* \
 *arg4* : Record name, *in the range* .\* \
 *arg5* : Search scope policy, *in the range* subtree,onelevel,base \
 *arg6* : Security level, *in the range* none,ssl,sasl \

Extract the first matching named value from ldap

**Example**:\
 \

~~~~ {.verbatim}
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
~~~~

**Notes**:\
 \

~~~~ {.example}
     
     (string) ldapvalue(uri,dn,filter,name,scope,security)
     
~~~~

This function retrieves a single field from a single LDAP record
identified by the search parameters. The first matching value it taken.

**ARGUMENTS**:

uri

String value of the ldap server. e.g. `"ldap://ldap.cfengine.com.no"` \

dn

Distinguished name, an ldap formatted name built from components, e.g.
"dc=cfengine,dc=com". \

filter

String filter criterion, in ldap search, e.g. "(sn=User)". \

name

String value, the name of a single record to be retrieved, e.g. `uid`. \

scope

Menu option, the type of ldap search, from the specified root. May take
values:

~~~~ {.smallexample}
              subtree
              onelevel
              base
~~~~
