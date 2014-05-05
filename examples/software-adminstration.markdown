---
layout: default
title: Software Administration Examples 
published: true
sorting: 4
tags: [Examples][Software Administration]
---

* [Software and patch installation][Software Administration and Execution#Software and patch installation]
* [Postfix mail configuration][Software Administration and Execution#Postfix mail configuration]
* [Set up a web server][Software Administration and Execution#Set up a web server]
* [Add software packages to the system][Software Administration and Execution#Add software packages to the system]
* [Application baseline][Software Administration and Execution#Application baseline]
* [Service management (windows)][Software Administration and Execution#Service management (windows)]
* [Software distribution][Software Administration and Execution#Software distribution]
* [Web server modules][Software Administration and Execution#Web server modules]
* Ensure a service is enabled and running
* Managing Software
* Install packages

## Software and patch installation ##

Example for Debian:

```cf3
# to see list of packages type "apt-cache pkgnames"

# to see list of installed packages type "dpkg --get-selections"

#

# Package managment

#


body common control
{
bundlesequence => { "packages" };
}

body agent control
{
environment => { "DEBIAN_FRONTEND=noninteractive" };
}

#############################################


bundle agent packages
{
vars:

 # Test the simplest case -- leave everything to the yum smart manager


 "match_package" slist => { 
                          "apache2" 
#                          "apache2-mod_php5",

#                          "apache2-prefork",

#                          "php5" 

                          };
packages:

  "$(match_package)"

     package_policy => "add",
     package_method => apt;

}

#############################################


body package_method apt

{
any::

# ii  acpi      0.09-3ubuntu1     


 package_changes => "bulk";
 package_list_command => "/usr/bin/dpkg -l";

 package_list_name_regex    => "ii\s+([^\s]+).*";
 package_list_version_regex => "ii\s+[^\s]+\s+([^\s]+).*";

# package_list_arch_regex    => "none";


 package_installed_regex => ".*"; # all reported are installed

 #package_name_convention => "$(name)_$(version)_$(arch)";

 package_name_convention => "$(name)";

 # Use these only if not using a separate version/arch string

 # package_version_regex => "";

 # package_name_regex => "";

 # package_arch_regex => "";


package_add_command => "/usr/bin/apt-get --yes install";
package_delete_command => "/usr/bin/apt-get --yes remove";
package_update_command =>  "/usr/bin/apt-get --yes dist-upgrade";
#package_verify_command => "/bin/rpm -V";

}
```

Examples MSI for Windows, by name:

```cf3
#

# MSI package managment using file name

#


body common control
{
bundlesequence => { "packages" };
}

#############################################


bundle agent packages
{
vars:

 "match_package" slist => { 
                          "7zip-4.65-x86_64.msi"
                          };
packages:

  "$(match_package)"

     package_policy => "add",

     package_method => msi_fmatch;


}

#############################################


body package_method msi_fmatch

{
 package_changes => "individual";

 package_file_repositories => { "$(sys.workdir)\software_updates\windows", "s:\su" };

 package_installed_regex => ".*";


 package_name_regex    => "^(\S+)-(\d+\.?)+";

 package_version_regex => "^\S+-((\d+\.?)+)";

 package_arch_regex    => "^\S+-(\d+\.?)+(^.+)";

 
 package_name_convention => "$(name)-$(version)-$(arch).msi";


 package_add_command => "\"$(sys.winsysdir)\msiexec.exe\" /qn /i";

 package_update_command => "\"$(sys.winsysdir)\msiexec.exe\" /qn /i";

 package_delete_command => "\"$(sys.winsysdir)\msiexec.exe\" /qn /x";

 }
```

Windows MSI by version:

```cf3
#

# MSI package managment using version criteria

#


body common control
{
bundlesequence => { "packages" };
}

#############################################


bundle agent packages
{
vars:

 "match_package" slist => { 
                          "7zip"
                          };
packages:

  "$(match_package)"

     package_policy => "update",
     package_select => ">=",
     package_architectures => { "x86_64" },
     package_version => "3.00",
     package_method => msi_vmatch;

}

#############################################


body package_method msi_vmatch

{
 package_changes => "individual";
 package_file_repositories => { "$(sys.workdir)\software_updates\windows", "s:\su" };

 package_installed_regex => ".*";
 
 package_name_convention => "$(name)-$(version)-$(arch).msi";

 package_add_command => "\"$(sys.winsysdir)\msiexec.exe\" /qn /i";
 package_update_command => "\"$(sys.winsysdir)\msiexec.exe\" /qn /i";
 package_delete_command => "\"$(sys.winsysdir)\msiexec.exe\" /qn /x";
}
```

Examples for solaris are more complex:

```cf3
#

# Package managment

#


body common control
{
bundlesequence => { "packages" };
inputs => { "cfengine_stdlb.cf" };
}

#############################################


bundle agent packages
{
vars:

  "solaris_packages[SMCzlib]" string => "zlib-1.2.3-sol10-sparc-local";
  "admin_file"                string => "cfengine_admin_file";

  "package_names"              slist => getindices("solaris_packages");

files:

  "/tmp/$(admin_file)"
	create => "true",
	edit_defaults => empty_file,
	edit_line => create_solaris_admin_file;

packages:

  "$(package_names)"

     package_policy => "add",
     package_method => solaris("$(package_names)", "$(solaris_packages[$(package_names)])", "$(admin_file)");

}
```

Examples for yum based systems:

```cf3
#

# Package managment

#


body common control
{
bundlesequence => { "packages" };
inputs => { "cfengine_stdlib.cf" }
}

#############################################


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

SuSE Linux's package manager zypper is the most powerful alternative:

```cf3
#

# Package managment

#


body common control
{
bundlesequence => { "packages" };
inputs => { "cfengine_stdlib.cf" }
}

#############################################


bundle agent packages
{
vars:

 # Test the simplest case -- leave everything to the zypper smart manager


 "match_package" slist => { 
                          "apache2", 
                          "apache2-mod_php5",
                          "apache2-prefork",
                          "php5" 
                          };
packages:

  "$(match_package)"

     package_policy => "add",
     package_method => zypper;

}
```

## Postfix mail configuration ##
## Set up a web server ##
## Add software packages to the system ##

```cf3

#
# Package managment

#


body common control
{
bundlesequence => { "packages" };
}

#############################################


bundle agent packages
{
vars:

 "match_package" slist => { 
                          "apache2", 
                          "apache2-mod_php5",
                          "apache2-prefork",
                          "php5" 
                          };
packages:

 solaris::

  "$(match_package)"

     package_policy => "add",
     package_method => solaris;

 redhat|SuSE::

  "$(match_package)"

     package_policy => "add",
     package_method => yum;

}
```

Note you can also arrange to hide all the differences between package managers on an OS basis, but since some OSs have multiple managers, this might not be 100 percent correct.

## Application baseline ##
## Service management (windows) ##
## Software distribution ##
## Web server modules ##