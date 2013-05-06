## CFEngine Components

CFEngine is comprised of a number of components: components
responsible for implementing promises, components responsible for
organizing large networks of agents, and other components responsible
for provide the infrastructure of CFEngine. This chapter provides an
overview of these components.

### Core Components

CFEngine's software agents are independent components running on the
various systems that make up your infrastructure. These independent
daemons communicate with one another as shown in the following figure
using a protocol that allows each node to distribute promises, act
upon them, and report status to a central server.

Unlike other approaches to automation, CFEngine does not rely on SSH
key authentication and configuring trust, the communication between
nodes is very structured and also able to react to availability
issues. This means that you don't have to arrange risk login
credentials to get CFEngine to work, and if large portions of your
network stop working individual nodes in the CFEngine system
understand how to keep on running and delivering promises.

![](fig/components-overview.png)

If the network is not working, CFEngine agents skip new promises and
continue with what they already have. CFEngine was specifically
designed to support systems with intermittent connectivty issues and
where the reliability of the network may be in question. CFEngine is
fault tolerant and opportunistic.

* cf-promises - The promise verifier and compiler. This is used to run a "pre-check" of configuration promises before attempting to execute.

* cf-agent - This is the instigator of change. Everything that happens on a client machine happens becuase of cf-agent. The agent is the part of CFEngine that manipulates system resources.

* cf-serverd - The server is able to share files and receive requests to execute existing policy on an individual machine. It is not possible to send (push) new information to CFEngine from outside. 

* cf-execd - This is a scheduling daemon (which can either supplement or replace cron). It also works as a wrapper, executing and collecting the output of cf-agent and E-mailing it if necessary to a system account.

* cf-runagent - This is a helper program that can talk to cf-serverd and request that it execute cf-agent with its existing policy. It can thus be used to simulate a push of changes to CFEngine hosts, if their policy includes that they check for updates.
 
* cf-report - This generates summary and other reports in a variety of formats for export or integration with other systems.

* cf-know - This agent can generate an ISO standard Topic Map from a number of promises about system knowledge. It is used for rendering documentation as a 'semantic web'.

### CFEngine Architecture

CFEngine operates autonomously in a network, under your guidance.
While CFEngine supports anything from 1-2 servers to 100,000+ servers,
the essence of any CFEngine deployment is the same. There are four
commonly cited phases in managing systems with CFEngine: Build,
Deploy, Manage, and Audit.

CFEngine supports networks of any size, from a handful of nodes to
hundreds of thousands of computers. It is built to scale. If your site
is very large (thousands or of servers) you should spend some time
discussing your requirements with the CFEngine experts. They will know
how to tune promises and configurations to your environment as scale
requires you to have more infrastructure, and a potentially more
complicated configuration.

These separate phases originate with a model of system management
based on transactional changes. CFEngine's conception of management is
somewhat different, as transaction processing is not a good model for
system management, but we can use this template to see how CFEngine
works differently.

Build::
    A system is based on a number of decisions and resources that need to be `built' before they can be implemented. You don't need to decide every detail, just enough to build trust and predictability into your system. In CFEngine, what you build is a template of proposed promises for the machines being managed.  If the machines in a system all make and keep these promises, the system will function seamlessly as planned.

* Deploy - Deploying really means implementing the policy that was already decided. In transaction systems, one tries to push out changes one-by-one, hence `deploying' the decision. In CFEngine you simply publish your policy (in CFEngine parlance these are `promise proposals') and the machines see the new proposals and can adjust accordingly. Each machine runs an agent that is capable of implementing policies and maintaining them over time without further assistance. 

* Manage - Once a decision is made, unplanned events will occur. Such incidents traditionally set off alarms and humans rush to make new transactions to repair them.  In CFEngine, the autonomous agent manages the system, and you only have to deal with rare events that cannot be dealt with automatically.  This is the key difference of CFEngine, a focus on autonomy and creating agents that are smart enough to adapt to changing situations.

* Audit - In traditional configuration systems, the outcome is far from clear after a one-shot transaction, so one audits the system to determine what actually happened. In CFEngine, changes are not just initiated once, but locally audited and maintained. Decision outcomes are assured by design in CFEngine and maintained automatically, so the main worry is managing conflicting. Users can sit back and examine regular reports of compliance generated by the agents, without having to arrange for new transactions to roll-out changes.

You should not think of CFEngine as a roll-out system, i.e. one that attempts to force out absolute changes and perhaps reverse them in case of error. Roll-out and roll-back are theoretically flawed concepts that only sometimes work in practice. With CFEngine, you publish a sequence of policy revisions, always moving forward (because like it or not, time only goes in one direction). All of the desired-state changes are managed locally by each individual computer, and continuously repaired to ensure on-going compliance with policy.

### Policy Decision Flow

CFEngine does not make absolute choices for you, like other tools.  Almost everything about its behavior is matter of policy and can be changed. However, a structure for use, like the following, is recommended (see the following figure).

In order to keep operations as simple as possible, CFEngine maintains a private working directory on each machine referred to in documentation as WORKDIR and in policy by the variable $(sys.workdir). By default, this is located at /var/cfengine or C:\var\CFEngine. It contains everything CFEngine needs to run.

The figure below shows how decisions flow through the parts of a system.

* It makes sense to have a single point of coordination. Decisions are therefore usually made in a single location (the Policy Definition Point). The history of decisions and changes can be tracked by a version control system of your choice (e.g. Subversion, CVS, etc.).

* Decisions are made by editing CFEngine's policy file promises.cf (or one of its included sub-files). This process is carried out off-line.

* Once decisions have been formalized and coded, this new policy is copied manually (a human decision) to a decision distribution point, which by default is located in the directory /var/cfengine/masterfiles
on all policy distribution servers. 

In this introduction, we shall assume that there is only one central policy distribution server, a specially-appointed server which is referred to simple as the policy server.

* Every client machine contacts the policy server and downloads these updates. The policy server can be replicated if the number of clients is very large, but we shall assume here that there is only one policy server.

Once a client machine has a copy of the policy, it extracts only those promise proposals that are relevant to it, and implements any changes without human assistance. This is how CFEngine manages change.

CFEngine tries to minimize dependencies by decoupling processes. By following this pull-based architecture, CFEngine will tolerate network outages and will recover from deployment errors easily. By placing the burden of responsibility for decision at the top, and for implementation at the bottom, we avoid needless fragility and keep two independent quality assurance processes apart.
