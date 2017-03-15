---
layout: default
title: Installing from Binary tarball on CoreOS
published: false
sorting: 50
tags: [getting started, installation, CoreOS]
---

CFEngine can be installed into a CoreOS host by means of a generic binary
tarball.

First download the binary onto the CoreOS host.

Next unpack the archive:

```sh
tar --gunzip --extract --directory / --file ./cfengine-{{site.cfengine.branch}}.{{site.cfengine.latest_patch_release}}-{{site.cfengine.latest_package_build}}.pkg.tar.gz
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

