---
layout: default
title: Regenerate Self Signed SSL Certificate
published: true
tags: [cfengine enterprise, hub administration, SSL]
---

When first installed a self-signed ssl certificate is automatically generated
and used to secure Mission Portal and API communications. You can regenerate
this certificate by running `cfe_enterprise_selfsigned_cert` bundle with the
`_cfe_enterprise_selfsigned_cert_regenerate_cert` class defined. This can be
done by running the following commands as root on the hub.

```console
# cf-agent --no-lock --inform \
         --bundlesequence cfe_enterprise_selfsigned_cert \
         --define _cfe_enterprise_selfsigned_cert_regenerate_certificate
```
