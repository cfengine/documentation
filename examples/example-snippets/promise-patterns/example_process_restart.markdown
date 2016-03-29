---
layout: default
title: Restart a Process
published: true
tags: [Examples, Policy, process, restart]
reviewed: 2013-06-08
reviewed-by: atsaloli
---

This is a standalone policy that will restart three CFEngine processes if they are not running.

```cf3
body common control
{
bundlesequence => { "process_restart" };
}


bundle agent process_restart
{
vars:

  "component" slist => {                  # List of processes to monitor
                         "cf-monitord",
                         "cf-serverd",
                         "cf-execd"
                       };
processes:

  "$(component)"
      restart_class => canonify("start_$(component)"); # Set the class "start_<component>" if it is not running

commands:

   "/var/cfengine/bin/$(component)"
       ifvarclass => canonify("start_$(component)"); # Evaluate the class "start_<component>", CFEngine will run
                                                   # the command if "start_<component> is set.

}
```

Notes: The `canonify` function translates illegal characters to underscores, e.g. `start_cf-monitord` becomes `start_cf_monitord`.  Only alphanumerics and underscores are allowed in CFEngine identifiers (names of variables, classes, bundles, etc.)

This policy can be found in `/var/cfengine/share/doc/examples/unit_process_restart.cf`.

Example run:

```
# ps -ef |grep cf-
root      4305     1  0 15:14 ?        00:00:02 /var/cfengine/bin/cf-execd
root      4311     1  0 15:14 ?        00:00:05 /var/cfengine/bin/cf-serverd
root      4397     1  0 15:15 ?        00:00:06 /var/cfengine/bin/cf-monitord
# kill 4311
# ps -ef |grep cf-
root      4305     1  0 15:14 ?        00:00:02 /var/cfengine/bin/cf-execd
root      4397     1  0 15:15 ?        00:00:06 /var/cfengine/bin/cf-monitord
# cf-agent -f unit_process_restart.cf
# ps -ef |grep cf-
root      4305     1  0 15:14 ?        00:00:02 /var/cfengine/bin/cf-execd
root      4397     1  0 15:15 ?        00:00:06 /var/cfengine/bin/cf-monitord
root      8008     1  0 18:18 ?        00:00:00 /var/cfengine/bin/cf-serverd
#
```

And again, in Inform mode:

```
# kill 8008
# cf-agent -f unit_process_restart.cf -I
2013-06-08T18:19:51-0700     info: This agent is bootstrapped to '192.168.183.208'
2013-06-08T18:19:51-0700     info: Running full policy integrity checks
2013-06-08T18:19:51-0700     info: /process_restart/processes/'$(component)': Making a one-time restart promise for 'cf-serverd'
2013-06-08T18:19:51-0700     info: Executing 'no timeout' ... '/var/cfengine/bin/cf-serverd'
2013-06-08T18:19:52-0700     info: Completed execution of '/var/cfengine/bin/cf-serverd'
#
```
