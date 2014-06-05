---
layout: default
title: Mission Portal Design Center App 
published: true
sorting: 5
---

## Design Center App (Beta) ##

### Graphical User Interface for Design Center ###

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

Please see [Version Control and Configuration Policy] for detailed
instructions for enabling the Version Control workflow in CFEngine
Enterprise.

## See Also ##

* [Deploy your first Policy (Enterprise)][Deploy your first Policy]
* [Version Control and Configuration Policy (Enterprise)][Version Control and Configuration Policy]
* [Write a new Sketch (Enterprise and Community)][Write a new Sketch]
