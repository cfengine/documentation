---
layout: default
<<<<<<< HEAD:reference/logs-and-records.markdown
title: Logs and Records
categories: [Reference, Logs and records]
=======
title: 
categories: [Logs and records]
>>>>>>> 702a8ca0231da6ae5e2672b6298561254d98aa29:bundles-logs-functions-variables/Logs-and-records-0.markdown
published: true
alias: reference-logs-and-records.html
tags: [reference, logs, records]
---  

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

-   [Embedded Databases](#Embedded-Databases)
-   [Text logs](#Text-logs)
-   [Reports in outputs](#Reports-in-outputs)
-   [Additional reports in commercial CFEngine
    versions](#Additional-reports-in-commercical-CFEngine-versions)
-   [State information](#State-information)
