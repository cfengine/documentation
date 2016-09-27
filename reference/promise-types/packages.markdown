---
layout: default
title: packages
published: true
tags: [reference, bundle agent, packages, packages promises, promise types]
---

CFEngine 3.7 and later supports package management through a simple promise
interface. Using a small set of attributes you can make promises about the state
of software on a host, whether it should be installed, not installed, or at a
specific version.

CFEngine 3.6 and older had a different package promise implementation, which is
still functional, but considered deprecated. However, it may still be in use by
existing policy files, and it may cover platforms which the new implementation
does not currently cover. To read about the old package promise, go to the
[old package promise section][packages (deprecated)].

The actual communication with the package manager on the system is handled by so
called [package modules][Package Modules], which are specifically written for
each type of package manager. CFEngine comes with out-of-the-box support for the
following package managers:

* `yum`: YUM package manager and accompanying rpm package manager.
* `apt_get`: Apt package manager and accompanying dpkg package manager.
* `freebsd_ports`: FreeBSD Ports
* `nimclient` - AIX NIM client
* `pkg` - FreeBSD pkg
* `pkgsrc` -  [pkgsrc](https://www.pkgsrc.org/)

Both ``yum`` and ``apt_get`` package managers require Python version 2 to be
installed on the host.


```cf3
  packages:
      "apache2"
        policy => "present",
        package_module => apt_get,
        version => "2.2.22";
```

In this example, we want the software package "apache2" to be present on the
system, and we want it to be version 2.2.22. If this requirement cannot be
fulfilled (for example because the package repository doesn't have it), the
promise will fail.

It is also possible to specify a package file name, if the package resides on
the local filesystem, like this:

```cf3
  packages:
      "/mnt/nfs/packages/apache2-2.2.22.x86_64.rpm"
        policy => "present",
        package_module => yum;
```

The default package module can be globally specified with the
[`package_module`][Components and Common Control#package_module] attribute
in body common control.

Note that if your `policy` attribute specifies "absent", then the promiser
string needs to be a bare package name, you cannot use a file name for this.

## Attributes ##

[%CFEngine_include_markdown(common-attributes-include.markdown)%]

### architecture

**Description:** The architecture we want the promise to consider.

The promise will only consider the architecture specified when performing
package manipulations, but depending on the underlying package manager, this may
indirectly affect other architectures.

**Type:** `string`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
  packages:
    "apache"
        policy => "present",
        package_module => apt_get,
        architecture => "x86_64";
```


### options

**Description:** Options to pass to the underlying package module.

`options` is a catchall attribute in order to pass arbitrary data into the
package module which is carrying out package operations. It is meant as a
rescue solution when a package module has added functionality which is not
covered by the package promise API. As such there is no official documentation
for this attribute, its usage depends on the package module in question.

**Type:** `slist`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
  packages:
    "apache"
        policy => "present",
        package_module => my_package_module,
        options => { "repository=myrepo" };
    debian::
      "php7.0"
        policy => "present",
        package_module => apt_get,
        options => { "-o", "APT::Install-Recommends=0" };
```


### policy

**Description:** Whether the package should be present or absent on the system.

`policy` is the only mandatory package promise attribute.

**Type:** `string`

**Allowed input range:** `present|absent`

**Example:**

```cf3
  packages:
    "apache"
        policy => "absent",
        package_module => apt_get;
```


### version

**Description:** The version we want the promise to consider.

**Type:** `string`

**Allowed input range:** (arbitrary string)

**Note:** When policy `present` is used version may be set to `latest` to
ensure the latest available version from a repository is installed.

**Example:**

```cf3
  packages:
    "apache"
        policy => "absent",
        package_module => apt_get,
        version => "2.2.22";

    "ssh"
        policy => "present",
        package_module => apt_get,
        version => "latest";
```


### package_module

**Type:** `body package_module`

The package module body you wish to use for the package promise. The default is
platform dependent, see
[`package_module`][Components and Common Control#package_module] in Components
and Common Control. The name of the body is expected to be the same as the name
of the package module inside `/var/cfengine/modules/packages`.

[%CFEngine_include_markdown(common-body-attributes-include.markdown)%]

#### default_options

**Description:** Options to pass to to the package module by default.

See the `options` attribute for details on what options do.

**Type:** `slist`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
body package_module apt_get
{
    default_options => { "use_curl=1" };
}
```


#### query_installed_ifelapsed

**Description:** How often to query the system for currently installed packages.

For performance reasons, CFEngine maintains a cache of currently installed
packages, to avoid calling the package manager too often. This attribute tells
CFEngine how often to update this cache (in minutes).

The cache is always updated when CFEngine makes changes to the system.

**Type:** `int`

**Allowed input range:** (Positive integer)

**Example:**

```cf3
body package_module apt_get
{
    # Query the package database only every four hours.
    query_installed_ifelapsed => "240";
}
```

**Note for `package_module` authors**:
[`list-installed`][Package Modules#list-installed] will be called when the agent
repairs a package using the given `package_module`, when the lock has expired or
when the agent is run without locks.

**See Also:** `Package Modules`

#### query_updates_ifelapsed

**Description:** How often to query the package manager for new updates.

In order not to query repository servers too often, CFEngine maintains a cache
of the currently available package updates. This attribute tells CFEngine how
often to update this cache (in minutes).

Even when making package changes to the system, CFEngine will not query this
information more often than this attribute specifies, however it may make a
local query in order to update the cache from local, already downloaded data.

**Type:** `int`

**Allowed input range:** (Positive integer)

**Example:**

```cf3
body package_module apt_get
{
    # Query package updates only every 24 hours.
    query_updates_ifelapsed => "1440";
}
```

**Note for `package_module` authors**:
[`list-updates`][Package Modules#list-updates] will be called when the lock has
expired or when the agent is run without locks.
[`list-updates-local`][Package Modules#list-updates-local] is called in all
other conditions.

**See Also:** `Package Modules`
