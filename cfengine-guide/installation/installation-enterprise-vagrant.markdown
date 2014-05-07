---
layout: default
title: Installing Enterprise Vagrant Environment
published: true
sorting: 30
tags: [getting started, installation, enterprise, vagrant]
---

This getting-started tutorial describes how to set up a client-server model
with CFEngine and, through policy, manage both machines. Vagrant will
create one VirtualBox VM to be the Policy Server (server), and another
machine that will be the Host Agent (client), or host that can be managed by CFEngine. Both will
will run CentOS 6.3 64-bit and communicate on a host-only network. Apart from
a one-time download of Vagrant and VirtualBox, this setup requires just one
command and takes between 5 and 15 minutes to complete (determined by your Internet
connection and disk speed). Upon installation, you are ready to start working with
CFEngine.

Note: VirtualBox requires that your computer support hardware virtualization in order to make use of the CentOS 64-bit virtual machines mentioned above. This is sometimes turned on or off in BIOS settings, but not all processors and motherboards necessarily support hardware virtualization. 

If your system lacks this support you will need to choose another computer to take advantage of the 64-bit virtual machines or install CFEngine using a different approach. See the following for other ways of installing CFEngine:

* Install and test the latest version using our [native version][Installing Enterprise 25 Free].
* Install CFEngine Enterprise for [production][Installing Enterprise for Production].
* Install and test the latest [version of Community][Installing Community]. 

## Overview

1. Install Vagrant
2. Install Virtualbox
3. Start CFEngine Enterprise
4. Log in to the Mission Portal
5. Stop CFEngine Enterprise
5. Uninstall 

## Install Vagrant

This tutorial uses Vagrant to configure your VMs. It is available for Linux,
Windows and MacOS and can be downloaded from vagrantup.com (use version
[1.3.5](http://downloads.vagrantup.com/tags/v1.3.5)). After downloading
Vagrant, install it on your computer.

## Install Virtualbox 

This tutorial uses VirtualBox to create virtual machines on your computer,
to which Vagrant deploys CFEngine. VirtualBox can be downloaded from
virtualbox.org (use version
[4.2.18](http://download.virtualbox.org/virtualbox/4.2.18/)). After downloading
VirtualBox, install it on your computer. 

**Note:** To avoid problems, disable other virtualization environments you are running.

## Start CFEngine Enterprise 

Step 1. Download our ready-made Vagrant project (use the
[tar-file](http://d1p7n4ueskxxum.cloudfront.net/enterprise-getting-started/vagrant_env-201311171314.tar.gz)
or the
[zip-file](http://d1p7n4ueskxxum.cloudfront.net/enterprise-getting-started/vagrant_env-201311171314.zip)
depending on your preference). 

Step 2. Save and unpack the file anywhere on your drive; this
creates a Vagrant Project directory called **vagrant_env**.

Step 3. Open a terminal
and navigate to the Vagrant Project directory (e.g. home/user/vagrant_env) and enter the following command: 

`$ vagrant up`
 
Vagrant performs the following processes:

* sets up two VirtualBox VMs 
* downloads a CentOS image and CFEngine packages 
* configures the VMs as a CFEngine Policy Server and a Host that are connected on a host-only
network. 

Depending on your Internet connection and disk speed, this process
should take about 5-15 minutes.

Note: If you want to use more hosts in your evaluation of CFEngine, you can
  edit the **Vagrantfile** text file in the directory that you have just created.
  Change the line that says "nodes = 1" to the number of hosts that you want in
  the setup. The maximum supported in this evaluation version of CFEngine is 25.

## Log in to the Mission Portal

At the end of the setup process, you can use your browser
to log in to the Mission Portal:

`http://localhost:9002`

username: admin

password: admin

The installation is complete! [Read on][Configure and Deploy a Policy Using Sketches (Enterprise Only)] to start your 
first lesson on how to use CFEngine.

## Stop CFEngine Enterprise 

To stop the VMs, but keep them around to continue your evaluation later,
open the terminal, go to the Vagrant directory, and type: 

`$ vagrant halt`

To resume, type:

`$ vagrant up`

## Uninstall the Enterprise Vagrant Environment

When you have completed your evaluation are ready to use CFEngine
on production servers, remove the VMs that you created above
by following these simple instructions:

To remove the VMs entirely, type: `vagrant destroy`

If you are completely done and do not anticipate using them anymore, you can
also remove the "base box" that was downloaded. To find the name of it, type
`vagrant box list`, copy the name of the box and then type `vagrant box remove
<name> virtualbox`. 

Vagrant and VirtualBox are useful general purpose programs,
so you might want to keep them around. If not, follow the standard procedures for
your OS to remove these applications.

<hr>
## Rate your experience

Everyone is a first-time user a some point. We want to make the CFEngine Enterprise installation process easy for all of our new users. 
Before you forget your first-time experience, we would love for you to let us know how we can improve on this process.

<iframe src="https://docs.google.com/forms/d/1i1bMHJltWEIL8K4FZ9HnuAOb7q0EeH6wswsKJ7oI1AM/viewform?embedded=true" width="760" height="800" frameborder="0" marginheight="0" marginwidth="0">Loading...</iframe>
