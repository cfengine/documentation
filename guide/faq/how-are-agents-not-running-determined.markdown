---
layout: default
title: How are agents not running determined?
published: true
sorting: 90
tags: [getting started, faq, health, enterprise]
---

Hosts who's last agent execution status is "FAIL" will show up under "Agents not
running". A hosts last agent execution status is set to "FAIL" when the hub
notices that there are no promise results within 3x of the expected agent run
interval. The agents average run interval is computed by a geometric average
based on the 4 most recent agent executions.

You can inspect hosts last execution time, execution status (from the hubs
perspective), and average run interval using the following SQL.

```sql
SELECT Hosts.HostName AS "Host name",
AgentStatus.LastAgentLocalExecutionTimeStamp AS "Last agent local execution
time", cast(AgentStatus.AgentExecutionInterval AS integer) AS "Agent execution
interval", AgentStatus.LastAgentExecutionStatus AS "Last agent execution status"
FROM AgentStatus INNER JOIN Hosts ON Hosts.HostKey = AgentStatus.HostKey
```

This can be queried over the API most easily by placing the query into a json
file. And then using the `query` API.

`agent_execution_time_interval_status.query.json`:

```
{
  "query": "SELECT Hosts.HostName, AgentStatus.LastAgentLocalExecutionTimeStamp, cast(AgentStatus.AgentExecutionInterval AS integer), AgentStatus.LastAgentExecutionStatus FROM AgentStatus INNER JOIN Hosts ON Hosts.HostKey = AgentStatus.HostKey"
}
```

```console
$ curl -s -u admin:admin http://hub/api/query -X POST -d @agent_execution_time_interval_status.query.json | jq ".data[0].rows"
[
  [
    "hub",
    "2016-07-25 16:53:23+00",
    "296",
    "OK"
  ],
  [
    "host001",
    "2016-07-25 16:06:50+00",
    "305",
    "FAIL"
  ]
]
```

**See Also**: `Enterprise API Reference`, `Enterprise API Examples`, `How are hosts not reporting determined?`
