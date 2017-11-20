---
layout: default
title: Design Center UI
sorting: 70
published: false
tags: [cfengine enterprise, user interface, mission portal]
---

The Design Center UI allows authorized infrastructure engineers to configure, deploy, and monitor data-driven policy templates known as *sketches*.  The engineer can target any group of hosts using pre-existing or custom classifications.

### Delegation of System Administrator Tasks ###

CFEngine experts can write their own sketches to address their exact needs. They can be hosted in a private Design Center repository so that other administrators, developers and line-of-business users can again configure, deploy, and monitor them without detailed CFEngine knowledge.

For more information, see [Write a new Sketch][]

### Version Control for Sketches ###

CFEngine Enterprise keeps track of sketch deployments, using Git integration to track authors, source-code and meta-information about policy deployments.

## CFEngine, Design Center and Version Control Systems ##

In CFEngine Enterprise, the Design Center is enabled through a Git
repository integration.  Out of the box, the software uses a "bare"
Git repository in `/opt/cfengine/masterfiles.git` but does **not**
deploy it automatically.  Thus any work you do with Design Center will
not propagate to your hosts without some help.

Please see
[Version Control and Configuration Policy][Best Practices#Version Control and Configuration Policy]
for detailed instructions for enabling the Version Control workflow in
CFEngine Enterprise.

## Sketches in the Design Center App ##

The CFEngine Design Center includes a number of data-driven policy templates called *sketches* that let you configure and deploy CFEngine policies without requiring detailed knowledge of the CFEngine language. You can select sketches from a categorized list and configure them in the interface, then apply them to any group of hosts.

Every organization using CFEngine can add their own custom *sketches* which will consequently be shown in the app's list of sketches.

Note: The Mission Portal's **Design Center App** requires a dedicated Git repository. If you have admin rights to the Mission Portal, you can configure it in the Settings panel.  Furthemore you have to enable the Git repository integration as explained above.

### Configuration ###

After selecting a sketch, you need to configure it (*activate it*). First, give your activation parameters a unique name so you can recognize it later. Then fill in the fields below (some will be optional, others mandatory). All of them show examples and a descriptive text.

You also need to define the hosts you want to target. You can select host categories through the drop-down menus. These categories are based on categorizations defined in the **Hosts App** for example.  You can select individual hosts too.

### Activation ###

When you're done configuring your sketch you need to activate it. This will require a commit to your configured Git repository that transforms your configuration parameters into CFEngine policy. You will then be able to follow the state of your activation (*In Progress*, *OK*, and *Failed*) and report on any problems.

Note: *Sketches* can be activated multiple times with different configurations and sets of hosts. The **Design Center UI** will show you each activation, its status, the hosts it targets, and the parameters specified.


### See Also ###

* [Enterprise Sketches][Enterprise Sketches]
* [Write a new Sketch][Write a new Sketch]
* [Deploy your first Policy (Enterprise)][Deploy your first Policy]
* [Version Control and Configuration Policy (Enterprise)][Best Practices#Version Control and Configuration Policy]
* [Write a new Sketch][]
