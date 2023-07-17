---
layout: default
title: packagesmatching
published: true
---

[%CFEngine_function_prototype(package_regex, version_regex, arch_regex, method_regex)%]

**Description:** Return a data container with the list of installed packages
matching the parameters.

This function searches for the [anchored][anchored] regular expressions in the
list of currently installed packages.

The return is a data container with a list of package descriptions, looking like
this:

```json
[
   {
      "arch":"default",
      "method":"dpkg",
      "name":"zsh-common",
      "version":"5.0.7-5ubuntu1"
   }
]
```

[%CFEngine_function_attributes(package_regex, version_regex, arch_regex, method_regex)%]

**IMPORTANT:** The data source used when querying depends on policy configuration.
When `package_inventory` in `body common control` is configured, CFEngine will record the packages installed and the package updates available for the configured package modules.
In the [Masterfiles Policy Framework][Masterfiles Policy Framework] `package_inventory` will be [configured](https://github.com/cfengine/masterfiles/blob/3dc1f629544b24261975ecf86e02554d4daf346e/promises.cf.in#L92) to the default for the hosts platform.
Since only one `body common control` can be present in a policy set any bundles which use these functions will typically need to execute in the context of a full policy run.
However, the `packagesmatching` and `packageupdatesmatching` policy functions will look for and use the existing software inventory databases (available in `$(sys.statedir)`), even if the default package inventory is not configured.
This enables the usage of these policy functions in standalone policy files. But please note that you still need the default package inventory attribute specified in the policy framework for the software inventory databases to exist in the first place and for them to be maintained/updated.
If there is no `package_inventory` attribute (such as on package module unsupported platforms) and there are no software inventory databases available in `$(sys.statedir)` then the legacy package methods data will be used instead.
At no time will both the standard and the legacy data be available to these functions simultaneously.

**Example:**

The following code extracts just the package names, then looks for
some desired packages, and finally reports if they are installed.


[%CFEngine_include_example(packagesmatching.cf)%]

**Refresh rules:**
* installed packages cache used by packagesmatching() is refreshed at the end of each agent run in accordance with constraints defined in the relevant package module body.
* installed packages cache is refreshed after installing or removing a package.
* installed packages cache is refreshed if no local cache exists.
        This means a reliable way to force a refresh of CFEngine's internal package cache is to simply delete the local cache:

```cf3
$(sys.statedir)/packages_installed_<package_module>.lmdb*
```

Or in the case of legacy package methods:

```cf3
$(sys.statedir)/software_packages.csv
```


**History:**

* Introduced in CFEngine 3.6

* Function started using `package_module` based data sources by default, even if
  there is no `package_inventory` attribute defined in `body common control` if
  available in 3.23.0, 3.21.3


**See also:** `packageupdatesmatching()`, [Package information cache tunables in the MPF][Masterfiles Policy Framework#Configure periodic package inventory refresh interval]
