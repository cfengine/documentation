---
layout: default
title: reglist
categories: [Reference, Functions, reglist]
published: true
alias: reference-functions-reglist.html
tags: [reference, functions, reglist]
---

**Prototype**: `reglist(list, regex)`

**Return type**: `class`

**Description**: Returns whether the regular expression `regex` matches any item in `list`.

**Arguments**:

* `list` : list identifier, in the range `@[(][a-zA-Z0-9]+[)]`
* `regex` : Regular expression, in the range `.*`

The regular expression is [anchored][anchored], meaning it must match the entire string.

**Example**:

```cf3
    vars:

     "nameservers" slist => {
                            "128.39.89.10",
                            "128.39.74.16",
                            "192.168.1.103"
                            };
    classes:

      "am_name_server" expression => reglist("@(nameservers)",escape("$(sys.ipv4[eth0])"));
```

In the example above, the IP address in `$(sys.ipv4[eth0])` must be `escape`d, 
so that the (.) characters in the IP address are not interpreted as the 
regular expression "match any" characters.
