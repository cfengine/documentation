---
layout: default
title: Enable plain http
published: true
tags: [cfengine enterprise, hub administration, SSL]
---

By default HTTPS is enforced by redirecting any non secure connection requests.

If you would like to enable plain HTTP you can do so by defining
`cfe_enterprise_enable_plain_http` from an [augments file][Augments].

For example, simply place the following inside `def.json` in the root of your
masterfiles.

```
{
  "classes": {
    "cfe_enterprise_enable_plain_http": [ "any" ]
    }

}
```
