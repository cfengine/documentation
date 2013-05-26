---
layout: default
title: executor control promises 
categories: [Reference, Components, cf-execd, executor control promises]
published: true
alias: reference-components-cfexecd-control-promises.html
tags: [Components, cf-execd, control promises]
---

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

## `splaytime`

**Type**: int

**Allowed input range**: `0,99999999999`

**Default value:** 0

**Synopsis**: Time in minutes to splay this host based on its name
hash

```cf3
    body executor control
    {
        splaytime => "2";
    }
```

**Notes**:  
Whenever any class listed in the `schedule` attribute is present,
`cf-execd` can schedule an execution of `cf-agent`. The actual
execution will be delayed an integer number of seconds between
0-`splaytime` minutes. The specific amount of delay for "this" host
is based on a hash of the hostname. Thus a collection of hosts will
all execute at different times, and surges in network traffic can
be avoided.

A rough rule of thumb for scaling of small updates is set the splay
time between 1-5 minutes for up a few thousand hosts. The splaytime
should not be set to a value larger than the `cf-execd` scheduling
interval, else multiple clients might contend for data.

**Default value**:

The default value is 0 minutes.

**See also:** The `splayclass()` function for a task-specific means
for setting splay times.

## `mailfrom`

**Type**: string

**Allowed input range**: `.*@.*`

**Synopsis**: Email-address cfengine mail appears to come from

```cf3
    body executor control
    {
        mailfrom => "mrcfengine@example.org";
    }
```

**Notes**:


## `mailto`

**Type**: string

**Allowed input range**: `.*@.*`

**Synopsis**: Email-address cfengine mail is sent to

```cf3
    body executor control
    {
        mailto => "cfengine_alias@example.org";
    }
```

**Notes**:

The address to whom email is sent if an smtp host is configured.


## `smtpserver`

**Type**: string

**Allowed input range**: `.*`

**Synopsis**: Name or IP of a willing smtp server for sending
email

```cf3
    body executor control
    {
        smtpserver => "smtp.example.org";
    }
```cf3

**Notes**:

This should point to a standard port 25 server without encyption. If you are 
running secured or encrypted email then you should run a mail relay on 
localhost and point this to localhost.


## `mailmaxlines`

**Type**: int

**Allowed input range**: `0,1000`

**Default value:** 30

**Synopsis**: Maximum number of lines of output to send by email

    body executor control
    {
    mailmaxlines => "100";
    }

**Notes**:

This limit prevents anomalously large outputs from clogging up a system 
administrator's mailbox. The output is truncated in the email report, but the 
complete original transcript is stored in `WORKDIR/outputs/*` where it can be 
viewed on demand. A reference to the appropriate file is given.


## `schedule`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: The class schedule used by cf-execd for activating
cf-agent

    body executor control
    {
    schedule => { "Min00", "(Evening|Night).Min15_20", "Min30", "(Evening|Night).Min45_50" };
    }

**Notes**:

The list should contain class expressions comprised of classes
which are visible to the `cf-execd` daemon. In principle, any
defined class expression will cause the daemon to wake up and
schedule the execution of the `cf-agent`. In practice, the classes
listed in the list are usually date- and time-based.

The actual execution of `cf-agent` may be delayed by `splaytime`,
and may be deferred by promise caching and the value of
`ifelapsed`. Note also that the effectiveness of the `splayclass`
function may be affected by changing the `schedule`.

**Default value**:

    schedule => { "Min00", "Min05", "Min10", "Min15", "Min20", "Min25",
              "Min30", "Min35", "Min40", "Min45", "Min50", "Min55" };


## `executorfacility`

**Type**: (menu option)

**Allowed input range**:

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

**Default value:** LOG\_USER

**Synopsis**: Menu option for syslog facility level

    body executor control
    {
    executorfacility => "LOG_USER";
    }

**Notes**:

See the syslog manual pages.


## `exec_command`

**Type**: string

**Allowed input range**: `"?(/.*)`

**Synopsis**: The full path and command to the executable run by
default (overriding builtin)

    exec_command => "$(sys.workdir)/bin/cf-agent -f failsafe.cf && $(sys.workdir)/bin/cf-agent";

**Notes**:

The command is run in a shell encapsulation so pipes and shell
symbols may be used if desired. Unlike, CFEngine 2, CFEngine 3 does
not automatically run a separate update sequence before its normal
run. This can be handled using the approach in the example above.


## `agent_expireafter`

**Type**: int

**Allowed input range**: `0,10080`

**Default value:** 10080

**Synopsis**: Maximum agent runtime (in minutes)

    body executor control
    {
    agent_expireafter => "120";
    }

**Notes**:  
Sets a maximum time on any run of the command in `exec_command`. If
no data is received from the pipe opened to the process created
with `exec_command` after the time has elapsed, the process gets
killed.

Note that if you have long-running jobs, they may get killed with
this setting. Therefore, you should ensure it is higher than any
run of `cf-agent` that you want to leave alone. Alternatively, you
can make your jobs output something to STDOUT at least as often as
this threshold. This will reset the timer.

The setting will effectively allow you to set a threshold on the
number of simultaneous agents that are running. For example, if you
set it to `120` and you are using a 5-minute agent schedule, a
maximum of 120 / 5 = 24 agents should be enforced.

**Default value**:

The default value is 10080 minutes (one week).

