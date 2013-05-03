---
layout: default
title: measurements-in-monitor-promises
categories: [Bundles-for-monitor,measurements-in-monitor-promises]
published: true
alias: Bundles-for-monitor-measurements-in-monitor-promises.html
tags: [Bundles-for-monitor,measurements-in-monitor-promises]
---

### `measurements` promises in monitor

\

*These features are available only in Enterprise versions of CFEngine.*

By default,CFEngine's monitoring component `cf-monitord` records
performance data about the system. These include process counts, service
traffic, load average and CPU utilization and temperature when
available.

CFEngine Nova extends this in two ways. First it adds a three year trend
summary based any \`shift'-averages. Second, it adds customizable
promises to monitor or log very specific user data through a generic
interface. The end result is to either generate a periodic time series,
like the above mentioned values, or to log the results to custom-defined
reports.

CFEngine Nova adds a new promise type in bundles for the monitoring
agent. These are written just like all other promises within a bundle
destined for the agent concerned (however, you do not need to add them
to the `bundlesequence` they are executed by `cf-monitord` because they
are bundles of type `monitor`). In this case:

~~~~ {.verbatim}
bundle monitor watch

{
measurements:

  # promises ...

}
~~~~

It is important to specify a promise `handle` for measurement promises,
as the names defined in the handle are used to determine the name of the
log file or variable to which data will be reported. Log files are
created under WORKDIR/state. Data that have no history type are stored
in a special variable context called mon, analogous to the system
variables in sys. Thus the values may be used in other promises in the
form `$(mon.handle)`.

\

~~~~ {.verbatim}
  # Follow a special process over time
  # using CFEngine's process cache to avoid resampling

   "/var/cfengine/state/cf_rootprocs"

      handle => "monitor_self_watch",
      stream_type => "file",
      data_type => "int",
      history_type => "weekly",
      units => "kB",
      match_value => proc_value(".*cf-monitord.*",
         "root\s+[0-9.]+\s+[0-9.]+\s+[0-9.]+\s+[0-9.]+\s+([0-9]+).*");


  # Discover disk device information

  "/bin/df"

      handle => "free_diskspace_watch",
      stream_type => "pipe",
      data_type => "slist",
      history_type => "static",
      units => "device",
      match_value => file_systems;
      # Update this as often as possible

}

##########################################################

body match_value proc_value(x,y)
{
select_line_matching => "$(x)";
extraction_regex => "$(y)";
}

body match_value file_systems
{
select_line_matching => "/.*";
extraction_regex => "(.*)";
}

~~~~

\

**Notes:**

The general pattern of these promises is to decide whether the source of
the information is either a file or pipe, determine the data type
(integer, string etc.), specify a pattern to match the result in the
file stream and then specify what to do with the result afterwards.

**Standard measurements:**

The `cf-monitord` service monitors a number of variables as standard on
Unix and Windows systems. Windows is fundamentally different from Unix
and currently has less support for out-of-the-box probes.

1.  users: Users logged in
2.  rootprocs: Privileged system processes
3.  otherprocs: Non-privileged process
4.  diskfree: Free disk on / partition
5.  loadavg: % kernel load utilization
6.  netbiosns\_in: netbios name lookups (in)
7.  netbiosns\_out: netbios name lookups (out)
8.  netbiosdgm\_in: netbios name datagrams (in)
9.  netbiosdgm\_out: netbios name datagrams (out)
10. netbiosssn\_in: netbios name sessions (in)
11. netbiosssn\_out: netbios name sessions (out)
12. irc\_in: IRC connections (in)
13. irc\_out: IRC connections (out)
14. cfengine\_in: CFEngine connections (in)
15. cfengine\_out: CFEngine connections (out)
16. nfsd\_in: nfs connections (in)
17. nfsd\_out: nfs connections (out)
18. smtp\_in: smtp connections (in)
19. smtp\_out: smtp connections (out)
20. www\_in: www connections (in)
21. www\_out: www connections (out)
22. ftp\_in: ftp connections (in)
23. ftp\_out: ftp connections (out)
24. ssh\_in: ssh connections (in)
25. ssh\_out: ssh connections (out)
26. wwws\_in: wwws connections (in)
27. wwws\_out: wwws connections (out)
28. icmp\_in: ICMP packets (in)
29. icmp\_out: ICMP packets (out)
30. udp\_in: UDP dgrams (in)
31. udp\_out: UDP dgrams (out)
32. dns\_in: DNS requests (in)
33. dns\_out: DNS requests (out)
34. tcpsyn\_in: TCP sessions (in)
35. tcpsyn\_out: TCP sessions (out)
36. tcpack\_in: TCP acks (in)
37. tcpack\_out: TCP acks (out)
38. tcpfin\_in: TCP finish (in)
39. tcpfin\_out: TCP finish (out)
40. tcpmisc\_in: TCP misc (in)
41. tcpmisc\_out: TCP misc (out)
42. webaccess: Webserver hits
43. weberrors: Webserver errors
44. syslog: New log entries (Syslog)
45. messages: New log entries (messages)
46. temp0: CPU Temperature core 0
47. temp1: CPU Temperature core 1
48. temp2: CPU Temperature core 2
49. temp3: CPU Temperature core 3
50. cpu: %CPU utilization (all)
51. cpu0: %CPU utilization core 0
52. cpu1: %CPU utilization core 1
53. cpu2: %CPU utilization core 2
54. cpu3: %CPU utilization core 3

Slots with a higher number are used for custom measurement promises in
CFEngine Nova.

These values collected and analysed by `cf-monitord` are transformed
into agent variables in the `$(mon.`name`)` context.

**Measurement promise syntax:**

-   [stream\_type in measurements](#stream_005ftype-in-measurements)
-   [data\_type in measurements](#data_005ftype-in-measurements)
-   [history\_type in measurements](#history_005ftype-in-measurements)
-   [units in measurements](#units-in-measurements)
-   [match\_value in measurements](#match_005fvalue-in-measurements)

#### `stream_type`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
               pipe
               file
~~~~

**Synopsis**: The datatype being collected.

**Example**:\
 \

~~~~ {.verbatim}
stream_type => "pipe";
~~~~

**Notes**:\
 \

CFEngine treats all input using a stream abstraction. The preferred
interface is files, since they can be read without incurring the cost of
a process. However pipes from executed commands may also be invoked.

#### `data_type`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
               counter
               int
               real
               string
               slist
~~~~

**Synopsis**: The datatype being collected.

**Example**:\
 \

~~~~ {.verbatim}
  "/bin/df"

      handle => "free_disk_watch",
      stream_type => "pipe",

      data_type => "slist",

      history_type => "static",
      units => "device",
      match_value => file_systems,
      action => sample_min(10,15);

~~~~

**Notes**:\
 \

When CFEngine (Nova) observes data, such as the attached partitions in
the example above, the datatype determines how that data will be
handled. Integer and real values, counters etc., are recorded as
time-series if the history type is \`weekly', or as single values
otherwise. If multiple items are matched by an observation (e.g. several
lines in a file match the given regular expression), then these can be
made into a list by choosing `slist`, else the first matching item will
be selected.

#### `history_type`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
               weekly
               scalar
               static
               log
~~~~

**Synopsis**: Whether the data can be seen as a time-series or just an
isolated value

**Example**:\
 \

~~~~ {.verbatim}
 "/proc/meminfo"

      handle => "free_memory_watch",
      stream_type => "file",
      data_type => "int",
      history_type => "weekly",
      units => "kB",
      match_value => free_memory;
~~~~

**Notes**:\
 \

scalar

A single value, with compressed statistics is retained. The value of the
data is not expected to change much for the lifetime of the daemon (and
so will be sampled less often by cf-monitord). \

static

A synonym for \`scalar'. \

log

The measured value is logged as an infinite time-series in
\$(sys.workdir)/state. \

weekly

A standard CFEngine two-dimensional time average (over a weekly period)
is retained.

#### `units`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: The engineering dimensions of this value or a note about
its intent used in plots

**Example**:\
 \

~~~~ {.verbatim}
   "/var/cfengine/state/cf_rootprocs"

      handle => "monitor_self_watch",
      stream_type => "file",
      data_type => "int",
      history_type => "weekly",
      units => "kB",
      match_value => proc_value(".*cf-monitord.*",
        
         "root\s+[0-9.]+\s+[0-9.]+\s+[0-9.]+\s+[0-9.]+\s+([0-9]+).*");
~~~~

**Notes**:\
 \

This is an arbitary string used in documentation only.

#### `match_value` (body template)

**Type**: (ext body)

`select_line_matching`

**Type**: string

**Allowed input range**: `.*`

**Synopsis**: Regular expression for matching line location

**Example**:\
 \

~~~~ {.verbatim}
     
     # Editing
     
     body location example
     {
     select_line_matching => "Expression match.* whole line";
     }
     
     # Measurement promises
     
     body match_value example
     {
     select_line_matching => "Expression match.* whole line";
     }
     
~~~~

**Notes**:\
 \

The expression is anchored, meaning it must match a whole line, and not
a fragment within a line (see [Anchored vs. unanchored regular
expressions](#Anchored-vs_002e-unanchored-regular-expressions)).

This attribute is mutually exclusive of `select_line_number`. \

`select_line_number`

**Type**: int

**Allowed input range**: `0,99999999999`

**Synopsis**: Read from the n-th line of the output (fixed format)

**Example**:\
 \

~~~~ {.verbatim}
     
     body match_value find_line
     {
     select_line_number => "2";
     }
     
~~~~

**Notes**:\
 \

This is mutually exclusive of `select_line_matching`. \

`extraction_regex`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: Regular expression that should contain a single
backreference for extracting a value

**Example**:\
 \

~~~~ {.verbatim}
     
     body match_value free_memory
     {
     select_line_matching => "MemFree:.*";
     extraction_regex => "MemFree:\s+([0-9]+).*";
     }
     
~~~~

**Notes**:\
 \

A single parenthesized backreference should be given to lift the value
to be measured out of the text stream. The regular expression is
unanchored, meaning it may match a partial string (see [Anchored vs.
unanchored regular
expressions](#Anchored-vs_002e-unanchored-regular-expressions)). \

`track_growing_file`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    true
                    false
                    yes
                    no
                    on
                    off
~~~~

**Synopsis**: If true, CFEngine remembers the position to which is last
read when opening the file, and resets to the start if the file has
since been truncated

**Example**:\
 \

~~~~ {.verbatim}
     bundle monitor watch
     {
     measurements:
     
        "/home/mark/tmp/file"
     
              handle => "line_counter",
         stream_type => "file",
           data_type => "counter",
         match_value => scan_log("MYLINE.*"),
        history_type => "log",
              action => sample_rate("0");
     
     }
     
     #
     
     body match_value scan_log(x)
     {
     select_line_matching => "^$(x)$";
     track_growing_file => "true";
     }
     
     #
     
     body action sample_rate(x)
     {
     ifelapsed => "$(x)";
     expireafter => "10";
     }
~~~~

**Notes**:\
 \

This option applies only to file based input streams. If this is true,
CFEngine treats the file as if it were a log file, growing continuously.
Thus the monitor reads all new entries since the last sampling time on
each invocation. In this way, the monitor does not count lines in the
log file redundantly.

This makes a log pattern promise equivalent to something like tail -f
logfile | grep pattern in Unix parlance. \

`select_multiline_policy`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    average
                    sum
                    first
                    last
~~~~

**Synopsis**: Regular expression for matching line location

**Example**:\
 \

~~~~ {.verbatim}
     
     body match_value myvalue(xxx)
     {
      select_line_matching => ".*$(xxx).*";
      extraction_regex => "root\s+\S+\s+\S+\s+\S+\s+\S+\s+\S+\s+\S+\s+\S+\s+(\S+).*";
      select_multiline_policy => "sum";
     } 
     
~~~~

**Notes**:\
 \

*History*: Was introduced in 3.4.0 (2012)

This option governs how CFEngine handels multiple matching lines in the
input stream. We can average or sum values if they are integer or real,
or use first or last representative samples. If non-numerical data types
are used on the the first match is used.
