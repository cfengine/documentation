---
layout: default
title: control_hub
aliases:
  - "/reference-special-variables-default:control_hub.html"
---

Variables in the `default:control_hub` context are automatically created from attributes defined in `body hub control` following the pattern `default:default:control_hub.<attribute>`.

### default:control_hub.exclude_hosts

Defines a list of hosts or network ranges to exclude from hub-initiated report collection. This is useful for excluding community agents, hosts behind NAT, or hosts using client-initiated reporting.

**See also:** [`exclude_hosts` in `body hub control`][cf-hub#exclude_hosts]

### default:control_hub.hub_schedule

Specifies the schedule for Enterprise hub-initiated pull collection as a list of classes that should trigger collection when defined.

**See also:** [`hub_schedule` in `body hub control`][cf-hub#hub_schedule]

### default:control_hub.port

Defines the port on which cf-hub listens for connections for report collection.

**See also:** [`port` in `body hub control`][cf-hub#port]

### default:control_hub.query_timeout

Configures the timeout (in seconds) for cf-hub outgoing connections. A value of "0" uses the binary default.

**See also:** [`query_timeout` in `body hub control`][cf-hub#query_timeout]

### default:control_hub.client_history_timeout

Controls the maximum age (in hours) of old reports that cf-hub will collect from clients. This prevents a build-up of reports that could cause a condition where the client is never able to send all reports within the collection window.

**See also:** [`client_history_timeout` in `body hub control`][cf-hub#client_history_timeout]
