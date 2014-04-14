---
layout: default
title: Policy Workflow
published: true
sorting: 20
tags: [overviews, systems, configuration management, automation, workflow]
---

CFEngine does not make absolute choices for you, like other tools.  Almost 
everything about its behavior is matter of policy and can be changed.

In order to keep operations as simple as possible, CFEngine maintains a 
private [working directory][The CFEngine Components#The Working Directory] 
on each machine, referred to in documentation as `WORKDIR` and in policy by 
the variable `$(sys.workdir)`. By default, this is located at `/var/cfengine` 
or `C:\var\CFEngine`. It contains everything CFEngine needs to run.

The figure below shows how decisions flow through the parts of a system.

![Policy decision and distribution flowchart](policy-decision-flow.png)

* It makes sense to have a single point of coordination. Decisions are 
  therefore usually made in a single location (the Policy Definition Point). 
  The history of decisions and changes can be tracked by a version control 
  system of your choice (e.g. git, Subversion, CVS etc.).

* Decisions are made by editing CFEngine's policy file `promises.cf` (or one 
  of its included sub-files). This process is carried out off-line.

* Once decisions have been formalized and coded, this new policy is copied 
  manually (a human decision) to a decision distribution point, which by 
  default is located in the directory `/var/cfengine/masterfiles`
  on all policy distribution servers.

* Every client machine contacts the policy server and downloads these updates. 
  The policy server can be replicated if the number of clients is very large, 
  but we shall assume here that there is only one policy server.

Once a client machine has a copy of the policy, it extracts only those promise 
proposals that are relevant to it, and implements any changes without human 
assistance. This is how CFEngine manages change.

CFEngine tries to minimize dependencies by decoupling processes. By following 
this pull-based architecture, CFEngine will tolerate network outages and will 
recover from deployment errors easily. By placing the burden of responsibility 
for decision at the top, and for implementation at the bottom, we avoid 
needless fragility and keep two independent quality assurance processes apart.
