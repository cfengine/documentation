---
layout: default
title: packageupdatessmatching
published: true
tags: [reference, utility functions, functions, packages, inventory, packageupdatessmatching]
---

[%CFEngine_function_prototype(package_regex, version_regex, arch_regex, method_regex)%]

**Description:** Return a data container with the list of available packages matching the parameters.

This function searches for the [unanchored][unanchored] regular expressions in 
the list of currently available packages.

The return is a data container with a list of package descriptions, looking like this:

```json
[
  {
    "name": "bfoobar",
    "version": "1",
    "arch": "besm6",
    "method": "printf"
  }
]
```

[%CFEngine_function_attributes(package_regex, version_regex, arch_regex, method_regex)%]

**Example:**  

```cf3
      "all_packages" data => packageupdatessmatching(".*", ".*", ".*", ".*");
```

**History:** Introduced in CFEngine 3.6

**See also:** [`packagesmatching()`][packagesmatching].
