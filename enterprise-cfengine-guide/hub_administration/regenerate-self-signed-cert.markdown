---
layout: default
title: Regenerate Self Signed SSL Certificate
published: true
tags: [cfengine enterprise, hub administration, SSL]
---

When first installed a self-signed ssl certificate is automatically generated
and used to secure Mission Portal and API communications. You can regenerate
this certificate by running the following commands.

```console
CFENGINE_MP_DEFAULT_CERT_LOCATION="/var/cfengine/httpd/ssl/certs"
CFENGINE_MP_DEFAULT_CERT_LINK_LOCATION="/var/cfengine/ssl"
CFENGINE_MP_DEFAULT_KEY_LOCATION="/var/cfengine/httpd/ssl/private"
CFENGINE_OPENSSL="/var/cfengine/bin/openssl"
CFENGINE_LOCALHOST=$(hostname -f)
CFENGINE_MP_CERT=$CFENGINE_MP_DEFAULT_CERT_LOCATION/$CFENGINE_LOCALHOST.cert
CFENGINE_MP_CERT_LINK=$CFENGINE_MP_DEFAULT_CERT_LINK_LOCATION/cert.pem
CFENGINE_MP_KEY=$CFENGINE_MP_DEFAULT_KEY_LOCATION/$CFENGINE_LOCALHOST.key
$CFENGINE_OPENSSL req -new -newkey rsa:2048 \
                  -days 3650 -nodes -x509 \
                  -utf8 -sha256 -subj "/CN=$CFENGINE_LOCALHOST" \
                  -keyout $CFENGINE_MP_KEY  \
                  -out $CFENGINE_MP_CERT \
                  -config /var/cfengine/ssl/openssl.cnf
```
