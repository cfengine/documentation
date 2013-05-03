---
layout: default
title: Function-selectservers
categories: [Special-functions,Function-selectservers]
published: true
alias: Special-functions-Function-selectservers.html
tags: [Special-functions,Function-selectservers]
---

### Function selectservers

**Synopsis**: selectservers(arg1,arg2,arg3,arg4,arg5,arg6) returns type
**int**

\
 *arg1* : The identifier of a cfengine list of hosts or addresses to
contact, *in the range* @[(][a-zA-Z0-9]+[)] \
 *arg2* : The port number, *in the range* 0,99999999999 \
 *arg3* : A query string, *in the range* .\* \
 *arg4* : A regular expression to match success, *in the range* .\* \
 *arg5* : Maximum number of bytes to read from server, *in the range*
0,99999999999 \
 *arg6* : Name for array of results, *in the range*
[a-zA-Z0-9\_\$(){}\\[\\].:]+ \

Select tcp servers which respond correctly to a query and return their
number, set array of names

**Example**:\
 \

~~~~ {.verbatim}
body common control

{
bundlesequence  => { "test"  };
}

###########################################################

bundle agent test

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

~~~~

**Notes**:\
 \

This function selects all the TCP ports that are active and functioning
from an ordered list and builds an array of their names. This allows us
to select a current list of failover alternatives that are pretested.

hostlist

A list of host names or IP addresses to attempt to connect to. \

port

The port number for the service. \

sendstr

An optional string to send to the server to elicit a response. If
`sendstr` is empty, then no query is sent to the server. \

regex\_on\_reply

If a string is sent, this regex is anchored, meaning it must match the
entire resulting reply (see [Anchored vs. unanchored regular
expressions](#Anchored-vs_002e-unanchored-regular-expressions)). If
there is a multi-line response from the server, special care must be
taken to ensure that you match the newlines, too (note the use of `(?s)`
in the example above, which allows . to also match newlines in the
multi-line HTTP response). If `regex_on_reply` is empty, then no
reply-checking is performed (and any server reply is deemed to be
satisfactory). \

maxbytesread\_reply

The maximum number of bytes to read as the server's reply. \

array\_name

The name of the array to build containing the names of hosts that pass
the above tests. The array is ordered `array_name[0],..` etc.
