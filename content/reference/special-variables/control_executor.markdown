---
layout: default
title: control_executor
aliases:
  - "/reference-special-variables-default:control_executor.html"
---

Variables in the `default:control_executor` context are automatically created from attributes defined in `body executor control` following the pattern `default:default:control_executor.<attribute>`.

### default:control_executor.agent_expireafter

Controls the number of minutes after no data has been received by cf-execd from a cf-agent process before that cf-agent process is killed.

**See also:** [`agent_expireafter` in `body executor control`][cf-execd#agent_expireafter]

### default:control_executor.exec_command

Defines the command that cf-execd runs when the schedule criteria are met. This is typically the command to run cf-agent.

**See also:** [`exec_command` in `body executor control`][cf-execd#exec_command]

### default:control_executor.mailfrom

Specifies the email address that cf-execd uses as the sender when sending email notifications.

**See also:** [`mailfrom` in `body executor control`][cf-execd#mailfrom]

### default:control_executor.mailfilter_exclude

Defines a list of regular expressions that match lines to be excluded from emails sent by cf-execd.

**See also:** [`mailfilter_exclude` in `body executor control`][cf-execd#mailfilter_exclude]

### default:control_executor.mailfilter_include

Defines a list of regular expressions that match lines to be included in emails sent by cf-execd.

**See also:** [`mailfilter_include` in `body executor control`][cf-execd#mailfilter_include]

### default:control_executor.mailmaxlines

Controls the maximum number of lines of output that cf-execd will email when sending notifications.

**See also:** [`mailmaxlines` in `body executor control`][cf-execd#mailmaxlines]

### default:control_executor.mailsubject

Controls the subject of emails sent by cf-execd when output differs from the previous execution.

**See also:** [`mailsubject` in `body executor control`][cf-execd#mailsubject]

### default:control_executor.splaytime

Defines the maximum number of minutes cf-execd should wait before executing exec_command, allowing for distribution of load over time.

**See also:** [`splaytime` in `body executor control`][cf-execd#splaytime]

### default:control_executor.runagent_socket_allow_users

On Enterprise hubs, defines a list of users who should be allowed access to cf-execd runagent sockets.

**See also:** [`runagent_socket_allow_users` in `body executor control`][cf-execd#runagent_socket_allow_users]

### default:control_executor.executorfacility

Menu option for syslog facility level. Valid values are LOG_USER, LOG_DAEMON, LOG_LOCAL0 through LOG_LOCAL7. See the syslog manual pages for more information.

**See also:** [`executorfacility` in `body executor control`][cf-execd#executorfacility]

### default:control_executor.mailto

Email-address CFEngine mail is sent to. The address to whom email is sent if an smtp host is configured.

**See also:** [`mailto` in `body executor control`][cf-execd#mailto]

### default:control_executor.schedule

The class schedule used by cf-execd for activating cf-agent. The list should contain class expressions comprised of classes which are visible to the `cf-execd` daemon. In principle, any defined class expression will cause the daemon to wake up and schedule the execution of the `cf-agent`. In practice, the classes listed in the list are usually date- and time-based.

**See also:** [`schedule` in `body executor control`][cf-execd#schedule]

### default:control_executor.smtpserver

Name or IP of a willing smtp server for sending email. This should point to a standard port 25 server without encryption. If you are running secured or encrypted email then you should run a mail relay on localhost and point this to localhost.

**See also:** [`smtpserver` in `body executor control`][cf-execd#smtpserver]
