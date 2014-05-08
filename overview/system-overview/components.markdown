---
layout: default
title: The CFEngine Components
published: true
sorting: 30
tags: [manuals, systems, configuration management, automation, components, cf-agent, directory]
---

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

### Core Components

The CFEngine software components exist in `/var/cfengine/bin`.

* [`cf-agent`][cf-agent]

This is the instigator of change. Everything that happens on a client machine 
happens because of cf-agent. The agent is the part of CFEngine that 
manipulates system resources.

`cf-agent`'s only contact with the network is via remote copy requests. It 
does not and cannot grant any access to a system from the network. It is only 
able request access to files from the server component.

* [`cf-serverd`][cf-serverd]

By starting this daemon you can set up a line of communication between hosts.
The server is able to share files and receive requests to execute existing 
policy on an individual machine. It is not possible to send (push) new 
information to CFEngine from outside.

This daemon authenticates requests from the network and processes them 
according to rules specified in the
[server control body][cf-serverd#Control Promises] and server bundles 
containing [access promises][access].

* [`cf-execd`][cf-execd]

This is a scheduling daemon for `cf-agent`, similar to cron.
It executes and collects the output of `cf-agent` and
e-mails any output to the configured e-mail address.

* [`cf-promises`][cf-promises]

The promise verifier and compiler. This is used to run a "pre-check" of 
configuration promises before attempting to execute.

* [`cf-runagent`][cf-runagent]

A helper program which can be used to run `cf-agent` on a number of remote 
hosts. It cannot be used to tell `cf-agent` what to do, it can only ask 
`cf-serverd` on the remote host to run the `cf-agent` with its existing 
policy. It can thus be used to trigger an immediate deployment of new policy, 
if their existing policy includes that they check for updates.

Privileges can be granted to users to provide a kind of Role Based Access 
Control (RBAC) to certain parts of the existing policy.




