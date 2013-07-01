---
layout: default
title: Known Issues
sorting: 50
categories: [Getting Started, Known Issues]
published: true
alias: getting-started-known-issues.html
tags: [getting started, known issues]
---

CFEngine defects are managed in our [bug tracker][bug tracker]. Please report
bugs or unexpected behavior there, following the documented guideline for new
bug reports.

The items below highlight issues that require additional awareness when starting
with CFEngine or when upgrading from a previous version.

### Comma in promiser/promisee declaration generates Syntax Error

The policy file parser is stricter in CFEngine 3.5.0 . The parser is now fully 
compliant with the CFEngine [language syntax reference][Language Concepts].
The main difference you will encounter is that promiser/promisee no longer 
allows a comma at the end of the line. This will cause your existing policies 
to produce errors when they are read by CFEngine 3.5.0.

An example of what you might see as a result of this issue can be found below:

```cf3
/var/cfengine/inputs/CFE_hub_specific.cf:621:28: error: syntax error
Q: ".../cf-execd"":    "/usr/sbin/a2enmod php5",
Q: ".../cf-execd"":                            ^
Q: ".../cf-execd"": /var/cfengine/inputs/CFE_hub_specific.cf:621:28: error: Expected attribute, got ','
Q: ".../cf-execd"":    "/usr/sbin/a2enmod php5",
Q: ".../cf-execd"":                            ^
```

This can be remedied by editing the policy and removing the comma at the end 
of the appropriate promiser/promisee line.

### On Windows platforms, cf-serverd listens only to IPv6 interface

There is a policy-level workaround for this one, add the following to `body server control` in `masterfiles/controls/cf-serverd.cf`:

```cf3
bindtointerface => "0.0.0.0";
```

### cf-execd sends out emails on every execution

The inclusion of the timestamp in the new log output format causes this
behavior. This will be resolved in the next release.

Current workaround options include disabling email by commenting out `mailto` and
`smtpserver` in `body executor control` or by running `cf-agent` from cron.

https://cfengine.com/dev/issues/3011


