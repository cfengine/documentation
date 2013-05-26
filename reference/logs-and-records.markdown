---
layout: default
title: Logs and Records
categories: [Reference, Logs and records]
published: true
alias: reference-logs-and-records.html
tags: [reference, logs, records]
---  

CFEngine  approaches monitoring and reporting from the viewpoint of 
scalability so there is no default centralization of reporting information, as 
this is untenable for more than a few hundred hosts. Instead, in the classic 
CFEngine way, every host is responsible for its own data.

On hosts, CFEngine writes numerous logs and records to its private workspace, 
referred  to as 
[`WORKDIR`](manuals-managing-environments-work-directory.html) in the 
documentation.

CFEngine Enterprise provides solutions for centralization and network-wide 
reporting at arbitrary scale.
