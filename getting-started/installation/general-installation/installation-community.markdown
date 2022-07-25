---
layout: default
title: Installing Community
published: true
sorting: 50
tags: [getting started, installation, community]
---

These instructions describe how to download and install the latest version of CFEngine Community using pre-compiled rpm and
deb packages for Ubuntu, Debian, Redhat, CentOS, and SUSE.

It also provides instructions for the following:

* **Install CFEngine on a Policy Server (hub) and on a Host (client).**
A Policy Server (hub) is a CFEngine instance that contains promises (business policy) that get deployed to Hosts.
Hosts are clients that retrieve and execute promises.
* **Bootstrap the Policy Server to itself and then bootstrap the Host(s) to the Policy Server.**
Bootstrapping establishes a trust relationship between the Policy Server
and all Hosts. Thus, business policy that you create in the Policy Server can be deployed to Hosts throughout your company.
Bootstrapping completes the installation process.

<hr>
## Quick Setup Installation Script

Please Note: Internet access is required from the host if you wish to use the quick install script.

Use the following script to install CFEngine on your 32- or 64-bit machine.

```
$ wget -O- http://cfengine.package-repos.s3.amazonaws.com/quickinstall/quick-install-cfengine-community.sh | sudo bash
```

1. Run this script on your designated Policy Server machine **and** on your designated Host machine(s).
2. Bootstrap the Policy Server to itself and then bootstrap your Host(s) to the Policy Server by running the following command:
```
$ sudo /var/cfengine/bin/cf-agent --bootstrap <IP address of policy server>
```

## 1. Download Packages

Packages can be downloaded from the [community download page][community download page].

## 2. Install CFEngine on a Policy Server

Install the package on a machine designated as a Policy Server.  A Policy Server is a CFEngine instance that contains promises (business policy)
that get deployed to Hosts. Hosts are instances (clients) that retrieve and execute promises.

Choose the right command for your operating system:

**Newer 64-bit RPM based distributions: (Redhat/CentOS/SUSE)**

```
$ sudo rpm -i cfengine-community-{{site.cfengine.branch}}.{{site.cfengine.latest_patch_release}}-{{site.cfengine.latest_package_build}}.el6.x86_64.rpm
```

**Older 64-bit RPM based distributions: (Redhat/CentOS/SUSE)** (not recommended for policy server)

```
$ sudo rpm -i cfengine-community-{{site.cfengine.branch}}.{{site.cfengine.latest_patch_release}}-{{site.cfengine.latest_package_build}}.el4.x86_64.rpm
```

**32-bit RPM based distributions: (Redhat/CentOS/SUSE)** (not recommended for policy server)

```
$ sudo rpm -i cfengine-community-{{site.cfengine.branch}}.{{site.cfengine.latest_patch_release}}-{{site.cfengine.latest_package_build}}.el4.i386.rpm
```

**Newer 64-bit DEB based distributions: (Ubuntu/Debian)**

```
$ sudo dpkg -i cfengine-community_{{site.cfengine.branch}}.{{site.cfengine.latest_patch_release}}-{{site.cfengine.latest_package_build}}_amd64-debian7.deb`
```

**Older 64-bit DEB based distributions: (Ubuntu/Debian)** (not recommended for policy server)

```
$ sudo dpkg -i cfengine-community_{{site.cfengine.branch}}.{{site.cfengine.latest_patch_release}}-{{site.cfengine.latest_package_build}}_amd64-debian4.deb`
```

**32-bit DEB based distributions: (Ubuntu/Debian)** (not recommended for policy server)

```
$ sudo dpkg -i cfengine-community_{{site.cfengine.branch}}.{{site.cfengine.latest_patch_release}}-{{site.cfengine.latest_package_build}}_i386-debian4.deb`
```

**Note:** You might get a message like this: "Policy is not found in /var/cfengine/inputs, not starting CFEngine." Do not worry;
this is taken care of during the bootstrapping process.


## 3. Bootstrap the Policy Server

The Policy Server must be bootstrapped to itself. Find the IP address of your Policy Server.

Run the bootstrap command:

```
$ sudo /var/cfengine/bin/cf-agent --bootstrap <IP address of policy server>
```

**Example: $ sudo /var/cfengine/bin/cf-agent --bootstrap 192.168.1.12**

Upon successful completion, a confirmation message appears: "Bootstrap to '192.168.1.12' completed successfully!"

Type the following to check which version of CFEngine your are running:

```
$ /var/cfengine/bin/cf-promises --version
```

The Policy Server is installed.

## 4. Install CFEngine on a Host

As stated earlier, Hosts are instances that retrieve and execute promises from the Policy Server. Install
a package on your Host. Use the same package you installed on the Policy Server in Step 2. Note that you must have access
to at least one more VM or server and it must be on the same network as the Policy Server that you just installed.

## 5. Bootstrap the Host to the Policy Server

The Host(s) must be bootstrapped to the Policy Server in order to establish a connection between the Host and
the Policy Server. Run the same commands that you ran in Step 3.

```
$ sudo /var/cfengine/bin/cf-agent --bootstrap <IP address of policy server>
```

**Example: $ sudo /var/cfengine/bin/cf-agent --bootstrap 192.168.1.12**

The CFEngine installation process is complete.
