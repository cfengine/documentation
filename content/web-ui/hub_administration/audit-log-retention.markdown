---
layout: default
title: Audit log retention
aliases:
  - "/web-ui-hub_administration-audit-log-retention.html"
---

The Mission Portal [Audit log API](/api/enterprise-api-ref/audit-logs-api/)
records administrative actions (user, role, settings, host, group, Build
project, and federated reporting changes) in the `audit_log` table of the
`cfsettings` PostgreSQL database.

## Default retention

There is no automatic purging of audit log entries. Records are kept
indefinitely until manually removed.

This is intentional for compliance use cases where a long, complete history is
desirable, but it means the `audit_log` table will grow without bound on
long-running hubs. Operators are expected to apply their own retention policy.

## Inspecting current size

To see how many entries you have and how old they are:

```console
sudo -u cfpostgres /var/cfengine/bin/psql cfsettings -c \
  "SELECT count(*) AS rows,
          min(time) AS oldest,
          max(time) AS newest,
          pg_size_pretty(pg_total_relation_size('audit_log')) AS size
   FROM audit_log;"
```

## Manually pruning old entries

To delete entries older than a chosen number of days, run as the `cfpostgres`
user on the hub:

```console
sudo -u cfpostgres /var/cfengine/bin/psql cfsettings -c \
  "DELETE FROM audit_log WHERE time < NOW() - INTERVAL '180 days';"
```

The `idx_audit_log_timestamp` index ensures this is efficient even on large
tables. Adjust the interval to match your retention policy (regulatory
requirements often dictate 1, 3, or 7 years).

## Scheduling pruning with CFEngine policy

Deletion of old records can be accomplished via policy using a `commands` promise. For example:

```cf3
bundle agent audit_log_retention
# @brief Prune Mission Portal audit_log entries older than $(days) days
{
  vars:
    "days" string => "365";

  commands:
    policy_server::
      "$(sys.bindir)/psql"
        args => "cfsettings -c \"DELETE FROM audit_log WHERE time < NOW() - INTERVAL '$(days) day';\"",
        contain => in_shell_and_silent,
        action => if_elapsed_day,
        handle => "audit_log_retention_prune",
        comment => "Prune Mission Portal audit_log entries older than $(days) days";
}
```

## RBAC

Viewing the Audit log in Mission Portal or via the API requires the
`audit-log.view` RBAC permission, granted to the `admin` role by default.

## See also

- [Audit log API](/api/enterprise-api-ref/audit-logs-api/) &mdash; query the log programmatically
- [Database schema: `audit_log`](/api/enterprise-api-ref/sql-schema/cfsettings/) &mdash; column reference
- [Event log](/web-ui/#event-log) &mdash; a separate, automatically-pruned log of host
  bootstraps, decommissions, and alert state changes
