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

The first step is to decide if you want to use version control, and if
so, if you want to keep using the bare repository or if you have your
own remote Git repository.  To use a remote repository, go to the
Mission Portal settings and adjust the version control system (VCS)
settings accordingly.

In any case the VCS repository should start with the contents of the
masterfiles, which we recommend to be the ones that are distributed
with CFEngine in `/var/cfengine/share/NovaBase/masterfiles`.  This is
the starting point for the "bare" Git repository in
`/opt/cfengine/masterfiles.git` already, but consult a Git expert to
ensure you don't lose policies or data.

To deploy your policy you can either run `cf-agent
-Dcfengine_internal_masterfiles_update -f update.cf` once or enable
auto-deployments.  Either way, you'll overwrite the contents of
`/var/cfengine/masterfiles` with the deployed policy, so make sure to
back it up beforehands.  It's best to enable auto-deployments early
on so you don't have to worry about this.

To enable auto-deployments, edit `update.cf` and enable the
`cfengine_internal_masterfiles_update` class permanently, and then
commit that to the repository (local "bare" Git repository in
`/opt/cfengine/masterfiles.git` or a remote repository).  You can
simply uncomment the line that has it enabled for Enterprise.

Note that if you don't commit that change, it will enable the
auto-deployment from the repository, which will promptly override
auto-deployment back to `off`.

## See Also ##

* [Deploy your first Policy (Enterprise)][Deploy your first Policy]
* [Configure the Design Center App (Enterprise)][Configure the Design Center App]
* [Write a new Sketch (Enterprise and Community)][Write a new Sketch]