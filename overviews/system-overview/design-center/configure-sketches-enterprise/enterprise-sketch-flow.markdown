---
layout: default
title: Sketch Flow in CFEngine Enterprise
published: true
sorting: 40
tags: [sketch, design center, version control, git, masterfiles, Mission Portal, enterprise, ui]
---

The CFEngine Enterprise Design Center app (UI) relies on 
several simple services and file structures. The interactions between these 
are shown in the diagram below.

![Enterprise Design Center data-flow diagram](enterprise-sketch-dataflow-diagram.png)

### Git repository service

This service must offer git over ssh. It is the canonical place for 
masterfiles, and must be initialized with the CFEngine Enterprise 
masterfiles (version 3.5 and onwards). It can be hosted on an internal git 
server or services like [github][github].

### Mission Portal GUI

The graphical interface with which the users interact. It includes the 
Design Center app for using sketches and getting reports about them.
The administrator of Mission Portal must configure its settings
with the git version control repository. Users are only allowed to use
the Design Center app if they are members of the `cf_vcs` role (see 
[Controlling Access to the Design Center UI][Controlling Access to the Design Center UI].


### /var/cfengine/masterfiles

The distribution point for policies for CFEngine.
This is a shared directory that contains the policy for all hosts.
CFEngine policy with sketches inside this directory automatically 
get pulled down by all CFEngine hosts.

### /var/cfengine/design-center

This is a stable version of the official [Design Center 
repository][github design-center]. It contains all the 
sketches that are available to the Mission Portal Design Center app (UI), as 
well as tools and APIs utilized internally by the app. Note in particular the 
`tools/cf-sketch/constdata.conf` file that contains out-of-the-box validations 
and other definitions. See the reference documentation for the [sketch 
structure][Sketch Structure] for a complete 
list of requirements necessary for a sketch to work well with the app.

### /opt/cfengine/userworkdir/$(user)/masterfiles

Each user of the Mission Portal has his or her own working directory here. It 
contains a local clone from the git repository service, using the shared 
Mission Portal git credentials that the administrator has set up for all 
users. The operations performed in the Design Center app will modify this directory, 
and it will be pushed to the git service for applying the changes to the CFEngine 
policy.

`/opt/cfengine` is chosen as the base directory rather than `/var/cfengine` 
due to space utilization concerns in `/var` when many users check out their 
local git clone. It should have enough free space to store the size of the 
git masterfiles clone times the number of users in the `cf_vcs` role.

### The hosts and /var/cfengine/inputs

The hosts copy from `/var/cfengine/masterfiles` on the CFEngine server to 
its local `/var/cfengine/inputs` every time CFEngine runs. The policy that hosts 
copy includes the sketches that have been activated by app users. The 
hosts run the policy, including the sketches, that apply to them. During 
each run they generate local reports that are pulled by the CFEngine 
Enterprise server, and this updates the app with a status about the sketch.

If a sketch is not compliant (red in the app), the user is given the option to 
invoke an agent run on a failing host from the app. This will capture the 
verbose agent output for the user. This is only allowed if the Mission Portal 
administrator has put the user in the `cf_remoteagent` role.
