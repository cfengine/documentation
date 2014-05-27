---
layout: default
title: Glossary
sorting: 10
published: true
tags: [overviews, leanring resources, glossary]
---

* [Agent][Glossary#agent]
* [Authentication][Glossary#authentication]
* [Body][Glossary#body]
* [Bootstrap][Glossary#bootstrap]
* [Bundles for Knowledge][Glossary#bundles-for-knowledge]
* [Bundle][Glossary#bundle]
* [Call Collect][Glossary#call-collect]
* [Classes][Glossary#classes]
* [CMDB][Glossary#cmdb]
* [Commands][Glossary#commands]
* [Common Control][Glossary#common-control] 
* [Components][Glossary#components]
* [Datatypes][Glossary#datatypes]
* [Decisions][Glossary#decisions]
* [Design Center][Glossary#design-center]
* [Design Center API][Glossary#design-center-api]
* [Design Center App][Glossary#design-center-app]
* [Directories][Glossary#directories]
* [Distribution][Glossary#distribution]
* [Enterprise API][Glossary#enterprise-api]
* [Enterprise Reporting][Glossary#enterprise-reporting]
* [File Structure][Glossary#file-structure]
* [Frequency][Glossary#frequency]
* [Functions][Glossary#functions]
* [Functions][Glossary#functions]
* [Host][Glossary#host]
* [Hub][Glossary#hub]
* [Logs][Glossary#logs]
* [Loops][Glossary#loops]
* [Menus][Glossary#menus]
* [Mission Portal][Glossary#mission-portal]
* [Monitoring][Glossary#monitoring]
* [Namespaces][Glossary#namespaces]
* [Networking][Glossary#networking]
* [Normal Ordering][Glossary#normal-ordering]
* [Operators][Glossary#operators]
* [Pattern Matching][Glossary#pattern-matching]
* [PCI compliance][Glossary#pci-compliance]
* [Policy Levels][Glossary#policy-levels]
* [Policy Server][Glossary#policy-server]
* [Policy Writing][Glossary#policy-writing]
* [Policy][Glossary#policy]
* [Precedence][Glossary#precedence]
* [Promise Attributes][Glossary#promise-attributes]
* [Promise Types][Glossary#promise-types]
* [Promise][Glossary#promise]
* [Referencing][Glossary#referencing]
* [Report Collector][Glossary#report-collector]
* [Reporting][Glossary#reporting]
* [Reports][Glossary#reports]
* [Role-Based Acess Control (RBAC)][Glossary#role-based-acess-control-(rbac)]
* [Scope][Glossary#scope]
* [Server][Glossary#server]
* [Sketch Activation][Glossary#sketch-activation]
* [Sketches][Glossary#sketches]
* [Special Variables][Glossary#special-variables]
* [Standard Library][Glossary#standard-library]
* [Syntax][Glossary#syntax]
* [Variables][Glossary#variables]
* [Version Control][Glossary#version-control]

#### Agent ####

A piece of software that runs independently and automatically to carry out a task (think software robot). Inn CFEngine, the agent is called cf-agent and is responsible for making changes to computers. 

#### Authentication ####
#### Body ####

A promise body is the description of exactly what is promised (as opposed to what/who is making the promise). The term `body' is used in the CFEngine syntax to mean a small template that can be used to contribute as part of a larger promise body. 

#### Bootstrap ####
#### Bundles for Knowledge ####
#### Bundle ####

In CFEngine, a bundle refers to a collection of promises that has a name. 

#### Call Collect ####
#### Classes ####

#### CMDB ####

A Configuration Management Database. A term coined as part of the IT Infrastructure Library (ITIL) as an outgrowth of an inventory database. 

#### Commands ####
#### Common Control ####
#### Components ####

Standalone applications include cf-agent, cf-promises, cf-runagent, cf-know, cf-report, cf-hub, cf-sketch

Daemons include cf-execd, cf-monitord, and cf-serverd
(Hello) Sketches

#### Datatypes ####
#### Decisions ####

#### Design Center ####

The collection of sketches and the tools that allow you to manipulate and manage them.

See Also: [Design Center Overview][Design Center Overview],
[Design Center in CFEngine Enterprise][Design Center in CFEngine Enterprise]

#### Design Center API ####

Performs all operations related to sketches, parameter sets, environments, validations, and deployment. 

See also: [The Design Center API][The Design Center API]

#### Design Center App #### 

The Design Center user interface app that is located on the Mission Portal console for CFEngine Enterprise users.

#### Directories ####
#### Distribution ####
#### Enterprise API ####
#### Enterprise Reporting ####
#### File Structure ####
#### Frequency ####
#### Functions ####
#### Host ####

UNIX terminology for a computer the runs `guest programs'. In practice, `host' is a synonym for `computer'. 

#### Hub ####

A software component in CFE Nova and CFE Constellation that works as a single point of management in a local `star-network'. The term hub is sometimes used to mean policy distribution server, but more commonly a running cf-hub process that does report collection from all CFEngine managed hosts. The term hub means the centre of a wheel, from which multiple spokes emerge. 

#### Logs ####
#### Loops ####
#### Menus ####
#### Mission Portal ####
#### Monitoring ####
#### Namespaces ####
#### Networking ####
#### Normal Ordering ####
#### Operators ####
#### Pattern Matching ####

#### PCI compliance ####

Payment Card Industry Data Security Standard (PCI DSS) is a set of requirements designed to ensure that ALL companies that process, store or transmit credit card information maintain a secure environment. 

#### Policy Levels ####
#### Policy Server ####
#### Policy Writing ####
#### Policy ####

A policy is a set of intentions about the system, coded as a list of promises. A policy is not a standard, but the result of specific organizational management decisions. 

#### Precedence ####
#### Promise Attributes ####
#### Promise Types ####
#### Promise ####

The CFEngine software manages every intended system outcome as `promises' to be kept. A CFEngine Promise corresponds roughly to a rule in other software products, but importantly promises are always things that can be kept and repaired continuously, on a real time basis, not just once at install-time. 

#### Referencing ####
#### Report Collector ####
#### Reporting ####
#### Reports ####
#### Role-Based Acess Control (RBAC) ####
#### Scope ####

#### Server ####

For historical reasons, certain computers are referred to as servers, especially when kept in datacentres because such computers often run services. 

In CFEngine, cf-serverd is a software component that serves files from one computer to another. All computers are recommended to run cf-serverd, making all computers CFEngine servers, whether they are laptops, phones or datacentre computers. 

#### Sketch Activation ####
#### Sketches ####
#### Special Variables ####
#### Standard Library ####
#### Syntax ####
#### Variables ####
#### Version Control ####














