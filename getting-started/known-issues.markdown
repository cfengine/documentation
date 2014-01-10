---
layout: default
title: Known Issues
sorting: 50
categories: [Getting Started, Known Issues]
published: true
alias: getting-started-known-issues.html
tags: [getting started, known issues]
---

CFEngine defects are managed in our [bug tracker][bug tracker]. Please report
bugs or unexpected behavior there, following the documented guideline for new
bug reports.

The items below highlight issues that require additional awareness when starting
with CFEngine or when upgrading from a previous version.

### Comma in promiser/promisee declaration generates Syntax Error

The policy file parser is stricter in CFEngine 3.5.0 . The parser is now fully 
compliant with the CFEngine [language syntax reference][Language Concepts].
The main difference you will encounter is that promiser/promisee no longer 
allows a comma at the end of the line. This will cause your existing policies 
to produce errors when they are read by CFEngine 3.5.0.

An example of what you might see as a result of this issue can be found below:

```cf3
/var/cfengine/inputs/CFE_hub_specific.cf:621:28: error: syntax error
Q: ".../cf-execd"":    "/usr/sbin/a2enmod php5",
Q: ".../cf-execd"":                            ^
Q: ".../cf-execd"": /var/cfengine/inputs/CFE_hub_specific.cf:621:28: error: Expected attribute, got ','
Q: ".../cf-execd"":    "/usr/sbin/a2enmod php5",
Q: ".../cf-execd"":                            ^
```

This can be remedied by editing the policy and removing the comma at the end 
of the appropriate promiser/promisee line.

### On Windows platforms, cf-serverd listens only to IPv6 interface

There is a policy-level workaround for this one, add the following to `body server control` in `masterfiles/controls/cf-serverd.cf`:

```cf3
bindtointerface => "0.0.0.0";
```

### cf-execd sends out emails on every execution

**This problem is solved as of CFEngine 3.5.1**

The inclusion of the timestamp in the new log output format causes this
behavior. This will be resolved in the next release.

Current workaround options include disabling email by commenting out `mailto` and
`smtpserver` in `body executor control` or by running `cf-agent` from cron.

https://cfengine.com/dev/issues/3011

### Enterprise upgrade using master_software_updates does not work

The behavior of packages promises on 3.5.x is slightly different from
3.0.x. This has caused the bundled policy in `update/update_bins.cf` to not work.
**Dropping the latest packages into the appropriate directory
will not work.**

The workaround is to patch the policy to be more specific regarding the
CFEngine version number. (`package_select => "=="` and `package_version =>
"3.5.3-1"`)

#### Linux Clients 
`update/update_bins.cf`:

```cf3
 !am_policy_hub.linux::

   "$(novapkg)"
                    comment => "Update Nova package to a newer version (package is there)",
                     handle => "cfe_internal_update_bins_packages_nova_update_not_windows_pkg_there",
             package_policy => "update",
             package_select => "==",
      package_architectures => { "$(pkgarch)" },
            package_version => "3.5.3-1",
             package_method => u_generic( "$(local_software_dir)" ),
                 ifvarclass => "nova_edition",
                    classes => u_if_else("bin_update_success", "bin_update_fail");
```

Diff of the changes required for linux clients:

```DiffLexer
diff --git a/update/update_bins.cf b/update/update_bins.cf
index b9747b8..8162826 100755
--- a/update/update_bins.cf
+++ b/update/update_bins.cf
@@ -156,15 +156,15 @@ bundle agent cfe_internal_update_bins
                  ifvarclass => "nova_edition",
                     classes => u_if_else("bin_update_success", "bin_update_fail");

-  !am_policy_hub.!windows::
+  !am_policy_hub.linux::

    "$(novapkg)"
                     comment => "Update Nova package to a newer version (package is there)",
                      handle => "cfe_internal_update_bins_packages_nova_update_not_windows_pkg_there",
              package_policy => "update",
-             package_select => ">=",            # picks the newest Nova available
+             package_select => "==",            # picks the newest Nova available
       package_architectures => { "$(pkgarch)" },
-            package_version => "9.9.9",         # Install new Nova anyway
+            package_version => "3.5.3-1",         # Install new Nova anyway
              package_method => u_generic( "$(local_software_dir)" ),
                  ifvarclass => "nova_edition",
                     classes => u_if_else("bin_update_success", "bin_update_fail");
```

Windows uses a slightly different version format from Linux. You may obtain the
information by running appwiz.cpl (Add or Remove Programs) and select
cfengine-nova. (3.5.0.65534)

#### Windows Clients

`update/update_bins.cf`:

```cf3
  !am_policy_hub.windows::

   "$(novapkg)"
                    comment => "Update Nova package to a newer version (package is there)",
                     handle => "cfe_internal_update_bins_packages_nova_update_windows_only_pkg_there",
             package_policy => "update",
             package_select => "==",
      package_architectures => { "$(pkgarch)" },
            package_version => "3.5.3.0",
             package_method => u_generic( "$(local_software_dir)" ),
                 ifvarclass => "nova_edition",
                    classes => u_if_else("bin_update_success", "bin_update_fail");
```

```DiffLexer
diff --git a/update/update_bins.cf b/update/update_bins.cf
index b9747b8..625416c 100755
--- a/update/update_bins.cf
+++ b/update/update_bins.cf
@@ -175,9 +175,9 @@ bundle agent cfe_internal_update_bins
                     comment => "Update Nova package to a newer version (package is there)",
                      handle => "cfe_internal_update_bins_packages_nova_update_windows_only_pkg_there",
              package_policy => "update",
-             package_select => ">=",            # picks the newest Nova available
+             package_select => "==",            # picks the newest Nova available
       package_architectures => { "$(pkgarch)" },
-            package_version => "9.9.9.9",       # Install new Nova anyway
+            package_version => "3.5.3.0",       # Install new Nova anyway
              package_method => u_generic( "$(local_software_dir)" ),
                  ifvarclass => "nova_edition",
                     classes => u_if_else("bin_update_success", "bin_update_fail");
```

#### Solaris Clients
**This is very important**

The `package_update_command` attribute is missing in `update/update_bins.cf`.
Add this line manually under Solaris package_method() section and let it roll
out before doing the Solaris upgrade. Otherwise, your Solaris clients will be
left alone without CFEngine running on the hosts!

`update/update_bins.cf`:

```cf3
solarisx86|solaris::

 package_changes => "individual";
 package_list_command => "/usr/bin/pkginfo -l";
 package_list_update_command => "/usr/bin/true";
 package_list_update_ifelapsed => "1440";  # cachine once a day

 package_multiline_start    => "\s*PKGINST:\s+[^\s]+";
 package_list_name_regex    => "\s*PKGINST:\s+([^\s]+)";
 package_list_version_regex => "\s*VERSION:\s+([^\s]+)";
 package_list_arch_regex    => "\s*ARCH:\s+([^\s]+)";

 package_file_repositories  => { "$(repo)" };

 package_installed_regex    => "\s*STATUS:\s*(completely|partially)\s+installed.*";
 package_name_convention    => "$(name)-$(version)-$(arch).pkg";
 package_delete_convention  => "$(name)";

 # Cfengine appends path to package and package name below, respectively
 package_add_command        => "/bin/sh $(repo)/add_scr $(repo)/admin_file";
 package_update_command     => "/bin/sh $(repo)/upg_scr $(repo)/admin_file";
 package_delete_command     => "/usr/sbin/pkgrm -n -a $(repo)/admin_file";
```

```DiffLexer
diff --git a/update/update_bins.cf b/update/update_bins.cf
index b9747b8..33535b8 100755
--- a/update/update_bins.cf
+++ b/update/update_bins.cf
@@ -403,6 +403,7 @@ solarisx86|solaris::

  # Cfengine appends path to package and package name below, respectively
  package_add_command        => "/bin/sh $(repo)/add_scr $(repo)/admin_file";
+ package_update_command     => "/bin/sh $(repo)/upg_scr $(repo)/admin_file";
  package_delete_command     => "/usr/sbin/pkgrm -n -a $(repo)/admin_file";

 aix::
```

On Solaris, a wrapper script and admin file are needed to automatically
silently upgrade CFEngine. The files are located in
`/var/cfengine/share/solaris_admin_files` on the policy server. You must have
those files along with PKG package in the directory. For example:

```
$ cp /var/cfengine/share/solaris_admin_files/sol_9_and_10/* /var/cfengine/master_software_updates/sunos_5.10_sun4u
$ ls -l /var/cfengine/master_software_updates/sunos_5.10_sun4u/
total 26468
-rwxr-xr-x 1 root root       36 Dec  6 16:34 add_scr
-rwxr-xr-x 1 root root      257 Dec  6 16:34 admin_file
-rw-r--r-- 1 root root 27090944 Dec  5 15:58 CFEcfengine-nova-3.5.3-sparc.pkg
-rwxr-xr-x 1 root root      125 Dec  6 16:34 upg_scr
```

Adjust the `package_select` and `package_version` attributes; (Version number on Solaris is
only major release number (3.5.3), not hypen and revision number. (-1))

`update/update_bins.cf`:

```cf3
  !am_policy_hub.solaris::

   "$(novapkg)"
                    comment => "Update Nova package to a newer version (package is there)",
                     handle => "cfe_internal_update_bins_packages_nova_update_windows_only_pkg_there",
             package_policy => "update",
             package_select => "==",
      package_architectures => { "$(pkgarch)" },
            package_version => "3.5.3",
             package_method => u_generic( "$(local_software_dir)" ),
                 ifvarclass => "nova_edition",
                    classes => u_if_else("bin_update_success", "bin_update_fail");
```

```DiffLexer
diff --git a/update/update_bins.cf b/update/update_bins.cf
index b9747b8..b26df4b 100755
--- a/update/update_bins.cf
+++ b/update/update_bins.cf
@@ -182,6 +182,18 @@ bundle agent cfe_internal_update_bins
                  ifvarclass => "nova_edition",
                     classes => u_if_else("bin_update_success", "bin_update_fail");

+  !am_policy_hub.solaris::
+
+   "$(novapkg)"
+                    comment => "Update Nova package to a newer version (package is there)",
+                     handle => "cfe_internal_update_bins_packages_nova_update_windows_only_pkg_there",
+             package_policy => "update",
+             package_select => "==",
+      package_architectures => { "$(pkgarch)" },
+            package_version => "3.5.3",
+             package_method => u_generic( "$(local_software_dir)" ),
+                 ifvarclass => "nova_edition",
+                    classes => u_if_else("bin_update_success", "bin_update_fail");
 #

  files:
```

If the client packages are copied but don't get installed, please verify that
the package_name matches `package_name_convention` in `body package_method
u_generic`.

### Installing cfengine-nova installs cfengine-nova-hub instead when packages are in yum repository

When a host attempts to install cfengine-nova from a private yum package
repository and that host also has the cfengine-nova-hub package available from
a repository source, the cfengine-nova-hub package gets installed instead.

https://cfengine.com/dev/issues/2956

#### Workaround

Remove cfengine-nova-hub from the yum repository and install the hub using rpm.
