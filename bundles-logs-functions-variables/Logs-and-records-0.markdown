---
layout: default
title: xxxx
categories: [xxx]
published: true
alias: Logs-and-records-0.markdown.html
tags: [xx]
---

Logs and records
----------------

\

CFEngine writes numerous logs and records to its private workspace,
referred to as WORKDIR. This chapter makes some brief notes about these
files. CFEngine approaches monitoring and reporting from the viewpoint
of scalability so there is no default centralization of reporting
information, as this is untenable for more than a few hundred hosts.
Instead, in the classic CFEngine way, every host is responsible for its
own data. Solutions for centralization and netwide reporting will be
given elsewhere.

The filenames referred to in this section are all relative to the
CFEngine work directory WORKDIR.

-   Embedded Databases
-   Text logs
-   Reports in outputs
-   Additional reports in commercial CFEngine versions
-   State information
