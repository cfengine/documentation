---
layout: default
title: How do I fix trust after an IP change?
published: true
sorting: 90
tags: [getting started, installation, faq]
---

Symptom:

After the policy server was restarted with the new IP address, clients would not connect:

```
error: Not authorized to trust public key of server '192.168.14.113' (trustkey = false)
error: Authentication dialogue with '192.168.14.113' failed
```

Bootstrapping the clients also fails:

```console
[root@dev /var/cfengine] /var/cfengine/bin/cf-agent --bootstrap  192.168.14.113
2014-06-23T13:57:07-0400   notice: R: This autonomous node assumes the role of voluntary client
2014-06-23T13:57:07-0400   notice: R: Failed to copy policy from policy server at 192.168.14.113:/var/cfengine/masterfiles
       Please check
       * cf-serverd is running on 192.168.14.113
       * network connectivity to 192.168.14.113 on port 5308
       * masterfiles 'body server control' - in particular allowconnects, trustkeysfrom and skipverify
       * masterfiles 'bundle server' -> access: -> masterfiles -> admit/deny
       It is often useful to restart cf-serverd in verbose mode (cf-serverd -v) on 192.168.14.113 to diagnose connection issues.
       When updating masterfiles, wait (usually 5 minutes) for files to propagate to inputs on 192.168.14.113 before retrying.
2014-06-23T13:57:07-0400   notice: R: Did not start the scheduler
2014-06-23T13:57:07-0400    error: Bootstrapping failed, no input file at '/var/cfengine/inputs/promises.cf' after bootstrap
```

Solution:

Assuming that `661df12c960af9afdde093e0cb339b4d` is the MD5 hostkey and
`192.168.14.113` is the new IP address:

```console
[root@hub]# cd /var/cfengine/ppkeys && mv -i root-MD5=661df12c960af9afdde093e0cb339b4d.pub root-192.168.14.113.pub
```
