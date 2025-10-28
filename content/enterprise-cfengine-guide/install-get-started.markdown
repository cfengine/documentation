---
layout: default
title: Install and get started
published: false
sorting: 10
aliases:
  - "/enterprise-cfengine-guide-install-get-started.html"
---

<!--
Delete  "Enterprise Install and Get Started"
https://docs.google.com/document/d/1CeRR8cuMtrrr0X27gzVzP2ndiU0HuHvo7dJT2vIWfp0/edit#heading=h.978wiks7ber1
-->

- [Installation][Install and Get Started#Installation]
- [Post-install configuration][Install and Get Started#Post-install configuration]

## Installation

The [General installation][General installation] instructions provide the detailed steps for installing CFEngine, which are generally the same steps to follow for CFEngine Enterprise, with the exception of license keys (if applicable), and also some aspects of post-installation and configuration.

### Installing Enterprise licenses

Before you begin, you should have your license key, unless you only
plan to use the free 25 node license. The installation instructions
will be provided with the key.

## Post-install configuration

### Change email setup after CFEngine Enterprise installation

For Enterprise 3.6 local mail relay is used, and it is assumed the server has a proper mail setup.

The default FROM email for all emails sent from the Mission Portal is `admin@organization.com`. This can be changed on the CFE Server in `/var/cfengine/httpd/htdocs/application/config/appsettings.php:$config['appemail']`.

### Version your policy

Consider enabling the built-in version control of your policy as
described in
[Version control and configuration policy][Best practices#Version control and configuration policy]

Whether you do or not, please put your policy in some kind of
backed-up VCS. Losing work because of "fat fingering" `rm` commands is
very, very depressing.

### Configure collection for monitoring data

[Measurements][Measurements app] allows you to sample a metric and assess its value
across your hosts over time. Collection of monitoring information is disabled by
default. Metrics must match `monitoring_include` in the appropriate
`report_data_select` body.
The [Masterfiles Policy Framework][Masterfiles Policy Framework] uses `body
report_data_select default_data_select_policy_hub` to specify metrics that
should be collected from policy hubs and `default_data_select_host` to specify
metrics that should be collected from non hubs. Augments can be used to [configure which metrics should be collected][Masterfiles Policy Framework#Configure Enterprise Measurement/Monitoring Collection] for central reporting.

### Review settings

See the [Masterfiles Policy Framework][Masterfiles Policy Framework] for a full
list of all the settings you can configure.
