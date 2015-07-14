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

[%CFEngine_include_example(packagesmatching.cf)%]

[%CFEngine_function_attributes(package_regex, version_regex, arch_regex, method_regex)%]

**Example:**  

```cf3
      "all_packages" data => packagesmatching(".*", ".*", ".*", ".*");
```

**History:** Introduced in CFEngine 3.6

**See also:** `packageupdatesmatching()`.
