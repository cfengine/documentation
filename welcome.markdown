---
layout: default
title: CFEngine 3.6
categories: [CFEngine 3.6]
published: true
sorting: 1
alias: index.html
---

# Introduction

* Learn [about CFEngine](#what-is-cfengine) and [how CFEngine works](#how-cfengine-works).
* See an [overview of the documentation](#documentation).
* [Get started](#getting-started) with CFEngine.
* Know more about CFEngine Community Edition and CFEngine Enterprise Edition.
* Read [about policy language](#policy-language) and see [some examples of policy language](#policy-language-by-way-of-example).
* Find out more about the [Design Center](#design-center).
* Search the [reference documentation](#reference-documentation).
  

## What is CFEngine? ##

CFEngine is a configuration management system that provides a framework for automated management of IT infrastructure throughout its life cycle.

CFEngine:

* Defines the configuration of an entire IT system that consists of interconnected:
	* Devices
	* Users
	* Applications
	* Services 
* Helps maintain that system over time. 
* Checks the system state at any given moment. 
* Ensure compliance with a desired system state. 
* Propagate real-time modifications or updates across the system.

## How CFEngine Works ##

CFEngine ensures that the actual state of a system is in compliance with the predefined model of desired state for the system. If it is not in compliance CFEngine will bring it into compliance.

That model is represented by one or more policies that have been written using the declarative CFEngine policy language. The policy language has been designed with a vocabulary that is intuitive, yet at the same time can still support the design of highly complex IT systems.

Those policies are distributed across all of the system’s policy distribution servers via pull requests, and then further disseminated to each end host within the system. Every host will then interpret and execute each of the instructions it has been given in a predetermined order. 

CFEngine continually monitors all of the hosts in real-time, and should the system’s current state begin to drift away from the intended state then CFEngine will automatically take corrective action to bring everything back into compliance.

# Documentation #

## Getting Started ##

* [How to Install CFEngine][Installing CFEngine]
* [Tutorials][Tutorials]
* [The CFEngine Components][The CFEngine Components]

### Policy Language ###

* [CFEngine Policy Language Concepts][Language Concepts]
	* [Promises][promises]
	* [Bundles][bundles]
	* [Bodies][bodies]
	* [Classes and Decisions][classes and decisions]
	* [Variables][variables]
	* [Normal Ordering][Normal Ordering]
	* [Loops][Loops]
	* [Pattern Matching and Referencing][Pattern Matching and Referencing]
	* [Namespaces][namespaces]
* [How to Write Policy][Writing Policy]

#### Policy Language By Way Of Example ####

* ["Hello World" Example Policy][Hello World]
* [Other Policy Language Examples][Policy]

#### More About Policy Language ####

* [Policy Workflow][Policy Workflow] 
* [Syntax, Identifiers, and Names][Syntax, identifiers and names] 
* [Promise Types and Attributes][Promise Types and Attributes]

### Design Center ###
 
* [Design Center][Design Center]
* [Design Center Advanced Walkthrough][Advanced Walkthrough]

### More Getting Started Information ###
* [More Getting Started][Getting Started]
* [Get CFEngine Up and Running Quickly][Up and Running]

## CFEngine Reference Documentation ##

* [Components and Common Control][Components and Common Control]
* [Promise Types and Attributes][Promise Types and Attributes]
* [Functions][Functions]
* [Hard and Soft Classes][Hard and Soft Classes]
* [Special Variables][Special Variables]
* [Syntax, identifiers and names][Syntax, identifiers and names]

## Enterprise Edition Documentation ##

### Reporting ###
* [Reporting Architecture][Reporting Architecture]
* [Creating Reports with SQL Queries][SQL Queries] 

### APIs ###
* [Enterprise API Reference Documentation][Enterprise API Reference]












