---
layout: default
title: Installation
published: true
sorting: 10
tags: [guide, getting started, installation, modules]
---

CFEngine allows you to configure and automate all your IT infrastructure, including, servers, desktops and IoT devices.
It enables efficient changes across large fleets of devices and automatic self-healing / drift correction according to the desired state.
With it's flexible and performant reporting system, you can have up to date inventory and compliance reports even with hundreds of thousands of endpoints under management.

[CFEngine Build](https://build.cfengine.com) is the website where the CFEngine users can share and find modules from the rest of the community.
These modules allow you to add functionality and achieve useful tasks in CFEngine without writing any code.

In this tutorial series we will learn CFEngine the easy way, first focusing on installation, out of the box functionality, ready to use modules, and the web user interface (Mission Portal).
Afterwards, we will continue to more advanced topics, such as policy writing and module development.

![](https://cfengine.com/images/overview/cfe-desktop.svg)

In CFEngine you mainly interact with the CFEngine Hub, for example using the Mission Portal Web UI, APIs, ssh, or git.
All other hosts in your infrastructure will communicate with the hub, to fetch policy, modules and data, and to send back reporting data.
For you, this means that the experience of working with just 1 host, or 1000 hosts, is largely the same.
So, the only thing you need to get started is to set up 1 CFEngine Hub.

## Linux virtual machine

CFEngine runs on a wide variety of platforms, including Windows, Mac, Linux, and BSD.
For this tutorial, to make things simple, we are going to recommend one way to install and work with CFEngine.
We will use an Ubuntu 20.04 Linux virtual machine as the CFEngine Hub, and we will interact with it using SSH and some python tools which you can install on your desktop / laptop.

If you've never set up a virtual machine (VM) before, these are some easy ways:

* Cloud: Create a VM in Digital Ocean, AWS, or any other cloud vendor. **(Recommended)**
* Mac OS: Install and run Vagrant and Virtual Box.
* Linux: Install and run Vagrant and libvirt.
* Windows: Use Windows Subsystem for Linux (WSL).

## Development machine and CFEngine Hub

When you've set up a Linux VM there are now 2 machines we will be talking about:

![](machines.png)

Your **development machine** is the machine you have in front of you, it can be any platform (Linux, Mac, Windows, ...).
This is where you will run a terminal, browser, text editor, and some python tools.

The **CFEngine hub** is the aforementioned Ubuntu 20.04 VM.
We will access this via SSH, and install CFEngine there.

## Install python 3 on your development machine

**On macOS:**

Install brew from [brew.sh](https://brew.sh/).
Use brew to install Python 3:

```
$ brew install python3
```

**On Ubuntu:**

```
$ sudo apt-get install python3 python3-pip
```

If you are using Windows and Ubuntu inside of WSL, the command is the same.
Not all systems use `apt-get` as the package manager - if you are not using Ubuntu, look up how to install python 3 and pip on your system.

**Check that it was successful:**

To continue, you will need to be able to use `python3` and `pip3`:

```
$ python3 --version
Python 3.8.10
```

```
$ pip3 --version
pip 20.0.2 from /usr/lib/python3/dist-packages/pip (python 3.8)
```

The python version must be at least 3.6, and it's important that the pip output shows a matching python version (otherwise pip is using another installation of python).

## Install CFEngine tools on your development machine

In this tutorial series, we will be using 2 command line tools: `cf-remote` and `cfbs`.
These are small python tools and don't make changes to your system, they are only for working with CFEngine projects, modules, and installing / deploying to remote machines.

**On macOS:**

```
pip3 install cfbs cf-remote
```

**On Linux / WSL:**

```
sudo pip3 install cfbs cf-remote
```

There are many ways to install command line tools with pip, if you want to do it without sudo, and install it in your home directory, and edit the PATH variable, you can.
The command above is a suggestion which should work for most people.
Importantly, you need the command line tools working after you've installed them:

```
$ cfbs --version
cfbs 1.2.1
$ cf-remote --version
cf-remote version 0.3.9
Available CFEngine versions:
master, 3.19.0, 3.18.x, 3.18.1, 3.18.0, 3.15.x, 3.15.5, 3.15.4, 3.15.3, 3.15.2, 3.15.1, 3.15.0, 3.15.0b1
```

## SSH user and IP address

Find the IP address of your virtual machine, and the username so you can log in with SSH.
In my case, in Digital Ocean, the username is `root`, and the IP is `128.199.44.119` (found in top left of droplet screen as "ipv4"):

![](digital_ocean.png)

**On your development machine:**

Test that ssh works:

```
$ ssh root@128.199.44.119
```

Remember to replace the IP and username with what works in your case.

## Install CFEngine

From your development machine, use `cf-remote` to install CFEngine on the Linux VM:

```
$ cf-remote install --hub "root@128.199.44.119" --bootstrap "$HUB"
```

## Open the CFEngine Web UI

Open a browser and put in the IP address of the hub in the address bar (same IP as in last step).
You should see the CFEngine Enterprise login screen.
Log in with username admin, password admin, and you will be asked to change the password.

![](mp_login.png)

After changing the password to something more secure, you should be able to log in and see the dashboard.

## Next steps

Now that you have a CFEngine Hub working and the tooling on your development machine, you can go to the next part and start adding modules:

[Modules from CFEngine Build][Modules from CFEngine Build]
