---
layout: default
title: CFEngine Architecture and Design
published: true
sorting: 10
tags: [overviews, system, configuration management, automation, architecture, design, promises]
---

CFEngine operates autonomously in a network, under your guidance. While
CFEngine supports anything from 1 servers to 100,000+ servers, the essence of
any CFEngine deployment is the same.

CFEngine supports networks of any size, from a handful of nodes to
hundreds of thousands of computers. It is built to scale. If your site
is very large (many thousands of servers) you should spend some time
discussing your requirements with CFEngine experts. They will know
how to tune promises and configurations to your environment as scale
requires you to have more infrastructure, and a potentially more
complicated configuration. No matter the scale, the essence of any
CFEngine deployment is the same, but with great power comes great
responsibility (a.k.a. don't break things before the weekend, on the
weekend, or in fact on any other day).

CFEngine was designed to enable scalable configuration management in
any kind of environment, with an emphasis on supporting large, Unix-like
systems that are connected via TCP/IP.

CFEngine doesn't depend on or assume the presence of reliable
infrastructure. It works opportunistically in any environment, using
the fewest possible resources, and it has a limited set of software
dependencies. It can run anywhere and this lean approach to
CFEngine's architecture makes it possible to support both traditional
server-based approaches to configuration as well as more novel
platforms for configuration including embedded and mobile systems.

CFEngine's design allows you to create fault-tolerant, available systems
which are independent of external requirements. CFEngine works in all
the places you think it should, and all the new places you haven't even
thought of yet.

## Managing Expectations with Promises

CFEngine works on a simple notion of **promises**. A promise is the
documentation of an intention to act or behave in some manner. When you make a
promise, it is an effort to improve trust. Trust is an economic time-saver. If
you can't trust you have to verify everything, and that is expensive.

Everything in CFEngine can be thought of as a promise to be kept by different
resources in the system. In a system that delivers a web site with Apache
`httpd`, an important promise may be to make sure that the `httpd` or `apache` package is installed,
running, and accessible on port 80. In a system which needs to satisfy mid-day
traffic on a busy web site, a promise may be to ensure that there are 200
application servers running during normal business hours.

These promises are not top-down directives for a central authority to push
through the system. A large organization can't run on top-down authority
alone. A group of people can't be managed without empowering and trusting them to
make independent decisions.

CFEngine is a system that emphasizes the promises a client makes to the
overall CFEngine network. They are the rules which clients are responsible for
implementing. We can create large systems of scale because we don't create a
bulky centralized authority. There should be no single point-of-failure when
managing machines and people.

Combining promises with patterns to describe where and when promises should
apply is what CFEngine is all about.

## Automation with CFEngine

Users are good at researching solutions and making design decisions, but awful
at repeated execution. Machines are pitiful at making decisions, but very good
at reliable implementation at very large scale. It makes sense to let each
side do the job that they are good at. With CFEngine, users make decisions and
write promises for machines to implement and satisfy.

A CFEngine user will declare a promise in CFEngine, and CFEngine will then
translate this promise into a series of actions to implement. For the most
part, CFEngine understands how to deliver on promises, and they don't need to
be given explicit instructions for completing tasks. It is your job to make
decisions about the systems you are managing and to describe those in suitable
promises. It is CFEngine's job to automate and deliver a promise.

CFEngine is a distributed solution that is completely independent of host
operating systems, network topology or system processes. You describe the
ideal state of a given system by creating promises and the CFEngine agents
ensures that the necessary steps are taken to achieve this state. Automation
in CFEngine is executed through a series of
[components][Overview#CFEngine Component Applications and Daemons] that run locally on hosts.

## Phases of System Management

There are four commonly cited phases in managing systems with CFEngine: Build,
Deploy, Manage, and Audit.

### Build

A system is based on a number of decisions and resources that need to be
`built' before they can be implemented. You don't need to decide every detail,
just enough to build trust and predictability into your system. In CFEngine,
what you build is a template of proposed promises for the machines being
managed.  If the machines in a system all make and keep these promises, the
system will function seamlessly as planned.

### Deploy

Deploying really means implementing the policy that was already decided. In
transaction systems, one tries to push out changes one-by-one, hence
`deploying' the decision. In CFEngine you simply publish your policy (in
CFEngine parlance these are "promise proposals") and the machines see the new
proposals and can adjust accordingly. Each machine runs an agent that is
capable of implementing policies and maintaining them over time without
further assistance.

### Manage

Once a decision is made, unplanned events will occur. Such incidents
traditionally set off alarms and humans rush to make new transactions to
repair them.  In CFEngine, the autonomous agent manages the system, and you
only have to deal with rare events that cannot be dealt with automatically.
This is the key difference of CFEngine, a focus on autonomy and creating
agents that are smart enough to adapt to changing situations.

### Audit

In traditional configuration systems, the outcome is far from clear after a
one-shot transaction, so one audits the system to determine what actually
happened. In CFEngine, changes are not just initiated once, but locally
audited and maintained. Decision outcomes are assured by design in CFEngine
and maintained automatically, so the main worry is managing conflicting. Users
can sit back and examine regular reports of compliance generated by the
agents, without having to arrange for new transactions to roll-out changes.

You should not think of CFEngine as a roll-out system, i.e. one that attempts
to force out absolute changes and perhaps reverse them in case of error.
Roll-out and roll-back are theoretically flawed concepts that only sometimes
work in practice. With CFEngine, you publish a sequence of policy revisions,
always moving forward (because like it or not, time only goes in one
direction). All of the desired-state changes are managed locally by each
individual host, and continuously repaired to ensure on-going compliance
with policy.

See Also: [Client server communication][Client server communication]
