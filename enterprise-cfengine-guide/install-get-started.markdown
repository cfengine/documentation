---
layout: default
title: Install and Get Started
published: true
sorting: 10
---

* [Installation][Install and Get Started#Installation]
* [Post-Install Configuration][Install and Get Started#Post-Install Configuration]

## Installation ##

The [General Installation][General Installation] instructions provide the detailed steps for installing CFEngine, which are generally the same steps to follow for CFEngine Enterprise, with the exception of license keys (if applicable), and also some aspects of post-installation and configuration.

### Installing Enterprise Licenses ###

Before you begin, you should have your license key, unless you only
plan to use the free 25 node license. The installation instructions
will be provided with the key.

## Post-Install Configuration ##

### Change Email Setup After CFEngine Enterprise Installation ###

For Enterprise 3.6 local mail relay is used, and it is assumed the server has a proper mail setup.

The default FROM email for all emails sent from the Mission Portal is ```admin@organization.com```. This can be changed on the CFE Server in ```/var/cfengine/httpd/htdocs/application/config/appsettings.php:$config['appemail']```.

### Version your policies

Consider enabling the built-in version control of your policies as
described in
[Version Control and Configuration Policy][Best Practices#Version Control and Configuration Policy]

Whether you do or not, please put your policies in some kind of
backed-up VCS. Losing work because of "fat fingering" `rm` commands is
very, very depressing.

### Configure collection for monitoring data

[Monitoring][Monitoring] allows you to sample a metric and assess its value
across your hosts over time. Collection of monitoring information is disabled by
default. Metrics must match `monitoring_include` in the appropriate
`report_data_select` body.
The [Masterfiles Policy Framework][Masterfiles Policy Framework] uses `body
report_data_select default_data_select_policy_hub` to specify metrics that
should be collected from policy hubs and `default_data_select_host` to specify
metrics that should be collected from non hubs.

For example:

To collect all metrics from hubs:

```cf3
body report_data_select default_data_select_policy_hub
# @brief Data to collect from policy servers by default
#
# By convention variables and classes known to be internal, (having no
# reporting value) should be prefixed with an underscore. By default the policy
# framework explicitly excludes these variables and classes from collection.
{
      metatags_include => { "inventory", "report" };
      metatags_exclude => { "noreport" };
      promise_handle_exclude => { "noreport_.*" };
      monitoring_include => { ".*" };
}
```

To collect ```cpu```, ```loadavg``` , ```diskfree```, ```swap_page_in```,
```cpu_utilization```, ```swap_utilization```, and ```memory_utilization``` from
non hubs:

```cf3
body report_data_select default_data_select_host
# @brief Data to collect from remote hosts by default
#
# By convention variables and classes known to be internal, (having no
# reporting value) should be prefixed with an underscore. By default the policy
# framework explicitly excludes these variables and classes from collection.
{
      metatags_include => { "inventory", "report" };
      metatags_exclude => { "noreport" };
      promise_handle_exclude => { "noreport_.*" };
      monitoring_include => {
                              "cpu",
                              "loadavg",
                              "diskfree",
                              "swap_page_in",
                              "cpu_utilization",
                              "swap_utilization",
                              "memory_utilization",
                              };
}
```

### Review settings

See the [Masterfiles Policy Framework][Masterfiles Policy Framework] for a full
list of all the settings you can configure.
