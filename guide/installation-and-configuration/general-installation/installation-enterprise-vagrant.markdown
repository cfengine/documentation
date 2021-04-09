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
* 1G memory
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
Windows and MacOS and can be downloaded from vagrantup.com. After
downloading Vagrant, install it on your computer. You may want to reference the
Windows Mac or Linux vagrant install guides.

## Install Virtualbox

This tutorial uses VirtualBox to create virtual machines on your computer, to
which Vagrant deploys CFEngine. VirtualBox can be downloaded from
virtualbox.org. After downloading VirtualBox, install it on your computer.

**Note:** To avoid problems, disable other virtualization environments you are
running.

## Start the CFEngine Enterprise {{site.cfengine.branch}} Vagrant Environment

Step 1. Download our ready-made Vagrant project
[tar-file](https://cfengine-package-repos.s3.amazonaws.com/enterprise/Enterprise-{{site.cfengine.branch}}.{{site.cfengine.latest_patch_release}}/misc/CFEngine_Enterprise_vagrant_quickstart-{{site.cfengine.branch}}.{{site.cfengine.latest_patch_release}}-{{site.cfengine.latest_package_build}}.tar.gz).

Step 2. Save and unpack the file anywhere on your drive; this
creates a Vagrant Project directory.

Step 3. Open a terminal and navigate to the Vagrant Project directory (e.g.
`/home/user/CFEngine_Enterprise_vagrant_quickstart-{{site.cfengine.branch}}.{{site.cfengine.latest_patch_release}}-{{site.cfengine.latest_package_build}}`, or `C:\CFEngine_Enterprise_vagrant_quickstart-{{site.cfengine.branch}}.{{site.cfengine.latest_patch_release}}-{{site.cfengine.latest_package_build}}`) and enter the following command:

```console
$ vagrant up
```

Vagrant performs the following processes:

* Downloads the CentOS basebox used for both the hub and the client (if it has
  not already been cached by vagrant.
* Provisions, installs and bootstraps the hub
* Provisions, installs and bootstraps clients

The basebox is ~500MB.

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
## Exploring the Environment

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
`CFEngine Enterprise {{site.cfengine.branch}}.{{site.cfengine.latest_patch_release}}-{{site.cfengine.latest_package_build}} hub`, and `CFEngine Enterprise {{site.cfengine.branch}}.{{site.cfengine.latest_patch_release}}-{{site.cfengine.latest_package_build}} agent host001`. Additionally, you can uncomment the `v.gui=true`
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
changes made inside.

```console
$ vagrant suspend
==> hub: Saving VM state and suspending execution...
==> host001: Saving VM state and suspending execution...
```

To suspend the vms run `vagrant suspend`. This will freeze the state of each vm
and allows for latter resuming of the environment.

```console
$ vagrant halt
==> host001: Attempting graceful shutdown of VM...
==> hub: Attempting graceful shutdown of VM...
```

At any time you can run `vagrant destroy` to remove the provisioned vms. This will
delete the vms and any modifications made to the environment will be lost.

```console
$ vagrant destroy
    host001: Are you sure you want to destroy the 'host001' VM? [y/N] y
==> host001: Forcing shutdown of VM...
==> host001: Destroying VM and associated drives...
==> host001: Running cleanup tasks for 'shell' provisioner...
==> host001: Running cleanup tasks for 'shell' provisioner...
==> host001: Running cleanup tasks for 'shell' provisioner...
    hub: Are you sure you want to destroy the 'hub' VM? [y/N] y
==> hub: Forcing shutdown of VM...
==> hub: Destroying VM and associated drives...
==> hub: Running cleanup tasks for 'shell' provisioner...
==> hub: Running cleanup tasks for 'shell' provisioner...
==> hub: Running cleanup tasks for 'shell' provisioner...
```

## Uninstall Vagrant Environment

When you have completed your evaluation are ready to use CFEngine on
production servers, remove the VMs that you created above by following these
simple instructions:

To remove the VMs entirely, type: `vagrant destroy`

If you are completely done and do not anticipate using them anymore, you can
also remove the base box `centos-6.5-x86_64-cfengine_enterprise-vagrant-201501201245` that was
downloaded. You can see it by typing `vagrant box list`. To delete the basebox
run `vagrant box remove centos-6.5-x86_64-cfengine_enterprise-vagrant-201501201245 virtualbox`.
**Note:** Running `vagrant up` from the vagrant project directory again will
re-download this basebox.

Vagrant and VirtualBox are useful general purpose programs, so you might want
to keep them around. If not, follow the standard procedures for your OS to
remove these applications.

[%CFEngine_include_markdown(common_next_steps.markdown)%]
