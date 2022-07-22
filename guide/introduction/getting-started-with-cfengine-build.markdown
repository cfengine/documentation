---
layout: default
title: Getting started with CFEngine Build
published: false
sorting: 40
tags: [guide, getting started, installation, modules]
---

{% comment %}
Nick Anderson set published to false as part of Information Architecture changes.
This content https://docs.cfengine.com/docs/master/guide-introduction-getting-started-with-cfengine-build.html
Seems to be incomplete and nearly duplicates https://docs.cfengine.com/docs/master/guide-getting-started-with-cfengine-build.html
Preferring the latter so unpublished this one.
Promises you cannot keep are no better than lies!
https://www.youtube.com/watch?v=Zd9-wdGzedU {% endcomment %}

[CFEngine Build](https://build.cfengine.com) is the website where the CFEngine users can share and find modules from the rest of the community.
These modules allow you to add functionality and achieve useful tasks in CFEngine without writing any code.

In this tutorial we will install CFEngine and use some modules from CFEngine Build.
No prior experience with CFEngine or policy language is required, the only thing you need is a Linux system.

## Linux virtual machine

We recommend using Ubuntu 20.04 and running it in a virtual machine (VM), but these are not strict requirements.
Most flavors of Linux will work.
A virtual machine is not required, but is nice - it enables you to experiment safely without making changes to your system, and provides you an easy way to start over (delete and recreate the VM).

If you've never set up a virtual machine before, these are some easy ways:

* Cloud: Create a VM in Digital Ocean, AWS, or any other cloud vendor. **(Recommended)**
* Mac OS: Install and run Vagrant and Virtual Box.
* Linux: Install and run Vagrant and libvirt.
* Windows: Use Windows Subsystem for Linux (WSL).

We will use SSH to log into the machine and deliver code/files to it, so make sure you are able to log in to the machine with ssh. If you are on Linux, and will not be using a virtual machine, please note that you will have to run some things as root using `sudo`, and you will be making some changes to your Linux machine.

## Install python on your development machine

First, we will set up the tooling you are going to use on the machine you are working on.
This is the machine where you can open terminals, and text editors, make `git commits`, etc.
It doesn't have to be Linux - macOS and Windows (WSL) work well.
If you are working on Ubuntu, run:

```
$ sudo apt-get install python3 python3-pip
```

Some platforms don't use `apt`, so use the package manager available to you, such as `brew`, or `yum`.
If you can't / don't want to use a package manager, you can also install python and pip from the python website.

## Insall dependencies for working with CFEngine Build and CFEngine hosts
