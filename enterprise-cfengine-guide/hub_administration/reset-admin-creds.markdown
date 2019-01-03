---
layout: default
title: Reset administrative credentials
published: true
tags: [cfengine enterprise, hub administration, credentials]
---

The default `admin` user can be reset to defaults using the following SQL.

cfsettings-setadminpassword.sql:

```sql
INSERT INTO "users" ("username", "password", "salt", "name", "email", "external", "active", "roles", "changetimestamp")
       SELECT 'admin', 'SHA=aa459b45ecf9816d472c2252af0b6c104f92a6faf2844547a03338e42e426f52', 'eWAbKQmxNP', 'admin',  'admin@organisation.com', false, '1',  '{admin,cf_remoteagent}', now()
ON CONFLICT (username, external) DO UPDATE 
  SET password = 'SHA=aa459b45ecf9816d472c2252af0b6c104f92a6faf2844547a03338e42e426f52', 
      salt = 'eWAbKQmxNP';
```

To reset the CFEngine admin user run the following sql as root on your hub

```console
root@hub:~# psql cfsettings < cfsettings-setadminpassword.sql
```

