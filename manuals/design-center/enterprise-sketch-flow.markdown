---
layout: default
title: Sketch Flow in CFEngine Enterprise
categories: [Manuals, Design Center, Enterprise Sketch Flow]
published: true
alias: manuals-design-center-enterprise-sketch-flow.html
tags: [sketch, design center, version control, git, masterfiles, Mission Portal, enterprise, ui]
---

The CFEngine Enterprise Design Center graphical user interface (GUI) relies on 
several simple services and file structures. The interactions between these 
are shown in the diagram below.

![Enterprise Design Center data-flow diagram](enterprise-sketch-dataflow-diagram.png)

### Git repository service

This service needs to offer git over ssh. It is the canonical place for 
masterfiles, and needs to be initialized with the CFEngine Enterprise 
masterfiles (version 3.5 and onwards). It can be hosted on an internal git 
server, or services like [github](http://www.github.com).

### Mission Portal GUI

The graphical interface that the users will interact with. It includes the 
Design Center app for using sketches and getting reports about them.
The administrator of Mission Portal needs to configure its settings
with the git version control repository. A user is only allowed to use
the Design Center app if he is member of the `cf_vcs` role.

### /var/cfengine/masterfiles

Distribution point for policies for CFEngine.
A shared directory containing the policy for all hosts.
CFEngine policy with sketches inside this directory will
automatically get pulled down by all CFEngine hosts.

### /var/cfengine/design-center

This is a stable version of the official [Design Center 
repository](https://github.com/cfengine/design-center). It contains all the 
sketches that becomes available to the Mission Portal Design Center GUI, as 
well as tools and APIs utilized internally by the GUI. Note in particular the 
`tools/cf-sketch/constdata.conf` file that contains out-of-the-box validations 
and other definitions. See the reference documentation for the [sketch 
structure](reference-design-center-sketch-structure.html) for a complete 
list of requirements for a sketch to work wellwith the GUI.

### /opt/cfengine/userworkdir/$(user)/masterfiles

Each user of the Mission Portal has his own working directory here. It 
contains a local clone from the git repository service, using the shared 
Mission Portal git credentials that the administrator has set up for all 
users. The operations performed in the GUI will modify this directory, and it 
will be pushed to the git service for applying the changes to the CFEngine 
policy.

`/opt/cfengine` is chosen as the base directory rather than `/var/cfengine` 
due tospace utilization concerns in `/var` when many users check out their 
local git  clone. It should have enough free space to store the size of the 
gitmasterfiles clone times the number of users in the `cf_vcs` role.

### The hosts and /var/cfengine/inputs

The hosts copy from `/var/cfengine/masterfiles` on the CFEngine server to 
their local `/var/cfengine/inputs` every time CFEngine runs. The policy they 
copy will include the sketches that have been activated by GUI users. The 
hosts will run the policy, including the sketches, that apply to them. During 
each run they will generate local reports that will be pulled by the CFEngine 
Enterprise server, and this will update the GUI with status about the sketch.

If a sketch is not compliant (red in the GUI), the user is given the option to 
invoke an agent run on a failing host from the GUI. This will capture the 
verbose agent output for the user. This is only allowed if the Mission Portal 
administrator has put the user in the `cf_remoteagent` role.
