---
layout: default
title: selectservers
categories: [Reference, Functions, selectservers]
published: true
alias: reference-functions-selectservers.html
tags: [reference, communication functions, functions, selectservers]
---

[%CFEngine_function_prototype(hostlist, port, query, regex, maxbytes, array)%]

**Description:** Returns the number of tcp servers from `hostlist` which 
respond with a reply matching `regex` to a `query` send to `port`, and 
populates `array` with their names.

The regular expression is [anchored][anchored]. If `query` is empty, then no
reply checking is performed (any server reply is deemed to be satisfactory), 
otherwise at most `maxbytes` bytes are read from the server and matched.

This function allows discovery of all the TCP ports that are active and 
functioning from an ordered list, and builds an array of their names. This 
allows maintaining a list of pretested failover alternatives.

[%CFEngine_function_attributes(hostlist, port, query, regex, maxbyes, array)%]

**Example:**

```cf3
    bundle agent example
    {     
    vars:

     "hosts" slist => { "slogans.iu.hio.no", "eternity.iu.hio.no", "nexus.iu.hio.no" };
     "fhosts" slist => { "www.cfengine.com", "www.cfengine.org" };
 
     "up_servers" int =>  selectservers("@(hosts)","80","","","100","alive_servers");
     "has_favicon" int =>
            selectservers(
                "@(hosts)", "80",
            "GET /favicon.ico HTTP/1.0$(const.n)Host: www.cfengine.com$(const.n)$(const.n)",
            "(?s).*OK.*",
            "200", "favicon_servers");

    classes:

      "someone_alive" expression => isgreaterthan("$(up_servers)","0");

      "has_favicon" expression => isgreaterthan("$(has_favicon)","0");

    reports:
        "Number of active servers $(up_servers)";

      someone_alive::
        "First server $(alive_servers[0]) fails over to $(alive_servers[1])";

      has_favicon::
        "At least $(favicon_servers[0]) has a favicon.ico";

    }
```

If there is a multi-line response from the server, special care must be
taken to ensure that newlines are matched, too. Note the use of `(?s)`
in the example, which allows `.` to also match newlines in the
multi-line HTTP response.
