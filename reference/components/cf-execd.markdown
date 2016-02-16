---
layout: default
title: cf-execd
published: true
sorting: 30
tags: [Components, cf-execd]
keywords: [executor]
---

`cf-execd` is the scheduling daemon for `cf-agent`. It runs
`cf-agent` locally according to a schedule specified in policy code (executor
control body). After a `cf-agent` run is completed, `cf-execd` gathers output
from `cf-agent`, and may be configured to email the output to a specified
address. It may also be configured to [splay][cf-execd#splaytime] (randomize)
the execution schedule to prevent synchronized `cf-agent` runs across a
network.

`cf-execd` keeps the promises made in `common` bundles, and is affected by
`common` and `executor` control bodies.

## Command reference ##

[%CFEngine_include_snippet(cf-execd.help, [\s]*--[a-z], ^$)%]

## Control Promises

These body settings determine the behavior of `cf-execd`,including scheduling
times and output capture to `WORKDIR/outputs` and relay via email.

```cf3
     body executor control
     {
         splaytime  => "5";
         mailto     => "cfengine@example.org";
         mailfrom   => "cfengine@$(host).example.org";
         smtpserver => "localhost";
         schedule   => { "Min00_05", "Min30_35" }
     }
```


### agent_expireafter

**Description:** Maximum agent runtime (in minutes)

Sets a maximum time on any run of the command in `exec_command`. If
no data is received from the pipe opened to the process created
with `exec_command` after the time has elapsed, the process gets
killed.

Note that if you have long-running jobs, they may get killed with
this setting. Therefore, you should ensure it is higher than any
run of `cf-agent` that you want to leave alone. Alternatively, you
can make your jobs output something to STDOUT at least as often as
this threshold. This will reset the timer.

**Type:** `int`

**Allowed input range:** `0,10080`

**Default value:** 120

**Example:**

```cf3
    body executor control
    {
    agent_expireafter => "120";
    }
```

**Notes:**
The setting will effectively allow you to set a threshold on the
number of simultaneous agents that are running. For example, if you
set it to `120` and you are using a 5-minute agent schedule, a
maximum of 120 / 5 = 24 agents should be enforced.

### executorfacility

**Description:** Menu option for syslog facility level

**Type:** (menu option)

**Allowed input range:**

    LOG_USER
    LOG_DAEMON
    LOG_LOCAL0
    LOG_LOCAL1
    LOG_LOCAL2
    LOG_LOCAL3
    LOG_LOCAL4
    LOG_LOCAL5
    LOG_LOCAL6
    LOG_LOCAL7

See the syslog manual pages.

**Default value:** `LOG_USER`

**Example:**

```cf3
    body executor control
    {
    executorfacility => "LOG_USER";
    }
```

### exec_command

**Description:** The full path and command to the executable run by
default (overriding `builtin`)

The command is run in a shell encapsulation so pipes and shell
symbols may be used if desired.

**Type:** `string`

**Allowed input range:** `"?(/.*)`

**Example:**

    exec_command => "$(sys.workdir)/bin/cf-agent -f failsafe.cf && $(sys.workdir)/bin/cf-agent";

### mailfrom

**Description:** Email-address cfengine mail appears to come from

**Type:** `string`

**Allowed input range:** `.*@.*`

**Example:**

```cf3
    body executor control
    {
        mailfrom => "mrcfengine@example.org";
    }
```

### mailmaxlines

**Description:** Maximum number of lines of output to send by email

This limit prevents anomalously large outputs from clogging up a system
administrator's mailbox. The output is truncated in the email report, but the
complete original transcript is stored in `WORKDIR/outputs/*` where it can be
viewed on demand. A reference to the appropriate file is given.

**Type:** `int`

**Allowed input range:** `0,1000`

**Default value:** 30

**Example:**

```cf3
    body executor control
    {
    mailmaxlines => "100";
    }
````

### mailsubject

**Description:** The subject in the mail sent by CFEngine.

The subject can contain system variables, like for example IP address or
architecture.

**Type:** `string`

**Allowed input range:** `.*`

**Example:**

```cf3
    body executor control
    {
        mailsubject => "CFEngine report ($(sys.fqhost))";
    }
```

### mailto

**Description:** Email-address cfengine mail is sent to

The address to whom email is sent if an smtp host is configured.

**Type:** `string`

**Allowed input range:** `.*@.*`

**Example:**

```cf3
    body executor control
    {
        mailto => "cfengine_alias@example.org";
    }
```

### schedule

**Description:** The class schedule used by cf-execd for activating
cf-agent

The list should contain class expressions comprised of classes
which are visible to the `cf-execd` daemon. In principle, any
defined class expression will cause the daemon to wake up and
schedule the execution of the `cf-agent`. In practice, the classes
listed in the list are usually date- and time-based.

The actual execution of `cf-agent` may be delayed by `splaytime`,
and may be deferred by promise caching and the value of
[`ifelapsed`][cf-agent#ifelapsed]. Note also that the effectiveness of the `splayclass`
function may be affected by changing the `schedule`.

**Type:** `slist`

**Allowed input range:** (arbitrary string)

**Default value:**

    schedule => { "Min00", "Min05", "Min10", "Min15", "Min20", "Min25",
              "Min30", "Min35", "Min40", "Min45", "Min50", "Min55" };

**Example:**

```cf3
    body executor control
    {
    schedule => { "Min00", "(Evening|Night).Min15_20", "Min30", "(Evening|Night).Min45_50" };
    }
```

### smtpserver

**Description:** Name or IP of a willing smtp server for sending
email

This should point to a standard port 25 server without encryption. If you are
running secured or encrypted email then you should run a mail relay on
localhost and point this to localhost.

**Type:** `string`

**Allowed input range:** `.*`

**Example:**

```cf3
  body executor control
  {
      smtpserver => "smtp.example.org";
  }
```

### splaytime

**Description:** Time in minutes to splay this host based on its name
hash

Whenever any class listed in the `schedule` attribute is present,
`cf-execd` can schedule an execution of `cf-agent`. The actual
execution will be delayed an integer number of seconds between
0-`splaytime` minutes. The specific amount of delay for "this" host
is based on a hash of the hostname. Thus a collection of hosts will
all execute at different times, and surges in network traffic can
be avoided.

A general rule for scaling of small updates is to set the splay time to
runinterval-1 minutes for up a few thousand hosts. For example, the default
schedule executes once every 5 minutes, so the splay time should be set to no
more than 4 minutes. The `splaytime` should be set to a value less than the
`cf-execd` scheduling interval, else multiple clients might contend for data.
In other words, `splaytime` + `cf-agent` run time should be less than the
scheduling interval.

**Type:** `int`

**Allowed input range:** `0,99999999999`

**Default value:** 0

The CFEngine default policy sets `splaytime` to 1.

**Example:**

```cf3
  body executor control
  {
      splaytime => "2";
  }
```

**See also:** The [`splayclass()`][splayclass] function for a task-specific
means for setting splay times.
