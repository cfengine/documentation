---
layout: default
title: sort
categories: [Reference, Functions, sort]
published: true
alias: reference-functions-sort.html
tags: [reference, data functions, functions, sort]
---

[%CFEngine_function_prototype(list, mode)%]

**Description:** Returns `list` sorted according to `mode`.

Lexicographical, integer, real, IP, and MAC address sorting is
supported currently.  The example below will show each sorting mode in
action.

Note IPv6 addresses can not use uppercase hexadecimal characters
(`A-Z`) but must use lowercase (`a-z`) instead.

[%CFEngine_function_attributes(regex, mode)%]

**Example:**

[%CFEngine_include_snippet(sort.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

```
2013-09-05T14:05:04-0400   notice: R: sorted lexicographically 'b,c,a' => 'a,b,c'
2013-09-05T14:05:04-0400   notice: R: sorted lexicographically '100,9,10,8.23' => '10,100,8.23,9'
2013-09-05T14:05:04-0400   notice: R: sorted lexicographically '' => ''
2013-09-05T14:05:04-0400   notice: R: sorted lexicographically ',a,,b' => ',,a,b'
2013-09-05T14:05:04-0400   notice: R: sorted lexicographically 'a,1,b' => '1,a,b'
2013-09-05T14:05:04-0400   notice: R: sorted integers '100,9,10,8.23' => '8.23,9,10,100'
2013-09-05T14:05:04-0400   notice: R: sorted reals '100,9,10,8.23' => '8.23,9,10,100'
2013-09-05T14:05:04-0400   notice: R: sorted IPs '100.200.100.0,1.2.3.4,9.7.5.1,9,9.7,9.7.5,,-1,where are the IP addresses?' => ',-1,9,9.7,9.7.5,where are the IP addresses?,1.2.3.4,9.7.5.1,100.200.100.0'
2013-09-05T14:05:04-0400   notice: R: sorted IPv6s 'FE80:0000:0000:0000:0202:B3FF:FE1E:8329,FE80::0202:B3FF:FE1E:8329,::1,2001:db8:0:0:1:0:0:1,2001:0db8:0:0:1:0:0:1,2001:db8::1:0:0:1,2001:db8::0:1:0:0:1,2001:0db8::1:0:0:1,2001:db8:0:0:1::1,2001:db8:0000:0:1::1,2001:DB8:0:0:1::1,8000:63bf:3fff:fdd2,::ffff:192.0.2.47,fdf8:f53b:82e4::53,fe80::200:5aee:feaa:20a2,2001:0000:4136:e378:,8000:63bf:3fff:fdd2,2001:0002:6c::430,2001:10:240:ab::a,2002:cb0a:3cdd:1::1,2001:db8:8:4::2,ff01:0:0:0:0:0:0:2,-1,where are the IP addresses?' => '-1,2001:0000:4136:e378:,2001:DB8:0:0:1::1,8000:63bf:3fff:fdd2,8000:63bf:3fff:fdd2,::ffff:192.0.2.47,FE80:0000:0000:0000:0202:B3FF:FE1E:8329,FE80::0202:B3FF:FE1E:8329,where are the IP addresses?,::1,2001:0002:6c::430,2001:10:240:ab::a,2001:db8:0000:0:1::1,2001:db8:0:0:1::1,2001:0db8::1:0:0:1,2001:db8::0:1:0:0:1,2001:db8::1:0:0:1,2001:0db8:0:0:1:0:0:1,2001:db8:0:0:1:0:0:1,2001:db8:8:4::2,2002:cb0a:3cdd:1::1,fdf8:f53b:82e4::53,fe80::200:5aee:feaa:20a2,ff01:0:0:0:0:0:0:2'
2013-09-05T14:05:04-0400   notice: R: sorted MACs '00:14:BF:F7:23:1D,0:14:BF:F7:23:1D,:14:BF:F7:23:1D,00:014:BF:0F7:23:01D,00:14:BF:F7:23:1D,0:14:BF:F7:23:1D,:14:BF:F7:23:1D,00:014:BF:0F7:23:01D,01:14:BF:F7:23:1D,1:14:BF:F7:23:1D,01:14:BF:F7:23:2D,1:14:BF:F7:23:2D,-1,where are the MAC addresses?' => '-1,:14:BF:F7:23:1D,:14:BF:F7:23:1D,where are the MAC addresses?,00:014:BF:0F7:23:01D,0:14:BF:F7:23:1D,00:14:BF:F7:23:1D,00:014:BF:0F7:23:01D,0:14:BF:F7:23:1D,00:14:BF:F7:23:1D,1:14:BF:F7:23:1D,01:14:BF:F7:23:1D,1:14:BF:F7:23:2D,01:14:BF:F7:23:2D'
```

**See also:** [`shuffle()`][shuffle].
