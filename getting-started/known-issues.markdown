---
layout: default
title: Known Issues
sortkey: 5
categories: [Getting Started, Known Issues]
published: true
alias: getting-started-known-issues.html
tags: [getting started, known issues]
---

<!--- 
TODO: move down when no longer a pre-release -->

* This is a pre-release, features are not complete and not fully tested

### New Syntax Errors

The policy file parser is stricter in CFEngine 3.5.0 . The parser is now fully 
compliant with the CFEngine [language syntax  reference](manuals-language-concepts.html).
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
