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

**Example:**

```cf3
      "all_package_updates" data => packageupdatesmatching(".*", ".*", ".*", ".*");
```

**History:** Introduced in CFEngine 3.6

**See also:** `packagesmatching()`.
