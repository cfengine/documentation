---
layout: default
title: control_monitor
aliases:
  - "/reference-special-variables-default:control_monitor.html"
---

Variables in the `default:control_monitor` context are automatically created from attributes defined in `body monitor control` following the pattern `default:default:control_monitor.<attribute>`.

### default:control_monitor.forgetrate

Controls the rate at which cf-monitord forgets historical monitoring data. A value between 0 and 1 determines how quickly older observations decay in significance.

**See also:** [`forgetrate` in `body monitor control`][cf-monitord#forgetrate]

### default:control_monitor.histograms

Determines whether cf-monitord should generate histograms for monitoring data. Setting this to true enables histogram-based data collection.

**See also:** [`histograms` in `body monitor control`][cf-monitord#histograms]

### default:control_monitor.monitorfacility

Controls the syslog facility level used by cf-monitord. Valid values are LOG_USER, LOG_DAEMON, LOG_LOCAL0 through LOG_LOCAL7.

**See also:** [`monitorfacility` in `body monitor control`][cf-monitord#monitorfacility]

### default:control_monitor.tcpdump

Enables or disables tcpdump-based network monitoring in cf-monitord.

**See also:** [`tcpdump` in `body monitor control`][cf-monitord#tcpdump]

### default:control_monitor.tcpdumpcommand

Specifies the command used for tcpdump-based network monitoring when tcpdump is enabled.

**See also:** [`tcpdumpcommand` in `body monitor control`][cf-monitord#tcpdumpcommand]
