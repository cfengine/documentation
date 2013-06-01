---
layout: default
title: Integrating Mission Portal with git
categories: [Manuals, Design Center UI, Integrating with git]
published: true
alias: reference-design-center-ui-integrating-with-git.html
tags: [sketch, design center, git, mission portal, enterprise, masterfiles, version control]
---

CFEngine Enterprise 3.5 introduces integration with a git repository for 
managing CFEngine policy. In particular, the Design Center GUI requires access 
to a git repository in order to manage sketches.

These instructions will cover the setup of a git repository with the initial 
CFEngine masterfiles together with configuring the CFEngine Mission Portal to 
use this repository.


## Setting up the git service

We will need a git service with the capability to serve git over a key-based 
SSH channel. The easiest way to do this is to use a service like 
[github](https://github.com/), but it is not hard to set up a local git 
service either.

For Red Hat (and derived distributions), we need to do the following steps to 
set up a local git service. Assume that gitserver is the server that will host 
the git service, and that we already have the ssh service running and it 
allows key-based authentication. Note that this will use your workstation's 
SSH key to authenticate with the Mission Portal. Please generate a new one if 
you want.

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

1. Log in to the Mission Portal as an administrator (member of the `admin` role).
2. Navigate to Settings -> Version control repository.
3. Input the settings from the git service that you are using or configured.
4. Click save settings and make sure it reports success.

![Mission Portal Version control repository settings](mp-vcs-settings.png)


## Testing first commit

TODO: show that author name and email matches MP settings
TODO: screenshot github?