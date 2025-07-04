---
layout: default
title: Installing Enterprise on CoreOS
sorting: 40
---

These instructions describe how to install the latest version of CFEngine
Enterprise on CoreOS. The CoreOS package uses a file-system image in order to
contain modifications to the root file-system.

## Download packages

Download the file-system image package for CoreOS from the [Enterprise Downloads Page](http://cfengine.com/product/free-download).

## Install package

1. On the CoreOS Host, extract the `fs-img-pkg.tar.gz` archive:

    ```command
    tar xvf cfengine-nova-{{site.cfengine.branch}}.{{site.cfengine.latest_patch_release}}-{{site.cfengine.latest_package_build}}.x86_64.fs-img.pkg.tar.gz
    ```

2. On the CoreOS Host, run the install script:

    ```command
    sudo ./cfengine-nova-{{site.cfengine.branch}}.{{site.cfengine.latest_patch_release}}-{{site.cfengine.latest_package_build}}.x86_64.fs-img.pkg/install.sh
    ```

Note: Install actions logged to `/var/log/CFEngine-Install.log`.

## Bootstrap

Run the bootstrap command:

```command
sudo /var/cfengine/bin/cf-agent --bootstrap <IP address of the Policy Server>
```

## Next steps

When bootstrapping is complete, CFEngine is up and running on your system. You
can begin to manage the host through policy and report on its state from Mission
Portal.
