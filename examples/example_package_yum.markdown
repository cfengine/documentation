---
layout: default
title: Software and Patch Installation
categories: [Examples, Software and Patch Installation]
published: true
alias: examples-software-and-patch-installation.html
tags: [Examples, software, package management, apt, msi, yum, zypper]
---

This is a standalone policy that will install a list of packages on a yum based system.
CFEngine interfaces with the package manager and lets it do the job. The CFEngine
Standard Library (cfengine_stdlib.cf) should be included in the
`/var/cfengine/inputs/libraries/` directory and input as below.

```cf3
	body common control
	{
	bundlesequence => { "packages" };
	inputs => { "libraries/cfengine_stdlib.cf" };
	}

	#############################################

	bundle agent packages
	{
	vars:

	 # Test the simplest case -- leave everything to the yum smart manager

	 "match_package" slist => {                   # List of packages to install
		                  "apache2",
		                  "apache2-mod_php5",
		                  "apache2-prefork",
		                  "php5"
		                  };
	packages:

	  "$(match_package)"

	     package_policy => "add",                 # Install the packages
	     package_method => yum;                   # Use yum to install

	}
```

CFEngine will download the necessary packages from the default repositories if they are not present on the local machine, then install them if they are not already installed.

This policy can be found in `/var/cfengine/share/doc/examples/unit_package_yum.cf`. Similar policy examples are available in `/var/cfengine/share/doc/examples/` for:

- Debian (unit_package_apt.cf)
- MSI for Windows (unit_package_msi_file.cf)
- Solaris (unit_package_solaris.cf)
- SuSE Linux (unit_package_zypper.cf)
