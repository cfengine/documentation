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

CFEngine can define and configure an entire system consisting of interconnected devices, users, applications and services; help maintain that system over time; check its state at any given moment; ensure compliance with a desired end state; and propagate real-time modifications or updates to any of the system's component pieces.

## How CFEngine Works

CFEngine brings the actual state of a system into compliance with a model that defines the desired state of the system. 

The model is represented in one or more policies that have been written using CFEngine policy language. The policy language is declarative and has been designed with a vocabulary that is intuitive, yet at the same time can still support the design of highly complex IT systems.

Policies for the desired state are deployed to all of the system’s server hosts via pull requests, and afterwards further disseminated to each client host within the system. Every host machine within the system will then interpret and execute each of the instructions it has been given in a predetermined order. 

CFEngine monitors all of these activities in real-time, and should the system’s current state begin to drift away from the intended state then CFEngine will automatically take corrective action to bring everything back into compliance.

# Documentation

## Getting Started

* [How to Install CFEngine][Installing CFEngine]
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
* [More Getting Started][Getting Started]

### Recommended for Beginners

* ["Hello World" policy][Hello World]
* [Policy Language Examples][Policy]

### More About Policy Language

* [Policy Workflow][Policy Workflow] 
* [Syntax, identifiers, and names][Syntax, identifiers and names] 
* [Promise types and attributes][Promise Types and Attributes]

### Design Center
 
* [Design Center API](https://cfengine.com/docs/master/manuals-design-center.html)
* [Design Center Advanced Walkthrough][Advanced Walkthrough]

## Enterprise Edition Documentation

* [Reporting Architecture][Reporting Architecture]
* [Creating Reports with SQL Queries][SQL Queries] 
* [Enterprise API Reference][Enterprise API Reference]

## Reference Documentation

* [Functions][Functions]
* [Special Variables][Special Variables]
* [Hard and Soft Classes][Hard and Soft Classes]
* [Components and Common Control][components]









