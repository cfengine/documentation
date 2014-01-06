---
layout: default
title: Distributed Discovery
categories: [Getting Started, Concepts]
published: true
sorting: 30
alias: manuals-architecture-distributed-discovery.html
tags: [manuals, troubleshooting, connectivity, network, server, access, remote, keys, encryption, security]
---

CFEngine's philosophy and modus operandi is to make machines as self-reliant 
as possible. This is the path to scalability. Sometimes we want machines to be 
able to detect one another and sample each others' behavior. This can be 
accomplished using probes and server functions.

For example, testing whether services are up and running can be a useful probe 
even from a local host. CFEngine has in-built functions for generically 
probing the environment; these are designed to encourage decentralized 
monitoring.
