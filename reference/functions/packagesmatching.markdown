---
layout: default
title: packagesmatching
published: true
tags: [reference, utility functions, functions, packages, inventory, packagesmatching]
---

[%CFEngine_function_prototype(package_regex, version_regex, arch_regex, method_regex)%]

**Description:** Return a data container with the list of installed packages
matching the parameters.

This function searches for the [unanchored][unanchored] regular expressions in
the list of currently installed packages.

The return is a data container with a list of package descriptions, looking like this:

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

[%CFEngine_include_example(packagesmatching.cf)%]

**Example:**

```cf3
      "all_packages" data => packagesmatching(".*", ".*", ".*", ".*");
```

**History:** Introduced in CFEngine 3.6

**See also:** `packageupdatesmatching()`.
