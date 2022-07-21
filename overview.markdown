---
layout: default
title: Overview
published: true
sorting: 10
---

CFEngine is a distributed system for managing and monitoring computers across an IT network. Machines on the network that have CFEngine installed, and have registered themselves with a policy server (see [Installation and Configuration][Installation and Configuration]), will each be running a set of CFEngine component applications that manage and interpret textual files called policies. Policy files themselves contain sets of instructions to ensure machines on the network are in full compliance with a defined state. At the atomic level are sets, or *bundles*, of what are known in the CFEngine world as [Promises][Promises]. *Promises* are at the heart of Promise Theory, which is in turn what CFEngine is all about.

## Policy Language and Compliance ##

For many users, CFEngine is simply a configuration tool – i.e. software for deploying and patching systems according to a policy. Policy is described using promises. Every statement in CFEngine 3 is a promise to be kept at some time or location. More than this, however, CFEngine is not like other automation tools that "roll out" an image of some software once and hope for the best. Every promise that you make in CFEngine is continuously verified and maintained. It is not a one-off operation, but a self-repairing process should anything deviate from the policy.

CFEngine ensures that the actual state of a system is in compliance with the predefined model of desired state for the system. If it is not in compliance CFEngine will bring it into compliance.  This is known as *convergence*.

That model is represented by one or more policies that have been written using the declarative CFEngine policy language. The policy language has been designed with a vocabulary that is intuitive, yet at the same time can still support the design of highly complex IT systems.

Those policies are distributed across all hosts within the system via download from the policy server. Every host will then interpret and execute each of the instructions it has been given in a predetermined order.

CFEngine continually monitors all of the hosts in real-time, and should the system’s current state begin to drift away from the intended state then CFEngine will automatically take corrective action to bring everything back into compliance.

See Also: [Language Concepts][], [Writing and Serving Policy][]

## CFEngine Policy Servers and Hosts ##

There are basically two categories of machines in a CFEngine environment: policy servers and their client hosts. Policy servers are responsible for making policy files available to each of the client hosts that have registered with it (a.k.a. bootstrapped), including itself. Hosts on the other hand are responsible for ensuring they continuously pull in the latest policies, or changes to policies, from the policy server. They are additionally responsible for ensuring they remain fully compliant with the instructions contained within the policy files, at all times.

The role of a particular machine where CFEngine is deployed determines which of the components will be installed and running at any given moment.

See Also: [Writing and Serving Policy][]

## CFEngine Component Applications and Daemons ##

There are a number of components in CFEngine, with each component performing a
unique function: components responsible for implementing promises, components
responsible for organizing large networks of agents, and other components
responsible for providing the infrastructure of CFEngine.

These components form the basis of automation with CFEngine. They are
independent software agents running on the various systems that make up your
infrastructure. They communicate with one another as shown in the following
figure, using a protocol that allows each host to distribute promises, act
upon them, and report status to a central server.

All CFEngine software components exist in `/var/cfengine/bin`.

![Components overview](components-overview.png)

* [Daemons][Overview#Daemons]
* [Other Applications][Overview#Other Component Applications]

### Daemons ###

All machines, whether they are policy servers or hosts, will have these three important daemons running at all times:

* [/var/cfengine/bin/cf-execd][Overview#cf-execd]
* [/var/cfengine/bin/cf-serverd][Overview#cf-serverd]
* [/var/cfengine/bin/cf-monitord][Overview#cf-monitord]

#### cf-execd ####

`cf-execd` is the scheduling daemon for `cf-agent`, similar to cron. It executes and collects the output of `cf-agent` and
e-mails any output to the configured e-mail address.

`cf-execd` runs `cf-agent` locally according to a schedule specified in policy code (executor control body). After a `cf-agent` run is completed, `cf-execd` gathers output from `cf-agent`, and may be configured to email the output to a specified address. It may also be configured to `splay` (randomize) the execution schedule to prevent synchronized `cf-agent` runs across a network.

`cf-execd` keeps the promises made in common bundles, and is affected by common and executor control bodies.

See also: [cf-execd][cf-execd] reference documentation.

#### cf-serverd ####

`cf-serverd` is a socket listening daemon providing two services: it acts as a file server for remote file copying and it allows an authorized `cf-runagent` to start a `cf-agent` run. `cf-agent` typically connects to a `cf-serverd` instance to request updated policy code, but may also request additional files for download. `cf-serverd` employs role based access control (defined in policy code) to authorize requests.

`cf-serverd` keeps the promises made in `common` and `server` bundles, and is affected by `common` and `server` control bodies.

By starting this daemon you can set up a line of communication between hosts.
The server is able to share files and receive requests to execute existing
policy on an individual machine. It is not possible to send (push) new
information to CFEngine from outside.

This daemon authenticates requests from the network and processes them
according to rules specified in the
[server control body][cf-serverd#Control Promises] and server bundles
containing [access promises][access].

See also: [cf-serverd][cf-serverd] reference documentation.

#### cf-monitord ####

`cf-monitord` is the monitoring daemon for CFEngine. It samples probes defined in policy using measurements type promises and attempts to learn the normal system state based on current and past observations. Current estimates are made available as special variables (e.g. $(mon.av_cpu)) to `cf-agent`, which may use them to inform policy decisions.

`cf-monitord` keeps the promises made in `common` and `monitor` bundles, and is affected by `common` and `monitor` control bodies.

See also: [cf-monitord][cf-monitord] reference documentation.

### Other Component Applications ###

* [/var/cfengine/bin/cf-agent][Overview#cf-agent]
* [/var/cfengine/bin/cf-key][Overview#cf-key]
* [/var/cfengine/bin/cf-promises][Overview#cf-promises]
* [/var/cfengine/bin/cf-runagent][Overview#cf-runagent]

#### cf-agent ####

`cf-agent` evaluates policy code and makes changes to the system. Policy bundles are evaluated in the order of the provided `bundlesequence` (this is normally specified in the common control body and defaults to just the `main` bundle if unspecified). For each bundle, cf-agent groups promise statements according to their type. Promise types are then evaluated in a preset order to ensure fast system convergence to policy.

`cf-agent` keeps the promises made in `common` and `agent` bundles, and is affected by `common` and `agent` control bodies.

`cf-agent` is the instigator of change. Everything that happens on a client machine
happens because of `cf-agent`. The agent is the part of CFEngine that
manipulates system resources.

`cf-agent`'s only contact with the network is via remote copy requests. It
does not and cannot grant any access to a system from the network. It is only
able to request access to files from the server component.

See also: [cf-agent][cf-agent] reference documentation.

#### cf-key ####

The CFEngine key generator makes key pairs for remote authentication.

See also: [cf-key][cf-key] reference documentation.

#### cf-promises ####

`cf-promises` is CFEngine's promise verifier. It is used to run a "pre-check" of
policy code before `cf-agent` attempts to execute.

`cf-promises` operates by first parsing policy code checking for syntax errors. Second, it validates the integrity of policy consisting of multiple files. Third, it checks for semantic errors, e.g. specific attribute set rules. Finally, `cf-promises` attempts to expose errors by partially evaluating the policy, resolving as many variable and classes promise statements as possible. At no point does `cf-promises` make any changes to the system.

In 3.6.0 and later, `cf-promises` will not evaluate function calls either. This may affect customers who use execresult for instance. Use the new --eval-functions yes command-line option (default is no) to retain the old behavior from 3.5.x and earlier.

See also: [cf-promises][cf-promises] reference documentation.

#### cf-runagent ####

`cf-runagent` is a helper program that can be used to run `cf-agent` on a number of remote
hosts. It cannot be used to tell `cf-agent` what to do, it can only ask
`cf-serverd` on the remote host to run the `cf-agent` with its existing
policy. It can thus be used to trigger an immediate deployment of new policy,
if their existing policy includes that they check for updates.

Privileges can be granted to users to provide a kind of Role Based Access
Control (RBAC) to certain parts of the existing policy.

`cf-runagent` connects to a list of running instances of `cf-serverd`. It allows foregoing the usual `cf-execd` schedule to activate `cf-agent`. Additionally, a user may send classes to be defined on the remote host. Two kinds of classes may be sent: classes to decide on which hosts `cf-agent` will be started, and classes that the user requests `cf-agent` should define on execution. The latter type is regulated by `cf-serverd`'s role based access control.

See also: [cf-runagent][cf-runagent] reference documentation.
