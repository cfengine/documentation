---
layout: default
title: packageupdatesmatching
published: true
---

[%CFEngine_function_prototype(package_regex, version_regex, arch_regex, method_regex)%]

**Description:** Return a data container with the list of available packages
matching the parameters.

This function searches for the [anchored][anchored] regular expressions in the
list of currently available packages.

The return is a data container with a list of package descriptions, looking like
this:

```
[
   {
      "arch":"default",
      "method":"dpkg",
      "name":"syncthing",
      "version":"0.12.8"
   }
]
```

[%CFEngine_function_attributes(package_regex, version_regex, arch_regex, method_regex)%]

**Argument Descriptions:**

* `package_regex` - Regular expression matching packge name
* `version_regex` - Regular expression matching package version
* `arch_regex` - Regular expression matching package architecutre
* `method_regex` - Regular expression matching package method (apt-get, rpm, etc ...)

**IMPORTANT:** The data source used when querying depends on policy configuration.
When `package_inventory` in `body common control` is configured, CFEngine will record the packages installed and the package updates available for the configured package modules.
In the [Masterfiles Policy Framework][Masterfiles Policy Framework] `package_inventory` will be [configured](https://github.com/cfengine/masterfiles/blob/3dc1f629544b24261975ecf86e02554d4daf346e/promises.cf.in#L92) to the default for the hosts platform.
Since only one `body common control` can be present in a policy set any bundles which use these functions will typically need to execute in the context of a full policy run.
However, since the release of CFEngine 3.22, the `packagesmatching` and `packageupdatesmatching` policy functions will look for and use the existing software inventory databases (available in `$(sys.statedir)`), if the default package inventory is not configured.
This change enables the usage of these policy functions in standalone policy files. But please note that you still need the default package inventory attribute specified in the policy framework for the software inventory databases to exist in the first place and for them to be maintained/updated.
If there is no `package_inventory` attribute (such as on package module unsupported platforms) and there are no software inventory databases available in `$(sys.statedir)` then the legacy package methods data will be used instead.
At no time will both the standard and the legacy data be available to these functions simultaneously.


**Example:**

```cf3
"all_package_updates" data => packageupdatesmatching(".*", ".*", ".*", ".*");
```

**Refresh rules:**
* updates cache used by packageupdatesmatching() is refreshed at the end of each agent run in accordance with constraints defined in the relevant package module body.
* updates cache is refreshed every time `repo` type package is installed or removed
* updates cache is refreshed if no local cache exists.
        This means a reliable way to force a refresh of CFEngine's internal package cache is to simply delete the local cache:

```cf3
$(sys.statedir)/packages_updates_<package_module>.lmdb*
```

Or in the case of legacy package methods:

```cf3
$(sys.statedir)/software_patches_avail.csv
```

**History:** Introduced in CFEngine 3.6

**See also:** `packagesmatching()`, [Package information cache tunables in the MPF][Masterfiles Policy Framework#Configure periodic package inventory refresh interval]
