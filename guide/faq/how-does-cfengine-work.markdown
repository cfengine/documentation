---
layout: default
title: How does CFEngine work?
published: true
sorting: 2
tags: [getting started, faq]
---

CFEngine is a fully distributed system that allows you to define desired states
of everything from very large-scale infrastructures to small devices. The
lightweight c-based cf-agent runs locally on each resource and persistently
tries to converge towards the defined desired state. The actual states of
managed resources are available in logs and an enterprise database for
compliance and easy reporting. Using CFEngine, can be described in the following
3 simple steps.

## 1. Define Desired State

As an end-user you can use the CFEngine Domain Specific Language (DSL) to define
desired states. CFEngine allows you to define a variety of states ranging from
process management to software deployment and file integrity. You can check out
CFEngine Promise Types to get an idea of the most common states you can define.

Normally, all desired states are stored in `.cf` text-files in the
`/var/cfengine/masterfiles` directory on one or more central distribution points,
referred to as CFEngine Policy Hubs.

## 2. Ensure Actual State

CFEngine typically runs locally on each managed resource. A resource can be
anything from a server, network switch, raspberry pi, or any other computational
device. CF-agent, the execution engine, is autonomous which means all the
evaluations occur on the local node.

Before each run, which by default is every 5 minutes, the agent tries to connect
to one of the Policy Hubs to check if there has been any policy updates. Upon
policy updates, cf-agent will download the latest policy to its own
`/var/cfengine/inputs` directory, run a syntax check and upon success start to
execute.

## 3. Verify Actual State

Whenever the agent runs, it creates a log of local inventory, system states and
execution results. The logs are stored in `/var/cfengine/outputs`. For enterprise
customers, all data is also stored in a local database. CFEngine also stores a
large number of asset information like software installed, CPU, memory, disk,
network activity, etc. As for execution results, CFEngine can have 3 states:

* **Promise Kept**: Actual state was equal to Desired State

* **Promise Repaired**: Actual state was not equal to Desired State, but the
agent was able to repair the state into compliance

* **Promise not Kept**: Actual state was not equal to Desired state and the
agent was not able to restore into compliance

{% comment %}Promises you cannot keep are no better than lies!
https://www.youtube.com/watch?v=Zd9-wdGzedU {% endcomment %}

## Graphical illustration of CFEngine process
￼
![Define -> Ensure -> Verify](how-does-cfengine-work-process.png)

End-user and CFEngine agents workflow

![Define -> Ensure -> Verify workflow](how-does-cfengine-work-agent-workflow.png)

Thanks to the autonomous nature of CFEngine, systems will be continuously
maintained even if the Server is down. CFEngine agents on the hosts will
opportunistically try to connect to the server. If it fails, last successful
policy will apply, and since all evaluation is local, it doesn’t matter if the
characteristics of the host changes and needs to be reconfigured. CFEngine will
figure it out and ensure compliance. CFEngine has been reported to run on many
different platforms in many different environments including traditional
servers, workstations and laptops, network gear (routers/switches), bus and tram
systems, point of sales systems, smart displays/signs, and even submarines.

