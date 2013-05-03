---
layout: default
title: processes-in-agent-promises
categories: [Bundles-for-agent,processes-in-agent-promises]
published: true
alias: Bundles-for-agent-processes-in-agent-promises.html
tags: [Bundles-for-agent,processes-in-agent-promises]
---

### `processes` promises in agent

\

Process promises refer to items in the system process table. Note that
this is not the same as commands (which are instructions that CFEngine
will execute). A process is a command in some state of execution (with a
Process Control Block). Promiser objects here are patterns that are
unanchored, meaning that they match line fragments in the system process
table (see [Anchored vs. unanchored regular
expressions](#Anchored-vs_002e-unanchored-regular-expressions)).

*Take care to note that process table formats differ between operating
systems, and the use of simple patterns such as program-names is
recommended. For more sophisticated matches, users should use
the*`process_select`*feature.* For example, on many systems, the process
pattern `"^cp"` may not match any processes, even though `"cp"` is
running. This is because the process table entry may list `"/bin/cp"`.
However, the process pattern `"cp"` will also match a process containing
`"scp"`, so take care not to oversimplify your patterns (the PCRE
pattern anchors `"\b"` and `"\B"` may prove very useful to you).

~~~~ {.smallexample}
     
      processes:
     
        "regex contained in process line"
     
            process_select = process_filter_body,
            restart_class = "activation class for process",
            ..;
     
~~~~

In CFEngine 2 there was a restart clause for directly executing a
command to restart a process. In CFEngine 3 there is instead a class to
activate. You must then describe a `command` in that class to restart
the process.

~~~~ {.verbatim}
commands:

  restart_me::

   "/path/executable" ... ;
~~~~

This rationalizes complex restart-commands and avoids unnecessary
overlap between `processes` and `commands`.

The `process_stop` is also arguably a command, but it should be an
ephemeral command that does not lead to a persistent process. It is
intended only for commands of the form /etc/inetd service stop, not for
processes that persist. Processes are restarted at the end of a bundle's
execution, but stop commands are executed immediately.

Note: `process_select` was previously called process `filters` in
CFEngine 2 and earlier.

\

~~~~ {.verbatim}
bundle agent example
{
processes:

 ".*"

    process_count   => anyprocs,
    process_select  => proc_finder;

reports:

 any_procs::

   "Found processes out of range";
}

########################################################

body process_select proc_finder

{
# Processes started between 5.5 hours and 20 minutes ago
stime_range => irange(ago(0,0,0,5,30,0),ago(0,0,0,0,20,0));
process_result => "stime";
}

########################################################

body process_count anyprocs

{
match_range => "0,0";
out_of_range_define => { "any_procs" };
}
~~~~

\

In CFEngine 3 we have

~~~~ {.smallexample}
      processes
      commands
~~~~

so that there is a clean separation between detection (promises about
the process table) and certain repairs (promises to execute commands
that start processes).

Executions are about jobs, services, scripts etc. They are properties of
an executable file. The referring \`promiser' is a file object. On the
other hand a process is a property of a "process identifier" which is a
kernel instantiation, a quite different object altogether. For example:

-   A "PID" (which is not an executable) promises to be reminded of a
    signal, e.g.

    ~~~~ {.smallexample}
                  kill signal pid
    ~~~~

-   An "command" promises to start or stop itself with a parameterized
    specification.

    ~~~~ {.smallexample}
                  exec command argument1 argument2 ...
    ~~~~

Neither the file nor the pid necessarily promise to respond to these
activations, but they are nonetheless physically meaningful phenomena or
attributes associated with these objects.

-   Executable files do not listen for signals as they have no active
    state.
-   PIDs do not run themselves or stop themselves with new arguments,
    but they can use signals as they are running.

Executions lead to processes for the duration of their lifetime, so
these two issues are related, although the promises themselves are not.

\
 **Services versus processes**: \

A service is an abstraction that requires processes to run and files to
be configured. It makes a lot of sense to wrap services in modular
bundles. Starting and stopping a service can be handled in at least two
ways. Take the web service as an example.

We can start the service by promising an execution of a daemon (e.g.
`httpd`). Normally this execution does not terminate without
intervention. We can terminate it in one of two ways:

-   Using a process signal, by promising a signal to processes matching
    a certain pid search
-   Using an execution of a termination command, e.g. /etc/init.d/apache
    stop.

The first case makes sense if we need to qualify the termination by
searching for the processes. The processes section of a CFEngine 3
policy includes a control promise to search for matching processes. If
matches are found, signals can be sent to precisely each specific
process.

Classes can also be defined, in principle triggering an execution of the
stop script, but then the class refers only to the presence of matching
pids, not to the individual pids concerned. So it becomes the
responsibility of the execution to locate and interact with the pids
necessary.

\

If you want to ensure that a service is running, check each in the agent
control promises individually.

~~~~ {.verbatim}
bundlesequence => { Update, Service("apache"), Service("nfsd") };
~~~~

or

~~~~ {.verbatim}
bundlesequence => { Update, @(globals.all_services)  };
~~~~

The bundle for this can look like this:

~~~~ {.verbatim}
bundle agent Service(service")
{
processes:

  "$(service)" 

      process_count => up("$(service)");

commands:

   "$daemons[$(service)]"  

      ifvarclass => "$(service)_up",
      args       => "$args[$(service)]";

}
~~~~

An alternative would be self-contained:

~~~~ {.verbatim}
bundle agent Service
{
vars:

  "service" slist => { "apache", "nfsd", "bind" };

processes:

  "$(service)" 

      process_count => up("$(service)");

commands:

   "$daemons[$(service)]"  

      ifvarclass => "$(service)_up",
      args       => "$args[$(service)]";

}

######################
# Parameterized body
######################

body process_count up("$(s)")

{
match_range => "[0,10]";
out_of_range_define => "$(s)_up";
}
~~~~

-   [process\_count in processes](#process_005fcount-in-processes)
-   [process\_select in processes](#process_005fselect-in-processes)
-   [process\_stop in processes](#process_005fstop-in-processes)
-   [restart\_class in processes](#restart_005fclass-in-processes)
-   [signals in processes](#signals-in-processes)

#### `process_count` (body template)

**Type**: (ext body)

`in_range_define`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: List of classes to define if the matches are in range

**Example**:\
 \

~~~~ {.verbatim}
     
     body process_count example
     {
     in_range_define => { "class1", "class2" };
     }
     
~~~~

**Notes**:\
 \

Classes are defined if the processes that are found in the process table
satisfy the promised process count, in other words if the promise about
the number of processes matching the other criteria is kept. \

`match_range`

**Type**: irange [int,int]

**Allowed input range**: `0,99999999999`

**Synopsis**: Integer range for acceptable number of matches for this
process

**Example**:\
 \

~~~~ {.verbatim}
     
     body process_count example
     {
     match_range => irange("10","50");
     }
     
~~~~

**Notes**:\
 \

This is a numerical range for the number of occurrences of the process
in the process table. As long as it falls within the specified limits,
the promise is considered kept. \

`out_of_range_define`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: List of classes to define if the matches are out of range

**Example**:\
 \

~~~~ {.verbatim}
     
     body process_count example(s)
     {
     out_of_range_define => { "process_anomaly", "anomaly_$(s)"};
     }
     
~~~~

**Notes**:\
 \

Classes to activate remedial promises conditional on this promise
failure to be kept.

#### `process_select` (body template)

**Type**: (ext body)

`command`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: Regular expression matching the command/cmd field of a
process

**Example**:\
 \

~~~~ {.verbatim}
     
     body process_select example
     
     {
     command => "cf-.*";
     
     process_result => "command";
     }
     
~~~~

**Notes**:\
 \

This expression should match the entire `COMMAND` field of the process
table, not just a fragment. This field is usually the last field on the
line, so it thus starts with the first non-space character and ends with
the end of line. \

`pid`

**Type**: irange [int,int]

**Allowed input range**: `0,99999999999`

**Synopsis**: Range of integers matching the process id of a process

**Example**:\
 \

~~~~ {.verbatim}
     
     body process_select example
     {
     pid => irange("1","10");
     process_result => "pid";
     }
     
~~~~

**Notes**:\
 \
 \

`pgid`

**Type**: irange [int,int]

**Allowed input range**: `0,99999999999`

**Synopsis**: Range of integers matching the parent group id of a
process

**Example**:\
 \

~~~~ {.verbatim}
     
     body process_select example
     {
     pgid => irange("1","10");
     process_result => "pgid";
     }
     
~~~~

**Notes**:\
 \
 \

`ppid`

**Type**: irange [int,int]

**Allowed input range**: `0,99999999999`

**Synopsis**: Range of integers matching the parent process id of a
process

**Example**:\
 \

~~~~ {.verbatim}
     
     body process_select example
     {
     ppid => irange("407","511");
     process_result => "ppid";
     }
     
~~~~

**Notes**:\
 \
 \

`priority`

**Type**: irange [int,int]

**Allowed input range**: `-20,+20`

**Synopsis**: Range of integers matching the priority field (PRI/NI) of
a process

**Example**:\
 \

~~~~ {.verbatim}
     
     body process_select example
     {
     priority => irange("-5","0");
     }
     
~~~~

**Notes**:\
 \
 \

`process_owner`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: List of regexes matching the user of a process

**Example**:\
 \

~~~~ {.verbatim}
     
     body process_select example
     {
     process_owner => { "wwwrun", "nobody" };
     }
     
~~~~

**Notes**:\
 \

Regular expression should match a legal user name on the system. The
regex is anchored, meaning it must match the entire name (see [Anchored
vs. unanchored regular
expressions](#Anchored-vs_002e-unanchored-regular-expressions)). \

`process_result`

**Type**: string

**Allowed input range**:
`[(process_owner|pid|ppid||pgid|rsize|vsize|status|command|ttime|stime|tty|priority|threads)[|!.]*]*`

**Synopsis**: Boolean class expression returning the logical combination
of classes set by a process selection test

**Example**:\
 \

~~~~ {.verbatim}
     
     body process_select proc_finder(p)
     
     {
     process_owner  => { "avahi", "bin" };
     command        => "$(p)";
     pid            => irange("100","199");
     vsize          => irange("0","1000");
     process_result => "command.(process_owner|vsize).!pid";
     }
     
~~~~

**Notes**:\
 \

A logical combination of the process selection classifiers. The syntax
is the same as that for class expressions. There should be no spaces in
the expressions. \

`rsize`

**Type**: irange [int,int]

**Allowed input range**: `0,99999999999`

**Synopsis**: Range of integers matching the resident memory size of a
process, in kilobytes

**Example**:\
 \

~~~~ {.verbatim}
     
     body process_select
     {
     rsize => irange("4000","8000");
     }
     
     
~~~~

**Notes**:\
 \
 \

`status`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: Regular expression matching the status field of a process

**Example**:\
 \

~~~~ {.verbatim}
     
     body process_select example
     {
     status => "Z";
     }
     
~~~~

**Notes**:\
 \

For instance, characters in the set NRSsl+... Windows processes do not
have status fields. \

`stime_range`

**Type**: irange [int,int]

**Allowed input range**: `0,2147483647`

**Synopsis**: Range of integers matching the start time of a process

**Example**:\
 \

~~~~ {.verbatim}
     
     body process_select example
     {
     stime_range => irange(ago(0,0,0,1,0,0),now);
     }
     
~~~~

**Notes**:\
 \

The calculation of time from process table entries is sensitive to
Daylight Savings Time (Summer/Winter Time) so calculations could be an
hour off. This is for now a bug to be fixed. \

`ttime_range`

**Type**: irange [int,int]

**Allowed input range**: `0,2147483647`

**Synopsis**: Range of integers matching the total elapsed time of a
process

**Example**:\
 \

~~~~ {.verbatim}
     
     body process_select example
     {
     ttime_range => irange(0,accumulated(0,1,0,0,0,0));
     }
     
~~~~

**Notes**:\
 \

This is total accumulated time for a process. \

`tty`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: Regular expression matching the tty field of a process

**Example**:\
 \

~~~~ {.verbatim}
     
     body process_select example
     {
     tty => "pts/[0-9]+";
     }
     
~~~~

**Notes**:\
 \

Windows processes are not regarded as attached to any terminal, so they
all have tty '?'. \

`threads`

**Type**: irange [int,int]

**Allowed input range**: `0,99999999999`

**Synopsis**: Range of integers matching the threads (NLWP) field of a
process

**Example**:\
 \

~~~~ {.verbatim}
     
     body process_select example
     {
     threads => irange(1,5);
     }
     
~~~~

**Notes**:\
 \
 \

`vsize`

**Type**: irange [int,int]

**Allowed input range**: `0,99999999999`

**Synopsis**: Range of integers matching the virtual memory size of a
process, in kilobytes

**Example**:\
 \

~~~~ {.verbatim}
     
     body process_select example
     {
     vsize => irange("4000","9000");
     }
     
~~~~

**Notes**:\
 \

On Windows, the virtual memory size is the amount of memory that cannot
be shared with other processes. In Task Manager, this is called Commit
Size (Windows 2008), or VM Size (Windows XP).

#### `process_stop`

**Type**: string

**Allowed input range**: `"?(/.*)`

**Synopsis**: A command used to stop a running process

**Example**:\
 \

~~~~ {.verbatim}
processes:

 "snmpd"

        process_stop => "/etc/init.d/snmp stop";

~~~~

**Notes**:\
 \

As an alternative to sending a termination or kill signal to a process,
one may call a \`stop script' to perform a graceful shutdown.

#### `restart_class`

**Type**: string

**Allowed input range**: `[a-zA-Z0-9_$(){}\[\].:]+`

**Synopsis**: A class to be defined globally if the process is not
running, so that a command: rule can be referred to restart the process

**Example**:\
 \

~~~~ {.verbatim}
processes:

   "cf-serverd"

     restart_class => "start_cfserverd";

commands:

  start_cfserverd::

    "/var/cfengine/bin/cf-serverd";
~~~~

**Notes**:\
 \

This is a signal to restart a process that should be running, if it is
not running. Processes are signaled first and then restarted later, at
the end of bundle execution, after all possible corrective actions have
been made that could influence their execution.

Windows does not support having processes start themselves in the
background, like Unix daemons usually do; as fork off a child process.
Therefore, it may be useful to specify an action bodypart that sets
background to true in a commands promise that is invoked by the class
set by restart\_class. See the commands promise type for more
information.

#### `signals`

**Type**: (option list)

**Allowed input range**: \

~~~~ {.example}
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
~~~~

**Synopsis**: A list of menu options representing signals to be sent to
a process

**Example**:\
 \

~~~~ {.verbatim}
processes:

 cfservd_out_of_control::

   "cfservd"

        signals         => { "stop" , "term" },
        restart_class   => "start_cfserv";

 any::

   "snmpd"

        signals         => { "term" , "kill" };
   
~~~~

**Notes**:\
 \

Signals are presented as an ordered list to the process. On Windows,
only the kill signal is supported, which terminates the process.
