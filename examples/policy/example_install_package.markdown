---
layout: default
title: Install packages
categories: [Examples, Policy, Install packages]
published: true
alias: examples-policy-install-package.html
tags: [Examples, Policy, packages]
reviewed: 2013-06-08
reviewed-by: atsaloli
---


Install desired packages.

```cf3
body common control
{
bundlesequence => { "install_packages" };
inputs => { "libraries/cfengine_stdlib.cf" };
}

bundle agent install_packages
{

vars:
    "desired_packages"
        slist => {        # list of packages we want
                  "ntp",
                  "lynx"
                 };

packages:

    "$(desired_packages)"  # operate on listed packages

         package_policy => "add",     # What to do with packages: install them.
         package_method => generic;   # Infer package manager (e.g. apt, yum) from the OS.
}
```

Caution: package management is a dirty business. If things don't go smoothly
using the generic method, you may have to use a method specific to your package
manager and get to your elbows in the details. But try `generic` first. You
may get lucky.

Mind package names can differ OS to OS.  For example, Apache httpd
is "httpd" on Red Hat, and "apache2" on Debian.  

Version comparison can be tricky when involving multipart version
identifiers with numbers and letters.

CFEngine downloads the necessary packages from the default repositories if they are not present on the local machine, then installs them if they are not already installed.

Example run:

```
# dpkg -r lynx ntp # remove packages so CFEngine has something to repair
(Reading database ... 234887 files and directories currently installed.)
Removing lynx ...
Removing ntp ...
 * Stopping NTP server ntpd                                                                                                                     [ OK ] 
Processing triggers for ureadahead ...
Processing triggers for man-db ...
# cf-agent -f install_packages.cf # install packages
# dpkg -l lynx ntp # show installed packages
Desired=Unknown/Install/Remove/Purge/Hold
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||/ Name                            Version              Architecture         Description
+++-===============================-====================-====================-====================================================================
ii  lynx                            2.8.8dev.12-2ubuntu0 all                  Text-mode WWW Browser (transitional package)
ii  ntp                             1:4.2.6.p3+dfsg-1ubu amd64                Network Time Protocol daemon and utility programs
# 
```

There are examples in `/var/cfengine/share/doc/examples/` of installing packages using specific package managers:
- Red Hat (unit_package_yum.cf)
- Debian (unit_package_apt.cf)
- MSI for Windows (unit_package_msi_file.cf)
- Solaris (unit_package_solaris.cf)
- SuSE Linux (unit_package_zypper.cf)
