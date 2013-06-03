---
layout: default
title: selectservers
categories: [Reference, Functions, selectservers]
published: true
alias: reference-functions-selectservers.html
tags: [reference, functions, selectservers]
---

**Prototype**: `selectservers(hostlist, port, query, regex,maxbytes, array)`

**Return type**: `int`

**Description**: Returns the number of tcp servers from `hostlist` which 
respond correctly to a query send to `port`, and populates array with their 
names.

This function allows discovery of all the TCP ports that are active and 
functioning from an ordered list, and builds an array of their names. This 
allows maintaining a list of pretested failover alternatives.

**Arguments**:

* `hostlist` : The identifier of a cfengine list of hosts or addresses to
contact, *in the range* @[(][a-zA-Z0-9]+[)]   
* `port` : The port number, *in the range* 0,99999999999   
* `query` : An optional query string, *in the range* .\*
* `regex` : A regular expression to match success, *in the range* .\*

If a query string is sent, this regular expression is anchored, meaning it 
must match the entire resulting reply. If `query` is empty, then no reply-checking is performed (and any server reply is deemed to be
satisfactory).

* `maxbytes` : Maximum number of bytes to read from server, *in the range*
0,99999999999   
* `array` : Name for array of results, *in the range*
[a-zA-Z0-9\_\$(){}\\[\\].:]+

**Example**:

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

      cfengine_3::
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
