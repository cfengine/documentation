---
layout: default
title: Installing Community
published: true
sorting: 50
---

These instructions describe how to download and install the latest version of CFEngine Community using pre-compiled rpm and
deb packages for Ubuntu, Debian, Redhat, CentOS, and SUSE.

It also provides instructions for the following:

* **Install CFEngine on a policy server (hub) and on a Host (client).**
A Policy Server (hub) is a CFEngine instance that contains promises (business policy) that get deployed to Hosts.
Hosts are clients that retrieve and execute promises.
* **Bootstrap the policy server to itself and then bootstrap the Host(s) to the Policy Server.**
Bootstrapping establishes a trust relationship between the Policy Server
and all Hosts. Thus, business policy that you create in the Policy Server can be deployed to Hosts throughout your company.
Bootstrapping completes the installation process.

<hr>
## Quick setup with cf-remote

`cf-remote` can be used to easily download, install, and bootstrap CFEngine on a host.

Once `cf-remote` is installed from the Python Package Index (e.g. `pipx install cf-remote`), execute it against a host (either local or remote).

For example, here we install CFEngine Community {{site.cfengine.branch}}.{{site.cfengine.latest_patch_release}} on two hosts and bootstrap to one of them:

```command
cf-remote --version={{site.cfengine.branch}}.{{site.cfengine.latest_patch_release}} install --edition community --clients 192.168.56.13,192.168.56.14 --bootstrap 192.168.56.13
```
## 1. Download packages

Packages can be downloaded from the [community download page][community download page] or using `cf-remote`.

For example, this command downloads CFEngine 3.24.1 packages for ubuntu24 into the current directory:

```command
cf-remote --version 3.24.1 download ubuntu24 --edition community --output-dir .
```
```output
Available releases: master, 3.25.0, 3.24.x, 3.24.1, 3.24.0, 3.21.x, 3.21.6, 3.21.5, 3.21.4, 3.21.3, 3.21.2, 3.21.1, 3.21.0
Using 3.24.1 LTS:
Downloading package: '/home/user/.cfengine/cf-remote/packages/cfengine-community_3.24.1-1.ubuntu24_arm64.deb'
Copied to '/tmp/cfengine-community_3.24.1-1.ubuntu24_arm64.deb' (Checksum OK).
Downloading package: '/home/user/.cfengine/cf-remote/packages/cfengine-community_3.24.1-1.ubuntu24_amd64.deb'
Copied to '/tmp/cfengine-community_3.24.1-1.ubuntu24_amd64.deb' (Checksum OK).
```

## 2. Install CFEngine on a policy server

Install the package on a machine designated as a Policy Server.  A Policy Server is a CFEngine instance that contains promises (business policy)
that get deployed to Hosts. Hosts are instances (clients) that retrieve and execute promises.

Choose the right command for your operating system:

**Newer 64-bit RPM based distributions: (Redhat/CentOS/SUSE)**

```command
sudo rpm -i cfengine-community-{{site.cfengine.branch}}.{{site.cfengine.latest_patch_release}}-{{site.cfengine.latest_package_build}}.el6.x86_64.rpm
```

**Older 64-bit RPM based distributions: (Redhat/CentOS/SUSE)** (not recommended for policy server)

```command
sudo rpm -i cfengine-community-{{site.cfengine.branch}}.{{site.cfengine.latest_patch_release}}-{{site.cfengine.latest_package_build}}.el4.x86_64.rpm
```

**32-bit RPM based distributions: (Redhat/CentOS/SUSE)** (not recommended for policy server)

```command
sudo rpm -i cfengine-community-{{site.cfengine.branch}}.{{site.cfengine.latest_patch_release}}-{{site.cfengine.latest_package_build}}.el4.i386.rpm
```

**Newer 64-bit DEB based distributions: (Ubuntu/Debian)**

```command
sudo dpkg -i cfengine-community_{{site.cfengine.branch}}.{{site.cfengine.latest_patch_release}}-{{site.cfengine.latest_package_build}}_amd64-debian7.deb`
```

**Older 64-bit DEB based distributions: (Ubuntu/Debian)** (not recommended for policy server)

```command
sudo dpkg -i cfengine-community_{{site.cfengine.branch}}.{{site.cfengine.latest_patch_release}}-{{site.cfengine.latest_package_build}}_amd64-debian4.deb`
```

**32-bit DEB based distributions: (Ubuntu/Debian)** (not recommended for policy server)

```command
sudo dpkg -i cfengine-community_{{site.cfengine.branch}}.{{site.cfengine.latest_patch_release}}-{{site.cfengine.latest_package_build}}_i386-debian4.deb`
```

**Note:** You might get a message like this: "Policy is not found in /var/cfengine/inputs, not starting CFEngine." Do not worry;
this is taken care of during the bootstrapping process.


## 3. Bootstrap the policy server

The Policy Server must be bootstrapped to itself. Find the IP address of your Policy Server.

Run the bootstrap command:

```command
sudo /var/cfengine/bin/cf-agent --bootstrap <IP address of policy server>
```

**Example: $ sudo /var/cfengine/bin/cf-agent --bootstrap 192.168.1.12**

Upon successful completion, a confirmation message appears: "Bootstrap to '192.168.1.12' completed successfully!"

Type the following to check which version of CFEngine your are running:

```command
/var/cfengine/bin/cf-promises --version
```

The Policy Server is installed.

## 4. Install CFEngine on a host

As stated earlier, Hosts are instances that retrieve and execute promises from the Policy Server. Install
a package on your Host. Use the same package you installed on the Policy Server in Step 2. Note that you must have access
to at least one more VM or server and it must be on the same network as the Policy Server that you just installed.

## 5. Bootstrap the host to the policy server

The Host(s) must be bootstrapped to the Policy Server in order to establish a connection between the Host and
the Policy Server. Run the same commands that you ran in Step 3.

```command
sudo /var/cfengine/bin/cf-agent --bootstrap <IP address of policy server>
```

**Example: $ sudo /var/cfengine/bin/cf-agent --bootstrap 192.168.1.12**

The CFEngine installation process is complete.
