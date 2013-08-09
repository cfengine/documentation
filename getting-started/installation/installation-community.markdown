---
layout: default
title: Installing Community
sorting: 15
categories: [Getting Started, Installing Community]
published: true
alias: getting-started-installing-community.html
tags: [getting started, installation, community]
---

Please complete the [General Requirements][Installation] if you have not already done so.

## Community Edition

The Community Edition is packaged using the following naming convention:

* RPM Package: `cfengine-community-3.5.0-1.x86_64.rpm`

* Debian Package: `cfengine-community_3.5.0-1_amd64.deb`

### Installation 

Download [Community](https://cfengine.com/community).

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

