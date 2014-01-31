---
layout: default
title: packagesmatching
categories: [Reference, Functions, packagesmatching]
published: true
alias: reference-functions-packagesmatching.html
tags: [reference, utility functions, functions, packages, inventory, packagesmatching]
---

[%CFEngine_function_prototype(package_regex, version_regex, arch_regex, method_regex)%]

**Description:** Return a data container with the list of packages matching the parameters.

This function searches for the [unanchored][unanchored] regular expressions in 
the list of currently known packages.

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

**Note** The `package_method` is **not** the authoritative source of
the `method` here.  Instead, the method is currently guessed to be the
basename of the first thing on the command line.  So, for instance,
the `apt_get` `package_method` uses `env` to set environment
variables, and CFEngine records `env` as the `method`.  This is a
known issue, see https://cfengine.com/dev/issues/4203

[%CFEngine_function_attributes(package_regex, version_regex, arch_regex, method_regex)%]

**Example:**  

```cf3
      "all_packages" data => packagesmatching(".*", ".*", ".*", ".*");
```

**History:** Introduced in CFEngine 3.6
