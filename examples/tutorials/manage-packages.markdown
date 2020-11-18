---
layout: default
title: Manage packages
published: true
sorting: 3
tags: [getting started, tutorial]
---

Package management is a critical task for any system administrator. In this
tutorial we will show you how easy it is to install, manage and remove packages
using CFEngine.

As a first example, we will use CFEngine to update OpenSSL, which is timely
given the recent disclosure of the Heartbleed vulnerability. If we simply want
to make sure the latest version of OpenSSL is installed in all our hosts, we can
use the packages promise type, like this:

```cf3
body common control
{
      inputs => { "$(sys.libdir)/stdlib.cf"" };
}

bundle agent manage_packages
{
packages:
  "openssl"
    policy => "present",
    version => "latest",
    package_module => yum;
}
bundle agent __main__
{
  methods:
    "manage_packages";
}
```

The `package_module` promise attribute tells CFEngine which package manager we
want to use. Defaults can be set up by using the `package_module` common control
attribute. When we run this on an CentOS 6 system, we can verify the openssl
version before and after running the policy, and we get the following output:

```console
# yum list installed | grep openssl
openssl.x86_64          1.0.0-27.el6    @anaconda-CentOS-201303020151.x86_64/6.4
openssl-devel.x86_64    1.0.0-27.el6    @anaconda-CentOS-201303020151.x86_64/6.4
# cf-agent -K ./manage_packages.cf"
# yum list installed | grep openssl
openssl.x86_64          1.0.1e-42.el6   @base                                   
openssl-devel.x86_64    1.0.1e-42.el6   @base         
```

Additionally, you may want to make sure certain packages are not installed on
the system. On my CentOS 6 system, I can see that the telnet package is
installed.

```console
# yum list installed | grep telnet
telnet.x86_64           1:0.17-48.el6   @base 
# which telnet
/usr/bin/telnet
```

Making sure this package is removed from the system is easy. Let's add one more
promise to our previous policy, this time using the absent policy:

```cf3
body common control
{
      inputs => { "$(sys.libdir)/stdlib.cf"" };
}

bundle agent manage_packages
{
packages:
  "openssl"
    policy => "present",
    version => "latest",
    package_module => yum;

"telnet"
    policy => "absent",
    package_module => yum;

}
bundle agent __main__
{
  methods:
    "manage_packages";
}
```

Note that we leave the previous line in place. This way, CFEngine will continue
to ensure that the openssl package is always updated to its latest version. We
can now see the policy in action:

```console
# cf-agent -K ./manage_packages.cf"
# yum list installed | grep telnet
# which telnet
/usr/bin/which: no telnet in (/sbin:/bin:/usr/sbin:/usr/bin:/var/cfengine/bin)
```

The packages promise also supports version pinning, so that you can specify
exactly the version you want to have installed. It is modular and extensible, so
that it is easy to add support for new platforms and package managers. For
complete documentation, please have a look at the reference manual for the
packages promise.

Of course, running the policy by hand is only good for initial testing. Once
your policy works the way you need, you will want to deploy it to your entire
infrastructure by integrating your policy into your regular cf-agent execution,
thus making sure that the desired state of your packages is always kept
automatically on all your machines. To do so, you need to do the following:

Copy `manage_packages.cf` to `/var/cfengine/masterfiles/` on your policy hub. In
`/var/cfengine/masterfiles/def.json`, add `manage_packages.cf` to the inputs
declaration, and `manage_packages` to the bundlesequence declaration.

```json
{
  "inputs": [ "manage_packages.cf" ],
  "vars": {
    "control_common_update_bundlesequence_end": [ "manage_packages" ]
    }
}
```

Run `cf-promises` on the policy to verify that there are no errors.

```
# cf-promises -cf /var/cfengine/masterfiles/promises.cf
```

Wait a few minutes for the new policy to propagate and start taking effect in
your entire infrastructure. This is where the real power of CFEngine becomes
apparent! With few changes in a single place, you can control the desired state
of your entire infrastructure, whether it’s composed of a few or many thousands
of machines.

