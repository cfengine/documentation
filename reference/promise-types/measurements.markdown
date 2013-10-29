---
layout: default
title: measurements
categories: [Reference, Promise Types, measurements]
published: true
alias: reference-promise-types-measurements.html
tags: [reference, bundle monitor, measurements, monitoring, promise types]
---

**These features are available only in CFEngine Enterprise.**

By default,CFEngine's monitoring component `cf-monitord` records performance data about the system. These include process counts, service traffic, load average and CPU utilization and temperature when available.

CFEngine Enterprise extends this in two ways. First it adds a three year trend
summary based any 'shift'-averages. Second, it adds customizable 
`measurements` promises to  monitor or log very specific user data through a 
generic interface. The end-result is to either generate a periodic time 
series, like the above mentioned values, or to log the results to 
custom-defined reports.

Promises of type `measurement` are written just like all other promises within 
a bundle destined for the agent concerned, in this case `monitor`. However, it 
is not necessary to add them to the `bundlesequence`, because `cf-monitord` 
executes all bundles of type `monitor`.

```cf3
    bundle monitor self_watch
    {
    measurements:
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
    }

    body match_value proc_value(x,y)
    {
      select_line_matching => "$(x)";
      extraction_regex => "$(y)";
    }
```

It is important to specify a promise `handle` for measurement promises, as the names defined in the handle are used to determine the name of the log file or variable to which data will be reported. Log files are created under `WORKDIR/state`. Data that have no history type are stored in a special variable context called `mon`, analogous to the system variables in sys. Thus the values may be used in other promises in the form `$(mon.handle)`.

```cf3
    bundle monitor watch_diskspace
    {
     measurements:
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

    body match_value file_systems
    {
      select_line_matching => "/.*";
      extraction_regex => "(.*)";
    }
```

The general pattern of these promises is to decide whether the source of the 
information is either a file or pipe, determine the data type (integer, string 
etc.), specify a pattern to match the result in the file stream and then 
specify what to do with the result afterwards.

***

## Attributes

### stream_type

**Description:** The datatype being collected.

CFEngine treats all input using a stream abstraction. The preferred interface 
is files, since they can be read without incurring the cost of a process. 
However pipes from executed commands may also be invoked.

**Type:** (menu option)

**Allowed input range:**

```cf3
     pipe
     file
```

**Example:**

```cf3
stream_type => "pipe";
```

### data_type

**Description:** The datatype being collected.

When CFEngine observes data, such as the attached partitions in the example above, the datatype determines how that data will be handled. Integer and real values, counters etc., are recorded as time-series if the history type is 'weekly', or as single values otherwise. If multiple items are matched by an observation (e.g. several lines in a file match the given regular expression), then these can be made into a list by choosing `slist`, else the first matching item will be selected.

**Type:** (menu option)

**Allowed input range:**   

```
    counter
    int
    real
    string
    slist
```

**Example:**

```cf3
  "/bin/df"

      handle => "free_disk_watch",
      stream_type => "pipe",

      data_type => "slist",

      history_type => "static",
      units => "device",
      match_value => file_systems,
      action => sample_min(10,15);

```

### history_type

**Description:** Whether the data can be seen as a time-series or just an
isolated value

**Type:** (menu option)

**Allowed input range:**   

* `scalar`

A single value, with compressed statistics is retained. The value of the
data is not expected to change much for the lifetime of the daemon (and
so will be sampled less often by cf-monitord).   

* `static`

A synonym for 'scalar'.   

* `log`

The measured value is logged as an infinite time-series in
\$(sys.workdir)/state.   

* `weekly`

A standard CFEngine two-dimensional time average (over a weekly period)
is retained.

**Example:**

```cf3
 "/proc/meminfo"

      handle => "free_memory_watch",
      stream_type => "file",
      data_type => "int",
      history_type => "weekly",
      units => "kB",
      match_value => free_memory;
```

### units

**Description:** The engineering dimensions of this value or a note about
its intent used in plots

This is an arbitrary string used in documentation only.

**Type:** `string`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
   "/var/cfengine/state/cf_rootprocs"

      handle => "monitor_self_watch",
      stream_type => "file",
      data_type => "int",
      history_type => "weekly",
      units => "kB",
      match_value => proc_value(".*cf-monitord.*",
        
         "root\s+[0-9.]+\s+[0-9.]+\s+[0-9.]+\s+[0-9.]+\s+([0-9]+).*");
```

### match_value

**Type:** `body match_value`

#### select_line_matching

**Description:** Regular expression for matching line location

The expression is [anchored][anchored], meaning it must match a whole line, and not
a fragment within a line.

This attribute is mutually exclusive of `select_line_number`.

**Type:** `string`

**Allowed input range:** `.*`

**Example:**

```cf3
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
```

#### select_line_number

**Description:** Read from the n-th line of the output (fixed format)

This is mutually exclusive of `select_line_matching`.   

**Type:** `int`

**Allowed input range:** `0,99999999999`

**Example:**

```cf3
     body match_value find_line
     {
     select_line_number => "2";
     }
```

**Notes:**


#### extraction_regex

**Description:** Regular expression that should contain a single
back-reference for extracting a value.

A single parenthesized back-reference should be given to lift the value to be 
measured out of the text stream. The regular expression is [unanchored][unanchored], meaning 
it may match a partial string

**Type:** `string`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
     body match_value free_memory
     {
     select_line_matching => "MemFree:.*";
     extraction_regex => "MemFree:\s+([0-9]+).*";
     }
```

#### track_growing_file

**Description:** If true, CFEngine remembers the position to which is last
read when opening the file, and resets to the start if the file has
since been truncated

This option applies only to file based input streams. If this is true, 
CFEngine treats the file as if it were a log file, growing continuously.
Thus the monitor reads all new entries since the last sampling time on
each invocation. In this way, the monitor does not count lines in the
log file redundantly.

This makes a log pattern promise equivalent to something like tail -f
logfile | grep pattern in Unix parlance.

**Type:** [`boolean`][boolean]

**Example:**

```cf3
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
```


#### select_multiline_policy

**Description:** Regular expression for matching line location

This option governs how CFEngine handles multiple matching lines in the
input stream. It can average or sum values if they are integer or real,
or use first or last representative samples. If non-numerical data types
are used only the first match is used.

**Type:** (menu option)

**Allowed input range:**   

```
    average
    sum
    first
    last
```

**Example:**

```cf3
     body match_value myvalue(xxx)
     {
      select_line_matching => ".*$(xxx).*";
      extraction_regex => "root\s+\S+\s+\S+\s+\S+\s+\S+\s+\S+\s+\S+\s+\S+\s+(\S+).*";
      select_multiline_policy => "sum";
     } 
```

**History:** Was introduced in 3.4.0 (2012)
