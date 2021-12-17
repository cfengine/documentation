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

## Internal credentials

Two internal credentials are present in an Enterprise Hub: Mission Portal API credentials and CFE Robot credentials.

If these credentials are not synchronized between configuration files and database, errors can occur in the Mission Portal UI as well as in hub policy.

Rotating these credentials is optional and can be performed at an interval based on your specific security policy.

### Mission Portal API credentials

These credentials enable Mission Portal to authenticate to the backend API.

If these credentials are not synchronized properly you can get "Authentication failed" messages in the Mission Portal UI.

To rotate these credentials execute the following shell script on the hub and then restart the system with `systemctl restart cfengine3` or similar.

```bash
#!/usr/bin/env bash
# rotate_mp_credentials.sh
pwgen() {
  dd if=/dev/urandom bs=1024 count=1 2>/dev/null | tr -dc 'a-zA-Z0-9' | fold -w $1 | head -n 1
}
PREFIX=/var/cfengine # adjust if needed, this is the default
MP_PW=`pwgen 40`
SECRETS_FILE="$PREFIX/httpd/secrets.ini" # 3.16 version and newer
if [ -f "$SECRETS_FILE" ]; then
  sed -i "/mp_client_secret/s/=.*/=$MP_PW/" $SECRETS_FILE
else
  APPSETTINGS_FILE="$PREFIX/httpd/htdocs/application/config/appsettings.php"
  sed -i "/MP_CLIENT_SECRET/c\$config['MP_CLIENT_SECRET'] = '$MP_PW';" $APPSETTINGS_FILE
fi
echo "UPDATE oauth_clients SET client_secret = '$MP_PW' where client_id = 'MP'" | $PREFIX/bin/psql cfsettings
```

### CFE Robot credentials

These credentials are used by PHP CLI scripts to authenticate to the backend API.

If these credentials are out of sync or incorrect you will see errors like "500 Internal Server Error" in `/var/cfengine/httpd/logs/application/` logs.


Execute the following shell script to rotate and synchronize the CFE Robot credentials and then restart the system with `systemctl restart cfengine3` or similar.

```bash
#!/usr/bin/env bash
# rotate_cfrobot_credentials.sh
pwgen() {
  dd if=/dev/urandom bs=1024 count=1 2>/dev/null | tr -dc 'a-zA-Z0-9' | fold -w $1 | head -n 1
}
PREFIX=/var/cfengine # adjust if needed, this is the default
pwhash() {
  echo -n "$1" | "$PREFIX/bin/openssl" dgst -sha256 | awk '{print $2}'
}
CFE_ROBOT_PW=`pwgen 40`
SECRETS_FILE="$PREFIX/httpd/secrets.ini" # 3.16 version and newer
if [ -f "$SECRETS_FILE" ]; then
  sed -i "/cf_robot_password/s/=.*/=$CFE_ROBOT_PW/" $SECRETS_FILE
else
  CFROBOT_FILE="$PREFIX/httpd/htdocs/application/config/cf_robot.php"
  sed -i "/CFE_ROBOT_PASSWORD/c\$config['CFE_ROBOT_PASSWORD'] = \"$CFE_ROBOT_PW\";" $CFROBOT_FILE
fi
CFE_ROBOT_PW_SALT=`pwgen 10` 
CFE_ROBOT_PW_HASH=`pwhash "$CFE_ROBOT_PW_SALT$CFE_ROBOT_PW"`
echo "UPDATE users SET password = 'SHA=$CFE_ROBOT_PW_HASH', salt = '$CFE_ROBOT_PW_SALT' WHERE username = 'CFE_ROBOT'" | "$PREFIX/bin/psql" cfsettings
```
