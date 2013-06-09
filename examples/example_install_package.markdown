---
layout: default
title: Install packages
categories: [Examples, Install packages]
published: true
alias: examples-install-package;.html
tags: [Examples, packages]
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
