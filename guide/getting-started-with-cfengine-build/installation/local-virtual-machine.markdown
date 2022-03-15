---
layout: default
title: Local virtual machine
published: true
sorting: 15
tags: [guide, getting started, installation, modules]
---

This short tutorial shows you how to set up a Linux Virtual Machine locally, if you prefer this over creating an account and using an online cloud provider like Digital Ocean.

**Note:** If you are using Digital Ocean or another cloud platform, you don't need this tutorial.

## Download and install virtualization software

Install Vagrant and VirtualBox from their respective websites:

* [Vagrant](https://www.vagrantup.com/downloads)
* [VirtualBox](https://www.virtualbox.org/)

VirtualBox is used for virtualization, and vagrant is a nice way of interacting with the VirtualBox software, through the `vagrant` Command Line Interface (CLI), and in a `Vagrantfile`.

## SSH key

If you've never used SSH before, you need to generate a new SSH key:

```
$ ssh-keygen
```

You can use the defaults, just press enter instead of typing things.
After running the commands or if you already have been using SSH, you should be able to find your public key:

```
$ ls ~/.ssh/
id_rsa         id_rsa.pub     known_hosts
```

`id_rsa.pub` is the public key, which we will copy into the virtual machine for easy access over SSH.

**Note:** `id_rsa.pub` is the default filename, if you are using a different filename for the public key, pay attention and replace it later in the `Vagrantfile`.

## Create a project folder and Vagrantfile

We need a project folder where we will place the file(s) needed for both vagrant and later CFEngine:

```
$ mkdir -p ~/cfengine_project
$ cd ~/cfengine_project
```

Now, inside the folder, we can create and edit the `Vagrantfile`:

```
$ touch Vagrantfile
$ code Vagrantfile
```

(We are using `code`, VS Code, but you can use any editor you want).

Put this in your `Vagrantfile`:

```ruby
# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

    # Copy the SSH key to the VM(s):
    config.vm.provision "shell" do |s|
      ssh_pub_key = File.readlines("#{Dir.home}/.ssh/id_rsa.pub").first.strip
      s.inline = <<-SHELL
        echo #{ssh_pub_key} >> /home/vagrant/.ssh/authorized_keys
        echo #{ssh_pub_key} >> /root/.ssh/authorized_keys
      SHELL
    end

    # Ubuntu 20.04 VM, for CFEngine Enterprise Hub:
    config.vm.define "hub", autostart: false do |hub|
        hub.vm.box = "ubuntu/focal64"
        hub.vm.hostname = "hub"
        hub.vm.network "private_network", ip: "192.168.56.2"
        hub.ssh.insert_key = true
        hub.vm.provider "virtualbox" do |v|
            v.memory = 2048
            v.cpus = 4
        end
    end
end
```

The `Vagrantfile` above does some important things:

* Defines a Ubuntu 20.04 Virtual machine called `hub`, with hostname `hub`
* Sets its IP address to be `192.168.56.2`
* Sets how much memory and CPU cores we want the VM to have
* Copies the `id_rsa.pub` public key into the host when it starts, so we can use `ssh`

**Note:** The machine will be called `hub` in `vagrant`, `cf-remote` and in Mission Portal (based on hostname), but this is just because we were consistent when naming it in all 3 places.
These 3 names do not have to match, but it is easier to remember

## Start the Virtual Machine

To start our VM, make sure you've saved the file above, with the filename `Vagrantfile` and run this command in the same folder:

```
$ vagrant up hub
```

At this point, the VM should work like any Linux VM, similar to if you spawned it in the cloud, and we won't be using more features of vagrant or VirtualBox.

**Note:** Later, when you are done working with the Virtual Machine and want to get rid of it, run the following command:

```
$ vagrant destroy hub
```

## Back to CFEngine Installation

Now that you have a Linux VM ready, go back to the main tutorial to install CFEngine:

[Installation][Installation]
