---
layout: default
title: Installing Enterprise Free 25
categories: [Getting Started, Installation, Installing Enterprise Free 25]
published: true
sorting: 20
alias: getting-started-installation-installing-enterprise-free.html
tags: [getting started, installation, enterprise free]
---

These instructions describe how to install the latest version of CFEngine Enterprise using pre-compiled rpm and 
deb packages for Ubuntu, Debian, Redhat, CentOS, and SUSE.

Note: You need a minimum of 2 GB of available memory and a modern 64 bit processor.

## 1. Download Packages

CFEngine Enterprise is provided in two packages; one is for the Policy
Server (hub) and the other is for each Host (client). 

**Select a Policy Server (hub) package to download:**

Ubuntu 10.04

```
wget http://s3.amazonaws.com/cfengine.packages/Enterprise-3.5.2/hub/ubuntu-10.04-x86_64/cfengine-nova-hub_3.5.2-1_amd64.deb
```

Ubuntu 12.04

```
wget http://s3.amazonaws.com/cfengine.packages/Enterprise-3.5.2/hub/ubuntu-12.04-x86_64/cfengine-nova-hub_3.5.2-1_amd64.deb
```

RHEL 5.4

```
wget http://s3.amazonaws.com/cfengine.packages/Enterprise-3.5.2/hub/rhel-5.4-x86_64/cfengine-nova-hub-3.5.2-1.x86_64.rpm
```

SUSE 11.1

```
wget http://s3.amazonaws.com/cfengine.packages/Enterprise-3.5.2/hub/sles-11.1-x86_64/cfengine-nova-hub-3.5.2-1.x86_64.rpm
```

Debian 6.0

```
wget http://s3.amazonaws.com/cfengine.packages/Enterprise-3.5.2/hub/debian-6.0-x86_64/cfengine-nova-hub_3.5.2-1_amd64.deb
```

RHEL 6.0 

```
wget http://s3.amazonaws.com/cfengine.packages/Enterprise-3.5.2/hub/rhel-6.0-x86_64/cfengine-nova-hub-3.5.2-1.x86_64.rpm
```

**Select a Host (client) package to download:**

Ubuntu/Debian 32-bit:

```
wget http://s3.amazonaws.com/cfengine.packages/Enterprise-3.5.2/client/agent_deb_i386/cfengine-nova_3.5.2-1_i386.deb
```

Ubuntu/Debian 64-bit:

```
wget http://s3.amazonaws.com/cfengine.packages/Enterprise-3.5.2/client/agent_deb_x86_64/cfengine-nova_3.5.2-1_x86_64.deb
```

Redhat/CentOS/SUSE 32-bit:

```
wget http://s3.amazonaws.com/cfengine.packages/Enterprise-3.5.2/client/agent_rpm_i386/cfengine-nova-3.5.2-1.i386.rpm
```

Redhat/CentOS/SUSE 64-bit:

```
wget http://s3.amazonaws.com/cfengine.packages/Enterprise-3.5.2/client/agent_rpm_x86_64/cfengine-nova-3.5.2-1.x86_64.rpm
```

## 2. Install Packages

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

## 3. Bootstrap

Run the bootstrap command, **first** on the policy server and then on each
host:

```
$ /var/cfengine/bin/cf-agent --bootstrap <IP address of the Policy Server>
```

## Next Steps

When bootstrapping is complete, CFEngine is up and running on your system.

The Mission Portal is immediately accessible. Connect to the Policy Server
through your web browser at http://`<IP address of your Policy Server>`.

To be able to use the [Mission Portal's][Mission Portal] Design Center
front-end, continue with [integrating Mission Portal with git] [Integrating Mission Portal with git]. 
 
Learn more about CFEngine by using the following resources:

* Tutorial: [Create a standalone policy (Hello World).][Hello World]

* Tutorial: [Configure and deploy a policy using sketches in the Design Center.][Configure and Deploy a Policy Using Sketches (Enterprise Only)] 

* CFEngine [manuals][CFEngine Manuals].

* Additional [tutorials, examples, and documentation][Learning Tools].
