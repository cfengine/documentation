---
layout: default
title: CFEngine 3.6
categories: [CFEngine 3.6]
published: true
sorting: 1
alias: index.html
---

# Overview

* Learn [about CFEngine](#what-is-cfengine) and [how CFEngine works](#how-cfengine-works).
* See an [overview of the documentation](#documentation).
* [Get started](#getting-started) with CFEngine.
* Read [about policy language](#policy-language) and see [some examples of policy language](#policy-language-by-way-of-example).
* Find out more about the [Design Center](#design-center).
* Search the [reference documentation](#reference-documentation).
* Discover [CFEngine Community Edition](#community-edition) and [CFEngine Enterprise Edition](#enterprise-edition).

# Introduction  

## What is CFEngine? ##

CFEngine is a configuration management system that provides a framework for automated management of IT infrastructure throughout its life cycle.

CFEngine is decentralized and highly scalable. It is powered by autonomous agents that can continuously monitor, self-repair, and update or restore an entire IT system every five minutes, with negligible impact on system resources or performance.

CFEngine:

* Defines the configuration of an entire IT system consisting of interconnected:
	* Devices
	* Users
	* Applications
	* Services 
* Helps maintain that system over time. 
* Checks the system state at any given moment. 
* Ensures compliance with a desired system state. 
* Propagates real-time modifications or updates across the system.

What next:
* Back to the [introduction](#introduction).
* Find out [how CFEngine works](#how-cfengine-works)
* See other [documentation](#documentation).

## How CFEngine Works ##

CFEngine ensures that the actual state of a system is in compliance with the predefined model of desired state for the system. If it is not in compliance CFEngine will bring it into compliance.

That model is represented by one or more policies that have been written using the declarative CFEngine policy language. The policy language has been designed with a vocabulary that is intuitive, yet at the same time can still support the design of highly complex IT systems.

Those policies are distributed across all of the system’s policy distribution servers via pull requests, and then further disseminated to each end host within the system. Every host will then interpret and execute each of the instructions it has been given in a predetermined order. 

CFEngine continually monitors all of the hosts in real-time, and should the system’s current state begin to drift away from the intended state then CFEngine will automatically take corrective action to bring everything back into compliance.

What next:
* Back to the [introduction](#introduction).
* See other [documentation](#documentation).

# Documentation #

## About CFEngine ##

* [Design of CFEngine][Design]
* Phases of CFEngine System Management
	* Build
	* Deploy
	* Manage
	* Audit 

## Getting Started ##

* [How to Install CFEngine][Installing CFEngine]
* [Get CFEngine Up and Running Quickly][Up and Running]
* [Tutorials][Tutorials]
* [More Getting Started][Getting Started]

### Components ###

* [The CFEngine Components][The CFEngine Components]
	* Core Components:
		* [cf-agent][cf-agent]
		* [cf-serverd][cf-serverd]
		* [cf-execd][cf-execd]
		* [cf-promises][cf-promises]
		* [cf-runagent][cf-runagent]

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

#### Design Center ####
 
* [Design Center][Design Center]
* [Advanced Walkthrough][Advanced Walkthrough]
* [Sketches][Sketch Structure]

## CFEngine Reference Documentation ##

* [Components and Common Control][Components and Common Control]
* [Promise Types and Attributes][Promise Types and Attributes]
* [Functions][Functions]
* [Hard and Soft Classes][Hard and Soft Classes]
* [Special Variables][Special Variables]
* [Syntax, identifiers and names][Syntax, identifiers and names]

# CFEngine Versions #

## Community Edition ##

Built upon well-established theory and high-quality engineering practices, CFEngine has enjoyed an outstanding security record over its 20-year history. 

CFEngine Community is licensed under the Gnu General Public License GPL, version 3 and available as a free-of charge download or in source form.

## Enterprise Edition ##

CFEngine Enterprise contains the following additional features:

* Graphical User Interface for Design Center 
* Design Center sketches with integrated monitoring and reporting
* Delegation of System Administrator Tasks 
* Version Control for Sketches 
* Increased scalability 	
* Configurable Data Feeds
* Federation and SQL Reporting

### Reporting ###
* [Reporting Architecture][Reporting Architecture]
* [Creating Reports with SQL Queries][SQL Queries] 

### APIs ###
* [Enterprise API Reference Documentation][Enterprise API Reference]












