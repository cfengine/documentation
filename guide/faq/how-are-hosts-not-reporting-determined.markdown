---
layout: default
title: How are hosts not reporting determined?
published: true
sorting: 90
tags: [getting started, faq, health, enterprise]
---

Hosts that have not been collected from within `blueHostHorizon` seconds will
show up under "Hosts not reporting".

`blueHostHorizon` defaults to 900 seconds (15 minutes). You can inspect the
current value of `blueHostHorizon` from Mission Portal or via the API:

```console
$ curl -s -u admin:admin http://hub/api/settings/ | jq ".data[0].blueHostHorizon"
900
```

**See Also**: `Enterprise API Reference`, `Enterprise API Examples`, `How are
agents not running determined?`
