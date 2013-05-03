---
layout: default
title: Function-regldap
categories: [Special-functions,Function-regldap]
published: true
alias: Special-functions-Function-regldap.html
tags: [Special-functions,Function-regldap]
---

### Function regldap

**Synopsis**: regldap(arg1,arg2,arg3,arg4,arg5,arg6,arg7) returns type
**class**

\
 *arg1* : URI, *in the range* .\* \
 *arg2* : Distinguished name, *in the range* .\* \
 *arg3* : Filter, *in the range* .\* \
 *arg4* : Record name, *in the range* .\* \
 *arg5* : Search scope policy, *in the range* subtree,onelevel,base \
 *arg6* : Regex to match results, *in the range* .\* \
 *arg7* : Security level, *in the range* none,ssl,sasl \

True if the regular expression in arg6 matches a value item in an LDAP
search.

**Example**:\
 \

~~~~ {.verbatim}
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
~~~~

**Notes**:\
 \

~~~~ {.example}
     
     (class) regldap(uri,dn,filter,name,scope,regex,security)
     
~~~~

This function retrieves a single field from all matching LDAP records
identified by the search parameters and compares it to a regular
expression. If there is a match, true is returned else false.

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

regex

A regular expression string to match to the results of an LDAP search.
The regular expression is anchored, meaning it must match the entire
named field (See [Anchored vs. unanchored regular
expressions](#Anchored-vs_002e-unanchored-regular-expressions)). If any
item matches the regex, the result will be true. \

security

Menu option indicating the encryption and authentication settings for
communication with the LDAP server. These features might be subject to
machine and server capabilities.

~~~~ {.smallexample}
               none
               ssl
               sasl
~~~~
