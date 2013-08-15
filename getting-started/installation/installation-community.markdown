---
layout: default
title: Installing Community
categories: [Getting Started, Installation, Installing Community]
published: true
alias: getting-started-installation-installing-community.html
tags: [getting started, installation, community]
---

Please complete the [General Requirements][Installing CFEngine] if you have not already done so.

## Packages

The Community Edition is packaged using the following naming convention:

* RPM Package: `cfengine-community-3.6.0-1.x86_64.rpm`

* Debian Package: `cfengine-community_3.6.0-1_amd64.deb`

## Installation 

1. Install the package **first** on the Policy Server, and then on each Host:

    ```
        [RedHat/CentOS/SUSE] $ rpm -i <package>.rpm
        [Debian/Ubuntu]      $ dpkg -i <package>.deb
    ```

2. Run the bootstrap command, **first** on the Policy Server, and then on each
Host:

    ```
        /var/cfengine/bin/cf-agent --bootstrap <IP address of policy server>
    ```

## Next Steps

Learn more about CFEngine by using the following resources:

Read CFEngine [manuals][CFEngine Manuals].

Get [Support][Support and Community] from the CFEngine community.

View additional [tutorials, examples, and documentation][Learning Tools].

