---
layout: default
title: Managing Software
published: false
tags: [Examples, Policy, Packages]
---

# Package Promises Examples

[%CFEngine_include_example(package_bundles.cf)%]

Package promises allow you to make promises about the state of software
installed on a host. Seven basic use cases are presented here which
represent the majority of scenarios typically encountered. Irregular or
unconventional package names can often be accommodated by studying the
implementation of Package Promises and creating special package methods.
Central to the way package promises are implemented is the standard
library, which makes use of regular expressions to match package names.

## Add a Package

In this case, only the name of the desired package is supplied. e.g.
"zip". The rest is taken care of by the software, which in turn, makes
use of the package manager native to the platform.

Here is a simple example of a bundle that installs the zip package for supported
architectures.

```cf3
bundle agent AddPackage
{
 methods:
    "ensureZip" usebundle => cfe_package_ensure_present("zip");
}
```

This code shows how to use the bundles `cfe_package_ensure_present()`
from the [packages][Packages Bundles and Bodies] standard library.

## Upgrade a Package

In this case, we would like to ensure our named package is the latest
available. This type of promise attempts to ensure that the latest
version of zip is installed. If the installed version is already the
latest, it does nothing. Otherwise it either upgrades to the latest
available or installs it if it's not already installed.



### Usage

[`cfe_package_ensure_upgrade(name)`][cfe_package_ensure_upgrade()]

name: string

A simple example follows.

```cf3
bundle agent UpgradePackage
{
 methods:
    "latestZip" usebundle => cfe_package_ensure_upgrade("zip");
}
```

This code shows how to use the bundles `cfe_package_ensure_upgrade()`
from the [packages][Packages Bundles and Bodies] standard library.

## Remove a Package

For this case, we would like to ensure that the named package is removed
or absent from the target system.

### Usage

[`cfe_package_ensure_absent(name)`][cfe_package_ensure_absent()]

name: string

```cf3
bundle agent RemovePackage
{
 methods:
    "noZip" usebundle => cfe_package_ensure_absent("zip");
}
```

This code shows how to use the bundles `cfe_package_ensure_absent()`
from the [packages][Packages Bundles and Bodies] standard library.

## Add a Specific Version of a Named Package for Specific Architecture

For cases where you would like to ensure a specific version and a
specific platform and architecture is present on the host, you can use
this method. A selection method is supplied which tells the software to
select a specified version. In this case "==" means we want the version
to be selected if it's equal to the supplied version string.

### Usage

[`cfe_package_named_ensure_present(name, selector, version, architecture)`][cfe_package_named_ensure_present()]

name: string

selector: ==, =\> or \<=

version: package version string

architecture: amd64, i386, x86\_64

Let's see how this looks as an example in which version 2.99 of the zip
package for the Debian amd64 architecture is promised to be installed.

```cf3
bundle agent SpecificPackageFromDebianRepo
{
 methods:
       "ensureSpecificZip" usebundle => cfe_package_named_ensure_present("zip","==","2.99","amd64");
}
```

This code shows how to use the bundles
`cfe_package_named_ensure_present()` from
the [packages][Packages Bundles and Bodies] standard library.

## Specific Version of a Named Package for Specific Architecture (from a file)

This use case is identical to the last except for the fact that our
package resides in a local directory as a platform specific package file
- e.g. .rpm or .deb.

### Usage

[`cfe_package_named_ensure_present(path_to_package,selector,version,architecture)`][cfe_package_named_ensure_present()]

name: string

selector: ==, =\> or \<=

version: package version string

architecture: amd64, i386, x86\_64

As an example, see the policy snippet below. We wish to install a
package on a Redhat system from an rpm file.

```cf3
bundle agent SpecificPackageFromRpmFile
{
 methods:
      "addZipFromRpmFile" usebundle =>
         cfe_package_named_ensure_present("/local/repo/zip-3.0-7_x86_64.rpm","==","3.0-7","x86_64");
}
```

This code shows how to use the bundles `cfe_package_named_ensure_present()` from the
[packages][Packages Bundles and Bodies] standard library.

## Ensure Present or Upgrade Named Package for Specific Architecture from File

Upgrade or install the package from a named package file. This is
similar to the previous example except that an existing package will be
upgraded if it is older, to the version specified.

### Usage

[`cfe_package_named_ensure_upgrade(path_to_package,selector,version,architecture)`][cfe_package_named_ensure_upgrade()]

name: string

selector: ==, =\> or \<=

version: package version string

architecture: amd64, i386, x86_64

For example, the following policy illustrates a debian based upgrade of
an existing package.

```cf3
bundle agent SpecificPackageUpgradeFromDebianFile
{
 methods:
        "upgradeZipFromDebFile" usebundle =>
           cfe_package_named_ensure_upgrade("/local/repo/zip-3.0-7_amd64.deb","==","3.0-7","amd64");
}
```

This code shows how to use the bundles `cfe_package_named_ensure_upgrade()` from the
[packages][Packages Bundles and Bodies] standard library.

## Ensure Present or Upgrade Named Package for Specific Architecture

Upgrade or install the package. This promises to upgrade the package to
the specified version and architecture.

### Usage

[`cfe_package_named_ensure_upgrade(name,selector,version,architecture)`][cfe_package_named_ensure_upgrade()]

name: string

selector: ==, =\> or \<=

version: package version string

architecture: amd64, i386, x86_64

For example, the following policy upgrades the zip package to the
specificed version.

```cf3
bundle agent SpecificPackageUpgradeDebian
{
 methods:
       "upgradeZip" usebundle =>
          cfe_package_named_ensure_upgrade("zip","==","3.0-7","amd64");
}
```

This code shows how to use the bundles `cfe_package_named_ensure_upgrade()` from the
[packages][Packages Bundles and Bodies] standard library.
