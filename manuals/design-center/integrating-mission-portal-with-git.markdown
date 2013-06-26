---
layout: default
title: Integrating Mission Portal with git
categories: [Manuals, Design Center, Integrating with git]
published: true
sorting: 10
alias: manuals-design-center-integrating-mission-portal-with-git.html
tags: [sketch, design center, git, mission portal, enterprise, masterfiles, version control, Mission Portal, ui]
---

CFEngine Enterprise 3.5 introduces integration with git repositories for 
managing CFEngine policy. In particular, the Design Center GUI requires access 
to a git repository in order to manage sketches.

These instructions will cover the setup of a git repository with the initial 
CFEngine masterfiles together with configuring the CFEngine Mission Portal to 
use this repository.

When following these steps, it might be helpful to look at the diagram
in the [CFEngine Enterprise sketch flow][Sketch Flow in CFEngine Enterprise].


## Setting up the git service

We will need a git service with the capability to serve git over a key-based 
SSH channel. The easiest way to do this is to use a service like 
[github][github], but it is not hard to set up a local git 
service either.

For Red Hat (and derived distributions), we need to do the following steps to 
set up a local git service. Assume that gitserver is the server that will host 
the git service, and that we already have the ssh service running and it 
allows key-based authentication. Note that this will use your workstation's 
SSH key to authenticate with the Mission Portal. Please generate a new SSH key if 
you do not want the Mission Portal users to use your private key to push to
the git service.

1. Log in to the git server and install the git package.


        user@workstation $ ssh root@gitserver
          root@gitserver # yum install git

2. Create the git user and a .ssh directory.

        root@gitserver # adduser git
        root@gitserver # su git
         git@gitserver $ mkdir ~/.ssh
         git@gitserver $ chmod 700 ~/.ssh

3. Use workstation's SSH key to authenticate with git.

         user@workstation $ scp ~/.ssh/id_rsa.pub root@gitserver:/home/git/.ssh/authorized_keys

4. Test that you can log in as the git user.

        user@workstation $ ssh git@gitserver
           git@gitserver $

5. Create the masterfiles repository.

           git@gitserver $ mkdir masterfiles.git
           git@gitserver $ cd masterfiles.git/
           git@gitserver $ git init --bare
                           Initialized empty Git repository in /home/git/masterfiles.git/

## Initializing the git repository

1. Make a local clone of the git repository.

        user@workstation $ git clone git@gitserver:masterfiles.git
        Initialized empty Git repository in /home/user/masterfiles/.git/
        warning: You appear to have cloned an empty repository.
        user@workstation $ cd masterfiles

2. Copy and push initial masterfiles.

Get the initial masterfiles from a cfengine-nova-hub package.
If you install it on a fresh system, they will end up in
/var/cfengine/masterfiles (copied from /var/cfengine/share/NovaBase).

        user@workstation $ cp -R /path/to/initial/cfengine/enterprise/masterfiles/* .
        user@workstation $ git add -A
        user@workstation $ git commit -m "initial masterfiles"
        user@workstation $ git push origin master


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
5. Fill out the fields as shown by the example below, and click `Show Hosts` and `Activate`.
![Test activation in Mission Portal](mission-portal-test-activation.png)
6. Type in "My test activation" into the commit message box and commit.

### See the commit in the log

Our test sketch is now committed to the git repository. Go to a clone of the
git repository, pull from the git service and see that the commit is there:

1. Fetch our latest commit.

        $ git fetch upstream

2. Rebase, adjust to the branch you are using (master in this example).

        $ git rebase upstream/master

3. Note that the git author (name and email) is set to the user of the Mission Portal,
while the git committer (name and email) comes from the Mission Portal settings, under Version Control Repository.

        $ git log --pretty=format:"%h - %an, %ae, %cn, %ce : %s"
                4190ca5 - test, test@localhost.com, Mission Portal, missionportal@cfengine.com : My test activation

We have now confirmed that the Mission Portal is able to commit to our
git service, and that author information is kept.


## Filtering commits by Mission Portal and users

If the Mission Portal is just one out of several users of your git service, you can easily filter
which commits came from the Mission Portal, and which users of the Mission Portal authored the commit.


### Show all commits done through Mission Portal

In order to see only commits made by users of the Mission Portal, we filter on the committer name.
Note that this needs to match what you have configured as the committer name in the settings,
under Version Control Repository (we are using 'Mission Portal' in the example below).

We can also see the user name of the Mission Portal user by printing the author name.

````
$ git log --pretty=format:"%h %an: %s" --committer='Mission Portal'
0ac4ae0 bob: Setting up dev environment. Ticket #123.
5ffc4d1 bob: Configuring postgres on test environment. Ticket #124.
4190ca5 bob: My test activation
0ac4ae0 tom: remove failed activation
5ffc4d1 tom: print echo example
dc9518d rachel: Rolling out Apache, Phase 2
3cfaf93 rachel: Rolling out Apache, Phase 1
````

### Show commits by a Mission Portal user

If you are only interested in seeing the commits by a particular user of the
Mission Portal, you can filter on the author name as well ('bob' in the example below).

````
 $ git log --pretty=oneline --abbrev-commit --committer='Mission Portal' --author='bob'
0ac4ae0 Setting up dev environment. Ticket #123.
5ffc4d1 Configuring postgres on test environment. Ticket #124.
4190ca5 My test activation
````


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

The following steps show how to configure `cf-agent` on the policy server to
pull from git every time it runs (by default every 5 minutes).

1. On a working copy of your git repository, add the promise to update from git.
Save the following in `update/update_from_repository.cf`.

    ```cf3
        bundle agent update_from_repository
        {
        commands:

        am_policy_hub::

          "/usr/bin/git fetch --all"
            contain => u_no_output;

          "/usr/bin/git reset --hard origin/master"   # change to your branch
            contain => u_no_output;
        }

        body contain u_no_output
        {
          no_output => "true";
          chdir => "/var/cfengine/masterfiles";
        }
    ```

2. Include the file into the failsafe policy, change the following in `failsafe/failsafe.cf`.

        ...
        "cfe_internal_update_policy",
        "cfe_internal_update_processes",
        ...

        ...
        "cfe_internal_update_policy",
        "update_from_repository",
        "cfe_internal_update_processes",
        ...


3. Commit the two above changes to the git service.

        user@workstation $ git add update.cf update/update_from_repository.cf
        user@workstation $ git commit -m "automatically fetch masterfiles from git"
        user@workstation $ git push origin master         # change to your branch

4. Log in to the policy server and make sure CFEngine is not running.

        root@policy_server # /etc/init.d/cfengine3 stop
        Shutting down cf-execd:                                    [  OK  ]
        Shutting down cf-serverd:                                  [  OK  ]
        Shutting down cf-monitord:                                 [  OK  ]

5. Move current masterfiles out of the way.

        root@policy_server # mv /var/cfengine/masterfiles/ /var/cfengine/masterfiles.orig

6. Clone your git repository into /var/cfengine/masterfiles. We assume
that the git service is running on the policy server here for simplicity.
Please adjust to use your git remote url, if necessary (you then also need
to make sure the root user has access to pull updates from git).

        root@policy_server # git clone /home/git/masterfiles.git /var/cfengine/masterfiles
        Initialized empty Git repository in /var/cfengine/masterfiles/.git/

7. Make sure that the policy has valid syntax. `cf-promises` should not give output.

        root@policy_server # /var/cfengine/bin/cf-promises -f /var/cfengine/masterfiles/update.cf

8. Start CFEngine again.

        root@policy_server # /etc/init.d/cfengine3 start


## End-to-end waiting time

If we set up the CFEngine policy server to pull automatically from git and CFEngine runs
every 5 minutes everywhere (the default), the maximum time elapsed from committing to git
until reports are collected is **15 minutes**:

*  0 minutes: commit to git (e.g. from the Design Center GUI).
*  5 minutes: the policy server has updated `/var/cfengine/masterfiles`.
* 10 minutes: all hosts have downloaded and run the policy.
* 15 minutes: `cf-hub` on the database server has collected reports from all hosts.


## Access control and security

Please see [Access control for Design Center in the Mission Portal][Controlling Access to the Design Center UI]
for an introduction to how to allow or limit the Mission Portal users' ability 
to commit to the git repository and make changes to the hosts.
