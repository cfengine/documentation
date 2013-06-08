---
layout: default
title: Integrating Mission Portal with git
categories: [Manuals, Design Center, Integrating with git]
published: true
alias: design-center-integrating-mission-portal-with-git.html
tags: [sketch, design center, git, mission portal, enterprise, masterfiles, version control]
---

CFEngine Enterprise 3.5 introduces integration with a git repository for 
managing CFEngine policy. In particular, the Design Center GUI requires access 
to a git repository in order to manage sketches.

These instructions will cover the setup of a git repository with the initial 
CFEngine masterfiles together with configuring the CFEngine Mission Portal to 
use this repository.

When following these steps, it might be helpful to look at the diagram
in the CFEngine Enterprise sketch flow (TODO: link to enterprise-sketch-flow.markdown).


## Setting up the git service

We will need a git service with the capability to serve git over a key-based 
SSH channel. The easiest way to do this is to use a service like 
[github](https://github.com/), but it is not hard to set up a local git 
service either.

For Red Hat (and derived distributions), we need to do the following steps to 
set up a local git service. Assume that gitserver is the server that will host 
the git service, and that we already have the ssh service running and it 
allows key-based authentication. Note that this will use your workstation's 
SSH key to authenticate with the Mission Portal. Please generate a new SSH key if 
you do not want the Mission Portal users to use your private key to push to
the git service.

1. Log in to the git server and install the git package

````
user@workstation $ ssh root@gitserver
  root@gitserver # yum install git
````

2. Create the git user and create .ssh directory

````
root@gitserver # adduser git
root@gitserver # su git
 git@gitserver $ mkdir ~/.ssh
 git@gitserver $ chmod 700 ~/.ssh
````

3. Use workstation's SSH key to authenticate with git

````
 user@workstation $ scp ~/.ssh/id_rsa.pub root@gitserver:/home/git/.ssh/authorized_keys
````

4. Test that you can log in as the git user

````
user@workstation $ ssh git@gitserver
   git@gitserver $
````

5. Create the masterfiles repository

````
   git@gitserver $ mkdir masterfiles.git
   git@gitserver $ cd masterfiles.git/
   git@gitserver $ $ git init --bare
                     Initialized empty Git repository in /home/git/masterfiles.git/
````

## Initializing the git repository

1. Make a local clone of the git repository

````
user@workstation $ git clone git@gitserver:masterfiles.git
Initialized empty Git repository in /home/user/masterfiles/.git/
warning: You appear to have cloned an empty repository.
user@workstation $ cd masterfiles
````

2. Copy and push initial masterfiles

Get the initial masterfiles from a cfengine-nova-hub package.
If you install it on a fresh system, they will end up in
/var/cfengine/masterfiles (copied from /var/cfengine/share/NovaBase).
````
user@workstation $ cp -R /path/to/initial/cfengine/enterprise/masterfiles/* .
user@workstation $ git add -A
user@workstation $ git commit -m "initial masterfiles"
user@workstation $ git push origin master
````


## Connecting the Mission Portal to the git repository

1. Log in to the Mission Portal as an administrator (e.g. the `admin` user).
2. Navigate to Settings -> Version control repository.
3. Input the settings from the git service that you are using or configured.
4. Click save settings and make sure it reports success.

![Mission Portal Version control repository settings](mp-vcs-settings.png)


## Testing first commit

1. Log in to the Mission Portal as an administrator (e.g. the `admin` user).
2. Click on the `Design Center` app at the left.
3. You should now see a listing of some sketches that are available out of the box.
4. Click on the `Packages::packages_removed` sketch.
5. Fill out the fields as shown by the example below, and click `Show hosts` and `Activate`.
6. Type in "My test activation" into the commit message box and commit.

TODO: screenshot of filled out packages_removed sketch
NOTE:
Fill out e.g. `Test activation` in the activation name field, and `nosuchpackage` in the 
field for packages that should not be installed (no change is made to the system if
the package is not already installed).
Under 

Our test sketch is now committed to the git repository. Go to a clone of the
git repository, pull from the git service and see that the commit is there:
1. $ git fetch upstream
2. $ git rebase upstream/master  # adjust to the branch you are using
3. $ 

TODO: git log author name, committer name command, etc.

TODO: show that author name and email matches MP settings

We have now confirmed that the Mission Portal is able to commit to our
git service, and that author information is kept. There is just one step remaining.


## Pulling from git to the policy server

We have now set up a git repository and allowed users to commit to it from
the Mission Portal. However, nothing will change on the CFEngine hosts until
we pull the policy from git into `/var/cfengine/masterfiles` on the policy server.
This can be done by CFEngine itself every time `cf-agent` runs on the
policy server, or by utilizing a cron job or similar facilities.

It is not a requirement to set up automatic pull from the git service,
but no actions will be taken by CFEngine on the end hosts, nor will any
reports come back, until the policy from git is copied into
`/var/cfengine/masterfiles` on your policy server.

The following steps show how to configure ´cf-agent´ on the policy server to
pull from git every time it runs (by default every 5 minutes).

1. 

TODO: steps + policy, create clone in /var/cfengine/masterfiles, etc.


## Access control and security

Please see Access control for git in the Mission Portal
(TODO: link to access-control-mission-portal.mardown) for an introduction
to how to allow or limit the Mission Portal users' ability to commit to the
git repository and make changes to the hosts.