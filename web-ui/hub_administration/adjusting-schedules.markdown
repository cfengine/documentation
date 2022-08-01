---
layout: default
title: Adjusting Schedules
published: true
tags: [cfengine enterprise, hub administration, scheduling, cf-execd, cf-agent, cf-hub]
---

## Set cf-execd agent execution schedule

By default `cf-execd` is configured to run `cf-agent` every 5 minutes. This can
be adjusted by tuning the [schedule][cf-execd#schedule] in `body executor
control`. In the [Masterfiles Policy Framework][Masterfiles Policy Framework] body
executor control can be found in `controls/cf_execd.cf`

## Set cf-hub hub_schedule

`cf-hub` the CFEngine Enterprise report collection component has a
[hub_schedule][cf-hub#hub_schedule] defined in `body hub control` which also
defaults to a 5 minute schedule. It can be adjusted to control how frequently
hosts should be collected from. In the
[Masterfiles Policy Framework][Masterfiles Policy Framework] `body hub control` can be
found in `controls/cf_hub.cf`

**Note:** Mission Portal has an "Unreachable host threshold" that defaults to 15
minutes. When a host has not been collected from within this window the host is
added to the "Hosts not reporting" report. When adjusting the `cf-hub`
`hub_schedule` consider adjusting the Unreachable host threshold proportionally.
For example, if you change the `hub_schedule` to execute only once every 15
minutes, then the Unreachable host threshold should be adjusted to 45 minutes
(2700 seconds).

### Set Unreachable host threshold via API

**Note:** This example uses [jq](https://stedolan.github.io/jq/) to filter API
results to only the relevant values. It is a 3rd party tool, and not shipped
with CFEngine.

Here we create a JSON payload with the new value for the Unreachable host
threshold (`blueHostHorizon`). We post the new settings and finally query the
API to validate the change in settings.

```console
[root@hub ~]# echo '{ "blueHostHorizon": 2700 }' > payload.json
[root@hub ~]# cat payload.json
{ "blueHostHorizon": 2700 }
[root@hub ~]# curl -u admin:admin http://localhost:80/api/settings -X POST -d @./payload.json
[root@hub ~]# curl -s -u admin:admin http://localhost:80/api/settings/ | jq '.data[0]|.blueHostHorizon'
2700
```
