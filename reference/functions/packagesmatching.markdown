---
layout: default
title: packagesmatching
published: true
tags: [reference, utility functions, functions, packages, inventory, packagesmatching]
---

[%CFEngine_function_prototype(package_regex, version_regex, arch_regex, method_regex)%]

**Description:** Return a data container with the list of installed packages matching the parameters.

This function searches for the [unanchored][unanchored] regular expressions in 
the list of currently installed packages.

The return is a data container with a list of package descriptions, looking like this:

```
[
  {
    "name": "bfoobar",
    "version": "1",
    "arch": "besm6",
    "method": "printf"
  }
]
```

The following code extracts just the package names, then looks for
some desired packages, and finally reports if they are installed.

```cf3
bundle agent missing_packages
{
  vars:
    "desired" slist => { "mypackage1", "mypackage2" };

    "installed" data => packagesmatching(".*",".*",".*",".*");
    "installed_indices" slist => getindices(installed);
    "installed_name[$(installed_indices)]" string => "$(installed[$(installed_indices)][name])";
    "installed_names" slist => getvalues("installed_name");

    "missing_list" slist => difference(desired,installed_names);

  reports:
    "Missing packages = $(missing)";
    "Installed packages = $(installed_names)";
    "Desired packages = $(desired)";
}
```

[%CFEngine_function_attributes(package_regex, version_regex, arch_regex, method_regex)%]

**Example:**  

```cf3
      "all_packages" data => packagesmatching(".*", ".*", ".*", ".*");
```

**History:** Introduced in CFEngine 3.6

**See also:** `packageupdatesmatching()`.
