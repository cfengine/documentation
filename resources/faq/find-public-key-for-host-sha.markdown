---
layout: default
title: How do I find the public key for a given host
published: true
sorting: 90
tags: [ FAQ, cf-key  ]
---

Trying to locate the public key for a host on your hub in order to validate
trust? Use this snippet to figure out which public key file in
`/var/cfengine/ppkeys` matches a given host.

```console
# KEY="SHA=31bcb32950d8b91ffdfca85bca71364ec8f67c93246e3617c3a49af58363c4a1"
# for each in $(ls /var/cfengine/ppkeys/*.pub); do
 if [ "$(cf-key -n -p ${each})" = "$KEY" ]; then
  echo "Found KEY in $each";
 fi
done
```

