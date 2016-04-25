---
layout: default
title: packageupdatesmatching
published: true
tags: [reference, utility functions, functions, packages, inventory, packageupdatesmatching]
---

[%CFEngine_function_prototype(package_regex, version_regex, arch_regex, method_regex)%]

**Description:** Return a data container with the list of available packages matching the parameters.

This function searches for the [unanchored][unanchored] regular expressions in
the list of currently available packages.

The return is a data container with a list of package descriptions, looking like this:

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

**IMPORTANT:** Please note that you need to provide `package_inventory` attribute in `body common control` in order to be able to use this function. Also depending on the value(s) of `package_inventory` only packages from selected package modules will be returned. For more information about `package_inventory` please read [`package_inventory`][Components and Common Control#package_inventory] section.


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


**History:** Introduced in CFEngine 3.6

**See also:** `packagesmatching()`.
