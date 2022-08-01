---
layout: default
title: Monitoring and Reporting
published: true
sorting: 10
---

## What are Monitoring and Reporting?

Monitoring is the sampling of system variables at regular intervals in
order to present an overview of actual changes taking place over time.
Monitoring data are often presented as extensive views of moving-line
time series. Monitoring has the ability to detect anomalous behavior by
comparing past and present.

The term reporting is usually taken to mean the creation of short
summaries of specific system properties suitable for management. System
reports describe both promises about the system, such as compliance,
discovered changes and faults.

The challenge of both these activities is to compare intended or
promised, behavior with the actual observed behavior of the system.

## Should Monitoring and Configuration be Separate?

The traditional view of IT operations is that configuration, monitoring,
and reporting are three different things that should not be joined. Traditionally,
all three have been independent centralized processes. This view has emerged
historically, but it has a major problem: Humans are needed to glue these parts back together.
Monitoring as an independent activity is inherently non-scalable. When numbers
of hosts grow beyond a few thousands, centralized monitoring schemes fail to
manage the information. Tying configuration (and therefore repair) to monitoring
at the host level is essential for the effective management of large and distributed
data facilities. CFEngine foresaw this need in 1998, with its Computer Immunology
initiative, and continues to develop this strategy.

CFEngine's approach is to focus on scalability. The commercial editions of
CFEngine provide what meaningful information they can in a manner that can
be scaled to tens of thousands of machines.
