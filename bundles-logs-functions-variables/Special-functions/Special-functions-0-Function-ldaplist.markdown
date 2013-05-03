---
layout: default
title: Function-ldaplist
categories: [Special-functions,Function-ldaplist]
published: true
alias: Special-functions-Function-ldaplist.html
tags: [Special-functions,Function-ldaplist]
---

### Function ldaplist

**Synopsis**: ldaplist(arg1,arg2,arg3,arg4,arg5,arg6) returns type
**slist**

\
 *arg1* : URI, *in the range* .\* \
 *arg2* : Distinguished name, *in the range* .\* \
 *arg3* : Filter, *in the range* .\* \
 *arg4* : Record name, *in the range* .\* \
 *arg5* : Search scope policy, *in the range* subtree,onelevel,base \
 *arg6* : Security level, *in the range* none,ssl,sasl \

Extract all named values from multiple ldap records

**Example**:\
 \

~~~~ {.verbatim}
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
~~~~

**Notes**:\
 \

~~~~ {.example}
     
     (slist) ldaplist(uri,dn,filter,name,scope,security)
     
~~~~

This function retrieves a single field from all matching LDAP records
identified by the search parameters.

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

\

security

Menu option indicating the encryption and authentication settings for
communication with the LDAP server. These features might be subject to
machine and server capabilities.

~~~~ {.smallexample}
               none
               ssl
               sasl
~~~~
