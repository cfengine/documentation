---
layout: default
title: Design Center in CFEngine Enterprise 
published: true
sorting: 1
---

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
