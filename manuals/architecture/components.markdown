---
layout: default
title: CFEngine Components
categories: [Manuals, Architecture, Components]
published: true
alias: manuals-architecture-components.html
tags: [manuals, systems, configuration management, automation, components, cf-agent, directory]
---

Previous: [Automation with CFEngine](manuals-architecture-automation.html)

****

There are a number of components in CFEngine, with each component performing a 
unique function: components responsible for implementing promises, components 
responsible for organizing large networks of agents, and other components 
responsible for providing the infrastructure of CFEngine.

These components form the basis of automation with CFEngine. They are 
independent software agents running on the various systems that make up your 
infrastructure. They communicate with one  another as shown in the following 
figure, using a protocol that allows each  host to distribute promises, act 
upon them, and report status to a central server.

![Components overview](components-overview.png)

Unlike other approaches to automation, CFEngine does not rely on SSH key 
authentication and configuring trust, the communication between hosts is very 
structured and also able to react to availability issues. This means that you 
don't have to arrange risk login credentials to get CFEngine to work. If large 
portions of your network stop working, individual host in the CFEngine system
understand how to keep on running and delivering promises.

If the network is not working, CFEngine agents skip new promises and continue 
with what they already have. CFEngine was specifically designed be resilient 
against connectivity issues network failure may be in question. CFEngine is
fault tolerant and opportunistic.


### Core Components

The CFEngine application is fully contained within the `/var/cfengine` 
directory tree. `/var/cfengine/bin` consists of the CFEngine software 
components:

* [cf-agent](reference-components-cfagent.html)

This is the instigator of change. Everything that happens on a client machine 
happens because of cf-agent. The agent is the part of CFEngine that 
manipulates system resources.

`cf-agent`'s only contact with the network is via remote copy requests. It 
does not and cannot grant any access to a system from the network. It is only 
able request access to files from the server component.

* [cf-serverd](reference-components-cfserverd.html)

By starting this daemon you can set up a line of communication between hosts.
The server is able to share files and receive requests to execute existing 
policy on an individual machine. It is not possible to send (push) new 
information to CFEngine from outside.

This daemon authenticates requests from the network and processes them 
according to rules specified in the
[server control body](reference-components-cfserverd-control-promises.html) 
and server bundles containing
[access promises](reference-components-cfserverd-bundles-for-server.html).

* [cf-execd](reference-components-cfexecd.html)

This is a scheduling daemon (which can either supplement or replace cron). It 
also works as a wrapper, executing and collecting the output of `cf-agent` and 
E-mailing it if necessary to a system account.

* [cf-promises](reference-components-cfpromises.html)

The promise verifier and compiler. This is used to run a "pre-check" of 
configuration promises before attempting to execute.

* [cf-runagent](reference-components-cfrunagent.html)

A helper program which can be used to run `cf-agent` on a number of remote 
hosts. It cannot be used to tell `cf-agent` what to do, it can only ask 
`cf-serverd` on the remote host to run the `cf-agent` with its existing 
policy. It can thus be used to trigger an immediate deployment of new policy, 
if their existing policy includes that they check for updates.

Privileges can be granted to users to provide a kind of Role Based Access 
Control (RBAC) to certain parts of the existing policy.


The `/var/cfengine/lib` directory stores shared objects and dependencies that 
are in the bundled packages.

### Policy files

* `/var/cfengine/masterfiles`

Policy repository which grants access to local or bootstrapped CFEngine 
clients when they need to update their policies. Policies obtained from 
`/var/cfengine/masterfiles` are then cached in `/var/cfengine/inputs` for 
local policy execution. The `cf-agent` executable does not execute policies 
directly from this repository. 

* `/var/cfengine/inputs`

Cached policy repository located on a CFEngine client. The `cf-agent` 
executable executes policies from this repository.

* `/var/cfengine/modules`

**TODO**

### Output Directories

* `/var/cfengine/outputs`

Directory where `cf-agent` creates its output files.

* `/var/cfengine/reports`

Directory used to store reports. **TODO: still there without cf-report?**

* `/var/cfengine/ppkeys`

Directory used to store encrypted public/private keys for CFEngine
client/server network communications.

* `/var/cfengine/state`

**TODO: what's there?**

* `/var/cfengine/lastseen`

**TODO**


* `/var/cfengine/share`

**TODO**


****

Next: [Workflows](manuals-architecture-workflows.html)
