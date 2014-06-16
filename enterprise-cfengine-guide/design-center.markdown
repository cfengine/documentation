---
layout: default
title: Design Center
sorting: 70
published: true
tags: [cfengine enterprise, user interface, mission portal]
---

Deploy infrastructure policy "Sketches" using a form-based approach to configure properties, selecting the hosts that need to be impacted, and then tracking the progress of the deployment via the Mission Portal user interface.  

### Delegation of System Administrator Tasks ###

CFEngine experts can create their own Sketches, that match the exact needs of the organization in which they are used. They can be hosted in the Design Center repository, so that other administrators, developers and line-of-business users can use them to perform sophisticated sysadmin tasks without the need for detailed CFEngine knowledge. 

### Version Control for Sketches ###

CFEngine Enterprise keeps track of all changes in sketches and sketch-deployments, using Git-integration to track autors, source-code and meta-information about policy deployments.

## CFEngine, Design Center and Version Control Systems ##

In CFEngine Enterprise, the Design Center is enabled through a Git
repository integration.  Out of the box, the software uses a "bare"
Git repository in `/opt/cfengine/masterfiles.git` but does **not**
deploy it automatically.  Thus any work you do with Design Center will
not propagate to your hosts without some help.

Please see [Best Practices#Version Control and Configuration Policy] for detailed
instructions for enabling the Version Control workflow in CFEngine
Enterprise.

## Sketches in the Design Center App ##

The CFEngine `Design Center` includes a number of templates, so called `sketches`, that let you configure and deploy CFEngine `policies` without requiring detailed knowledge of the CFEngine language. You can select `sketches` from a categorized list, and configure them in the interface.

Every organization using CFEngine can add their own custom `sketches` which will consequently be shown in the app's list of sketches.

Note: The `Design Center App` requires a dedicated git repository. If you have admin rights to the `Mission Portal`, you can configure it in `Settings`.

### Configuration ###

After selecting a sketch, you need to configure a number of parameters. Start with giving your current configuration a unique name which will make it easier for your to recognize it again later. Then fill in the mandatory fields below. All of them show examples and a descriptive text.

You also need to define the hosts you want to activate your configured sketch on. You can select host categories of varying size by following the step-by-step selection presented in the drop-down menus. These categories are based on categorizations defined for example in the `Hosts App`.

### Activation ###

When you're done configuring your sketch you need to activate it. This will trigger a commit to your configured git repository, and transform your configured sketch into CFEngine policy. You will then be able to follow-up on the state of your activation (`In Progress`, `OK`, and `Failed`), and report on potential issues.

Note: `Sketches` can be activated multiple times with varying configuration and on different sets of hosts. The `Design Center App` indicates which sketches have been activated in your environment.


### See Also ###

* [Enterprise Sketches][Enterprise Sketches]
* [Write a new Sketch][Write a new Sketch]
* [Deploy your first Policy (Enterprise)][Deploy your first Policy]
* [Version Control and Configuration Policy (Enterprise)][Best Practices#Version Control and Configuration Policy]
* [Write a new Sketch (Enterprise and Community)][Write a new Sketch]