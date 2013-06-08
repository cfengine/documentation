---
layout: default
title: Access control for Design Center in the Mission Portal
categories: [Manuals, Design Center, Access control]
published: true
alias: mission-portal-design-center-access-control.html
tags: [access, security, role, user, sketch, design center, git, mission portal, enterprise, version control]
---

After you have set up the integration between CFEngine Enterprise and git
(TODO: link to integrating-mission-portal-with-git.markdown), you may grant or revoke
access rights for making changes with the Design Center GUI to your users.

Please note that use of the role-based access control (RBAC) for reporting in the Mission Portal
is not yet supported in conjunction with the Design Center GUI. For the time being, 
we recommend turning RBAC globally off in the Mission Portal settings when using the
Design Center GUI. Support may be included in future versions.


## Roles

There are two user roles that impact users' abilities in the Design Center GUI.

TODO: is this correct markdown for itemizing?
* cf_vcs. If a user is member of the cf_vcs role, he is allowed to use the Design Center GUI
in the Mission Portal and commit to the git service configured in the settings. Conversely,
if a user is not member of this role, he will not be able to access the Desing Center GUI -- not
even to list the available sketches.
* cf_remoteagent. This role allows users to invoke `cf-agent` on remote hosts and display the verbose
output from the agents. In the context of the Design Center GUI this is used if a sketch activation
is non-compliant (red), and a user clicks a failed host followed by the "Verbose output" button.
Users can benefit from the Design Center GUI even though they are not member of the `cf_remoteagent` role.
But they will not be able to invoke remote `cf-agent` runs to get additional diagnostics data.


## Allowed changes

Users only get access to what the sketches available in the Design Center GUI offers. For example,
if only a sketch that controls file integrity monitoring (Security::file_integrity) is available in
the GUI, users can only change files that CFEngine monitors. All users will see the same sketches,
and be allowed to activate on all hosts. There is not yet a concept of RBAC for the Design Center GUI.

The sketches that are available are controlled with the contents of `/var/cfenigne/design-center` on the
Mission Portal server. Please see (TODO: link to doc for creating new sketches) for more information.

Note however, that malicious users can potentially do damage to hosts even if you limit their
abilities. For example, if a user creates many activations of the Security::file_integrity sketch
for a large amount of directories, this will have a performance impact across the infrastructure.

To get complete control over what users do, changes can be reviewed before they are copied to
`/var/cfengine/masterfiles` on the policy server. Please see Integrating Mission Portal with git
(TODO: link to integrating-mission-portal-with-git.markdown) for more information.


## Audit log

All changes that Mission Portal users make through the Design Center graphical user interface
becomes part of the git commit log. Each change in sketch activation corresponds to one
commit in git. In the git commit log, the git committer name and email is configured
in the Mission Portal settings. This allows for easily recognizing and parsing which commits
are made through the Mission Portal as opposed to other users of the git service.

In addition, the git author name and email is set to the user name and email address of the
user logged into the Mission Portal when the commit is made. This allows you to see exactly
which users are making which changes in the git commit log.

TODO: insert git log command to see committer and author name/email.