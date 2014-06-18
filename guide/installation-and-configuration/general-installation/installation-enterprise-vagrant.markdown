---
layout: default
title: Using Vagrant
published: true
sorting: 30
tags: [getting started, installation, enterprise, vagrant]
---

The CFEngine Enterprise Vagrant Environment provides an easy way to test and
explore CFEngine Enterprise. This guide describes how to set up a client-server
model with CFEngine and, through policy, manage both machines. Vagrant will
create one VirtualBox VM to be the Policy Server (server), and another machine
that will be the Host Agent (client), or host that can be managed by CFEngine.
Both will will run CentOS 6.5 64-bit and communicate on a host-only network.
Apart from a one-time download of Vagrant and VirtualBox, this setup requires
just one command and takes between 5 and 15 minutes to complete (determined by
your Internet connection and disk speed). Upon completion, you are ready to
start working with CFEngine.

## Requirements
* 2G disk space
* 2G memory
* CPU with VT extensions capable of running 64bit guests

Note: VirtualBox requires that your computer support hardware virtualization
in order to make use of the CentOS 64-bit virtual machines mentioned above.
This is sometimes turned on or off in BIOS settings, but not all processors
and motherboards necessarily support hardware virtualization.

If your system lacks this support you will need to choose another computer to
take advantage of the 64-bit virtual machines or [install CFEngine using a
different approach][General Installation#More Detailed Installation Guides].

## Overview

1. Install Vagrant
2. Install Virtualbox
3. Start the CFEngine Enterprise Vagrant Environment
4. Log in to the Mission Portal
5. Stop CFEngine Enterprise
5. Uninstall

## Install Vagrant

This tutorial uses Vagrant to configure your VMs. It is available for Linux,
Windows and MacOS and can be downloaded from vagrantup.com (this guide has been
tested with version [1.6.3](http://www.vagrantup.com/download-archive/v1.6.3.html)). After
downloading Vagrant, install it on your computer. You may want to reference the
Windows Mac or Linux vagrant install guides.

## Install Virtualbox

This tutorial uses VirtualBox to create virtual machines on your computer, to
which Vagrant deploys CFEngine. VirtualBox can be downloaded from
virtualbox.org (use version
[4.3.12](http://download.virtualbox.org/virtualbox/4.3.12/)). After
downloading VirtualBox, install it on your computer.

**Note:** To avoid problems, disable other virtualization environments you are
running.

## Start the CFEngine Enterprise 3.6 Vagrant Environment

Step 1. Download our ready-made Vagrant project (use the
[tar-file](http://cfengine.vagrant-baseboxes.s3.amazonaws.com/enterprise-getting-started/enterprise-3.6-vagrant_free25-201406171618.tar.gz)
or the
[zip-file](http://cfengine.vagrant-baseboxes.s3.amazonaws.com/enterprise-getting-started/enterprise-3.6-vagrant_free25-201406171618.zip)
depending on your preference).

Step 2. Save and unpack the file anywhere on your drive; this
creates a Vagrant Project directory called **vagrant_env**.

Step 3. Open a terminal and navigate to the Vagrant Project directory (e.g.
`/home/user/vagrant_env`, or `C:\vagrant_env`) and enter the following command:

```console
$ vagrant up
```

Vagrant performs the following processes:

* Downloads the CentOS basebox used for both the hub and the client (if it has
  not already been cached by vagrant.
* Provisions, installs and bootstraps the hub
* Provisions, installs and bootstraps clients

The basebox is ~450MB.

Note: If you want to use more hosts in this environment, you can
  edit the **Vagrantfile** text file in the directory that you have just created.
  Change the line that says "hosts = 1" to the number of hosts that you want in
  the setup. The maximum supported in this evaluation version of CFEngine is 25.

## Log in to the Mission Portal

At the end of the setup process, you can use your browser to log in to the
Mission Portal:

`http://localhost:9002`

username: admin

password: admin

**Note:** It may take up to 15 minutes before the hosts register in Mission
Portal.

That's all there is to it, the install is complete! Move on and explore the environment.
## Exploring the Environemnt

### Accessing VMs

#### Accessing via SSH

The standard vagrant ssh key is configured. To ssh to a host run `vagrant ssh
myhost` where `myhost` is the name of a running vm as seen in the `vagrant
status` output. Both the 'root' and 'vagrant' users passwords are set to
'vagrant'.

**Example:**

```console
$ vagrant ssh hub
Last login: Fri Jun 13 18:58:10 2014 from 10.0.2.2
```

#### Accessing via GUI

If you launch the virtualbox GUI you should find the vagrant vms named
`hub` and `agent_host001`. Additionally, you can uncomment the `v.gui=true`
option in the `Vagrantfile` to have the console gui start with the vms.
**Note:** There are two `v.gui` settings to uncomment; one for the hub, and one
for the clients.

### Check the status of the vms

Running `vagrant status` from the vagrant project directroy will produce
output like this.

```console
$ vagrant status
Current machine states:

hub                       not created (virtualbox)
host001                   not created (virtualbox)

This environment represents multiple VMs. The VMs are all listed
above with their current state. For more information about a specific
VM, run `vagrant status NAME`.
```

### Start or resume the environment

To start or resume a halted environment simply run `vagrant up` from within the
vagrant project directory.

```console
$ vagrant up
```

### Stop the environment (Halt/Suspend/Destroy)

To shut down the vms run `vagrant halt`. This will preserve the vms and any
changes made inside.  To suspend the vms run `vagrant suspend`. This will
freeze the state of each vm and allows for latter resuming of the environment.
To remove the provisioned vms run `vagrant destroy`. This will delete the vms
and any modifications made to the environment will be lost.

## Uninstall Vagrant Environment

When you have completed your evaluation are ready to use CFEngine on
production servers, remove the VMs that you created above by following these
simple instructions:

To remove the VMs entirely, type: `vagrant destroy`

If you are completely done and do not anticipate using them anymore, you can
also remove the base box `cfengine-3.6-free25-centos-6.5-x86_64` that was
downloaded. You can see it by typing `vagrant box list`. To delete the basebox
run `vagrant box remove cfengine-3.6-free25-centos-6.5-x86_64 virtualbox`.
**Note:** Runing `vagrant up` from the vagrant project directory again will
re-download this basebox.

Vagrant and VirtualBox are useful general purpose programs, so you might want
to keep them around. If not, follow the standard procedures for your OS to
remove these applications.
