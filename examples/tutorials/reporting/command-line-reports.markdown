---
layout: default
title: Command-Line Reports
published: true
sorting: 60
---

#### Command-line reporting is available to Enterprise and Community users.

### Overview

The following report topics are included:

[CFEngine output levels][Command-Line Reports#CFEngine output levels]

[Creating custom reports][Command-Line Reports#Creating custom reports]

[Including data in reports][Command-Line Reports#Including data in reports]

[Excluding data from reports][Command-Line Reports#Excluding data from reports]

[Creating custom logs][Command-Line Reports#Creating custom logs]

[Redirecting output to logs][Command-Line Reports#Redirecting output to logs]

[Change detection: tripwires][Command-Line Reports#Change detection: tripwires]


### CFEngine output levels

CFEngine's default behavior is to report to the console (known as standard output). It's
default behavior is to report nothing except errors that are judged to be of a critical
nature.

By using CFEngine with the inform flag, you can alter the default to report on action
items (actual changes) and warnings:

```
# cf-agent -I
# cf-agent --inform
```

By using CFEngine with the verbose flag, you can alter the default to report all of its
thought-processes. You should not interpret a message that only appears in CFEngine's
verbose mode as an actual error, only as information that might be relevant to decisions
being made by the agent:

```
# cf-agent -v
# cf-agent --verbose
```

### Creating custom reports

CFEngine allows you to use `reports` promises to make reports of your own. A simple
example of this is shown below.

```cf3
body common control
{
bundlesequence => { "test" };
}

#

bundle agent test
{
reports:

  cfengine_3::

   "$(sys.date),This is a report"
     report_to_file => "/tmp/test_log";
}
```
We can apply this idea to make more useful custom reports. In this example,
the agent tests for certain software package and creates a simple HTML file of
existing software:

```cf3
body common control
{
bundlesequence => { "test" };
}

#

bundle agent test
{
vars:

 "software" slist => { "gpg", "zip", "rsync" };

classes:

 "no_report"        expression => fileexists("/tmp/report.html");
 "have_$(software)" expression => fileexists("/usr/bin/$(software)");

reports:

  no_report::

      "
      <html>
      Name of this host is: $(sys.host)<br>
      Type of this host is: $(sys.os)<br>
      "

         report_to_file => "/tmp/report.html";

      #

      "
      Host has software $(software)<br>
      "

        if             => "have_$(software)",
        report_to_file => "/tmp/report.html";

      #

      "
      </html>
      "
         report_to_file => "/tmp/report.html";

}
```

The outcome of this promise is a file called /tmp/report.html which contains
the following output:

```cf3
      <html>
      Name of this host is: atlas<br>
      Type of this host is: linux<br>

      Host has software gpg<br>

      Host has software zip<br>

      Host has software rsync<br>

      </html>
```

The mechanism shown above can clearly be used to create a wide variety of report formats,
but it requires a lot of coding and maintenance by the user.

### Including data in reports

CFEngine generates information internally that you might want to use in reports.
For example, the agent `cf-agent` interfaces with the local light-weight monitoring agent
`cf-monitord` so that system state can be reported simply:

```cf3
body common control

{
bundlesequence  => { "report" };
}

###########################################################

bundle agent report

{
reports:

  linux::

   "/etc/passwd except $(const.n)"

     showstate => { "otherprocs", "rootprocs" };

}
```

A bonus to this is that you can get CFEngine to report system anomalies:

```cf3
reports:

 rootprocs_high_dev2::

   "RootProc anomaly high 2 dev on $(mon.host) at approx $(mon.env_time)
    measured value $(mon.value_rootprocs)
    average $(mon.average_rootprocs) pm $(mon.stddev_rootprocs)"

      showstate => { "rootprocs" };

 entropy_www_in_high&anomaly_hosts.www_in_high_anomaly::

   "High entropy incoming www anomaly on $(mon.host) at $(mon.env_time)
    measured value $(mon.value_www_in)
    average $(mon.average_www_in) pm $(mon.stddev_www_in)"

      showstate => { "incoming.www" };

```

This produces the following standard output:

```cf3
R: State of otherprocs peaked at Tue Dec  1 12:12:21 2014

R: The peak measured state was q = 98:
R: Frequency: [kjournald]      |**      (2/98)
R: Frequency: [pdflush]        |**      (2/98)
R: Frequency: /var/cfengine/bin/cf-execd|**     (2/98)
R: Frequency: COMMAND          |*       (1/98)
R: Frequency: init [5]         |*       (1/98)
R: Frequency: [kthreadd]       |*       (1/98)
R: Frequency: [migration/0]    |*       (1/98)
R: Frequency: [ksoftirqd/0]    |*       (1/98)
R: Frequency: [events/0]       |*       (1/98)
R: Frequency: [khelper]        |*       (1/98)
R: Frequency: [kintegrityd/0]  |*       (1/98)
```

Finally, you can quote lines from files in your data for convenience:

```cf3
body common control

{
bundlesequence  => { "report" };
}

###########################################################

bundle agent report

{
reports:

  linux::

   "/etc/passwd except $(const.n)"

     printfile => pr("/etc/passwd","5");

}

######################################################################

body printfile pr(file,lines)

{
file_to_print => "$(file)";
number_of_lines => "$(lines)";
}
```

This produces the following output:

```cf3
R: /etc/passwd except
R: at:x:25:25:Batch jobs daemon:/var/spool/atjobs:/bin/bash
R: avahi:x:103:105:User for Avahi:/var/run/avahi-daemon:/bin/false
R: beagleindex:x:104:106:User for Beagle indexing:/var/cache/beagle:/bin/bash
R: bin:x:1:1:bin:/bin:/bin/bash
R: daemon:x:2:2:Daemon:/sbin:/bin/bash
```

### Excluding data from reports

CFEngine generates information internally that you might want exclude from
reports. Any promise outcome can be excluded from report collection based on its
handle. `vars` and `classes` type promises can be excluded using its handle
**or** by meta tag.

```cf3
bundle agent main
{
  files:

    linux::

     "/var/log/noisy.log"
       handle => "noreport_noisy_log_rotation",
       rename => rotate(5);
}

body report_data_select default_data_select_policy_hub
# @brief Data to collect from policy servers by default
#
# By convention variables and classes known to be internal, (having no
# reporting value) should be prefixed with an underscore. By default the policy
# framework explicitly excludes these variables and classes from collection.
{
 # Collect all classes or vars tagged with `inventory` or `report`
      metatags_include => { "inventory", "report" };

 # Exclude any classes or vars tagged with `noreport`
      metatags_exclude => { "noreport" };

 # Exclude any promise with handle matching `noreport_.*` from report collection.
      promise_handle_exclude => { "noreport_.*" };

 # Include all metrics from cf-monitord
      monitoring_include => { ".*" };
}
```

### Creating custom logs

Logs can be attached to any promise. In this example, an executed shell command logs a
message to the standard output. CFEngine recognizes thestdoutfilename for Standard Output,
in the Unix/C standard manner:

```cf3
bundle agent test
{
commands:

  "/tmp/myjob",

     action => logme("executor");

}

############################################

body action logme(x)
{
log_repaired => "stdout";
log_string => " -> Started the $(x) (success)";
}
```

In the following example, a file creation promise logs different outcomes
(success or failure) to different log files:

```cf3
body common control
{
bundlesequence => { "test" };
}

bundle agent test
{
vars:

  "software" slist => { "/root/xyz", "/tmp/xyz" };

files:

  "$(software)"

    create => "true",
     action => logme("$(software)");

}

#

body action logme(x)
{
log_kept => "/tmp/private_keptlog.log";
log_failed => "/tmp/private_faillog.log";
log_repaired => "/tmp/private_replog.log";
log_string => "$(sys.date) $(x) promise status";
}
```

This generates three different logs with the following output:

```cf3
atlas$ more /tmp/private_keptlog.log
Sun Dec  6 11:58:16 2009 /tmp/xyz promise status
Sun Dec  6 11:58:43 2009 /tmp/xyz promise status
```

### Redirecting output to logs

CFEngine interfaces with the system logging tools in different ways. `Syslog` is the
default log for Unix-like systems, while the `event logger` is the default on Windows.
You may choose to copy a fixed level of CFEngine's standard screen messaging to the
system logger on a per-promise basis:

```cf3
body common control
{
bundlesequence => { "one" };
}


bundle agent one
{
files:

  "/tmp/xyz"

       create => "true",
       action => log;
}

body action log
{
log_level => "inform";
}
```

### Change detection: tripwires

Doing a change detection scan is a convergent process, but it can still detect changes
and present the data in a compressed format that is often more convenient than a full-scale
audit. The result is less precise, but there is a trade-off between precision and cost.

To make a change tripwire, use a files promise, as shown below:

```cf3
body common control
{
bundlesequence  => { "testbundle"  };
}
#

bundle agent testbundle

{
files:

  "/home/mark/tmp" -> "me"
       changes      => scan_files,
       depth_search => recurse("inf");
}

# library code ...

body changes scan_files
{
report_changes => "all";
update_hashes  => "true";
}

body depth_search recurse(d)
{
depth        => "$(d)";
}
```

In CFEngine Enterprise, reports of the following form are generated when these promises
are kept by the agent:

```cf3
Change detected 	 File change
Sat Dec 5 18:27:44 2013  group for /tmp/testfile changed 100 -> 0
Sat Dec 5 18:27:44 2013  /tmp/testfile
Sat Dec 5 18:20:45 2013  /tmp/testfile
```

These reports are generated automatically in Enterprise, and are integrated into the
web-browsable knowledge map. Community edition users must extract the data and create
these themselves.
