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
each type of package manager.

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
[`package_module`][Components#package_module] attribute
in body common control.

Note that if your `policy` attribute specifies "absent", then the promiser
string needs to be a bare package name, you cannot use a file name for this.

<a name=noteable-differences-from-package_modules></a>
**Noteable differences from `package_method` based implementation:**

* The promiser must be the fully qualified path to a file *or* a *package name*.
  `package_modules` do not have the concept of a
  flexible [naming convention][packages (deprecated)#package_name_convention].

  For example, here are valid ways to specify a specific package version when
  using the `package_module` based implementation.

  ```cf3
    packages:

      debian::

        "apache2"
          policy => "present",
          version => "2.2.22",
          package_module => apt_get,
          comment => "Install apache from repository";

      redhat::

        "/mnt/nfs/packages/apache2-2.2.22.x86_64.rpm"
          policy => "present",
          package_module => yum,
          comment => "Install apache from a specific RPM";
  ```

  The following usage is NOT valid.

  ```cf3
    packages:

      debian::

        "apache2-2.2.22"
          policy => "present",
          package_module => apt_get,
          comment => "INVALID specification of package version";

    redhat::
        "/mnt/nfs/packages/apache2-2.2.22.x86_64.rpm"
          policy => "present",
          package_module => yum,
          version => "2.2.22",
          comment => "INVALID specification of package version.";
  ```

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

**Default value:** ```present```

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
[`package_module`][Components#package_module] in Components
and Common Control. The name of the body is expected to be the same as the name
of the package module inside `/var/cfengine/modules/packages`.

**See also:** [Common Body Attributes][common-body-attributes]

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

#### interpreter

**Description:** Absolute path to the interpreter to run the package module (script) with.

If the package module is implemented as a script, it has to be executed with
some interpreter. Using a hashbang/shebang may not always be possible or easy
(different versions/paths of python, etc.). This attribute tells CFEngine the
path to the interpreter to use when running the package module.

**Type:** `string`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
body package_module apt_get
{
    # better use variable like $(def.python)
    interpreter => "/usr/bin/python3.6";
}
```

**See Also:** `Package Modules`

**History:** Introduced in 3.13.0, 3.12.2

#### module_path

**Description:** Absolute path to the the package module.

By default, the package module implementation has to be in a file with the same
name as the package module itself, under the `$(sys.workdir)/modules/packages`
directory. In some cases, it might be useful to use a different name or path or
to have multiple package modules using the same implementation just with
different attributes (e.g. `default_options`).

**Type:** `string`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
body package_module yum_all_repos
{
    module_path => $(sys.workdir)/modules/packages/yum;
    default_options => { "--enablerepo=*" };
}
```

**See Also:** `Package Modules`

**History:** Introduced in 3.13.0, 3.12.2

## Package modules out-of-the-box
### yum

Manage packages using ```yum```. This is the [default package module](lib/packages.cf#package_module_knowledge) for Red Hat, CentOS and Amazon Linux.

**Examples:**

File based package source.

```cf3
  packages:
    redhat|centos|amazon_linux::
      "/mnt/nfs/packages/httpd-2.2.22.x86_64.rpm"
        policy => "present";
```

Repository based package source with a specific version of the package.

```cf3
  packages:
    redhat|centos|amazon_linux::
      "httpd"
        policy => "present",
        version => "2.2.22";
```

Enable a specific repository for a specific promise.

```cf3
bundle agent example
{
  packages:

    redhat|centos|amazon_linux::
      # Enable the EPEL repo when making sure git is installed
      # and up to date.

      "git"
         policy => "present",
         version => "latest",
         options => { "enablerepo=EPEL" };

      # Only consider updates from the main repositories for
      # httpd and disable all other repositories

      "httpd"
         policy => "present",
         version => "latest",
         options => { "disablerepo=* enablerepo=UPDATES" };
}
```

**Notes:**

* Supports file path and repository sourced packages.

* Requires Python version 2 or 3 to be installed on the host.

* If ```policy => "present"``` *and* ```version``` is set this package module will downgrade the promised package if necessary.

  ```console
  [root ~]# yum --show-duplicates list screen
  Loaded plugins: fastestmirror
  Loading mirror speeds from cached hostfile
   * base: centos.mirror.constant.com
   * epel: epel.mirror.constant.com
   * extras: mirror.ette.biz
   * updates: mirror.trouble-free.net
  Installed Packages
  screen.x86_64            4.1.0-0.25.20120314git3c2946.el7             @base     
  Available Packages
  screen.x86_64            4.1.0-0.19.20120314git3c2946.el7             local-repo
  screen.x86_64            4.1.0-0.25.20120314git3c2946.el7             base      
  ```

  Policy with promise that old version of screen is installed.

  ```cf3
  bundle agent example_yum_downgrades_if_necessary
  {
    packages:
      redhat_7|centos_7::
        "screen"
          policy => "present",
          version => "4.1.0-0.19.20120314git3c2946.el7";
  }
  ```

  Executing policy and the version of screen installed after policy run.

  ```console
  [root ~]# cf-agent -Kb example_yum_downgrades_if_necessary; rpm -q screen
  screen-4.1.0-0.19.20120314git3c2946.el7.x86_64
  ```

**History:**

* Added in CFEngine 3.7.0
* `enablerepo` and `disablerepo` option support added in 3.7.8, 3.10.4, 3.12.0

### apt_get

Manage packages using ```apt-get```.

**Example:**

Example showing file based package source.

```cf3
  packages:
      "/mnt/nfs/packages/apache2-2.2.22.x86_64.deb"
        policy => "present",
        package_module => apt_get;
```

Example showing repository based package source.

```cf3
  packages:
      "apache2"
        policy => "present",
        package_module => apt_get,
        version => "2.2.22",
        options => { "-o", "APT::Install-Recommends=0" };
```

**Notes:**

* Requires Python version 2 to be installed on the host.
* Supports [```options```][packages#options] attribute. Each space separate
  option must be added as a separate list element. The options are passed
  directly through to the package manager.

**History:**

* Added in CFEngine 3.7.0

### freebsd_ports

Manage packages using
FreeBSD [Ports](https://www.freebsd.org/doc/handbook/ports-using.html).

**History:**

* Added in CFEngine 3.9.0

### nimclient

Manage packages using `nimclient` on AIX.

**Example:**

```cf3
  packages:
    aix::
      "expect.base"
        policy => "present",
        package_module => nimclient,
        options => { "lpp_source=lppaix710304" };
```


**Notes:**

* [```options```][packages#options] attribute support to specify
  ```lpp_source```. Please note it is **REQUIRED** to specify an
  ```lpp_source``` when using this package module.

**History:**

* Added in CFEngine 3.9.0

### pkg

Manage packages using
FreeBSD [pkg](https://www.freebsd.org/doc/handbook/pkgng-intro.html).

**Example:**

```cf3
  packages:
    freebsd::
      "emacs-nox11"
        policy => "present",
        package_module => pkg;

      "emacs"
        policy => "absent",
        package_module => pkg;
```

**History:**

* Added in CFEngine 3.9.0

### pkgsrc

Manage packages using [pkgsrc](https://www.pkgsrc.org).

**History:**

* Added in CFEngine 3.9.0

### slackpkg

Manage packages using Slackware's [slackpkg](https://slackpkg.org).

**Example**

```cf3
  packages:
    slackware::
      "nmap"
        policy => "absent",
        package_module => slackpkg;
```

**History:**

* Added in CFEngine 3.12.0

### msiexec

Manage MSI packages using MSI installer on Windows.

Due to lack of central software repository on supported versions of Windows,
neither installation from repository nor checking for upgrades is supported.
The full path to the MSI package file must be supplied in order to promise the
package is installed. In order to promise a package is absent (not installed)
the package name must be used.

**Example**: install [Google Chrome][] but prevent it from self-upgrading
(otherwise Google Chrome's self-upgrading will conflict with CFEngine ensuring
that version from this particluar MSI is installed):

[Google Chrome]: https://cloud.google.com/chrome-enterprise/browser/download/#chrome-browser-update

```cf3
  packages:
    windows::
      "C:\GoogleChromeStandaloneEnterprise.msi"
        policy => "present",
        package_module => msiexec;

      "Google Update Helper"
        policy => "absent",
        package_module => msiexec;
```

**History:**

* Added in CFEngine 3.12.2 and 3.14.0

### snap

Manage packages using [snap](https://en.wikipedia.org/wiki/Snappy_(package_manager)).

```cf3
bundle agent main
{
  packages:
    ubuntu::
      "genpw"
        policy => "present",
        package_module => snap;

      "genpw"
        policy => "absent",
        package_module => snap;

       "genpw"
         policy => "present",
         package_module => snap,
         version => "2.0.0";

       "genpw"
         policy => "absent",
         package_module => snap,
         version => "2.0.0";

       "genpw"
         policy => "present",
         package_module => snap,
         version => "latest";
}
```

**History:**

* Added in CFEngine 3.15.0, 3.12.3, 3.10.7

**Notes:**

- version `latest` is *not* supported when promising an absence
- `list-updates` is *not* implemented, snaps are automatically updated by default


