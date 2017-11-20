---
layout: default
title: Glossary
sorting: 100
published: false
tags: [guide, glossary]
---

#### Agent ####

A program that runs independently and automatically to carry out a task (think software robot). In CFEngine, the agent is called cf-agent and is responsible for making changes to computers.

(Originally, the word *robot*, meaning "servile worker," was coined
for the influential Czech writer Karel Čapek's play R.U.R by his
brother. The characters in that play are capable of fairly independent
thought, so the original sense of the word is apt to describe
CFEngine's agents as well.)

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

Standalone applications include cf-agent, cf-promises, cf-runagent, cf-know, cf-report, cf-hub

Daemons include cf-execd, cf-monitord, and cf-serverd

#### Datatypes ####

CFEngine's data types describe what a variable can contain.  A variable can't be assigned a different type once it's been set.  The commonly used data types are `string`, `slist`, `int`, `real`, and `data`.

#### Directories ####
#### Distribution ####
#### Enterprise API ####
#### Enterprise Reporting ####
#### File Structure ####
#### Frequency ####
#### Functions ####
#### Host ####

UNIX terminology for a computer the runs "guest programs." In practice, "host" is a synonym for "computer."

#### Hub ####

A software component in CFEngine Enterprise that acts as a single point of management in a local "star-network." The term "hub" is sometimes used to mean policy distribution server, but more commonly a running cf-hub process that does report collection from all CFEngine managed hosts. The term hub means the centre of a wheel, from which multiple spokes emerge.

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

The special server that others consult for the latest policies is called the *Policy Server*.

Typically the policy server is set by the bootstrapping process.

#### Policy Writing ####
#### Policy ####

A policy is a set of intentions about the system, coded as a list of promises. A policy is not a standard, but the result of specific organizational management decisions.

#### Precedence ####
#### Promise Attributes ####
#### Promise Types ####
#### Promise ####

The CFEngine software manages every intended system outcome as "promises" to be kept. A CFEngine Promise corresponds roughly to a rule in other software products, but importantly promises are always things that can be kept and repaired continuously, on a real time basis, not just once at install-time.

Promises are idempotent, meaning they can be executed many times with the same outcome.

They are also convergent, meaning they can only nudge the system closer to a steady state, never destabilize it.  While there are ways a user could override this, it's almost never a good idea to do so.

#### Referencing ####
#### Report Collector ####
#### Reporting ####
#### Reports ####
#### Role-Based Access Control (RBAC) ####
#### Scope ####

#### Server ####

For historical reasons, certain computers are referred to as servers, especially when kept in datacentres because such computers often run services.

In CFEngine, cf-serverd is a software component that serves files from one computer to another. All computers are recommended to run cf-serverd, making all computers CFEngine servers, whether they are laptops, phones or datacentre computers.

The special server that others consult for the latest policies is called the Policy Server.

#### Special Variables ####
#### Standard Library ####

The standard library lives in a `masterfiles/lib` subdirectory.  It's a collection of useful bundles and bodies you can use.

#### Syntax ####
#### Variables ####
#### Version Control ####
