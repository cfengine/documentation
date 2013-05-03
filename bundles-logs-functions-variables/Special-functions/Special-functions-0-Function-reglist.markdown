---
layout: default
title: Function-reglist
categories: [Special-functions,Function-reglist]
published: true
alias: Special-functions-Function-reglist.html
tags: [Special-functions,Function-reglist]
---

### Function reglist

**Synopsis**: reglist(arg1,arg2) returns type **class**

\
 *arg1* : Cfengine list identifier, *in the range* @[(][a-zA-Z0-9]+[)] \
 *arg2* : Regular expression, *in the range* .\* \

True if the regular expression in arg2 matches any item in the list
whose id is arg1

**Example**:\
 \

~~~~ {.verbatim}
vars:

 "nameservers" slist => {
                        "128.39.89.10",
                        "128.39.74.16",
                        "192.168.1.103"
                        };
classes:

  "am_name_server" expression => reglist("@(nameservers)",escape("$(sys.ipv4[eth0])"));
~~~~

**Notes**:\
 \

Matches a list of test strings to a regular expression. In the example
above, the IP address in `$(sys.ipv4[eth0])` must be `escape`d, because
if not, the dot (.) characters in the IP address would be interpreted as
regular expression "match any" characters.

**ARGUMENTS**:

list

The list of strings to test with the regular expression. \

regex

The scalar regular expression string. The regular expression is
anchored, meaning it must match the entire string (See [Anchored vs.
unanchored regular
expressions](#Anchored-vs_002e-unanchored-regular-expressions)).
