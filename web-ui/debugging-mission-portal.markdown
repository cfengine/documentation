---
layout: default
title: Debugging Mission Portal
published: true
sorting: 90
---

1.  Set the API log level to DEBUG in Mission Portal settings.

2.  Edit `/var/cfengine/share/GUI/index.php` and set `ENVIRONMENT` to `development`

    ```php
    [file=/var/cfengine/share/GUI/index.php]
    define('ENVIRONMENT', 'development');
    ```

3.  Run the hubs policy.

    ```command
    cf-agent -KI
    ```

4.  Restart `cf-apache`.

    For systemd manged systems (RedHat/Centos7, Debian 7+, Ubuntu 15.04+):

    ```command
    systemctl restart cf-apache
    ```

    For sysv init managed systems:

    ```command
    pkill httpd && cf-agent -KI
    ```

    or

    ```command
    LD_LIBRARY_PATH=/var/cfengine/lib:$LD_LIBRARY_PATH /var/cfengine/httpd/bin/apachectl restart
    ```

5. Watch the logs:
* `/var/cfengine/httpd/logs/error_log`
* `/var/cfengine/httpd/htdocs/application/logs/log-$(date +%Y-%m-%d).php`
