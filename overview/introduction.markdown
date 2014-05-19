---
layout: default
title: Introduction
published: true
sorting: 1
---

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

## Summary ##

CFEngine is a distributed system for managing and monitoring computers across an IT network. Machines on the network that have CFEngine installed, and have registered themselves (see [Bootstrapping][Bootstrapping]), will each be running a set of CFEngine component applications that manage and interpret textual files called policies. Policy files themselves contain sets of instructions to ensure machines on the network are in full compliance with a defined state. At the atomic level are sets, or bundles, of what are known in the CFEngine world as [Promises][Promises]. Promises are at the heart of Promise Theory, which is in turn what CFEngine is all about.

There are basically two categories of machines in a CFEngine environment: policy servers and their client hosts. Policy servers are responsible for making policy files available to each of the client hosts that have registered with it (a.k.a. bootstrapped), including itself. Hosts on the other hand are responsible for ensuring they continuously pull in the latest policies, or changes to policies, from the policy server. They are additionally responsible for ensuring they remain fully compliant with the instructions contained within the policy files, at all times.

The role of a particular machine where CFEngine is deployed determines which of the components will be installed and running at any given moment.


## More About Policy Language and Compliance ##

CFEngine ensures that the actual state of a system is in compliance with the predefined model of desired state for the system. If it is not in compliance CFEngine will bring it into compliance.

That model is represented by one or more policies that have been written using the declarative CFEngine policy language. Policy Language has been designed with a vocabulary that is intuitive, yet at the same time can still support the design of highly complex IT systems.

Those policies are distributed across all of the system’s policy distribution servers via pull requests, and then further disseminated to each end host within the system. Every host will then interpret and execute each of the instructions it has been given in a predetermined order. 

CFEngine continually monitors all of the hosts in real-time, and should the system’s current state begin to drift away from the intended state then CFEngine will automatically take corrective action to bring everything back into compliance.

See Also: [Guide][Guide],[System Overview][System Overview],[Policy and Promises Overview][Policy and Promises Overview]