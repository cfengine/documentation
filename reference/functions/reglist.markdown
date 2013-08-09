---
layout: default
title: reglist
categories: [Reference, Functions, reglist]
published: true
alias: reference-functions-reglist.html
tags: [reference, data functions, functions, reglist]
---

[%CFEngine_function_prototype(list, regex)%]

**Description:** Returns whether the [anchored][anchored] regular expression 
`regex` matches any item in `list`.

[%CFEngine_function_attributes(list, regex)%]

**Example:**

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
