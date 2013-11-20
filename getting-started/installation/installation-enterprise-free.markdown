---
layout: default
title: Installing Enterprise Free 25
categories: [Getting Started, Installation, Installing Enterprise Free 25]
published: true
sorting: 20
alias: getting-started-installation-installing-enterprise-free.html
tags: [getting started, installation, enterprise free]
---

Note: You need a minimum of 2 GB of available memory and a modern 64 bit processor.

## Packages

CFEngine Enterprise is provided in two packages; one is for the Policy
Server (hub) and the other is for each Host (client). These packages contain the
following naming convention:

**Policy Server**: Only 64bit packages

* RPM Package: `cfengine-nova-hub-3.6.0-1.x86_64.rpm`

* Debian Package: `cfengine-nova-hub_3.6.0-1_amd64.deb`

**Hosts**: Both 64bit and 32bit

* RPM Package: `cfengine-nova-3.6.0-1.i386.rpm` or
  `cfengine-nova-3.6.0-1.x86_64.rpm`

* Debian Package: `cfengine-nova_3.6.0-1_i386.deb` or
  `cfengine-nova_3.6.0-1_amd64.deb`

**Select a Policy Server (hub) package to download:**

wget http://s3.amazonaws.com/cfengine.packages/Enterprise-3.5.2/hub/ubuntu-10.04-x86_64/cfengine-nova-hub_3.5.2-1_amd64.deb

wget http://s3.amazonaws.com/cfengine.packages/Enterprise-3.5.2/hub/ubuntu-12.04-x86_64/cfengine-nova-hub_3.5.2-1_amd64.deb

wget http://s3.amazonaws.com/cfengine.packages/Enterprise-3.5.2/hub/rhel-5.4-x86_64/cfengine-nova-hub-3.5.2-1.x86_64.rpm

wget http://s3.amazonaws.com/cfengine.packages/Enterprise-3.5.2/hub/sles-11.1-x86_64/cfengine-nova-hub-3.5.2-1.x86_64.rpm

wget http://s3.amazonaws.com/cfengine.packages/Enterprise-3.5.2/hub/debian-6.0-x86_64/cfengine-nova-hub_3.5.2-1_amd64.deb

wget http://s3.amazonaws.com/cfengine.packages/Enterprise-3.5.2/hub/rhel-6.0-x86_64/cfengine-nova-hub-3.5.2-1.x86_64.rpm


**Select a Host (client package to download:**

wget http://s3.amazonaws.com/cfengine.packages/Enterprise-3.5.2/client/agent_deb_i386/cfengine-nova_3.5.2-1_i386.deb

wget http://s3.amazonaws.com/cfengine.packages/Enterprise-3.5.2/client/agent_rpm_x86_64/cfengine-nova-3.5.2-1.x86_64.rpm

wget http://s3.amazonaws.com/cfengine.packages/Enterprise-3.5.2/client/agent_rpm_i386/cfengine-nova-3.5.2-1.i386.rpm

wget http://s3.amazonaws.com/cfengine.packages/Enterprise-3.5.2/client/agent_deb_x86_64/cfengine-nova_3.5.2-1_x86_64.deb


## Installation

Follow these steps to install CFEngine:

1. Install packages

    On the designated Policy Server, install the `cfengine-nova-hub` package:

    ```
        [RedHat/CentOS/SUSE] $ rpm -i <hub package>.rpm
        [Debian/Ubuntu]      $ dpkg -i <hub package>.deb
    ```

    On each Host, install the `cfengine-nova` package:

    ```
        [RedHat/CentOS/SUSE] $ rpm -i <agent package>.rpm
        [Debian/Ubuntu]      $ dpkg -i <agent package>.deb
    ```

2. Run the bootstrap command, **first** on the policy server and then on each
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
