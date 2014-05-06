---
layout: default
title: Software Administration Examples 
published: true
sorting: 4
tags: [Examples,Software Administration]
---

* [Software and patch installation][Software Administration and Execution Examples#Software and patch installation]
* [Postfix mail configuration][Software Administration and Execution Examples#Postfix mail configuration]
* [Set up a web server][Software Administration and Execution Examples#Set up a web server]
* [Add software packages to the system][Software Administration and Execution Examples#Add software packages to the system]
* [Application baseline][Software Administration and Execution Examples#Application baseline]
* [Service management (windows)][Software Administration and Execution Examples#Service management (windows)]
* [Software distribution][Software Administration and Execution Examples#Software distribution]
* [Web server modules][Software Administration and Execution Examples#Web server modules]
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

## Postfix mail configuration

```cf3
#######################################################
#

# Postfix

#

#######################################################


body common control

{
any::

  bundlesequence  => {
                     postfix
                     };   
}

#######################################################


bundle agent postfix

{
vars:

 "prefix"     string => "/etc";
 "smtpserver" string => "localhost";
 "mailrelay"  string => "mailx.example.org";

files:

  "$(prefix)/main.cf"     
      edit_line => prefix_postfix;

  "$(prefix)/sasl-passwd" 
      create    => "true",
      perms     => mo("0600","root"),
      edit_line => append_if_no_line("$(smtpserver) _$(sys.fqhost):chmsxrcynz4etfrejizhs22");
}

#######################################################

# For the library

#######################################################


bundle edit_line prefix_postfix

{
#

# Value have the form NAME = "quoted space separated list"

#

vars:

  "ps[relayhost]"                  string => "[$(postfix.mailrelay)]:587";
  "ps[mydomain]"                   string => "iu.hio.no";
  "ps[smtp_sasl_auth_enable]"      string => "yes";
  "ps[smtp_sasl_password_maps]"    string => "hash:/etc/postfix/sasl-passwd";
  "ps[smtp_sasl_security_options]" string => "";
  "ps[smtp_use_tls]"               string => "yes";
  "ps[default_privs]"              string => "mailman";
  "ps[inet_protocols]"             string => "all";
  "ps[inet_interfaces]"            string => "127.0.0.1";

  "parameter_name" slist => getindices("ps");

delete_lines: 

  "$(parameter_name).*";

insert_lines:

  "$(parameter_name) = $(ps[$(parameter_name)])";

}

########################################################


bundle edit_line AppendIfNSL(parameter)
  {
  insert_lines:

    "$(parameter)"; # This is default
  }
```

## Set up a web server

Adapt this template to your operating system by adding multiple classes. Each web server runs something like the present module, which is entered into the bundlesequence like this:

```cf3
#####################################################
#

# Apache webserver module

# 

#####################################################


bundle agent web_server(state)
{
vars:

  "document_root" string => "/";

 ####################################################

 # Site specific configuration - put it in this file

 ####################################################


  "site_http_conf" string => "/home/mark/CFEngine-inputs/httpd.conf";

 ####################################################

 # Software base

 ####################################################


  "match_package" slist => { 
                           "apache2", 
                           "apache2-mod_php5",
                           "apache2-prefork",
                           "php5" 
                           };

 #########################################################


processes:

  web_ok.on::

   "apache2"
 
     restart_class => "start_apache";

  off::

   "apache2"

     process_stop => "/etc/init.d/apache2 stop";


 #########################################################


commands:

 start_apache::

   "/etc/init.d/apache2 start"; # or startssl

 #########################################################


packages:

  "$(match_package)"

     package_policy => "add",
     package_method => zypper,
     classes => if_ok("software_ok");

 #########################################################


files:

 software_ok::

  "/etc/sysconfig/apache2" 

     edit_line => fixapache,
     classes => if_ok("web_ok");

 #########################################################


reports:

 !software_ok.on::

    "The web server software could not be installed";
 
 #########################################################


classes:

  "on"  expression => strcmp("$(state)","on");
  "off" expression => strcmp("$(state)","off");
}

#######################################################

# For the library

#######################################################


bundle edit_line fixapache

{
vars:

 "add_modules"     slist => { 
                            "ssl", 
                            "php5" 
                            };

 "del_modules"     slist => { 
                            "php3",
                            "php4",
                            "jk"
                            };

insert_lines:

 "APACHE_CONF_INCLUDE_FILES=\"$(web_server.site_http_conf)\"";

field_edits:

 #####################################################################

 # APACHE_MODULES="actions alias ssl php5 dav_svn authz_default jk" etc..

 #####################################################################


   "APACHE_MODULES=.*"

      # Insert module "columns" between the quoted RHS 

      # using space separators


      edit_field => quotedvar("$(add_modules)","append");

   "APACHE_MODULES=.*"

      # Delete module "columns" between the quoted RHS 

      # using space separators


      edit_field => quotedvar("$(del_modules)","delete");

   # if this line already exists, edit it  


}
```

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

## Application baseline

```cf3
#########################################################################

#

#   app_baseline.cf - Verify Existence of Applications

#

#   NOTE: Sometimes applications are not correctly installed even

#         though the native package manager reports them to be.

#         Cfengine can check for application-specific configuration

#         and act upon or report any anomalies.

#

#########################################################################



bundle agent app_baseline
{

methods:
windows::
"any" usebundle => detect_adobereader;


}

###


bundle agent detect_adobereader
{
vars:

windows::
  "value1" string => registryvalue("HKEY_LOCAL_MACHINE\SOFTWARE\Adobe\Acrobat Reader\9.0\Installer", "ENU_GUID");
  "value2" string => registryvalue("HKEY_LOCAL_MACHINE\SOFTWARE\Adobe\Acrobat Reader\9.0\Installer", "VersionMax");
  "value3" string => registryvalue("HKEY_LOCAL_MACHINE\SOFTWARE\Adobe\Acrobat Reader\9.0\Installer", "VersionMin");
 
classes:

windows::
  "is_correct" and => { 
                       strcmp("$(value1)", "{AC76BA86-7AD7-1033-7B44-A93000000001}"),
                       strcmp("$(value2)", "90003"),
                       islessthan("$(value3)", "10001" )
                      };
 
 reports:

windows.!is_correct::
 "Adobe Reader is not correctly deployed - got \"$(value1)\", \"$(value2)\", \"$(value3)\"";
}
```

## Service management (windows)

```cf3
body common control

{
bundlesequence  => { "winservice" };
}

###########################################################


bundle agent winservice

{
vars:

  "bad_services" slist => { "Alerter",  "ClipSrv" };

services:

 windows::

  "$(bad_services)"

       service_policy => "disable",
       comment => "Disable services that create security issues";
}
```

## Software distribution

```cf3
#########################################################################

#

#   software_local.cf - Application Deployment From Directory Repository

#

#   NOTE: Windows needs to support WMI queries about installed msi files

#         in order for Cfengine to detect them. On Windows 2003,

#         go to Control Panel -> Add/Remove Programs -> 

#         Windows Components -> Mgmnt and Monitoring Tools and check

#         WMI Windows Installer Provider.

#

#   NOTE: Naming conventions are important when updating packages.

#         By default, Cfengine expects "name-version-arch.msi" 

#         on Windows, where name is lowercase, and arch is 

#         i686 or x86_64. No spaces should be included in the filename.

#         The Caption and Version fields inside the msi package

#         are important. They must correspond to the file name as 

#         follows: name = lowercase(spacetodash(Caption)), 

#         version = Version. For any msi-file, use InstEd 

#         (www.instedit.com) to check/modify the 

#         Caption and Version fields 

#         (Tables->Property->ProductName/ProductVersion).

#

#         For example, ProductName "CFEngine Nova" with ProductVersion

#         "1.1.2" for 32-bit Windows will correspond to the filename

#         "cfengine-nova-1.1.2-i686.msi".

#

#########################################################################


bundle agent check_software
{
vars:

# software to install if not installed

 "include_software" slist => {
                             "7-zip-4.50-$(sys.arch).msi"
                             };

# this software gets updated if it is installed

 "autoupdate_software" slist => { 
                               "7-zip"
                               };							 

# software to uninstall if it is installed

 "exclude_software" slist => {
                             "7-zip-4.65-$(sys.arch).msi"
                             };

methods:
#  "any" usebundle => add_software( "@(check_software.include_software)", "$(sys.policy_hub)" );

#  "any" usebundle => update_software( "@(check_software.autoupdate_software)", "$(sys.policy_hub)" );

#  "any" usebundle => remove_software( "@(check_software.exclude_software)", "$(sys.policy_hub)" );

}

#########################################################################


bundle agent add_software(pkg_name,
{
vars:
# dir to install from locally - can also check multiple directories

 "local_software_dir" string => "C:\Program Files\Cfengine\software\add";

 
files:

  "$(local_software_dir)"
       copy_from => remote_cp("/var/cfengine/master_software_updates/$(sys.flavour)_$(sys.arch)/add", "$(srv)"),

    depth_search => recurse("1"),

         classes => if_repaired("got_newpkg"),

		 comment => "Copy software from remote repository";



packages:

# When to check if the package is installed ?

 got_newpkg|any::
  "$(pkg_name)"
    package_policy           => "add",

    package_method           => msi_implicit( "$(local_software_dir)" ),

    classes                  => if_else("add_success", "add_fail" ),

    comment                  => "Install new software, if not already present";


reports::
 add_fail::
   "Failed to install one or more packages";
}

#########################################################################


bundle agent update_software(sw_names,
{
vars:
# dir to install from locally - can also check multiple directories

 "local_software_dir" string => "C:\Program Files\Cfengine\software\update";

 
files:

  "$(local_software_dir)"
       copy_from => remote_cp("/var/cfengine/master_software_updates/$(sys.flavour)_$(sys.arch)/update", "$(srv)"),

    depth_search => recurse("1"),

         classes => if_repaired("got_newpkg"),

		 comment => "Copy software updates from remote repository";

 
 
packages:

# When to check if the package is updated ?

 got_newpkg|any::
  "$(sw_names)"
    package_policy           => "update",

    package_select           => ">=",                 # picks the newest update available

    package_architectures    => { "$(sys.arch)" },    # install 32 or 64 bit package ?
    package_version          => "1.0",                # at least version 1.0

    package_method           => msi_explicit( "$(local_software_dir)" ),

    classes                  => if_else("update_success", "update_fail");


	
reports::
 update_fail::
   "Failed to update one or more packages";
}

#########################################################################


bundle agent remove_software(pkg_name,
{
vars:
# dir to install from locally - can also check multiple directories

 "local_software_dir" string => "C:\Program Files\Cfengine\software\remove";

 
files:

  "$(local_software_dir)"
       copy_from => remote_cp("/var/cfengine/master_software_updates/$(sys.flavour)_$(sys.arch)/remove", "$(srv)"),

    depth_search => recurse("1"),

         classes => if_repaired("got_newpkg"),

         comment => "Copy removable software from remote repository";


packages:
got_newpkg::
  "$(pkg_name)"
    package_policy           => "delete",

    package_method           => msi_implicit( "$(local_software_dir)" ),

    classes                  => if_else("remove_success", "remove_fail" ),

    comment                  => "Remove software, if present";


reports::
 remove_fail::
   "Failed to remove one or more packages";
}
```

## Web server modules

The problem of editing the correct modules into the list of standard modules for the Apache web server. This example is based on the standard configuration deployment of SuSE Linux. Simply provide the list of modules you want and another list that you don't want.

```cf3
#######################################################
#

# Apache 2 reconfig - modelled on SuSE

#

#######################################################


body common control

{
any::

  bundlesequence  => {
                     apache
                     };   
}

#######################################################


bundle agent apache

{
files:

 SuSE::

  "/etc/sysconfig/apache2" 

     edit_line => fixapache;
}

#######################################################

# For the library

#######################################################


bundle edit_line fixapache

{ 
vars:

 "add_modules"     slist => { 
                            "dav", 
                            "dav_fs", 
                            "ssl", 
                            "php5", 
                            "dav_svn",
                            "xyz",
                            "superduper"
                            };

 "del_modules"     slist => { 
                            "php3",
                            "jk",
                            "userdir",
                            "imagemap",
                            "alias"
                            };

insert_lines:

 "APACHE_CONF_INCLUDE_FILES=\"/site/masterfiles/local-http.conf\"";

field_edits:

 #####################################################################

 # APACHE_MODULES="authz_host actions alias ..."

 #####################################################################


    # Values have the form NAME = "quoted space separated list"


   "APACHE_MODULES=.*"

      # Insert module "columns" between the quoted RHS 

      # using space separators


      edit_field => quotedvar("$(add_modules)","append");

   "APACHE_MODULES=.*"

      # Delte module "columns" between the quoted RHS 

      # using space separators


      edit_field => quotedvar("$(del_modules)","delete");

   # if this line already exists, edit it  


}
```