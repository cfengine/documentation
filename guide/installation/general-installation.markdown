---
layout: default
title: General Installation
published: true
sorting: 3
tags: [guide, installation, install]
---

[%CFEngine_include_markdown(include-install-bootstrap-configure-summary.markdown)%]

## Before Installation ##

Check the [Pre-Installation Checklist][Pre-Installation Checklist] and [Supported Platforms][Supported Platforms] for requirements and other information that is useful for the installation procedure.

## Install Packages ##

CFEngine Enterprise is provided in two packages; one is for the Policy
Server (hub) and the other is for each Host (client). 

Note: See [Installing Community][Installing Community] for the community version of CFEngine)

**Log in as root** and then follow these steps to install CFEngine Enterprise:

1. On the designated Policy Server, install the `cfengine-nova-hub` package:

    ```
        [RedHat/CentOS/SUSE] $ rpm -i <hub package>.rpm
        [Debian/Ubuntu]      $ dpkg -i <hub package>.deb
    ```

2. On each Host, install the `cfengine-nova` package:

    ```
        [RedHat/CentOS/SUSE] $ rpm -i <agent package>.rpm
        [Debian/Ubuntu]      $ dpkg -i <agent package>.deb
    ```

Note: Install actions logged to `/var/logs/cfengine-install.log`.

## Bootstrap ##

Run the bootstrap command, **first** on the policy server and then on each
host:

```
$ /var/cfengine/bin/cf-agent --bootstrap <IP address of the Policy Server>
```

## Next Steps ##

* Learn about [Writing Policy and Promises][Writing Policy and Promises]


Although most install procedures follow the same general workflow, there are several ways of installing CFEngine depending on your environment and which version of CFEngine you are using.

* [Installing Enterprise for Production][Installing Enterprise for Production]
* Install and test the latest version using our [native version][Installing Enterprise 25 Free], for free!
* Installing CFEngine on virtual machine instances using [Amazon Web Services' (AWS) EC2 service][Installing CFEngine on RHEL Using AWS]
	* This is especially useful for people running Windows on their workstation or laptop.
* Install and test the latest version using our pre-packaged [Vagrant environment][Installing Enterprise Vagrant Environment]
* [Installing CFEngine Community Edition][Installing Community]

