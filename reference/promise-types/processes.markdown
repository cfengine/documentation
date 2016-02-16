---
layout: default
title: processes
published: true
tags: [reference, bundle agent, promise types, processes, processes promises, promise types]
---

Process promises refer to items in the system process table, i.e., a command in
some state of execution (with a Process Control Block). Promiser objects are
patterns that are [unanchored][unanchored], meaning that they match line
fragments in the system process table.

```cf3
      processes:

        "regex contained in process line"

            process_select = process_filter_body,
            restart_class = "activation class for process",
            ..;
```

**Note**: Process table formats differ between platforms. You can see
how cfengine views the process table for your platform by inspecting
`cf_otherprocs`, `cf_procs`, and `cf_rootprocs` which can be found in
`$(sys.workdir)/state/` (typically `/var/cfengine/state`).

For example, this is a sample of `$(sys.workdir)/state/cf_rootprocs` on a linux system:

```
USER       PID  PPID  PGID %CPU %MEM    VSZ  NI       RSS NLWP STIME     ELAPSED     TIME COMMAND
root         1     0     1  0.0  0.2  19232   0      1096    1 Sep14  1-21:41:52 00:00:00 /sbin/init
root         2     0     0  0.0  0.0      0   0         0    1 Sep14  1-21:41:52 00:00:00 [kthreadd]
root         3     2     0  0.0  0.0      0   -         0    1 Sep14  1-21:41:52 00:00:00 [migration/0]
```

This is an example showing how to restart splunk when a splunkd process owned
by root is using 80% or more of the CPU.

```cf3
bundle agent example
{
  processes:
      # Reference process table in $(sys.workdir)/state/cf_procs
      # Find lines in the process table starting with root (USER column)
      # followed by one or more spaces, followed by a digit (PID column),
      # followed by one or more spaces, followed by a digit (PGID column),
      # followed by one or more spaces, followed by 8 or 9 followed by a number
      # in the range 0-9 (to match numbers greater than 80), followed by a dot,
      # followed by anything, and containing splunkd (expected to match the
      # COMMAND column).

      "^root\s+\d+\s+\d+\s+\d+\s+[89][0-9]\..*splunkd"
        handle => "example_splunk_high_cpu_stop_gracefully",
        process_stop => "/opt/splunkforwarder/bin/splunk stop",
        comment => "Find splunkd processes owned by root that are consuming more
		    than 80% of a CPU and restart it with it's preferred
                    utility. Stop it gracefully with the internal splunk binary.";

      "^root\s.*splunkd"
        restart_class => "splunk_not_running",
        comment => "Set splunk_not_running class if we cant find any root owned
		    splunkd processes so that we can restart it using a
                    commands promise";

  commands:
    splunk_not_running::
      "/opt/splunkforwarder/bin/splunk"
        args => "--accept-license --answer-yes --no-prompt start";
}
```

Getting complex regular expressions just right can be difficult, so for most
sophisticated matches, users should use a simple pattern match such as program
names combinded with a *`process_select`* body before delving into complex regular
expressions.

This example shows using `process_select` and `process_count` to define a class when a process has been running for longer than a day.

[%CFEngine_include_example(processes_define_class_based_on_process_runtime.cf)%]

Take care to not oversimplify your patterns as it may match
unexpected processes. For example, on many systems, the process pattern `"^cp"`
may not match any processes, even though `"cp"` is running. This is because the
process table entry may list `"/bin/cp"`. However, the process pattern `"cp"`
will also match a process containing `"scp"`, (the PCRE pattern anchors `"\b"`
and `"\B"` may prove very useful to you).

To restart a process, you should set a class to activate and then describe a
`command` in that class.

```cf3
    commands:

      restart_me::

       "/path/executable" ... ;
```

This rationalizes complex restart-commands and avoids unnecessary overlap
between `processes` and `commands`.

The `process_stop` is also arguably a command, but it should be an
ephemeral command that does not lead to a persistent process. It is
intended only for commands of the form /etc/inetd service stop, not for
processes that persist. Processes are restarted at the end of a bundle's
execution, but stop commands are executed immediately.

### Commands and Processes

CFEngine distinguishes between `processes` and [`commands`][commands] so that
there is a clean separation between detection (promises about the process
table) and certain repairs (promises to execute commands that start
processes).

Command executions are about jobs, services, scripts etc. They are properties
of an executable file, and the referring 'promiser' is a file object. On the
other hand a process is a property of a "process identifier" which is a kernel
instantiation, a quite different object altogether. For example:

-   A "PID" (which is not an executable) promises to be reminded of a
    signal, e.g.

```cf3
    kill signal pid
```

-   An "command" promises to start or stop itself with a parameterized
    specification.

```cf3
    exec command argument1 argument2 ...
```

Neither the file nor the pid necessarily promise to respond to these
activations, but they are nonetheless physically meaningful phenomena or
attributes associated with these objects.

-   Executable files do not listen for signals as they have no active
    state.
-   PIDs do not run themselves or stop themselves with new arguments,
    but they can use signals as they are running.

Executions lead to processes for the duration of their lifetime, so
these two issues are related, although the promises themselves are not.

### Platform notes

Process promises depend on the `ps` native tool, which by default truncates
lines at 128 columns on HP-UX. It is recommended to edit the file
`/etc/default/ps` and increase the `DEFAULT_CMD_LINE_WIDTH` setting to 1024 to
guarantee that process promises will work smoothly on that platform.

****

## Attributes ##

[%CFEngine_include_markdown(common-attributes-include.markdown)%]

### process_count

**Type:** `body process_count`

[%CFEngine_include_markdown(common-body-attributes-include.markdown)%]

#### in_range_define

**Description:** List of classes to define if the matches are in range

Classes are defined if the processes that are found in the process table
satisfy the promised process count, in other words if the promise about
the number of processes matching the other criteria is kept.

**Type:** `slist`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
     body process_count example
     {
     in_range_define => { "class1", "class2" };
     }
```

#### match_range

**Description:** Integer range for acceptable number of matches for this
process

This is a numerical range for the number of occurrences of the process
in the process table. As long as it falls within the specified limits,
the promise is considered kept.

**Type:** `irange[int,int]`

**Allowed input range:** `0,99999999999`

**Example:**

```cf3
     body process_count example
     {
     match_range => irange("10","50");
     }
```

#### out_of_range_define

**Description:** List of classes to define if the matches are out of range

Classes to activate remedial promises conditional on this promise
failure to be kept.

**Type:** `slist`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
     body process_count example(s)
     {
     out_of_range_define => { "process_anomaly", "anomaly_$(s)"};
     }
```

### process_select

**Type:** `body process_select`

[%CFEngine_include_markdown(common-body-attributes-include.markdown)%]

#### command

**Description:** Regular expression matching the command/cmd field of a
process

This expression should match the entire `COMMAND` field of the process
table, not just a fragment. This field is usually the last field on the
line, so it thus starts with the first non-space character and ends with
the end of line.

**Type:** `string`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
     body process_select example

     {
     command => "cf-.*";

     process_result => "command";
     }
```

#### pid

**Description:** Range of integers matching the process id of a process

**Type:** `irange[int,int]`

**Allowed input range:** `0,99999999999`

**Example:**

```cf3
     body process_select example
     {
     pid => irange("1","10");
     process_result => "pid";
     }
```

#### pgid

**Description:** Range of integers matching the parent group id of a
process

**Type:** `irange[int,int]`

**Allowed input range:** `0,99999999999`

**Example:**

```cf3
     body process_select example
     {
     pgid => irange("1","10");
     process_result => "pgid";
     }
```

#### ppid

**Description:** Range of integers matching the parent process id of a
process

**Type:** `irange[int,int]`

**Allowed input range:** `0,99999999999`

**Example:**

```cf3
     body process_select example
     {
     ppid => irange("407","511");
     process_result => "ppid";
     }
```

#### priority

**Description:** Range of integers matching the priority field (PRI/NI) of
a process

**Type:** `irange[int,int]`

**Allowed input range:** `-20,+20`

**Example:**

```cf3
     body process_select example
     {
     priority => irange("-5","0");
     }
```

#### process_owner

**Description:** List of regexes matching the user of a process

The regular expressions should match a legal user name on the system. The
regex is [anchored][anchored], meaning it must match the entire name.

**Type:** `slist`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
     body process_select example
     {
     process_owner => { "wwwrun", "nobody" };
     }
```

#### process_result

**Description:** Boolean class expression with the logical combination
of process selection criteria

A logical combination of the process selection classifiers. The syntax
is the same as that for class expressions. If `process_result` is not
specified, then all set attributes in the `process_select` body are AND'ed
together.

**Type:** `string`

**Allowed input range:**
`[(process_owner|pid|ppid||pgid|rsize|vsize|status|command|ttime|stime|tty|priority|threads)[|!.]*]*`

**Example:**

```cf3
     body process_select proc_finder(p)

     {
     process_owner  => { "avahi", "bin" };
     command        => "$(p)";
     pid            => irange("100","199");
     vsize          => irange("0","1000");
     process_result => "command.(process_owner|vsize).!pid";
     }
```

**See also:** `file_result`

#### rsize

**Description:** Range of integers matching the resident memory size of a
process, in kilobytes

**Type:** `irange[int,int]`

**Allowed input range:** `0,99999999999`

**Example:**

```cf3
     body process_select
     {
     rsize => irange("4000","8000");
     }

```

#### status

**Description:** Regular expression matching the status field of a process

For instance, characters in the set `NRSsl+..`. Windows processes do not
have status fields.

**Type:** `string`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
     body process_select example
     {
     status => "Z";
     }
```

#### stime_range

**Description:** Range of integers matching the start time of a process

The calculation of time from process table entries is sensitive to
Daylight Savings Time (Summer/Winter Time) so calculations could be an
hour off. This is for now a bug to be fixed.

**Type:** `irange[int,int]`

**Allowed input range:** `0,2147483647`

**Example:**

```cf3
     body process_select example
     {
     stime_range => irange(ago(0,0,0,1,0,0),now);
     }
```

#### ttime_range

**Description:** Range of integers matching the total elapsed time of a
process.

This is total accumulated time for a process.

**Type:** `irange[int,int]`

**Allowed input range:** `0,2147483647`

**Example:**

```cf3
     body process_select example
     {
     ttime_range => irange(0,accumulated(0,1,0,0,0,0));
     }
```

#### tty

**Description:** Regular expression matching the tty field of a process

Windows processes are not regarded as attached to any terminal, so they
all have tty '?'.

**Type:** `string`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
     body process_select example
     {
     tty => "pts/[0-9]+";
     }
```

#### threads

**Description:** Range of integers matching the threads (NLWP) field of a
process

**Type:** `irange[int,int]`

**Allowed input range:** `0,99999999999`

**Example:**

```cf3
     body process_select example
     {
     threads => irange(1,5);
     }
```

#### vsize

**Description:** Range of integers matching the virtual memory size of a
process, in kilobytes.

On Windows, the virtual memory size is the amount of memory that cannot
be shared with other processes. In Task Manager, this is called Commit
Size (Windows 2008), or VM Size (Windows XP).

**Type:** `irange[int,int]`

**Allowed input range:** `0,99999999999`

**Example:**

```cf3
     body process_select example
     {
     vsize => irange("4000","9000");
     }
```

### process_stop

**Description:** A command used to stop a running process

As an alternative to sending a termination or kill signal to a process,
one may call a 'stop script' to perform a graceful shutdown.

**Type:** `string`

**Allowed input range:** `"?(/.*)`

**Example:**

```cf3
    processes:

     "snmpd"

            process_stop => "/etc/init.d/snmp stop";
```


### restart_class

**Description:** A class to be defined globally if the process is not
running, so that a `command:` rule can be referred to restart the process

This is a signal to restart a process that should be running, if it is
not running. Processes are signaled first and then restarted later, at
the end of bundle execution, after all possible corrective actions have
been made that could influence their execution.

Windows does not support having processes start themselves in the
background, like Unix daemons usually do; as fork off a child process.
Therefore, it may be useful to specify an `action` body that sets
`background` to true in a commands promise that is invoked by the class
set by `restart_class`. See the `commands` promise type for more
information.

**Type:** `string`

**Allowed input range:** `[a-zA-Z0-9_$(){}\[\].:]+`

**Example:**

```cf3
processes:

   "cf-serverd"

     restart_class => "start_cfserverd";

commands:

  start_cfserverd::

    "/var/cfengine/bin/cf-serverd";
```

### signals

**Description:** A list of menu options representing signals to be sent to
a process.

Signals are presented as an ordered list to the process. On Windows,
only the kill signal is supported, which terminates the process.

**Type:** (option list)

**Allowed input range:**

```cf3
       hup
       int
       trap
       kill
       pipe
       cont
       abrt
       stop
       quit
       term
       child
       usr1
       usr2
       bus
       segv
```

**Example:**

```cf3
    processes:

     cfservd_out_of_control::

       "cfservd"

            signals         => { "stop" , "term" },
            restart_class   => "start_cfserv";

     any::

       "snmpd"

            signals         => { "term" , "kill" };
```

