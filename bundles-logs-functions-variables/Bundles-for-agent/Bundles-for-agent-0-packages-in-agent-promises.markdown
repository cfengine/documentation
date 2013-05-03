---
layout: default
title: packages-in-agent-promises
categories: [Bundles-for-agent,packages-in-agent-promises]
published: true
alias: Bundles-for-agent-packages-in-agent-promises.html
tags: [Bundles-for-agent,packages-in-agent-promises]
---

### `packages` promises in agent

\

~~~~ {.verbatim}
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
~~~~

CFEngine supports a generic approach to integration with native
operating support for packaging. Package promises allow CFEngine to make
promises regarding the state of software packages *conditionally*, given
the assumption that a native package manager will perform the actual
manipulations. Since no agent can make unconditional promises about
another, this is the best that can be achieved.

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

**Domain knowledge**

CFEngine does not maintain operating system specific expert knowledge
internally, rather it uses a generic model for dealing with promises
about packages (which depend on the behaviour of an external package
manager). The approach is to define package system details in
body-constraints that can be written once and for all, for each package
system.

Package promises are like `commands` promises in the sense that CFEngine
promises nothing about the outcome of executing a command. All it can
promise is to interface with it, starting it and using the results in
good faith. Packages are basically \`outsourced', to invoke IT parlance.

**Behaviour**

A package promise consists of a name, a version and an architecture,
*(n,v,a)*, and behaviour to be promised about packages that match
criteria based on these. The components *(n,v,a)* can be determined in
one of two different ways:

-   They may be specified independently, e.g.

    ~~~~ {.verbatim}
         packages:
         
           "mypackage"
         
              package_policy => "add",
              package_method => rpm,
              package_select => ">=",
              package_architectures => { "x86_64", "i586" },
              package_version => "1.2.3";
         
    ~~~~

-   They may be extracted from a package identifier (promiser) or
    filename, using pattern matching. For example, a promiser
    7-Zip-4.50-x86\_64.msi and a package\_method containing the
    following:

    ~~~~ {.verbatim}
          package_name_regex => "^(\S+)-(\d+\.?)+";
          package_version_regex => "^\S+-((\d+\.?)+)";
          package_arch_regex => "^\S+-[\d\.]+-(.*).msi";
    ~~~~

When scanning a list of installed packages different managers present
the information *(n,v,a)* in quite different forms and pattern
extraction is necessary. When making a promise about a specific package,
the CFEngine user may choose one or the other model.

**Smart and dumb package systems**

Package managers vary enormously in their capabilities and in the kinds
of promises they make. There are broadly two types:

-   Smart package systems that resolve dependencies and require only a
    symbolic package name.
-   Dumb package managers that do not resolve dependencies and need
    filename input.

Normal ordering for packages is the following:

-   Delete
-   Add
-   Update
-   Patch

**Promise repair logic**

We can discuss package promise repair in the following table:

Identified package matches version constraints

  ----------- ---------
  add         never \
              

  delete      =,=,= \
              

  reinstall   =,=,= \
              

  upgrade     =,=,= \
              

  patch       =,=,= \
              
  ----------- ---------

Identified package matched by name, but not version

  -------------------------------------------------
  Command     Dumb manager   Smart manager \
                             
  ----------- -------------- ----------------------
  add         unable         Never \
                             

  delete      unable         Attempt deletion \
                             

  reinstall   unable         Attempt delete/add \
                             

  upgrade     unable         Upgrade if capable \
                             

  patch       unable         Patch if capable \
                             
  -------------------------------------------------

Package not installed

  --------------------------------------------------------------
  Command     Dumb manager               Smart manager \
                                         
  ----------- -------------------------- -----------------------
  add         Attempt to install named   Install any version \
                                         

  delete      unable                     unable \
                                         

  reinstall   Attempt to install named   unable \
                                         

  upgrade     unable                     unable \
                                         

  patch       unable                     unable \
                                         
  --------------------------------------------------------------

\

~~~~ {.verbatim}
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
~~~~

\

Packages promises can be very simple if the package manager is of the
smart variety that handles details for you. If you need to specify
architecture and version numbers of packages, this adds some complexity,
but the options are flexible and designed for maximal adaptability.

**Patching**

Some package systems also support the idea of \`patches'. These might be
formally different objects to packages. A patch might contain material
for several packages and be numbered differently. When you select
patching-policy the package name (promiser) can be a regular expression
that will match possible patch names, otherwise identifying specific
patches can be cumbersome.

Note that patching is a subtle business. There is no simple way using
the patch settings to install \`all new system patches'.

If we specify the name of a patch, then CFEngine will try to see if it
exists and/or is installed. If it exists in the pending list, it will be
installed. If it exists in the installed list it will not be installed.
Now consider the pattern .\*. This will match any installed package, so
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

**Installers without package/patch arguments**

CFEngine supports the syntax \$ at the end of a command to mean that no
package name arguments should be used or appended after the dollar sign.
This is because some commands require a list of packages, while others
require an empty list. The default behaviour is to try to append the
name of one or more packages to the command, depending on whether the
policy is for individual or bulk installation.

**Default package method**

As of core 3.3.0, if no `package_method` is defined, CFEngine will look
for a method called generic. Such a method is defined in the standard
library for supported operating systems.

-   [package\_architectures in
    packages](#package_005farchitectures-in-packages)
-   [package\_method in packages](#package_005fmethod-in-packages)
-   [package\_policy in packages](#package_005fpolicy-in-packages)
-   [package\_select in packages](#package_005fselect-in-packages)
-   [package\_version in packages](#package_005fversion-in-packages)

#### `package_architectures`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: Select the architecture for package selection

**Example**:\
 \

~~~~ {.verbatim}
packages:

  "$(exact_package)"

     package_policy => "add",
     package_method => rpm,
     package_architectures => { "x86_64" };
~~~~

**Notes**:\
 \

It is possible to specify a list of packages of different architectures
if it is desirable to install multiple architectures on the host. If no
value is specified, CFEngine makes no promise about the result; the
package manager's behaviour prevails.

#### `package_method` (body template)

**Type**: (ext body)

`package_add_command`

**Type**: string

**Allowed input range**: `.+`

**Synopsis**: Command to install a package to the system

**Example**:\
 \

~~~~ {.verbatim}
     
     body package_method rpm
     {
     package_add_command => "/bin/rpm -i ";
     }
     
~~~~

**Notes**:\
 \

This command should install a package when appended with the package
reference id, formed using the `package_name_convention`, using the
model of (name,version,architecture). If `package_file_repositories` is
specified, the package reference id will include the full path to a
repository containing the package.

Package managers generally expect the name of a package to be passed as
a parameter. However, in some cases we do not need to pass the name of a
particular package to the command. Ending the command string with \$
prevents CFEngine from appending the package name to the string. \

`package_arch_regex`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: Regular expression with one backreference to extract
package architecture string

**Example**:\
 \

~~~~ {.verbatim}
     
     body package_method rpm
     
     {
     package_list_arch_regex    => "[^.]+\.([^.]+)";
     }
     
~~~~

**Notes**:\
 \

This is for use when extracting architecture from the name of the
promiser, when the architecture is not specified using the
`package_architectures` list. It is a regular expression that contains
exactly one parenthesized back reference which marks the location in the
*promiser* at which the architecture is specified. The regex may match a
portion of the string (see [Anchored vs. unanchored regular
expressions](#Anchored-vs_002e-unanchored-regular-expressions)). If no
architecture is specified for the given package manager, then do not
define this. \

`package_changes`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    individual
                    bulk
~~~~

**Synopsis**: Menu option - whether to group packages into a single
aggregate command

**Example**:\
 \

~~~~ {.verbatim}
     
     body package_method rpm
     
     {
     package_changes => "bulk";
     }
     
~~~~

**Notes**:\
 \
 This indicates whether the package manager is capable of handling
package operations with multiple arguments. If this is set to bulk then
multiple arguments will be passed to the package commands. If set to
individual packages will be handled one by one. This might add a
significant overhead to the operations, and also affect the ability of
the operating system's package manager to handle dependencies. \

`package_delete_command`

**Type**: string

**Allowed input range**: `.+`

**Synopsis**: Command to remove a package from the system

**Example**:\
 \

~~~~ {.verbatim}
     
     body package_method rpm
     
     {
     package_delete_command => "/bin/rpm -e --nodeps";
     }
     
~~~~

**Notes**:\
 \

The command that deletes a package from the system when appended with
the package reference identifier specified by `package_name_convention`.

Package managers generally expect the name of a package to be passed as
a parameter. However, in some cases we do not need to pass the name of a
particular package to the command. Ending the command string with \$
prevents CFEngine from appending the package name to the string. \

`package_delete_convention`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: This is how the package manager expects the package to be
referred to in the deletion part of a package update, e.g. \$(name)

**Example**:\
 \

~~~~ {.verbatim}
     body package_method freebsd
     
     {
     package_file_repositories => { "/path/to/packages" };
     package_name_convention => "$(name)-$(version).tbz";
     package_delete_convention => "$(name)-$(version)";
     }
     
~~~~

**Notes**:\
 \

This attribute is used when `package_policy` is delete, or
`package_policy` is update and `package_file_repositories` is set and
`package_update_command` is not set. It is then used to set the pattern
for naming the package in the way expected by the package manager during
the deletion of existing packages.

Three special variables are defined from the extracted data, in a
private context for use: \$(name), \$(version) and \$(arch). version and
arch is the version and arch (if `package_list_arch_regex` is given) of
the already installed package. Additionally, if
`package_file_repositories` is defined, \$(firstrepo) can be prepended
to expand the first repository containing the package. For example:
\$(firstrepo)\$(name)-\$(version)-\$(arch).msi.

If this is not defined, it defaults to the value of
`package_name_convention`. \

`package_file_repositories`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: A list of machine-local directories to search for packages

**Example**:\
 \

~~~~ {.verbatim}
     
     body package_method filebased
     {
     package_file_repositories => { "/package/repos1", "/packages/repos2" };
     }
     
~~~~

**Notes**:\
 \

If specified, CFEngine will assume that the package installation occurs
by filename and will search the named paths for a package matching the
pattern `package_name_convention`. If found the name will be prefixed to
the package name in the package commands. \

`package_installed_regex`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: Regular expression which matches packages that are already
installed

**Example**:\
 \

~~~~ {.verbatim}
     
     body package_method yum
     {
     package_installed_regex => ".*installed.*";
     }
     
~~~~

**Notes**:\
 \

This regular expression must match complete lines in the output of the
list command that are actually installed packages (see [Anchored vs.
unanchored regular
expressions](#Anchored-vs_002e-unanchored-regular-expressions)). If all
the lines match then the regex can be set of .\*, however most package
systems output prefix lines and a variety of human padding that needs to
be ignored. \

`package_default_arch_command`

**Type**: string

**Allowed input range**: `"?(/.*)`

**Synopsis**: Command to detect the default packages' architecture

**Example**:\
 \

~~~~ {.verbatim}
     body package_method dpkg
     {
       package_default_arch_command => "/usr/bin/dpkg --print-architecture";
     
       # ...
     }
~~~~

**Notes**:\
 \

*History*: Was introduced in 3.4.0, Enterprise 3.0.0 (2012)

This command allows CFEngine to detect default architecture of packages
managed by package manager. As an example, multiarch-enabled dpkg only
lists architectures explicitly for multiarch-enabled packages.

In case this command is not provided, CFEngine treats all packages
without explicit architecture set as belonging to implicit default
architecture. \

`package_list_arch_regex`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: Regular expression with one backreference to extract
package architecture string

**Example**:\
 \

~~~~ {.verbatim}
     
     body package_method rpm
     {
     package_list_arch_regex    => "[^|]+\|[^|]+\|[^|]+\|[^|]+\|\s+([^\s]+).*";
     }
     
~~~~

**Notes**:\
 \

A regular expression that contains exactly one parenthesized back
reference that marks the location in the listed package at which the
architecture is specified. The regular expression may match a portion of
the string (see [Anchored vs. unanchored regular
expressions](#Anchored-vs_002e-unanchored-regular-expressions)). If no
architecture is specified for the given package manager, then do not
define this regex. \

`package_list_command`

**Type**: string

**Allowed input range**: `.+`

**Synopsis**: Command to obtain a list of available packages

**Example**:\
 \

~~~~ {.verbatim}
     
     body package_method rpm
     
     {
     package_list_command => "/bin/rpm -qa --queryformat \"%{name} %{version}-%{release}\n\"";
     }
     
~~~~

**Notes**:\
 \

This command should provide a complete list of the packages installed on
the system. It might also list packages that are not installed. Those
should be filtered out using the `package_installed_regex`.

Package managers generally expect the name of a package to be passed as
a parameter. However, in some cases we do not need to pass the name of a
particular package to the command. Ending the command string with \$
prevents CFEngine from appending the package name to the string. \

`package_list_name_regex`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: Regular expression with one backreference to extract
package name string

**Example**:\
 \

~~~~ {.verbatim}
     
     body package_method rpm
     
     {
     package_list_name_regex    => "([^\s]+).*";
     }
     
~~~~

**Notes**:\
 \

A regular expression that contains exactly one parenthesized back
reference which marks the name of the package from the package listing.
The regular expression may match a portion of the string (see [Anchored
vs. unanchored regular
expressions](#Anchored-vs_002e-unanchored-regular-expressions)). \

`package_list_update_command`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: Command to update the list of available packages (if any)

**Example**:\
 \

~~~~ {.verbatim}
     body package_method xyz
     {
     debian|ubuntu::
     
     package_list_update_command => "/usr/bin/apt-get update";
     package_list_update_ifelapsed => "240";        # 4 hours
     }
~~~~

**Notes**:\
 \

Not all package managers update their list information from source
automatically. This command allows a separate update command to be
executed at intervals determined by `package_list_update_ifelapsed`. \

`package_list_update_ifelapsed`

**Type**: int

**Allowed input range**: `-99999999999,9999999999`

**Synopsis**: The ifelapsed locking time in between updates of the
package list

**Example**:\
 \

~~~~ {.verbatim}
     body package_method xyz
     {
     debian|ubuntu::
     
     package_list_update_command => "/usr/bin/apt-get update";
     package_list_update_ifelapsed => "240";        # 4 hours
     }
~~~~

**Notes**:\
 \

Not all package managers update their list information from source
automatically. This command allows a separate update command to be
executed at intervals determined by `package_list_update_ifelapsed`. \

`package_list_version_regex`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: Regular expression with one backreference to extract
package version string

**Example**:\
 \

~~~~ {.verbatim}
     body package_method rpm
     
     {
     package_list_version_regex => "[^\s]+ ([^.]+).*";
     }
     
~~~~

**Notes**:\
 \

This regular expression should containe exactly one parenthesized
back-reference that marks the version string of packages listed as
installed. The regular expression may match a portion of the string (see
[Anchored vs. unanchored regular
expressions](#Anchored-vs_002e-unanchored-regular-expressions)) \

`package_name_convention`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: This is how the package manager expects the package to be
referred to, e.g. \$(name).\$(arch)

**Example**:\
 \

~~~~ {.verbatim}
     body package_method rpm
     
     {
     package_name_convention => "$(name).$(arch).rpm";
     }
     
~~~~

**Notes**:\
 \

This sets the pattern for naming the package in the way expected by the
package manager. Three special variables are defined from the extracted
data, in a private context for use: \$(name), \$(version) and \$(arch).
Additionally, if `package_file_repositories` is defined, \$(firstrepo)
can be prepended to expand the first repository containing the package.
For example: \$(firstrepo)\$(name)-\$(version)-\$(arch).msi.

When `package_policy` is update, and `package_file_repositories` is
specified, `package_delete_convention` may be used to specify a
different convention for the delete command.

If this is not defined, it defaults to the value \$(name). \

`package_name_regex`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: Regular expression with one backreference to extract
package name string

**Example**:\
 \

~~~~ {.verbatim}
     
     body package_method rpm
     {
     package_name_regex => "([^\s]).*";
     }
     
~~~~

**Notes**:\
 \

This regular expression is only used when the *promiser* contains not
only the name of the package, but its version and architecture also. In
that case, this expression should contain a single parenthesized
back-reference to extract the name of the package from the string. The
regex may match a portion of the string (see [Anchored vs. unanchored
regular expressions](#Anchored-vs_002e-unanchored-regular-expressions))
\

`package_noverify_regex`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: Regular expression to match verification failure output

**Example**:\
 \

~~~~ {.verbatim}
     body package_method xyz
     
     {
     package_noverify_regex => "Package .* is not installed.*";
     package_verify_command => "/usr/bin/dpkg -s";
     }
     
~~~~

**Notes**:\
 \

A regular expression to match output from a package verification
command. If the output string matches this expression, the package is
deemed broken. The regex must match the entire line (see [Anchored vs.
unanchored regular
expressions](#Anchored-vs_002e-unanchored-regular-expressions)) \

`package_noverify_returncode`

**Type**: int

**Allowed input range**: `-99999999999,9999999999`

**Synopsis**: Integer return code indicating package verification
failure

**Example**:\
 \

~~~~ {.verbatim}
     body package_method xyz
     {
     package_noverify_returncode => "-1";
     package_verify_command => "/bin/rpm -V";
     }
~~~~

**Notes**:\
 \

For use if a package verification command uses the return code as the
signal for a failed package verification. \

`package_patch_arch_regex`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: Regular expression with one backreference to extract
update architecture string

**Example**:\
 \

~~~~ {.verbatim}
     
     body package_method zypper
     {
     package_patch_arch_regex => "";
     }
     
~~~~

**Notes**:\
 \

A few package managers keep a separate notion of patches, as opposed to
package updates. OpenSuSE, for example, is one of these. This provides
an analogous command struct to the packages for patch updates. The
regular expression must match the entire line (see [Anchored vs.
unanchored regular
expressions](#Anchored-vs_002e-unanchored-regular-expressions)). \

`package_patch_command`

**Type**: string

**Allowed input range**: `.+`

**Synopsis**: Command to update to the latest patch release of an
installed package

**Example**:\
 \

~~~~ {.verbatim}
     body package_method zypper
     
     {
     package_patch_command => "/usr/bin/zypper -non-interactive patch";
     }
~~~~

**Notes**:\
 \
 If the package manager supports patching, this command should patch a
named package. If only patching of all packages is supported then
consider running that as a batch operation in `commands`. Alternatively
one can end the command string with a \$ symbol, which CFEngine will
interpret as an instruction to not append package names.

Package managers generally expect the name of a package to be passed as
a parameter. However, in some cases we do not need to pass the name of a
particular package to the command. Ending the command string with \$
prevents CFEngine from appending the package name to the string. \

`package_patch_installed_regex`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: Regular expression which matches packages that are already
installed

**Example**:\
 \

~~~~ {.verbatim}
     
     body package_method zypper
     {
     package_patch_installed_regex => ".*(Installed|Not Applicable).*";
     }
     
~~~~

**Notes**:\
 \

A few package managers keep a separate notion of patches, as opposed to
package updates. OpenSuSE, for example, is one of these. This provide an
analogous command struct to the packages for patch updates. The regular
expression must match the entire string (see [Anchored vs. unanchored
regular expressions](#Anchored-vs_002e-unanchored-regular-expressions)).
\

`package_patch_list_command`

**Type**: string

**Allowed input range**: `.+`

**Synopsis**: Command to obtain a list of available patches or updates

**Example**:\
 \

~~~~ {.verbatim}
     
      package_patch_list_command => "/usr/bin/zypper patches";
     
~~~~

**Notes**:\
 \

This command, if it exists at all, is presumed to generate a list of
patches that are available on the system, in a format analogous to (but
not necessarily the same as) the package-list command. Patches might
formally be available in the package manager's view, but if they have
already been installed, CFEngine will ignore them.

Package managers generally expect the name of a package to be passed as
a parameter. However, in some cases we do not need to pass the name of a
particular package to the command. Ending the command string with \$
prevents CFEngine from appending the package name to the string. \

`package_patch_name_regex`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: Regular expression with one backreference to extract
update name string

**Example**:\
 \

~~~~ {.verbatim}
     
     body package_method zypper
     {
     package_patch_name_regex    => "[^|]+\|\s+([^\s]+).*";
     }
~~~~

**Notes**:\
 \

A few package managers keep a separate notion of patches, as opposed to
package updates. OpenSuSE, for example, is one of these. This provides
an analogous command struct to the packages for patch updates. The
regular expression may match a partial string (see [Anchored vs.
unanchored regular
expressions](#Anchored-vs_002e-unanchored-regular-expressions)). \

`package_patch_version_regex`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: Regular expression with one backreference to extract
update version string

**Example**:\
 \

~~~~ {.verbatim}
     
     body package_method zypper
     {
     package_patch_version_regex => "[^|]+\|[^|]+\|\s+([^\s]+).*";
     }
     
~~~~

**Notes**:\
 \

A few package managers keep a separate notion of patches, as opposed to
package updates. OpenSuSE, for example, is one of these. This provides
an analogous command struct to the packages for patch updates. The
regular expression is unanchored, meaning it may match a partial string
(see [Anchored vs. unanchored regular
expressions](#Anchored-vs_002e-unanchored-regular-expressions)). \

`package_update_command`

**Type**: string

**Allowed input range**: `.+`

**Synopsis**: Command to update to the latest version a currently
installed package

**Example**:\
 \

~~~~ {.verbatim}
     
     body package_method zypper
     {
     package_update_command => "/usr/bin/zypper -non-interactive update";
     }
     
~~~~

**Notes**:\
 \

If supported this should be a command that updates the version of a
single currently installed package. If only bulk updates are supported,
consider running this as a single command under `commands`. The package
reference id is appended, with the pattern of `package_name_convention`.

When `package_file_repositories` is specified, the package reference id
will include the full path to a repository containing the package. If
`package_policy` is update, and this command is not specified, the
`package_delete_command` and `package_add_command` will be executed to
carry out the update. \

`package_verify_command`

**Type**: string

**Allowed input range**: `.+`

**Synopsis**: Command to verify the correctness of an installed package

**Example**:\
 \

~~~~ {.verbatim}
     body package_method rpm
     
     {
     package_verify_command => "/bin/rpm -V";
     package_noverify_returncode => "-1";
     }
     
     
~~~~

**Notes**:\
 \

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
particular package to the command. Ending the command string with \$
prevents CFEngine from appending the package name to the string. \

`package_version_regex`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: Regular expression with one backreference to extract
package version string

**Example**:\
 \

~~~~ {.verbatim}
     
     body package_method rpm
     {
     package_version_regex => "[^\s]+ ([^.]+).*";
     }
     
~~~~

**Notes**:\
 \

If the version of a package is not specified separately using
`package_version`, then this should be a regular expression that
contains exactly one parenthesized back-reference that matches the
version string in the promiser. The regular expression is unanchored,
meaning it may match a partial string (see [Anchored vs. unanchored
regular expressions](#Anchored-vs_002e-unanchored-regular-expressions)).
\

`package_multiline_start`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: Regular expression which matches the start of a new
package in multiline output

**Example**:\
 \

~~~~ {.verbatim}
     
     body package_method solaris (pkgname, spoolfile, adminfile)
     {
     package_changes => "individual";
     package_list_command => "/usr/bin/pkginfo -l";
     package_multiline_start    =>  "\s*PKGINST:\s+[^\s]+";
     ...
     }
     
~~~~

**Notes**:\
 \

This pattern is used in determining when a new package record begins. It
is used when package managers (like the Solaris package manager) use
multi-line output formats. This pattern matches the first line of a new
record. \

`package_commands_useshell`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    true
                    false
                    yes
                    no
                    on
                    off
~~~~

**Synopsis**: Whether to use shell for commands in this body

**Default value:** true

**Example**:\
 \

~~~~ {.verbatim}
     
     Fill me in (./bodyparts/package_commands_useshell_example.texinfo)
     ""
~~~~

**Notes**:\
 \

*History*: Was introduced in 3.4.0b1.70bd7ea, Nova 2.3.0.a1.3167b00
(2012)

~~~~ {.verbatim}
     
     Fill me in (./bodyparts/package_commands_useshell_notes.texinfo)
     ""
~~~~

\

`package_version_less_command`

**Type**: string

**Allowed input range**: `.+`

**Synopsis**: Command to check whether first supplied package version is
less than second one

**Example**:\
 \

~~~~ {.verbatim}
     body package_method deb
     {
     ...
     package_version_less_command => "dpkg --compare-versions ${v1} lt ${v2}";
     }
~~~~

**Notes**:\
 \
 *History*: Was introduced in 3.4.0 (2012)

This attribute allows overriding of the built-in CFEngine algorithm for
version comparison, by calling an external command to check whether the
first passed version is less than another.

The built-in algorithm does a good approximation of version comparison,
but different packaging systems differ in corner cases (e.g Debian
treats symbol \~ less than any other symbol and even less than empty
string), so some sort of override is necessary.

Variables `v1` and `v2` are substituted with the first and second
version to be compared. Command should return code 0 if v1 is less than
v2 and non-zero otherwise.

Note that if package\_version\_equal\_command is not specified, but
package\_version\_less\_command is, then equality will be tested by
issuing less comparison twice (v1 equals to v2 if v1 is not less than
v2, and v2 is not less than v1). \

`package_version_equal_command`

**Type**: string

**Allowed input range**: `.+`

**Synopsis**: Command to check whether first supplied package version is
equal to second one

**Example**:\
 \

~~~~ {.verbatim}
     body package_method deb
     {
     ...
     package_version_equal_command => "dpkg --compare-versions ${v1} eq ${v2}";
     }
~~~~

**Notes**:\
 \
 *History*: Was introduced in 3.4.0 (2012)

This attribute allows overriding of the built-in CFEngine algorithm for
version comparison by calling an external command to check whether the
passed versions are the same. Some package managers consider textually
different versions to be the same (e.g. optional epoch component, so
0:1.0-1 and 1.0-1 versions are the same), and rules for comparing vary
from package manager to package manager, so override is necessary.

Variables `v1` and `v2` are substituted with the versions to be
compared. Command should return code 0 if versions are equal and
non-zero otherwise.

Note that if package\_version\_equal\_command is not specified, but
package\_version\_less\_command is, then equality will be tested by
issuing less comparison twice (v1 equals to v2 if v1 is not less than
v2, and v2 is not less than v1).

#### `package_policy`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
               add
               delete
               reinstall
               update
               addupdate
               patch
               verify
~~~~

**Default value:** verify

**Synopsis**: Criteria for package installation/upgrade on the current
system

**Example**:\
 \

~~~~ {.verbatim}
packages:

  "$(match_package)"

     package_policy => "add",
     package_method => xyz;
~~~~

**Notes**:\
 \

This decides what fate is intended for the named package.

add

Ensure that a package is present (this is the default setting from
3.3.0). \

delete

Ensure that a package is not present. \

reinstall

Delete then add package (warning, non-convergent). \

update

Update the package if an update is available (manager dependent). \

addupdate

Equivalent to add if the package is not installed, and update if it is
installed. \

patch

Install one or more patches if available (manager dependent). \

verify

Verify the correctness of the package (manager dependent). The promise
is kept if the package is installed correctly, not kept otherwise.
Requires setting `package_verify_command`.

#### `package_select`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
               
               
               ==
               !=
               =
               =
~~~~

**Synopsis**: A criterion for first acceptable match relative to
"package\_version"

**Example**:\
 \

~~~~ {.verbatim}
packages:

  "$(exact_package)"

     package_policy => "add",
     package_method => xyz,
     package_select => ">=",
     package_architectures => { "x86_64" },
     package_version => "1.2.3-456";
~~~~

**Notes**:\
 \

This selects the operator that compares the promiser to the state of the
system packages currently installed. If the criterion matches, the
policy action is scheduled for promise-keeping.

#### `package_version`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: Version reference point for determining promised version

**Example**:\
 \

~~~~ {.verbatim}
packages:

  "mypackage"

     package_policy => "add",
     package_method => rpm,
     package_select => "==",
     package_version => "1.2.3";
~~~~

**Notes**:\
 \

Used for specifying the targeted package version when the version is
written separately from the name of the command.
