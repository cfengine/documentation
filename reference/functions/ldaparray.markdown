---
layout: default
title: ldaparray
categories: [Reference, Functions, ldaparray]
published: true
alias: reference-functions-ldaparray.html
tags: [reference, functions, ldaparray]
---

**This function is only available in CFEngine Enterprise.**



**Prototype**: ldaparray(arg1,arg2,arg3,arg4,arg5,arg6) 

**Return type**:

`class`

  
 *arg1* : Array name, *in the range* .\*   
 *arg2* : URI, *in the range* .\*   
 *arg3* : Distinguished name, *in the range* .\*   
 *arg4* : Filter, *in the range* .\*   
 *arg5* : Search scope policy, *in the range* subtree,onelevel,base   
 *arg6* : Security level, *in the range* none,ssl,sasl   

Extract all values from an LDAP record

**Example**:  
   

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

**Notes**:  
   

```cf3
     
     (class) ldaparray (array,uri,dn,filter,scope,security)
     
```

This function retrieves an entire record with all elements and populates
an associative array with the entries. It returns a class that is true
if there was a match for the search, and false if nothing was retrieved.

**ARGUMENTS**:

array

String name of the array to populate with the result of the search   

uri

String value of the ldap server. e.g. `"ldap://ldap.cfengine.com.no"`   

dn

Distinguished name, an ldap formatted name built from components, e.g.
"dc=cfengine,dc=com".   

filter

String filter criterion, in ldap search, e.g. "(sn=User)".   

scope

Menu option, the type of ldap search, from

```cf3
              subtree
              onelevel
              base
```

  

security

Menu option indicating the encryption and authentication settings for
communication with the LDAP server. These features might be subject to
machine and server capabilities.

```cf3
               none
               ssl
               sasl
```
