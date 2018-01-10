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

_Tutorials, recommended reading. and production environment recommendations appear at the end of this page._

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
If you require more details on bootstrapping, review Step 3 below. Bootstrapping completes the installation.
3. Go to the [Tutorials][Installing Community#Tutorials] section to learn how to use CFEngine.
<hr>

## 1. Download Packages

Select the package to download that matches your operating system.
This stores the cfengine-community_3.6.1-1_* file onto your machine.

**Redhat/CentOS/SUSE 64-bit:**

```
$ wget http://cfengine.package-repos.s3.amazonaws.com/community_binaries/cfengine-community-3.6.1-1.x86_64.rpm
```

**Redhat/CentOS/SUSE 32-bit:**

```
$ wget http://cfengine.package-repos.s3.amazonaws.com/community_binaries/cfengine-community-3.6.1-1.i386.rpm
```

**Ubuntu/Debian 64-bit:**

```
$ wget http://cfengine.package-repos.s3.amazonaws.com/community_binaries/cfengine-community_3.6.1-1_amd64.deb
```

**Ubuntu/Debian 32-bit:**

```
$ wget http://cfengine.package-repos.s3.amazonaws.com/community_binaries/cfengine-community_3.6.1-1_i386.deb
```


## 2. Install CFEngine on a Policy Server

Install the package on a machine designated as a Policy Server.  A Policy Server is a CFEngine instance that contains promises (business policy)
that get deployed to Hosts. Hosts are instances (clients) that retrieve and execute promises.

Choose the right command for your operating system:

**Redhat/CentOS/SUSE 64-bit:**

```
$ sudo rpm -i cfengine-community-3.6.1-1.x86_64.rpm
```

**Redhat/CentOS/SUSE 32-bit:**

```
$ sudo rpm -i cfengine-community_3.6.1-1.i386.rpm
```

**Ubuntu/Debian 64-bit:**

```
$ sudo dpkg -i cfengine-community_3.6.1-1_amd64.deb
```

**Ubuntu/Debian 32-bit:**

```
$ sudo dpkg -i cfengine-community_3.6.1-1_i386.deb
```

**Note:** You might get a message like this: "Policy is not found in /var/cfengine/inputs, not starting CFEngine." Do not worry;
this is taken care of during the bootstrapping process.


## 3. Bootstrap the Policy Server

The Policy Server must be bootstrapped to itself. Find the IP address of your Policy Server (type $ ifconfig).

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
