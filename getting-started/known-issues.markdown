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

**This problem is solved as of CFEngine 3.5.1**

The inclusion of the timestamp in the new log output format causes this
behavior. This will be resolved in the next release.

Current workaround options include disabling email by commenting out `mailto` and
`smtpserver` in `body executor control` or by running `cf-agent` from cron.

https://cfengine.com/dev/issues/3011

### Enterprise upgrade using master_software_updates does not work for redhat derivitives

Packages placed in master_software_updates are not detected as being from a
higher version so upgrade does not happen.

#### Workaround

Modify the promise with handle
`cfe_internal_update_bins_packages_nova_update_not_windows_pkg_there`
in `update/update_bins.cf`.

Set package_select to `==` and package_version to the specific version for
example `3.5.1-1`.

```
diff --git a/update/update_bins.cf b/update/update_bins.cf 
index 81afc28..841dbb9 100755 
--- a/update/update_bins.cf 
+++ b/update/update_bins.cf 
@@ -162,9 +162,9 @@ bundle agent cfe_internal_update_bins 
comment => "Update Nova package to a newer version (package is there)", 
handle => "cfe_internal_update_bins_packages_nova_update_not_windows_pkg_there", 
package_policy => "update", 
- package_select => ">=", # picks the newest Nova available 
+ package_select => "==", # picks the newest Nova available 
package_architectures => { "$(pkgarch)" }, 
- package_version => "9.9.9", # Install new Nova anyway 
+ package_version => "3.5.1-1", # Install new Nova anyway 
package_method => u_generic( "$(local_software_dir)" ), 
ifvarclass => "nova_edition", 
classes => u_if_else("bin_update_success", "bin_update_fail");
```
