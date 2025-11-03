---
layout: default
title: control_common
aliases:
  - "/reference-special-variables-default:control_common.html"
---

Variables in the `default:control_common` context are automatically created from attributes defined in `body common control` following the pattern `default:default:control_common.<attribute>`.

### default:control_common.bundlesequence

Allows appending bundles to the end of the default bundlesequence. This makes it possible to extend the execution order without modifying the core policy.

**See also:** [`bundlesequence` in `body common control`][Components#bundlesequence]

### default:control_common.ignore_missing_bundles

Controls whether errors should be ignored when a bundle specified in body common control bundlesequence is not found. Valid values are "true" or "false".

**See also:** [`ignore_missing_bundles` in `body common control`][Components#ignore_missing_bundles]

### default:control_common.ignore_missing_inputs

Controls whether errors should be ignored when a file specified in body common control inputs is not found. Valid values are "true" or "false".

**See also:** [`ignore_missing_inputs` in `body common control`][Components#ignore_missing_inputs]

### default:control_common.lastseenexpireafter

Configures the number of minutes after which last-seen entries in `cf_lastseen.lmdb` are purged. The default value is typically 1 week (10080 minutes).

**See also:** [`lastseenexpireafter` in `body common control`][Components#lastseenexpireafter]

### default:control_common.protocol_version

Restricts the protocol to a specified version instead of negotiating the newest protocol available. Valid values include "1", "classic", "2", "tls", "3", "cookie", "4", "filestream", "latest".

**See also:** [`protocol_version` in `body common control`][Components#protocol_version]

### default:control_common.system_log_level

Controls the minimum log level required for log messages to go to the system log (e.g. syslog, Windows Event Log). Valid values are "critical", "error", "warning", "notice", "info".

**See also:** [`system_log_level` in `body common control`][Components#system_log_level]

### default:control_common.tls_ciphers

Specifies the ciphers that should be used for outgoing connections by cf-agent.

**See also:** [`tls_ciphers` in `body common control`][Components#tls_ciphers]

### default:control_common.tls_min_version

Specifies the minimum TLS version that should be used for outgoing connections by cf-agent.

**See also:** [`tls_min_version` in `body common control`][Components#tls_min_version]
