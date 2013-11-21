---
layout: default
title: Installing CFEngine
sorting: 10
categories: [Getting Started, Installation]
published: true
alias: getting-started-installation.html
tags: [getting started, installation]
---

## General Requirements

CFEngine recommends the following:

**Host(s) Memory** 

256 MB available memory in order to run the CFEngine agent software (cf-agent).

**Disk Storage** 

<<<<<<< HEAD
A full installation of CFEngine requires 25 MB. Additional disk usage
depends on your specific policies, especially those that concern reporting.
=======
Install and test the latest [version of Community][Installing Community]. In addition to 
instructions, the section also includes simple tutorials to get you started, followed by more 
advanced tutorials to help your learn the CFEngine language and functionality.
>>>>>>> dd8938b... Minor tweaks to all docs; added Feedback page to installation docs

**Network** 

* Verify that the machine’s network connection is working and that port 5308
  (used by CFEngine) is open for both incoming and outgoing connections.

<<<<<<< HEAD
* If iptables are active on your operating system, stop this service or adapt
  it to allow for communication on the above ports. If applicable, type the
  following two commands: /`etc/init.d/iptables stop` and `chkconfig iptables
  off`

CFEngine bundles all critical dependencies into the package; therefore,
additional software is not required.
=======
All installations feature instructions and tutorials. One tutorial teaches you how to use the 
Mission Portal console; the others help your learn the CFEngine language and functionality. 

Just the installation that best suits your needs.

#### CFEngine Enterprise (Evaluation: 25 free servers)

* Install and test the latest version using our pre-packaged [Vagrant environment][Installing Enterprise Vagrant Environment].

* Install and test the latest version using our [native version][Installing Enterprise 25 Free].

#### CFEngine Enterprise (Production)

Install CFEngine Enterprise for [production][Installing Enterprise for Production].
>>>>>>> dd8938b... Minor tweaks to all docs; added Feedback page to installation docs

## Specific Requirements

Click here to complete the [Community][Installing Community] installation.

Click here to complete the [Enterprise][Installing Enterprise] installation.
