---
layout: default
title: CFEngine 3.6
categories: [CFEngine 3.6]
published: true
sorting: 1
alias: index.html
---

# Introduction

## What is CFEngine?

CFEngine is a configuration management system that provides a framework for automated management of IT infrastructure throughout its lifecycle.

CFEngine can:

* Define and configure an entire IT system consisting of interconnected:
	* Devices
	* Users
	* Applications
	* Services 
* Help maintain that system over time. 
* Check the system state at any given moment. 
* Ensure compliance with a desired system state. 
* Propagate real-time modifications or updates across the system.

## How CFEngine Works

CFEngine brings the actual state of a system into compliance with a defined model for the desired state of the system. 

That model is represented in one or more policies that have been written using the declarative CFEngine policy language. The policy language has been designed with a vocabulary that is intuitive, yet at the same time can still support the design of highly complex IT systems.

Policies for the desired state are deployed to all of the system’s server hosts via pull requests, and then further disseminated to each client host within the system. Every host machine within the system will then interpret and execute each of the instructions it has been given in a predetermined order. 

CFEngine continually monitors all of these activities in real-time, and should the system’s current state begin to drift away from the intended state then CFEngine will automatically take corrective action to bring everything back into compliance.

# Documentation

## Getting Started

* [How to Install CFEngine][Installing CFEngine]
* [The CFEngine Components][The CFEngine Components]

### Define Your Desired State Using Policy Language

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

#### Policy Language by Example

* ["Hello World" Policy Language Example][Hello World]
* [Other Policy Language Examples][Policy]

#### More About Policy Language

* [Policy Workflow][Policy Workflow] 
* [Syntax, Identifiers, and Names][Syntax, identifiers and names] 
* [Promise Types and Attributes][Promise Types and Attributes]

### Design Center
 
* [Design Center][Design Center]
* [Design Center Advanced Walkthrough][Advanced Walkthrough]

### More Getting Started Information
* [More Getting Started][Getting Started]

## Enterprise Edition Documentation

### Reporting
* [Reporting Architecture][Reporting Architecture]
* [Creating Reports with SQL Queries][SQL Queries] 

### APIs
* [Enterprise API Reference Documentation][Enterprise API Reference]

## Reference Documentation

* [Components and Common Control][Components and Common Control]
* [Promise Types and Attributes][Promise Types and Attributes]
* [Functions][Functions]
* [Hard and Soft Classes][Hard and Soft Classes]
* [Special Variables][Special Variables]
* [Syntax, identifiers and names][Syntax, identifiers and names]










