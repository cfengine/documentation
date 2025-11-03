---
layout: default
title: control_runagent
aliases:
  - "/reference-special-variables-default:control_runagent.html"
---

Variables in the `default:control_runagent` context are automatically created from attributes defined in `body runagent control` following the pattern `default:default:control_runagent.<attribute>`.

### default:control_runagent.background_children

Controls whether child processes spawned by cf-runagent should run in the background.

**See also:** [`background_children` in `body runagent control`][cf-runagent#background_children]

### default:control_runagent.encrypt

Controls whether communication between cf-runagent and remote hosts should be encrypted.

**See also:** [`encrypt` in `body runagent control`][cf-runagent#encrypt]

### default:control_runagent.force_ipv4

Forces cf-runagent to use IPv4 connections even when IPv6 is available.

**See also:** [`force_ipv4` in `body runagent control`][cf-runagent#force_ipv4]

### default:control_runagent.hosts

Defines a list of hosts that cf-runagent will attempt to connect to for remote execution.

**See also:** [`hosts` in `body runagent control`][cf-runagent#hosts]

### default:control_runagent.max_children

Controls the maximum number of concurrent child processes that cf-runagent will spawn.

**See also:** [`max_children` in `body runagent control`][cf-runagent#max_children]

### default:control_runagent.output_directory

Specifies the directory where output files from remote executions should be stored when output_to_file is enabled.

**See also:** [`output_directory` in `body runagent control`][cf-runagent#output_directory]

### default:control_runagent.output_to_file

Controls whether output from remote executions should be saved to files rather than displayed on the console.

**See also:** [`output_to_file` in `body runagent control`][cf-runagent#output_to_file]

### default:control_runagent.port

Defines the port number that cf-runagent uses for connections to remote hosts.

**See also:** [`port` in `body runagent control`][cf-runagent#port]

### default:control_runagent.timeout

Sets the timeout (in seconds) for connections to remote hosts. Connections that exceed this timeout will be terminated.

**See also:** [`timeout` in `body runagent control`][cf-runagent#timeout]

### default:control_runagent.trustkey

Controls whether cf-runagent should automatically trust new keys from remote hosts during the connection process.

**See also:** [`trustkey` in `body runagent control`][cf-runagent#trustkey]
