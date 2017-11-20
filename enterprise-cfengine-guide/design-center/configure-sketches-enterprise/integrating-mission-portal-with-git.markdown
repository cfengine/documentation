---
layout: default
title: Integrating Mission Portal with git
published: false
sorting: 10
tags: [sketch, design center, git, mission portal, enterprise, masterfiles, version control, Mission Portal, ui]
---

CFEngine Enterprise 3.6 integrates with Git repositories to
manage CFEngine policy. In particular, the **Design Center App** requires access
to a Git repository in order to manage sketches.

[Version Control and Configuration Policy][Best Practices#Version Control and Configuration Policy] describes an out-of-the-box Git repository that is hosted on the
Policy Server with the initial CFEngine `masterfiles` and how to configure
CFEngine Enterprise to use this repository. If you already have a Git
server, ensure that you have a passphraseless SSH key.

**NOTE that if you don't want to use a remote Git server, you don't need to change the Mission Portal settings**

As you follow these steps, refer to the diagram
in the [CFEngine Enterprise sketch flow][Sketch Flow in CFEngine Enterprise]. It provides
a detailed look at the file structure and services that make up the **Design Center App**.

## Overview

1. [Check access][Integrating Mission Portal with git#Check access]
2. [Connect the Mission Portal to the git repository][Integrating Mission Portal with git#Connect the Mission Portal to the git repository]
3. [Test the Design Center app][Integrating Mission Portal with git#Test the Design Center app]
4. [End to end waiting time][Integrating Mission Portal with git#End to end wait time]
5. [Access control and security][Integrating Mission Portal with git#Access control and security]

## Check access

**If you want to use a remote Git server**, test that you can log in as the `git` user by using the generated
passphraseless ssh key.

        root@policyserver $ ssh -i my_id_rsa git@remote-git-server
        git@remote-git-server $

Once the authorization is tested successfully, move the keypair
to a secure storage location. You might want to authorize additional keys
for users to interface with the repository directly. Only the Mission
Portal key needs to be passphraseless. Your Git server can have additional
features like the ability to make a specific key read-only. See your Git
repository provider's documentation for more information.

## Connect the Mission Portal to the git repository

**NOTE that if you don't want to use a remote Git server, you don't need to change the Mission Portal settings**

**If you want to use a remote Git server**, do the following.

1. Log in to the Mission Portal as an administrator (e.g. the `admin` user).
2. Navigate to *Settings* -> *Version control repository*.
3. Input the settings from the Git service that you are using or configured.

   * Git server url: `git@remote-git-server:masterfiles.git`
   * Git branch: `master`
   * Committer email `git@your-domain-here`
   * Committer name `CFEngine Mission Portal`
   * Git private key `my_id_rsa`
    (You will need to copy the private key to your workstation
    so that it can be accessed via the file selection.

4. Click save settings and make sure it reports success.

## Test the Design Center app

1. Log in to the Mission Portal as an administrator (e.g. the `admin` user).
2. Select the [Design Center][Design Center UI] at the left.
3. View the listing of some sketches that are available out of the box.
4. Click the `Packages::packages_removed` sketch.
5. Fill out the fields as shown by the example below, and click `Show Hosts` and then `Activate`.
   ![Test activation in Mission Portal](mission-portal-test-activation.png)
6. Type "My test activation" into the commit message box and commit.

### Review the change history from the git commit log

Our test sketch (created above) is now committed to the Git repository. Go to a clone of the
Git repository, pull, and see that the commit is there:

1. Fetch your latest commit (```origin``` and ```master``` depend on your settings).

        $ git fetch origin master

2. Rebase, and adjust to the branch you are using (```master``` in this example).

        $ git rebase origin/master

3. Note that the Git author (name and email) is set to the user of the Mission Portal,
while the Git committer (name and email) comes from the Mission Portal settings, under Version Control Repository.

        $ git log --pretty=format:"%h - %an, %ae, %cn, %ce : %s"
                4190ca5 - test, test@localhost.com, Mission Portal, missionportal@cfengine.com : My test activation

We have now confirmed that the Mission Portal is able to commit to our
Git repository and that author information is kept.


### Filter commits by Mission Portal and users

If the Mission Portal is just one out of several users of your git service, you can easily filter
which commits came from the Mission Portal, and which users of the Mission Portal authored the commit.


#### Show all commits made through the Mission Portal

In order to see only commits that are made by users of the Mission Portal, filter on the committer name.
Note that this needs to match what you have configured as the committer name in the settings,
under Version Control Repository (we are using 'Mission Portal' in the example below).

We can also see the user name of the Mission Portal user by printing the author name.

```console
$ git log --pretty=format:"%h %an: %s" --committer='Mission Portal'
0ac4ae0 bob: Setting up dev environment. Ticket #123.
5ffc4d1 bob: Configuring postgres on test environment. Ticket #124.
4190ca5 bob: My test activation
0ac4ae0 tom: remove failed activation
5ffc4d1 tom: print echo example
dc9518d rachel: Rolling out Apache, Phase 2
3cfaf93 rachel: Rolling out Apache, Phase 1
```

#### Show commits by a Mission Portal user

If you are only interested in seeing the commits by a particular user of the
Mission Portal, you can filter on the author name as well ('bob' in the example below).

```console
 $ git log --pretty=oneline --abbrev-commit --committer='Mission Portal' --author='bob'
0ac4ae0 Setting up dev environment. Ticket #123.
5ffc4d1 Configuring postgres on test environment. Ticket #124.
4190ca5 My test activation
```

## End to end wait time

If we set up the CFEngine policy server to pull automatically from git and CFEngine runs
every 5 minutes everywhere (the default), the maximum time elapsed from committing to git
until reports are collected is **15 minutes**:

*  0 minutes: commit to git (e.g. from the Design Center GUI).
*  5 minutes: the policy server has updated `/var/cfengine/masterfiles`.
* 10 minutes: all hosts have downloaded and run the policy.
* 15 minutes: `cf-hub` on the database server has collected reports from all hosts.


## Access control and security

Go to [Controlling Access to the Design Center UI][Design Center Access Control]
to learn how to allow or limit the Mission Portal user's ability
to commit to the git repository and make changes to the hosts.
