---
layout: default
title: Ensure a process is not running
reviewed: 2013-06-08
reviewed-by: atsaloli
aliases:
  - "/examples-example-snippets-promise-patterns-example_process_kill.html"
---

This is a standalone policy that will kill the `sleep` process. You can adapt
it to make sure that any undesired process is not running.

```cf3
body common control
{
bundlesequence => { "process_kill" };
}

bundle agent process_kill
{
processes:

  "sleep"

    signals => { "term", "kill" }; #Signals are presented as an ordered list to the process.
                                   #On Windows, only the kill signal is supported, which terminates the process.

}
```

This policy can be found in `/var/cfengine/share/doc/examples/unit_process_kill.cf`.

Example run:

```command
/bin/sleep 1000 &
```

```output
[1] 5370
```

```command
cf-agent -f unit_process_kill.cf
```

```output
[1]+  Terminated              /bin/sleep 1000
```

Now let's do it again with inform mode turned on, and CFEngine will show the process table entry that matched the pattern we specified ("sleep"):

```command
/bin/sleep 1000 &
```

```output
[1] 5377
```

```command
cf-agent -f unit_process_kill.cf -IK
```

```output
2013-06-08T16:30:06-0700     info: This agent is bootstrapped to '192.168.183.208'
2013-06-08T16:30:06-0700     info: Running full policy integrity checks
2013-06-08T16:30:06-0700     info: /process_kill/processes/'sleep': Signalled 'term' (15) to process 5377 (root      5377  3854  5377  0.0  0.0  11352   0   612    1 16:30 00:00:00 /bin/sleep 1000)
[1]+  Terminated              /bin/sleep 1000
```

If we add the -v switch to turn on verbose mode, we see the /bin/ps command CFEngine used to dump the process table:

```command
cf-agent -f unit_process_kill.cf -Kv
```

```output
...
2013-06-08T16:38:20-0700  verbose: Observe process table with /bin/ps -eo user,pid,ppid,pgid,pcpu,pmem,vsz,ni,rss,nlwp,stime,time,args
2013-06-08T16:38:20-0700  verbose: Matched 'root      5474  3854  5474  0.0  0.0  11352   0   612    1 16:38 00:00:00 /bin/sleep 1000'
...
```
