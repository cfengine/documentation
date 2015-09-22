---
layout: default
title: packages (deprecated)
published: true
tags: [reference, bundle agent, packages, packages promises, promise types]
---

**NOTE:** This package promise is deprecated and has been superseded by
[the new package promise][packages]. It is recommended to use the new package
promise whenever possible. Simply using attributes from the new package promise
interface will select the new implementation.

NOTE: CFEngine 3.6 introduces bundles `package_absent`, `package_present`,
`package_latest`, `package_specific_present`, `package_specific_absent`, and
`package_specific_latest` that provide a higher-level abstraction for
working with packages. This is the recommended way to make promises about
packages. The bundles can be found in the file packages.cf in masterfiles.

CFEngine supports a generic approach to integration with native
operating support for packaging. Package promises allow CFEngine to make
promises regarding the state of software packages *conditionally*, given
the assumption that a native package manager will perform the actual
manipulations. Since no agent can make unconditional promises about
another, this is the best that can be achieved.

```cf3
 vars:

  "match_package" slist => { 
                           "apache2", 
                           "apache2-mod_php5",
                           "apache2-prefork",
                           "php5" 
                           };
 packages:

    "$(match_package)"

         package_policy => "add",
         package_method => yum;
```

Packages are treated as black-boxes with three labels:

-   A package name
-   A version string
-   An architecture name

Package managers are treated as black boxes that may support some or all
of the following promise types:

-   List installed packages
-   Add packages
-   Delete packages
-   Reinstall (repair) packages
-   Update packages
-   Patch packages
-   Verify packages

If these services are promised by a package manager, `cf-agent` promises
to use the service and encapsulate it within the overall CFEngine
framework. It is possible to set classes based on the return code of a
package-manager command in a very flexible way. See the
`kept_returncodes`, `repaired_returncodes` and `failed_returncodes`
attributes.

### Domain knowledge

CFEngine does not maintain operating system specific expert knowledge
internally, rather it uses a generic model for dealing with promises
about packages (which depend on the behavior of an external package
manager). The approach is to define package system details in
body-constraints that can be written once and for all, for each package
system.

Package promises are like `commands` promises in the sense that CFEngine
promises nothing about the outcome of executing a command. All it can
promise is to interface with it, starting it and using the results in
good faith. Packages are basically 'outsourced', to invoke IT parlance.

### Behavior

A package promise consists of a name, a version and an architecture,
*(n,v,a)*, and behavior to be promised about packages that match
criteria based on these. The components *(n,v,a)* can be determined in
one of two different ways:

* They may be specified independently, e.g.

```cf3
     packages:
     
       "mypackage"
     
          package_policy => "add",
          package_method => rpm,
          package_select => ">=",
          package_architectures => { "x86_64", "i586" },
          package_version => "1.2.3";
```

* They may be extracted from a package identifier (promiser) or
    filename, using pattern matching. For example, a promiser
    7-Zip-4.50-x86_64.msi and a `package_method` containing the
    following:

```cf3
      package_name_regex => "^(\S+)-(\d+\.?)+";
      package_version_regex => "^\S+-((\d+\.?)+)";
      package_arch_regex => "^\S+-[\d\.]+-(.*).msi";
```

When scanning a list of installed packages different managers present
the information *(n,v,a)* in quite different forms and pattern
extraction is necessary. When making a promise about a specific package,
the CFEngine user may choose one or the other model.

### Smart and dumb package systems

Package managers vary enormously in their capabilities and in the kinds
of promises they make. There are broadly two types:

- Smart package systems that resolve dependencies and require only a
  symbolic package name.
- Dumb package managers that do not resolve dependencies and need
  filename input.

Normal ordering for packages is the following:

- Delete
- Add
- Update
- Patch

### Promise repair logic

**Identified package matched by name, but not version**

| Command | Dumb manager | Smart manager |
|---------|--------------|---------------|
| add | unable | Never |
| delete | unable | Attempt deletion |
| reinstall | unable | Attempt delete/add |
| upgrade | unable | Upgrade if capable |
| patch | unable | Patch if capable |

**Package not installed**

| Command | Dumb manager | Smart manager |
|---------|--------------|---------------|
| add | Attempt to install named | Install any version |
| delete | unable | unable |
| reinstall | Attempt to install named | unable |
| upgrade | unable | unable |
| patch | unable | unable |


```cf3
    bundle agent packages
    {
    vars:

     # Test the simplest case -- leave everything to the yum smart manager

     "match_package" slist => { 
                              "apache2", 
                              "apache2-mod_php5",
                              "apache2-prefork",
                              "php5" 
                              };
    packages:

      "$(match_package)"

         package_policy => "add",
         package_method => yum;

    }
```

Packages promises can be very simple if the package manager is of the
smart variety that handles details for you. If you need to specify
architecture and version numbers of packages, this adds some complexity,
but the options are flexible and designed for maximal adaptability.

### Patching

Some package systems also support the idea of 'patches'. These might be
formally different objects to packages. A patch might contain material
for several packages and be numbered differently. When you select
patching-policy the package name (promiser) can be a regular expression
that will match possible patch names, otherwise identifying specific
patches can be cumbersome.

Note that patching is a subtle business. There is no simple way using
the patch settings to install 'all new system patches'.

If we specify the name of a patch, then CFEngine will try to see if it
exists and/or is installed. If it exists in the pending list, it will be
installed. If it exists in the installed list it will not be installed.
Now consider the pattern `.*`. This will match any installed package, so
CFEngine will assume the relevant patch has been installed already. On
the other hand, the pattern no match will not match an installed patch,
but it will not match a named patch either.

Some systems provide a command to do this, which can be specified
without specific patch arguments. If so, that command can be called
periodically under `commands`. The main purposes of patching body items
are:

-   To install specific named patches in a controlled manner.
-   To generate reports of available and installed patches during system
    reporting.

### Installers without package/patch arguments

CFEngine supports the syntax `$` at the end of a command to mean that no
package name arguments should be used or appended after the dollar sign.
This is because some commands require a list of packages, while others
require an empty list. The default behavior is to try to append the
name of one or more packages to the command, depending on whether the
policy is for individual or bulk installation.

### Default package method

As of core 3.3.0, if no `package_method` is defined, CFEngine will look
for a method called `generic`. Such a method is defined in the standard
library for supported operating systems.

### Platform notes

Currently, `packages` promises do not work on HP-UX because CFEngine
does not come with package bodies for that platform.

## Attributes ##

[%CFEngine_include_markdown(common-attributes-include.markdown)%]

### package_architectures

**Description:** Select the architecture for package selection

It is possible to specify a list of packages of different architectures
if it is desirable to install multiple architectures on the host. If no
value is specified, CFEngine makes no promise about the result; the
package manager's behavior prevails.

**Type:** `slist`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
packages:

  "$(exact_package)"

     package_policy => "add",
     package_method => rpm,
     package_architectures => { "x86_64" };
```

### package_method

**Type:** `body package_method`

[%CFEngine_include_markdown(common-body-attributes-include.markdown)%]

#### package_add_command

**Description:** Command to install a package to the system

This command should install a package when appended with the package
reference id, formed using the `package_name_convention`, using the
model of (name,version,architecture). If `package_file_repositories` is
specified, the package reference id will include the full path to a
repository containing the package.

Package managers generally expect the name of a package to be passed as
a parameter. However, in some cases we do not need to pass the name of a
particular package to the command. Ending the command string with `$`
prevents CFEngine from appending the package name to the string.   

**Type:** `string`

**Allowed input range:** `.+`

**Example:**

```cf3
     body package_method rpm
     {
     package_add_command => "/bin/rpm -i ";
     }
```

#### package_arch_regex

**Description:** Regular expression with one back-reference to extract
package architecture string

This is for use when extracting architecture from the name of the
promiser, when the architecture is not specified using the
`package_architectures` list. It is an [unanchored][unanchored] regular expression that 
contains exactly one parenthesized back-reference which marks the location in 
the *promiser* at which the architecture is specified.

**Type:** `string`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
     body package_method rpm
     
     {
     package_list_arch_regex    => "[^.]+\.([^.]+)";
     }
```

**Notes:** If no architecture is specified for thegiven package manager, then 
do not define this.   

#### package_changes

**Description:** Defines whether to group packages into a single aggregate 
command.

This indicates whether the package manager is capable of handling
package operations with multiple arguments. If this is set to `bulk` then
multiple arguments will be passed to the package commands. If set to
`individual` packages will be handled one by one. This might add a
significant overhead to the operations, and also affect the ability of
the operating system's package manager to handle dependencies.   

**Type:** (menu option)

**Allowed input range:**   

```
      individual
      bulk
```

**Example:**

```cf3
     body package_method rpm
     
     {
     package_changes => "bulk";
     }
```

#### package_delete_command

**Description:** Command to remove a package from the system

The command that deletes a package from the system when appended with
the package reference identifier specified by `package_name_convention`.

Package managers generally expect the name of a package to be passed as
a parameter. However, in some cases we do not need to pass the name of a
particular package to the command. Ending the command string with `$`
prevents CFEngine from appending the package name to the string.   

**Type:** `string`

**Allowed input range:** `.+`

**Example:**

```cf3
     body package_method rpm
     {
     package_delete_command => "/bin/rpm -e --nodeps";
     }
```

#### package_delete_convention

**Description:** This is how the package manager expects the package to be
referred to in the deletion part of a package update, e.g. `$(name)`

This attribute is used when `package_policy` is `delete`, or
`package_policy` is `update` and `package_file_repositories` is set and
`package_update_command` is not set. It is then used to set the pattern
for naming the package in the way expected by the package manager during
the deletion of existing packages.

Three special variables are defined from the extracted data, in a
private context for use: `$(name)`, `$(version)` and `$(arch)`. `version` and
`arch` is the version and architecture (if `package_list_arch_regex` is given) 
of the already installed package. Additionally, if
`package_file_repositories` is defined, `$(firstrepo)` can be prepended
to expand the first repository containing the package. For example:
`$(firstrepo)$(name)-$(version)-$(arch).msi`.

**Type:** `string`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
     body package_method freebsd
     
     {
     package_file_repositories => { "/path/to/packages" };
     package_name_convention => "$(name)-$(version).tbz";
     package_delete_convention => "$(name)-$(version)";
     }
```

**Notes:**
If this is not defined, it defaults to the value of
`package_name_convention`.   

#### package_file_repositories

**Description:** A list of machine-local directories to search for packages

If specified, CFEngine will assume that the package installation occurs
by filename and will search the named paths for a package matching the
pattern `package_name_convention`. If found the name will be prefixed to
the package name in the package commands.   

**Type:** `slist`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
     body package_method filebased
     {
     package_file_repositories => { "/package/repos1", "/packages/repos2" };
     }
```

#### package_installed_regex

**Description:** Regular expression which matches packages that are already
installed

This regular expression must match complete lines in the output of the
list command that are actually installed packages. If all
the lines match, then the regex can be set of `.*`, however most package
systems output prefix lines and a variety of human padding that needs to
be ignored.

**Type:** `string`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
     body package_method yum
     {
     package_installed_regex => ".*installed.*";
     }
```

#### package_default_arch_command

**Description:** Command to detect the default packages' architecture

This command allows CFEngine to detect default architecture of packages
managed by package manager. As an example, multiarch-enabled dpkg only
lists architectures explicitly for multiarch-enabled packages.

In case this command is not provided, CFEngine treats all packages
without explicit architecture set as belonging to implicit default
architecture.   

**Type:** `string`

**Allowed input range:** `"?(/.*)`

**Example:**

```cf3
     body package_method dpkg
     {
       package_default_arch_command => "/usr/bin/dpkg --print-architecture";
     
       # ...
     }
```

**History:** Was introduced in 3.4.0, Enterprise 3.0.0 (2012)

#### package_list_arch_regex

**Description:** Regular expression with one back-reference to extract
package architecture string

An [unanchored][unanchored] regular expression that contains exactly one parenthesized back
reference that marks the location in the listed package at which the
architecture is specified.

**Type:** `string`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
     body package_method rpm
     {
     package_list_arch_regex    => "[^|]+\|[^|]+\|[^|]+\|[^|]+\|\s+([^\s]+).*";
     }
```

**Notes:** If no architecture is specified for the given package manager, then 
do not define this regex.

#### package_list_command

**Description:** Command to obtain a list of available packages

This command should provide a complete list of the packages installed on
the system. It might also list packages that are not installed. Those
should be filtered out using the `package_installed_regex`.

Package managers generally expect the name of a package to be passed as
a parameter. However, in some cases we do not need to pass the name of a
particular package to the command. Ending the command string with `$`
prevents CFEngine from appending the package name to the string.

**Type:** `string`

**Allowed input range:** `.+`

**Example:**

```cf3
     body package_method rpm
     
     {
     package_list_command => "/bin/rpm -qa --queryformat \"%{name} %{version}-%{release}\n\"";
     }
```

#### package_list_name_regex

**Description:** Regular expression with one back-reference to extract
package name string

An [unanchored][unanchored] regular expression that contains exactly one parenthesized back
reference which marks the name of the package from the package listing.

**Type:** `string`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
     body package_method rpm
     
     {
     package_list_name_regex    => "([^\s]+).*";
     }
```

#### package_list_update_command

**Description:** Command to update the list of available packages (if any)

Not all package managers update their list information from source
automatically. This command allows a separate update command to be
executed at intervals determined by `package_list_update_ifelapsed`.

**Type:** `string`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
     body package_method xyz
     {
     debian|ubuntu::
     
     package_list_update_command => "/usr/bin/apt-get update";
     package_list_update_ifelapsed => "240";        # 4 hours
     }
```

#### package_list_update_ifelapsed

**Description:** The [`ifelapsed`][Promise Types and Attributes#ifelapsed]
locking time in between updates of the package list

**Type:** `int`

**Allowed input range:** `-99999999999,9999999999`

**Example:**

```cf3
     body package_method xyz
     {
     debian|ubuntu::
     
     package_list_update_command => "/usr/bin/apt-get update";
     package_list_update_ifelapsed => "240";        # 4 hours
     }
```

#### package_list_version_regex

**Description:** Regular expression with one back-reference to extract
package version string

This [unanchored][unanchored] regular expression should contain exactly one parenthesized
back-reference that marks the version string of packages listed as
installed.

**Type:** `string`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
     body package_method rpm
     
     {
     package_list_version_regex => "[^\s]+ ([^.]+).*";
     }
```

#### package_name_convention

**Description:** This is how the package manager expects the package to be
referred to, e.g. `$(name).$(arch)`

This sets the pattern for naming the package in the way expected by the
package manager. Three special variables are defined from the extracted
data, in a private context for use: `$(name)`, `$(version)` and `$(arch)`.
Additionally, if `package_file_repositories` is defined, `$(firstrepo)`
can be prepended to expand the first repository containing the package.
For example: `$(firstrepo)$(name)-$(version)-$(arch).msi`.

When `package_policy` is update, and `package_file_repositories` is
specified, `package_delete_convention` may be used to specify a
different convention for the delete command.

If this is not defined, it defaults to the value `$(name)`.

**Type:** `string`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
     body package_method rpm
     {
     package_name_convention => "$(name).$(arch).rpm";
     }
```

#### package_name_regex

**Description:** Regular expression with one back-reference to extract
package name string

This [unanchored][unanchored] regular expression is only used when the *promiser* contains 
not only the name of the package, but its version and architecture also. In
that case, this expression should contain a single parenthesized 
back-reference to extract the name of the package from the string.

**Type:** `string`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
     body package_method rpm
     {
     package_name_regex => "([^\s]).*";
     }
```

#### package_noverify_regex

**Description:** Regular expression to match verification failure output

An[anchored][anchored] regular expression to match output from a package verification
command. If the output string matches this expression, the package is deemed 
broken.

**Type:** `string`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
     body package_method xyz
     
     {
     package_noverify_regex => "Package .* is not installed.*";
     package_verify_command => "/usr/bin/dpkg -s";
     }
```

#### package_noverify_returncode

**Description:** Integer return code indicating package verification
failure

For use if a package verification command uses the return code as the
signal for a failed package verification.

**Type:** `int`

**Allowed input range:** `-99999999999,9999999999`

**Example:**

```cf3
     body package_method xyz
     {
     package_noverify_returncode => "-1";
     package_verify_command => "/bin/rpm -V";
     }
```

#### package_patch_arch_regex

**Description:** [Anchored][anchored] regular expression with one back-reference to 
extract update architecture string

A few package managers keep a separate notion of patches, as opposed to
package updates. OpenSuSE, for example, is one of these. This provides
an analogous command struct to the packages for patch updates.

**Type:** `string`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
     body package_method zypper
     {
     package_patch_arch_regex => "";
     }
```

#### package_patch_command

**Description:** Command to update to the latest patch release of an
installed package

If the package manager supports patching, this command should patch a
named package. If only patching of all packages is supported then
consider running that as a batch operation in `commands`. Alternatively
one can end the command string with a `$` symbol, which CFEngine will
interpret as an instruction to not append package names.

**Type:** `string`

**Allowed input range:** `.+`

**Example:**

```cf3
     body package_method zypper
     
     {
     package_patch_command => "/usr/bin/zypper -non-interactive patch";
     }
```

#### package_patch_installed_regex

**Description:** [Anchored][anchored] regular expression which matches packages that are 
already installed

A few package managers keep a separate notion of patches, as opposed to
package updates. OpenSuSE, for example, is one of these. This provide an
analogous command struct to the packages for patch updates.

**Type:** `string`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
     body package_method zypper
     {
     package_patch_installed_regex => ".*(Installed|Not Applicable).*";
     }
```

#### package_patch_list_command

**Description:** Command to obtain a list of available patches or updates

This command, if it exists at all, is presumed to generate a list of
patches that are available on the system, in a format analogous to (but
not necessarily the same as) the package-list command. Patches might
formally be available in the package manager's view, but if they have
already been installed, CFEngine will ignore them.

Package managers generally expect the name of a package to be passed as
a parameter. However, in some cases we do not need to pass the name of a
particular package to the command. Ending the command string with `$`
prevents CFEngine from appending the package name to the string.   

**Type:** `string`

**Allowed input range:** `.+`

**Example:**

```cf3
      package_patch_list_command => "/usr/bin/zypper patches";
```

#### package_patch_name_regex

**Description:** [Unanchored][unanchored] regular expression with one back-reference to 
extract update name string.

A few package managers keep a separate notion of patches, as opposed to
package updates. OpenSuSE, for example, is one of these. This provides
an analogous command struct to the packages for patch updates.

**Type:** `string`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
     body package_method zypper
     {
     package_patch_name_regex    => "[^|]+\|\s+([^\s]+).*";
     }
```

#### package_patch_version_regex

**Description:** [Unanchored][unanchored] regular expression with one back-reference to 
extract update version string.

A few package managers keep a separate notion of patches, as opposed to
package updates. OpenSuSE, for example, is one of these. This provides
an analogous command struct to the packages for patch updates.

**Type:** `string`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
     body package_method zypper
     {
     package_patch_version_regex => "[^|]+\|[^|]+\|\s+([^\s]+).*";
     }
```

#### package_update_command

**Description:** Command to update to the latest version a currently
installed package

If supported this should be a command that updates the version of a
single currently installed package. If only bulk updates are supported,
consider running this as a single command under `commands`. The package
reference id is appended, with the pattern of `package_name_convention`.

When `package_file_repositories` is specified, the package reference id
will include the full path to a repository containing the package. If
`package_policy` is update, and this command is not specified, the
`package_delete_command` and `package_add_command` will be executed to
carry out the update.

**Type:** `string`

**Allowed input range:** `.+`

**Example:**

```cf3
     body package_method zypper
     {
     package_update_command => "/usr/bin/zypper -non-interactive update";
     }
```

#### package_verify_command

**Description:** Command to verify the correctness of an installed package

If available, this is a command to verify an already installed package.
It is required only when `package_policy` is verify.

The outcome of the command is compared with
`package_noverify_returncode` or `package_noverify_regex`, one of which
has to be set when using this command. If the package is not installed,
the command will not be run the promise gets flagged as not kept before
the verify command executes.

In order for the promise to be considered kept, the package must be
installed, and the verify command must be successful according to
`package_noverify_returncode` xor `package_noverify_regex`.

Package managers generally expect the name of a package to be passed as
a parameter. However, in some cases we do not need to pass the name of a
particular package to the command. Ending the command string with `$`
prevents CFEngine from appending the package name to the string.   

**Type:** `string`

**Allowed input range:** `.+`

**Example:**

```cf3
     body package_method rpm
     
     {
     package_verify_command => "/bin/rpm -V";
     package_noverify_returncode => "-1";
     }
```

#### package_version_regex

**Description:** Regular expression with one back-reference to extract
package version string

If the version of a package is not specified separately using
`package_version`, then this should be an [unanchored][unanchored] regular expression that
contains exactly one parenthesized back-reference that matches the
version string in the promiser.

**Type:** `string`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
     body package_method rpm
     {
     package_version_regex => "[^\s]+ ([^.]+).*";
     }
```

#### package_multiline_start

**Description:** Regular expression which matches the start of a new
package in multiline output

This pattern is used in determining when a new package record begins. It
is used when package managers (like the Solaris package manager) use
multi-line output formats. This pattern matches the first line of a new
record.   

**Type:** `string`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
     body package_method solaris (pkgname, spoolfile, adminfile)
     {
     package_changes => "individual";
     package_list_command => "/usr/bin/pkginfo -l";
     package_multiline_start    =>  "\s*PKGINST:\s+[^\s]+";
     ...
     }
```

#### package_commands_useshell

**Description:** Whether to use shell for commands in this body

**Type:** [`boolean`][boolean]

<!-- **TODO: useshell/noshell/powershell?** -->

**Default value:** true

**History:** Was introduced in 3.4.0, Nova 2.3.0 (2012)

#### package_version_less_command

**Description:** Command to check whether first supplied package version is
less than second one

This attribute allows overriding of the built-in CFEngine algorithm for
version comparison, by calling an external command to check whether the
first passed version is less than another.

The built-in algorithm does a good approximation of version comparison,
but different packaging systems differ in corner cases (e.g Debian
treats symbol `~` less than any other symbol and even less than empty
string), so some sort of override is necessary.

Variables `v1` and `v2` are substituted with the first and second
version to be compared. Command should return code 0 if v1 is less than
v2 and non-zero otherwise.

Note that if `package_version_equal_command` is not specified, but
`package_version_less_command` is, then equality will be tested by
issuing less comparison twice (v1 equals to v2 if v1 is not less than
v2, and v2 is not less than v1).

**Type:** `string`

**Allowed input range:** `.+`

**Example:**

```cf3
     body package_method deb
     {
     ...
     package_version_less_command => "dpkg --compare-versions ${v1} lt ${v2}";
     }
```

**History:** Was introduced in 3.4.0 (2012)

#### package_version_equal_command

**Description:** Command to check whether first supplied package version is
equal to second one

This attribute allows overriding of the built-in CFEngine algorithm for
version comparison by calling an external command to check whether the
passed versions are the same. Some package managers consider textually
different versions to be the same (e.g. optional epoch component, so
0:1.0-1 and 1.0-1 versions are the same), and rules for comparing vary
from package manager to package manager, so override is necessary.

Variables `v1` and `v2` are substituted with the versions to be
compared. Command should return code 0 if versions are equal and
non-zero otherwise.

Note that if `package_version_equal_command` is not specified, but
`package_version_less_command` is, then equality will be tested by
issuing less comparison twice (v1 equals to v2 if v1 is not less than
v2, and v2 is not less than v1).

**Type:** `string`

**Allowed input range:** `.+`

**Example:**

```cf3
     body package_method deb
     {
     ...
     package_version_equal_command => "dpkg --compare-versions ${v1} eq ${v2}";
     }
```

**Notes:**  
   
**History:** Was introduced in 3.4.0 (2012)


### package_policy

**Description:** Criteria for package installation/upgrade on the current
system

**Type:** (menu option)

**Allowed input range:**   

* `add`

Ensure that a package is present (this is the default setting from
3.3.0).   

* `delete`

Ensure that a package is not present.   

* `reinstall`

Delete then add package (warning, non-convergent).   

* `update`

Update the package if an update is available (manager dependent).   

* `addupdate`

Equivalent to add if the package is not installed, and update if it is
installed. Note: This attribute requires the specification of `package_version`
and `package_select` in order to select the proper version to update to if
available. *See Also* [package_latest][Packages Bundles and Bodies#package_latest]
[package_specific_latest][Packages Bundles and Bodies#package_specific_latest] in the
standard library.

* `patch`

Install one or more patches if available (manager dependent).   

* `verify`

Verify the correctness of the package (manager dependent). The promise
is kept if the package is installed correctly, not kept otherwise.
Requires setting `package_verify_command`.


**Default value:** verify

**Example:**

```cf3
packages:

  "$(match_package)"

     package_policy => "add",
     package_method => xyz;
```

### package_select

**Description:** Selects which comparison operator to use with
`package_version`.

This selects the operator used to compare available packages. If an
available package is found to satisfy the version requirement, it may
be selected for install (if `package_policy` is `add`, `update` or
`addupdate`). To select the right package, imagine the available package
being on the left hand side of the operator, and the value in
`package_version` being on the right.

Note that in the case of deleting a package, you must specify an exact
version.

If `package_policy` is `update` or `addupdate`, CFEngine will always
try to keep the most recent package installed that satisfies the version
requirement. For example, if `package_select` is `<` and
`package_version` is `3.0.0`, you may still match updates to 2.x.x
series, like: `2.2.1`, `2.2.2`, `2.3.0`, because they all satisfy the
version requirement.


**Type:** (menu option)

**Allowed input range:**   

```
     <
     >
     ==
     !=
     >=
     <=
```

**Example:**

```cf3
packages:

  "$(exact_package)"

     package_policy => "add",
     package_method => xyz,
     package_select => ">=",
     package_architectures => { "x86_64" },
     package_version => "1.2.3-456";
```

### package_version

**Description:** Version reference point for determining promised version

Used for specifying the targeted package version when the version is
written separately from the name of the command.

**Type:** `string`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
packages:

  "mypackage"

     package_policy => "add",
     package_method => rpm,
     package_select => "==",
     package_version => "1.2.3";
```

