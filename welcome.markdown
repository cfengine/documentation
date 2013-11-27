---
layout: default
title: CFEngine 3.6
categories: [CFEngine 3.6]
published: true
sorting: 1
alias: index.html
---

## Welcome to the CFEngine Documentation site

CFEngine is a configuration management system that enables system administrators to define 
the desired end states of IT-systems throughout their organizations. The desired state is 
expressed through policies written using the CFEngine policy language. A **policy** is a 
collection of **promises**, or declared intentions that you wish to reach based on your business needs. 
This policy is typically version-controlled like any other software code, and is made available on a server (hub). 
From there, the policy is automatically pulled down by hosts (clients) that retrieve and execute these promises 
locally. They ensure the defined state.

CFEngine agents continuously ensure compliance with your desired state. The hub pulls down 
and collects reports on actual states or failures encountered while implementing the desired 
state on each and every host. You can read logs or run reports to verify the actual state of your IT-system.

Follow this workflow and examine the relevant links as you get started with CFEngine:

## Install CFEngine

* Choose from Community or Enterprise [versions][Installing CFEngine]

## Define your desired state

Your system state is defined by **writing policy**.

* Create a Hello World [policy][Hello World]
* Learn how to write your own [policy][Writing Policy]
* View policy [examples][Policy]

Your system state can also be defined through reusable policy templates, called **sketches**. 

* [Enterprise Edition](https://cfengine.com/docs/master/manuals-design-center.html): Learn how to use the Design Center API via the Mission Portal to 
install, configure, and deploy sketches. View and activate sketches in the Design Center 
through the Mission Portal.  
* [Community Edition][Advanced Walkthrough]: Learn how to use the Design Center API (via cf-sketch) to install, 
configure, and deploy sketches into the Masterfiles directory. 

**Recommended for Beginners**

* Policy is written in [CFEngine Language][Language Concepts]
* Learn the policy [workflow][Policy Workflow] 
* Learn CFEngine [syntax][Syntax, identifiers and names], identifiers, and names 
* [Promise types and attributes][Promise Types and Attributes] are necessary for writing policy

## Verify your actual state (Enterprise Only)

Verify your actual state through **Reports**.

* Learn about the [reporting architecture][Reporting Architecture]
* Create reports with [SQL Queries][SQL Queries] 
* Use the Design Center Reports (Documentation is forthcoming)

## References

* [Functions][Functions]
* Special [variables][Special Variables]
* Hard and soft [classes][Hard and Soft Classes]
* [Enterprise API][Enterprise API] reference

**Recommended for Beginners**

* Learn the [components][Components and Common Control] that make up CFEngine


