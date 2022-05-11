---
layout: default
title: packagesmatching
published: true
tags: [reference, utility functions, functions, packages, inventory, packagesmatching]
---

[%CFEngine_function_prototype(package_regex, version_regex, arch_regex, method_regex)%]

**Description:** Return a data container with the list of installed packages
matching the parameters.

This function searches for the [anchored][anchored] regular expressions in the
list of currently installed packages.

The return is a data container with a list of package descriptions, looking like
this:

```
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

**Argument Descriptions:**

* `package_regex` - Regular expression matching packge name
* `version_regex` - Regular expression matching package version
* `arch_regex` - Regular expression matching package architecutre
* `method_regex` - Regular expression matching package method (apt-get, rpm, etc ...)

The following code extracts just the package names, then looks for
some desired packages, and finally reports if they are installed.

**IMPORTANT:** Please note that you need to provide `package_inventory` attribute in `body common control` in order to be able to use this function. Also depending on the value(s) of `package_inventory` only packages from selected package modules will be returned. For more information about `package_inventory` please read [`package_inventory`][Components#package_inventory] section.

[%CFEngine_include_example(packagesmatching.cf)%]

**Example:**

```cf3
      "all_packages" data => packagesmatching(".*", ".*", ".*", ".*");
```

**Refresh rules:**
* installed packages cache used by packagesmatching() is refreshed at the end of each agent run in accordance with constraints defined in the relevant package module body.
* installed packages cache is refreshed after installing or removing a package.
* installed packages cache is refreshed if no local cache exists.
        This means a reliable way to force a refresh of CFEngine's internal package cache is to simply delete the local cache:

```cf3
            $(sys.statedir)/packages_installed_<package_module>.lmdb*
```

**History:** Introduced in CFEngine 3.6

**See also:** `packageupdatesmatching()`, [Package information cache tunables in the MPF][Masterfiles Policy Framework#Configure periodic package inventory refresh interval]
