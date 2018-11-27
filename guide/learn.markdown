---
layout: default
title: Learn
published: false
sorting: 10
---

## Why CFEngine?

<iframe width="560" height="315" src="https://www.youtube.com/embed/HLZ7EeqNdLs" frameborder="0" allowfullscreen></iframe>

Mark Burgess, Founder and author of CFEngine talks about the reasons CFEngine is a Configuration Management system for the decade.

## What Is CFEngine?

CFEngine is a software solution that helps system administrators and other
stakeholders in the IT organization become more agile and respond faster to
business requirements while ensuring SLAs and regulatory compliance, through
automation.

CFEngine allows users, in code using the domain specific language of CFEngine,
to define desired states of the IT infrastructure. Lightweight CFEngine agents
continuously ensures that the actual states are converging toward the desired
states, while reporting the outcome of each run. The solution is heavily
researched and built upon Promise Theory.

Written in C, CFEngine runs on multiple platforms and architectures, from the
smallest embedded devices, on servers, in the cloud to mainframes, easily
handling tens and hundreds of thousands of hosts.

The solution comes in a free open source Community Edition and paid commercial
Enterprise Edition.

Being a general purpose automation solution, CFEngine is used in a wide
variety of ways, from building servers, deploying and patching software to
configuration management tasks like scheduling, local user-management,
process-management, security hardening, inventory and compliance management.

Many DevOps organizations use CFEngine to ensure consistency across different
staging environments and automated application deployment. Due to its strong
security track-record CFEngine is widely used in heavily regulated industries
like financial services, telecom, health care and governmental agencies.

## How does CFEngine Work?

CFEngine is a fully distributed system that allows you to define desired states
of everything from very large-scale infrastructures to small devices. The
lightweight c-based cf-agent runs locally on each resource and persistently
tries to converge towards the defined desired state. The actual states of
managed resources are available in logs and an enterprise database for
compliance and easy reporting. Using CFEngine, can be described in the
following 3 simple steps.

1. Define Desired State

As an end-user you can either use the CFEngine Domain Specific Language (DSL) to
define desired states. CFEngine allows you to define a variety of states ranging
from process management to software deployment and file integrity. You can check
out CFEngine Promise Types to get an idea of the most common states you can
define.

Normally, all desired states are stored in ```.cf``` text-files in the
```/var/cfengine/masterfiles``` directory on one or more central distribution
points, referred to as CFEngine Policy Hubs.

2. Ensure Actual State

CFEngine typically runs locally on each managed resource. A resource can be
anything from a server, network switch, raspberry pi, or any other computational
device. `cf-agent`, the execution engine, is autonomous which means all the
evaluations occur on the local node.

Before each run, which by default is every 5 minutes, the agent tries to connect
to one of the Policy Hubs to check if there has been any policy updates. Upon
policy updates, `cf-agent` will download the latest policy to its own
```/var/cfengine/inputs``` directory, run a syntax check and upon success start
to execute.

3. Verify Actual State

Whenever the agent runs, it creates a log of local inventory, system states and
execution results. The logs are stored in ```/var/cfengine/outputs```. For
enterprise customers, all data is also stored in a local database. CFEngine also
stores a large number of asset information like software installed, CPU, memory,
disk, network activity, etc. As for execution results, CFEngine can have 3
states:

| Promise Result/Outcome | Description                             |
|------------------------|:----------------------------------------|
| Promise Kept           | Actual state was equal to Desired State |
| Promise Repaired       | Actual state was not equal to Desired State, but the agent was able to repair the state into compliance |
| Promise not Kept       | Actual state was not equal to Desired state and the agent was not able to restore into compliance |


Graphical illustration of CFEngine process
![Graphical illustration of high level workflow](learn_CFEngine-process-in-1-2-3_blocks_with_arrows.png)

End-user and CFEngine agents workflow
![End-User and CFEngine agent workflow](CFEngine-workflow-agents-and-users.png)

Thanks to the autonomous nature of CFEngine, systems will be continuously
maintained even if the Server is down. CFEngine agents on the hosts will
opportunistically try to connect to the server. If it fails, last successful
policy will apply, and since all evaluation is local, it doesn’t matter if the
characteristics of the host changes and needs to be reconfigured. CFEngine will
figure it out and ensure compliance. Did you know that CFEngine is used to
manage systems on submarines?

