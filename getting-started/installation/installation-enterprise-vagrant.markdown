---
layout: default
title: Installing Enterprise Vagrant Environment
categories: [Getting Started, Installation, Installing Enterprise Vagrant Environment]
published: true
alias: getting-started-installation-installing-enterprise-vagrant.html
tags: [getting started, installation, enterprise, vagrant]
---

This getting started tutorial will show you how to set up a client-server model
with CFEngine, and through policy, manage both machines. Vagrant will
create one VirtualBox VM to be the server (Policy Server), while the other
machine will be the Client, a host that can be managed by CFEngine. Both will
will run CentOS 6.3 64-bit, and communicate on a host only network. Apart from
a one-time download of Vagrant and VirtualBox, the setup requires just one
command and takes less 5 - 15 minutes to complete (determined by your internet
connection and disk speed). After that you are ready to start working with
CFEngine.

Overview

1. Install Vagrant
2. Install Virtualbox
3. Initalize CFEngine Enterprise Vagrant Project
4. Log in to Mission Portal
5. Uninstall

# Install Vagrant

This guide will use Vagrant to configure your VMs. It is available for Linux,
Windows and MacOS and can be downloaded from vagrantup.com (please use version
[1.3.5](http://downloads.vagrantup.com/tags/v1.3.5)). After downloading
Vagrant, install it on your computer.

# Install Virtualbox 

This tutorial will use VirtualBox to create virtual machines on your computer,
to which Vagrant will deploy CFEngine. VirtualBox can be downloaded from
virtualbox.org (please use version
[4.2.18](http://download.virtualbox.org/virtualbox/4.2.18/)). After downloading
VirtualBox, install it on your computer.

# Initalize CFEngine Enterprise Vagrant Project

Download our ready made Vagrant project (use the
[tar-file](http://d1p7n4ueskxxum.cloudfront.net/enterprise-getting-started/vagrant_env-201311171314.tar.gz)
or the
[zip-file](http://d1p7n4ueskxxum.cloudfront.net/enterprise-getting-started/vagrant_env-201311171314.zip)
depending on your preference). Save and unpack the file on your drive - this
will create a Vagrant Project directory called "vagrant_env". Open a terminal
and navigate to this directory and enter the command `vagrant up`. Vagrant will
set up 2 VirtualBox VMs, download a CentOS image and CFEngine packages, and
configure them as a CFEngine Policy Server and a Host, connected on a host-only
network. Depending on your internet connection and disk speed, this process
should take about 5-15 minutes.

  Note: If you want to use more hosts in your evaluation of CFEngine, you can
  edit the "Vagrantfile" text-file in the directory that you have just created.
  Change the line that says "nodes = 1" to the number of hosts that you want in
  the setup. The maximum supported in this evaluation version of CFEngine is 25).

# Log in to Mission Portal

At the end of the setup process, you'll see the instruction to use your browser
to log into the Mission Portal (in our case at http://localhost:9002). Log in
with username and password both "admin".

Congratulations, you are now ready to start your first lesson on how to use
CFEngine! [Read on][Configure and Deploy a Policy Using Sketches (Enterprise
Only)] to get going.

# Uninstall

When you are done with your evaluation and want to graduate to using CFEngine
on production servers you can remove the VMs that you created in the above
steps with very simple instructions:

To stop the VMs, but keep them around to continue your evaluation later,
open the terminal, go to the Vagrant directory and type: `vagrant halt` (type
`vagrant up` to resume after that) To remove the VMs entirely, type `vagrant
destroy`.

If you are completely done and do not anticipate to use them anymore, you can
also remove the "base box" that was downloaded. To find the name of it, type
`vagrant box list`, copy the name of the box and then type `vagrant box remove
<name> virtualbox` Vagrant and VirtualBox are useful general purpose programs,
so you may want to keep them around. If not, follow the standard procedures for
your OS to remove these applications.

