---
layout: default
title: Installing CFEngine Enterprise Agent
published: true
sorting: 3
tags: [getting started, tutorial]
---

<iframe width="560" height="315" src="https://www.youtube.com/embed/CBkTS-kmbos" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

This is the full version of CFEngine Enterprise host, but the number of hosts is limited to 25.

**NOTE:** Please make sure to have installed the CFEngine Policyserver before moving on to install the hosts.

**System requirements**

CFEngine Hosts (clients)
* 32/64-bit machines with a recent version of Linux
* 20 mb of memory
* 20mb of disk space
* Port 5308 needs to be open

The installation script below has been tested on Red Hat, CentOS, SUSE, Debian and Ubuntu.

1. Download and Install CFEngine Host
Run the following command to download and automatically install CFEngine on a 32-bit or 64-bit Linux machine (the script will detect correct flavor and architecture).

```console
wget https://s3.amazonaws.com/cfengine.packages/quick-install-cfengine-enterprise.sh  && sudo bash ./quick-install-cfengine-enterprise.sh agent
```

2. Bootstrap the Host
Once installed, the host needs to bootstrap to your CFEngine policy server.

```console
sudo /var/cfengine/bin/cf-agent --bootstrap <Name or IP address of policy server>
```
If you encounter any issue, please make sure the host is on the same domain/subnet as CFEngine policy server will only allow connection from these trusted sources as default configuration.

3. Congratulation you are done!
The CFEngine host is installed and ready. That was easy, wasn’t it?

If you would like to see what version of CFEngine you are running, type:

```console
/var/cfengine/bin/cf-promises --version
```

Now, you have a client-server CFEngine running. If you would like to install more hosts, simply repeat steps 1 to 3 above. You are free to have up to 25 hosts. Enjoy!

Once you have installed the number of hosts you want, a good next step would be to take a look at our [How-to write your first policy][Write cfengine policy] tutorial.
