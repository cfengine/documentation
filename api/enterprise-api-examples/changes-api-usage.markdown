---
layout: default
title: Tracking changes
published: true
sorting: 50
tags: [examples, enterprise, rest, api, reporting, hosts, changes, repairs]
---

Changes REST API allows to track the changes made by cf-agent in the infrastructure.

## Example: Count changes

This examples shows how to count changes performed by cf-agent within last 24h hours.

Example is searching for changes that are performed by *linux* machines within *generate_repairs* bundle.

**Request**

```
curl --user admin:admin 'https://test.cfengine.com/api/v2/changes/policy/count?include[]=linux&bundlename=generate_repairs'
```

**Response**

```
{
  "count": 381
}
```

## Example: Show vacuum command executions

Show all *vacuumdb* executions within last 24 hours executed on policy server.

Example is searching for changes that are performed by *policy_server* machines that execute *commands* promise with command */var/cfengine/bin/vacuumdb%* - there is '%' sign at the end which is a wildcard as vacuumdb is executed with different options across policy.

**Request**

```
curl --user admin:admin 'https://test.cfengine.com/api/v2/changes/policy?include[]=policy_server&promisetype=commands&promiser=/var/cfengine/bin/vacuumdb%'
```

**Response**

```
{
  "data": [
    {
      "bundlename": "cfe_internal_postgresql_vacuum",
      "changetime": 1437642099,
      "hostkey": "SHA=6ddfd5eaa85ee681ec12ce833fd7206e4d21c76e496be5f8b403ad0ead60a6ce",
      "hostname": "hub.provisioned.1436361289.cfengine.com.com",
      "logmessages": [
        "Executing 'no timeout' ... '/var/cfengine/bin/vacuumdb --analyze --quiet --dbname=cfdb'",
        "Completed execution of '/var/cfengine/bin/vacuumdb --analyze --quiet --dbname=cfdb'"
      ],
      "policyfile": "/var/cfengine/inputs/lib/cfe_internal_hub.cf",
      "promisees": [],
      "promisehandle": "cfe_internal_postgresql_maintenance_commands_run_vacuumdb",
      "promiser": "/var/cfengine/bin/vacuumdb --analyze --quiet --dbname=cfdb",
      "promisetype": "commands",
      "stackpath": "/default/cfe_internal_management/methods/'CFEngine_Internals'/default/cfe_internal_enterprise_main/methods/'hub'/default/cfe_internal_postgresql_vacuum/commands/'/var/cfengine/bin/vacuumdb --analyze --quiet --dbname=cfdb'[0]"
    }
  ],
  "total": 1,
  "next": null,
  "previous": null
}
```
