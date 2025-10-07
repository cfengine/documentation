---
layout: default
title: Ensure a service is enabled and running
reviewed: 2016-06-28
reviewed-by: nickanderson
aliases:
  - "/examples-example-snippets-promise-patterns-example_enable_service.html"
---

This example shows how to ensure services are started or stopped appropriately.

{{< CFEngine_include_example(services.cf) >}}

**Note:** Not all services behave in the standard way. Some services may require
custom handling. For example it is not uncommon for some services to not provide
correct return codes for status checks.

**See also:**

- [Services promise type reference][services]
- [Services bundles and bodies in the standard library][lib/services.cf]

## Example usage on systemd

We can see that before the policy run `sysstat` is _inactive_, `apache2` is
_active_, `cups` is _active_, `ssh` is _active_ and `cron` is _inactive_.

```command
systemctl is-active sysstat apache2 cups ssh cron
```

```output
inactive
active
active
active
inactive
```

Now we run the policy to converge the system to the desired state.

```command
cf-agent --no-lock --inform --file ./services.cf
```

```output
info: Executing 'no timeout' ... '/bin/systemctl --no-ask-password --global --system -q stop apache2'
info: Completed execution of '/bin/systemctl --no-ask-password --global --system -q stop apache2'
info: Executing 'no timeout' ... '/bin/systemctl --no-ask-password --global --system -q stop cups'
info: Completed execution of '/bin/systemctl --no-ask-password --global --system -q stop cups'
info: Executing 'no timeout' ... '/bin/systemctl --no-ask-password --global --system -q start cron'
info: Completed execution of '/bin/systemctl --no-ask-password --global --system -q start cron'
```

After the policy run we can see that `systat`, `apache2`, and `cups` are
_inactive_. `ssh` and `cron` are _active_ as specified in the policy.

```command
systemctl is-active sysstat apache2 cups ssh cron
```

```output
inactive
inactive
inactive
active
active
```

## Example usage with System V

We can see that before the policy run `sysstat` is not reporting status
correctly , `httpd` is _running_, `cups` is _running_, `sshd` is _running_ and
`crond` is _not running_.

```command
service sysstat status; echo $?
```

```output
3
```

```command
service httpd status; echo $?
```

```output
httpd (pid  3740) is running...
0
```

```command
service cups status; echo $?
```

```output
cupsd (pid  3762) is running...
0
```

```command
service sshd status; echo $?
```

```output
openssh-daemon (pid  3794) is running...
0
```

```command
service crond status; echo $?
```

```output
crond is stopped
3
```

Now we run the policy to converge the system to the desired state.

```command
cf-agent -KIf ./services.cf
```

```output
info: Executing 'no timeout' ... '/etc/init.d/crond start'
info: Completed execution of '/etc/init.d/crond start'
info: Executing 'no timeout' ... '/etc/init.d/httpd stop'
info: Completed execution of '/etc/init.d/httpd stop'
info: Executing 'no timeout' ... '/etc/init.d/cups stop'
info: Completed execution of '/etc/init.d/cups stop'
```

After the policy run we can see that `systat` is still not reporting status correctly (some services do not respond to standard checks), `apache2`, and `cups` are
_inactive_. `ssh` and `cron` are _active_ as specified in the policy.

```command
service sysstat status; echo $?
```

```output
3
```

```command
service httpd status; echo $?
```

```output
httpd is stopped
3
```

```command
service cups status; echo $?
```

```output
cups is stopped
3
```

```command
service sshd status; echo $?
```

```output
openssh-daemon (pid  3794) is running...
0
```

```command
service crond status; echo $?
```

```output
crond (pid  3929) is running...
0
```
