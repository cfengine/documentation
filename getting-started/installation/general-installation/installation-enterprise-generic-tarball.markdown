---
layout: default
title: Installing from Binary tarball
published: true
sorting: 50
tags: [getting started, installation]
---

Not all systems come with a package manager. For these systems you can install
CFEngine by means of a generic binary tarball.

First download the binary onto the host.

Next unpack the archive. For the 64 bit tarball use:

```sh
tar --gunzip --extract --directory / --file ./cfengine-nova-{{site.cfengine.branch}}.{{site.cfengine.latest_patch_release}}-{{site.cfengine.latest_package_build}}.x86_64.pkg.tar.gz
```

Otherwise, for 32 bit tarball, use:

```sh
tar --gunzip --extract --directory / --file ./cfengine-nova-{{site.cfengine.branch}}.{{site.cfengine.latest_patch_release}}-{{site.cfengine.latest_package_build}}.i386.pkg.tar.gz
```

Generate a keypair for the client:

```sh
/var/cfengine/bin/cf-key
```

Then install the systemd units:

```sh
  for each in $(ls /var/cfengine/share/usr/lib/systemd/system); do
    cp /var/cfengine/share/usr/lib/systemd/system/${each} /etc/systemd/system/${each}
    chmod 664 /etc/systemd/system/${each}
  done
  systemctl daemon-reload 
```

Next enable the necessary service units:

```sh
  systemctl enable cf-execd 
  systemctl enable cf-monitord 
  systemctl enable cf-serverd 
  systemctl enable cfengine3 
```

Finally, bootstrap the agent, and start the cfengine services:

```sh

  export POLICY_SERVER="myhub";

  # Bootstrap to hub
  /var/cfengine/bin/cf-agent --bootstrap ${POLICY_SERVER}

  # Start the cfengine3 service.
  systemctl start cfengine3 
```

