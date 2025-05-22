---
layout: default
title: Custom LDAPs certificate
---

To use a custom LDAPs certificate install it into your hubs operating system.

Note you can use the `LDAPTLS_CACERT` environment variable to use a custom
certificate for testing with `ldapsearch` before it has been installed into the
system.

```command
env LDAPTLS_CACERT=/tmp/MY-LDAP-CERT.cert.pem ldapsearch -xLLL -H ldaps://ldap.example.local:636 -b "ou=people,dc=example,dc=local"
```
