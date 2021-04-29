---
layout: default
title: Installing Enterprise 25 Free
published: true
sorting: 20
tags: [getting started, installation, enterprise free]
---

These instructions describe how to install the latest version of CFEngine Enterprise 25 Free. This is the full
version of CFEngine Enterprise, but the number of Hosts (clients) is limited to 25.

**Note the following requirements:**

* To install this version of CFEngine Enterprise, your machine must be running a recent version of Linux.
This installation script has been tested on RHEL 5 and 6, SLES 11, CentOS 5 and 6, and Debian 6 and 7.
* You need a minimum of 2 GB of available memory and a modern 64 bit processor.
* Plan for approximately 100MB of disk space per host. You should provide an
extra 2G to 4G of disk space if you plan to bootstrap more hosts later.
* You need a least two VMs/servers, one for the Policy Server and one for a Host (client). They must be on the same network.
* The Policy Server needs to run on a dedicated OS with a vanilla installation (i.e. it only has repositories and packages officially
supported by the OS vendor)

## Installation Overview

During the course of the instructions outlined in this guide, you will perform the following tasks:

* **Install CFEngine Enterprise onto a Policy Server and onto Hosts.**
A Policy Server (hub) is a CFEngine instance that contains promises (business policy) that get deployed to Hosts.
Hosts are clients that retrieve and execute promises.
* **Bootstrap the Policy Server to itself and then bootstrap each of the Hosts to the Policy Server.** Bootstrapping establishes a trust relationship between the Policy Server
and all Hosts. Thus, business policy that you create in the Policy Server can be deployed to Hosts throughout your company.
Bootstrapping completes the installation process.
* **Log in to the Mission Portal.** The Mission Portal is a graphical user interface that allows you to verify the
the actual state of all your Hosts, thus ensuring that your promises are being executed.
* **Try out the Tutorials.** Links to three tutorials give you a head start on learning CFEngine.


## 1. Download and install Enterprise on a Policy Server

Please Note: Internet access is required from the host if you wish to use the quick install script.

Run the following script on your designated Policy Server (hub) 64-bit machine (32-bit is not supported on the Policy Server):

```console
$ wget https://s3.amazonaws.com/cfengine.packages/quick-install-cfengine-enterprise.sh  && sudo bash ./quick-install-cfengine-enterprise.sh hub
```

This script installs the latest CFEngine Enterprise Policy Server on your machine.

## 2. Bootstrap the Policy Server

The Policy Server must be bootstrapped to itself. Find the IP address of your Policy Server (type $ ifconfig).

Run the bootstrap command:

```console
$ sudo /var/cfengine/bin/cf-agent --bootstrap <IP address of policy server>
```

**Example: $ sudo /var/cfengine/bin/cf-agent --bootstrap 192.168.1.12**

Upon successful completion, a confirmation message appears: "Bootstrap to '192.168.1.12' completed successfully!"

Type the following to check which version of CFEngine your are running:

```console
$ /var/cfengine/bin/cf-promises --version
```

The Policy Server is installed.

## 3. Install Enterprise on Hosts

Install Enterprise on your designated Host(s) by running the script below. Per the **Free 25** agreement, you can
install Enterprise on 25 Hosts. Note that the Hosts must be
on the same network as the Policy Server that you just installed in Step 2.

```console
$ wget https://s3.amazonaws.com/cfengine.packages/quick-install-cfengine-enterprise.sh  && sudo bash ./quick-install-cfengine-enterprise.sh agent
```

Note that this installation works on 64- and 32-bit machines.

## 4. Bootstrap the Host to the Policy Server

All Hosts must be bootstrapped to the Policy Server in order to establish a connection between the Host and
the Policy Server. Run the same commands that you ran in Step 3.

```console
$ sudo /var/cfengine/bin/cf-agent --bootstrap <IP address of policy server>
```

**Example: $ sudo /var/cfengine/bin/cf-agent --bootstrap 192.168.1.12**

The installation process is complete and CFEngine Enterprise is up and running on your system.

## 5. Log in to the Mission Portal

The Mission Portal is immediately accessible. Connect to the Policy Server
through your web browser at:

http://`<IP address of your Policy Server>`

username: admin
password: admin

The Mission Portal runs TCP port 80 by default. (Click [here] (https://cfengine.zendesk.com/entries/25005193-Configure-Mission-Portal-to-use-HTTPS-instead-of-HTTP)
to configure the Mission Portal to use HTTPS instead of HTTP.) During the initial setup, the Host(s) might take a few minutes to show up in the Mission Portal. Simply refresh the web page
and login again if necessary.

Note: If you are running Enterprise with Vagrant, you must add the
correct port: http://localhost:<port> in your browser.  The <port> is the port-forwarder
number you use in your **Vagrantfile** (e.g. policyserver.vm.network "forwarded_port", guest: 80, host: 8080; the port will be 8080).

<hr>

## Tutorials

* [Tutorial for Running Examples][Examples and Tutorials#Tutorial for Running Examples]

* [Distribute files from a central location.][Distribute files from a central location]

  Whereas the first tutorial in this list teaches you how to deploy business policy
  through the Mission Portal, this advanced, command-line tutorial shows you how to distribute policy files from the Policy Server to all pertinent Hosts.

## Recommended Reading

* [CFEngine Guide][Guide]
* [Tutorials and Examples][Examples and Tutorials]
