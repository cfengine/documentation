---
layout: default
title: Glossary
sorting: 50
aliases:
  - "/overview-glossary.html"
---

#### Agent

A piece of software that runs independently and automatically to carry out a task (think software robot).
In CFEngine, the agent is called `cf-agent` and is responsible for making changes to computers.

Historically, all the hosts in the infrastructure which are not hubs / policy servers have been referred to as agents.
The preferred terms to distinguish between the different roles are hub and client.
See CFEngine roles.

#### Body

A promise body is the description of exactly what is promised (as opposed to what/who is making the promise).
The term `body` is used in the CFEngine syntax to mean a small template that can be used to contribute as part of a larger promise body.

#### Bootstrap

After installing the CFEngine package, the software does not automatically start running.
It is missing some information, most notably where it should be fetching policy from.
In order to start CFEngine, you run the bootstrap command on all hosts in the infrastructure, with the IP address of the hub as an argument:

```command
cf-agent --bootstrap <hub IP>
```

After running this command, CFEngine knows where (which IP address) to use when fetching policy.
It can also infer its CFEngine role (hubs fetch policy from themselves, while clients fetch policy from a hub).
Having this information, CFEngine can start the various components in the background, ensuring that policy is fetched, enforced, and reported regularly, every 5 minutes by default.

#### Bundle

In CFEngine, a bundle refers to a collection of promises that has a name.

#### Contend driven policy (CDP)

A way of simplifying the way users provide information to CFEngine about policy by hiding the overhead of policy coding.
A CDP is a set of promises designed to solve a particular task in a standard way.
Users provide only a little data in the form of a simple spreadsheet of data in a table.

#### CFEngine

CFEngine comes from a contraction of _ConFiguration Engine_ and is maintained by Northern.tech (previously the CFEngine company).

#### CFEngine 3.x

Major version 3 of the CFEngine software was initiated in 2008 and is maintained to the present day.
It comes in both Enterprise and Open Source Community editions.

#### CFEngine Community

Free and Open Source edition of the CFEngine software, published under the GPL3 license, and optionally under the COSL license.

#### CFEngine Enterprise

Refers to commercial (paid) editions of the CFEngine software.

#### CFEngine Nova

An older name for CFEngine Enterprise, which is no longer used.
See CFEngine Enterprise.

#### CFEngine role

As far as CFEngine is concerned, all hosts in your infrastructure can be thought of as having one of two possible roles.
The CFEngine role describes how a specific host interacts with other installations of CFEngine on other hosts.

The hub is the centralized place which serves policy and collects reports.
When starting out / for smaller infrastructures, it is common to have just 1 hub.
For larger / more complex infrastructures, multiple hubs are common.
Due to the multiple purposes this host serves, it is sometimes referred to as the policy server or the report collector, however _hub_ is the preferred term.

Clients are all the other hosts which fetch policy from the hub and deliver reporting data back.
In a typical setup, all hosts which are not hubs are considered clients.
Historically, clients were sometimes referred to as agents, however this can be confusing, as agent also refers to the software component `cf-agent` which is installed on all hosts, not just the clients.

Hub and client are the preferred terms when talking about the role a host performs, and which type of package to install on it.
See hub and client.

#### Changelog

A file used to describe the changes made since the last version of the software.

#### Class

Classes are used to classify a system (or the state of it) and to make decisions in CFEngine policy.
Classes are sometimes referred to as contexts.

#### Class expressions

Multiple classes separated by operators (and, or) to make more complex decisions.

#### Class guards

Used to restrict when / where promises are evaluated.
Appear in front of promises in CFEngine policy, consisting of a class expression followed by two colons.
Class guards are sometimes called context class expressions.

#### Client

In traditional computer networks and software, the client is the program which connects to a server, i.e., the software which initiates the connection in a networked system.
We say that a server is listening for incoming connections, and servers frequently serve thousands or even millions of clients simultaneously.

In CFEngine, we use the word client to describe all of the hosts which are not hubs.
A CFEngine hub runs a policy server, which all clients connect to in order to fetch policy.

Historically, the term agent has sometimes been used for this same meaning.
However, agent also refers to the agent component (the `cf-agent` binary), and thus, when discussing the role of a CFEngine host, _client_ is the preferred term for these hosts which are not hubs, and which packages to install on them.

#### Client initiated reporting

A mode where you change the configuration so that the hub does not initiate connections to client hosts to fetch reports.
Instead, the clients will establish a connection, and leave it open, until the hub is ready to use it to query for reporting data.
Sometimes referred to as call collect.

#### Configuration management database (CMDB)

A term coined as part of the IT Infrastructure Library (ITIL) as an outgrowth of an inventory database.

#### Code branch

The development of software is a branching process.
At certain times, the software code splits into different versions following different paths.
Each path needs to be maintained separately for a while.
This often happens when a release is made, because one wants to freeze the development of a public release (allowing only for some minor bug fixes), while continuing to add features to a branch leading to future versions.

#### Components

The programs (binaries) installed with CFEngine are referred to as components of CFEngine.
These include: `cf-agent`, `cf-promises`, `cf-runagent`, `cf-hub`, `cf-execd`, `cf-monitord`, and `cf-serverd`.
The "d" in the last 3, is a common acronym for daemon - long-running backgrounded programs.

#### COSL license

The Commercial Open Source License used for the CFEngine.

#### Datatypes

CFEngine's data types describe what a variable can contain.
A variable can't be assigned a different type once it's been set.
The commonly used data types are `string`, `slist` (string list), `int`, `real`, and `data`.

#### Diff

A `diff` is a report (originally that generated by the UNIX diff command) that details the differences between two files.
The term is often used as slang meaning a file comparison.

#### Enterprise API

The Enterprise API is a JSON HTTP REST API, allowing users to access CFEngine's functionality and reporting data programmatically.
It can be used to generate reports, query data, create alerts, manage users, etc.

#### Enterprise reporting

CFEngine's reporting system allows you to access information about your hosts and the results of your policy in a centralized system.
You can access the reporting system through the hub's JSON REST API, the Web UI, the SQL database, and generated PDF / CSV reports.

#### GPL3

The GNU Public License, version 3.

#### Graphical user interface (GUI)

In contrast to text / command-line-based interfaces, GUIs use icons, images, color, spacing, and more complex layouts to improve the user experience.

The CFEngine GUI is called Mission Portal and is accessible via a web browser.
It shows you useful information about your infrastructure and provides easy ways to make changes.

#### Host

UNIX terminology for a computer the runs _guest programs_.
In practice, _host_ is a synonym for _computer_.

In CFEngine, all machines (physical or virtual) which have an installation of CFEngine are considered _hosts_.
We split them into 2 roles (categories) - hubs and clients.

#### Hub

The term hub means the center of a wheel, from which multiple spokes emerge.

In CFEngine, the hub is the host responsible for collecting reports from hosts and serving them policy.
In addition to the components installed on other CFEngine hosts (clients), the hub runs a database (PostgreSQL), a web server (Apache) and a few additional CFEngine components, most notably `cf-hub`, which connects to hosts and retrieves their reporting data.

Due to the multiple purposes this host serves, it is sometimes referred to as the policy server, the reporting hub, or the report collector.
In typical CFEngine Enterprise setups, all hubs are policy servers, and all policy servers are hubs, so the distinction is not so important.
In general, hub is the preferred term to describe the role of what this host does, and which package to install on it.

See CFEngine role.

#### Lightweight directory access protocol (LDAP)

A kind of _phone book_ service providing information about persons and computers in an organization.

#### Libraries

A library generally refers to a collection of standardized CFEngine code that can be reused in different scenarios and environments.
This might be reusable bundles of promises, or bodies.

#### Logs

Log files tell you some historical, usually timestamped, information about events that happened in the past.
In CFEngine, there are a few notable log files:

- `/var/logs/CFEngineInstall.log` - Information about the installation, especially useful if installing the package failed.
- `/var/cfengine/outputs/` - Output logs of previous scheduled agent runs (if any).
- `/var/cfengine/httpd/logs/error_log` - Apache errors (Mission Portal / API)

#### Mission Portal (MP)

Name of the user interface used in commercial CFEngine editions, where all reports and progress summaries are kept.

#### Namespaces

Namespaces allow you to define new scopes for bundles, variables, and classes.
By using a specific name for the namespace, you can use short and generic names for the identifiers inside of it.

By default, if you don't specify a namespace, you are using the namespace called `default`.
The CMDB (group data / host-specific data in Mission Portal) uses the `data` namespace unless you specify a namespace.

You can think of namespaces in a similar way as putting files inside folders, instead of having all of your files in one folder.
The result is that things are more organized and less chances of files / classes / variables / bundles having conflicting names.

#### Normal ordering

In CFEngine, the promises you write in policy files are evaluated according to a predetermined order, not from top to bottom of your policy file.

**See also:** [Policy evaluation][Policy evaluation]

#### Packages

Software binaries or executable files.
The CFEngine company compiles and tests software into packages suitable for different platforms.

#### PCI compliance

Payment Card Industry Data Security Standard (PCI DSS) is a set of requirements designed to ensure that ALL companies that process, store or transmit credit card information maintain a secure environment.

#### Platforms

This usually refers to an operating system type, e.g., Linux (in its many flavors), Windows, etc.
Platforms are described using short identifiers, e.g., RHEL 8, SuSE 11, SLES, etc.

#### Policy

In CFEngine, code describes the desired state of a system, and we refer to this code as _policy_.
The CFEngine components, most prominently `cf-agent`, evaluate this policy and make changes to the system to bring it closer to the desired state.
Policy mainly consists of promises (rules) about the system, organized into bundles.

Never pluralize or _count_ policy - terms like _policy set_, and _policy file_ should be preferred over the ambiguous _policies_, _one policy_, and similar.
Refering to policy in a generic, uncountable way, is still correct: "Policy style guide", "Writing policy", "All policy should be written in utf-8" are all good uses.
This is similar to the term _code_ in programming - "writing code" is normal and clear, but "one code" is not (one line of code? one function? one file?).

#### Policy file

A file with `.cf` extension, written in CFEngine policy language, which `cf-agent` and the other components parse and evaluate.

#### Policy language

Another name for CFEngine policy language, the programming language you write to express promises as code.

#### Policy server

The special server that others consult for the latest policy is called the _policy server_.
Typically the policy server is set by the bootstrapping process.

#### Policy set

A collection of policy files inside a folder hierarchy.
The policy set is typically deployed to a policy server's `/var/cfengine/masterfiles` directory, and then distributed to the `/var/cfengine/inputs` on each host, where it is run.
The `cfbs build` command converts a CFEngine Build project into a ready-to-deploy policy set.

#### Promise attributes

As opposed to the promiser string (which is usually the unique identifier of a resource), promise attributes specify the desired specifics for that resource.
A basic example is that if you want to ensure a file has a specific set of permissions, you would make a promise where the promiser string is the filename, and the desired permissions are specified as attributes.

Sometimes referred to as promise constraints.

#### Promise

The CFEngine software manages every intended system outcome as "promises" to be kept.
A CFEngine promise corresponds roughly to a rule in other software products, but importantly promises are always things that can be kept and repaired continuously, on a real time basis, not just once at install-time.

Promises are idempotent, meaning they can be executed many times with the same outcome.

They are also convergent, meaning they can only nudge the system closer to a steady state, never destabilize it.
While there are ways a user could override this, it's almost never a good idea to do so.

#### Promise types

Different types of resources you can manage with CFEngine.
Typical examples include files, users, services, packages, etc.
Making promises with these types results in CFEngine checking the state of those resources and making changes to the system if necessary.

There are also promise types which are not traditional resources on a system, but rather just for managing state within the CFEngine binaries, such as variables, classes, meta, etc.
Setting a class or a variable will not alter the system directly, but makes that information available for further policy and promise types in the same execution.

#### Role based access control (RBAC)

RBAC allows you to control the level of access granted to individuals at a granular level.
Each user can have one or more roles, and each role can grant them access to specific resources and actions.
A flexible RBAC system improves the security of the system, especially when combined with a principle of least privilege approach.

#### Server

For historical reasons, certain computers are referred to as servers, especially when kept in data centers because such computers often run services.

In CFEngine, `cf-serverd` is a software component that serves files from one computer to another.
All computers are recommended to run `cf-serverd`, making all computers CFEngine servers, whether they are laptops, phones, or data center computers.

The special server that others consult for the latest policy is called the policy server.

#### Service catalogue

A kind of directory of _services_ provided in an environment.
The concept of a service could be anything from a human help desk to a machine-controlled email subsystem.
In the CFEngine Mission Portal, the service catalog (for maintenance) treats promise bundles of promises as low-level maintenance services and relates these to high-level business goals.

#### SOX compliance

Sarbanes-Oxley Act compliance.
An audited accolade for financial data security required by all companies on the New York Stock Exchange.

#### Standard library

The standard library lives in a `masterfiles/lib` subdirectory.
It's a collection of useful bundles and bodies you can use.

#### Template

A template usually refers to text that can be expanded based on the current CFEngine context.
CFEngine has a native template language, but generally, `mustache`, a logic-less templating language, is preferred.
Sometimes a template is an incomplete piece of CFEngine code, with blanks to fill in.
It is often a policy fragment that can be reused in different scenarios.
This is often used interchangeably with the term _library_.

#### Variables

Variables have a name, a type, and a value (and some optional metadata).
In CFEngine policy language, variables are similar to variables in other programming languages, they can hold strings, lists, complex data structures, etc.
