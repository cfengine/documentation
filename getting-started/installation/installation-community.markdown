---
layout: default
title: Installing Community
categories: [Getting Started, Installation, Installing Community]
published: true
sorting: 10
alias: getting-started-installation-installing-community.html
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
Use the following script to install CFEngine on your 32- or 64-bit machine. 

```
$ wget -O- https://s3.amazonaws.com/cfengine.packages/quick-install-cfengine-community.sh | sudo bash
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
This stores the cfengine-community_3.5.2-1_* file onto your machine. 

**Ubuntu/Debian 32-bit:**

```
$ wget http://cfengine.com/inside/binarydownload/download/items/1182 -O cfengine-community_3.5.2-1_i386.deb
```

**Ubuntu/Debian 64-bit:**

```
$ wget http://cfengine.com/inside/binarydownload/download/items/1183 -O cfengine-community_3.5.2-1_amd64.deb
```

**Redhat/CentOS/SUSE 32-bit:**

```
$ wget http://cfengine.com/inside/binarydownload/download/items/1180 -O cfengine-community-3.5.2-1.i386.rpm 
```

**Redhat/CentOS/SUSE 64-bit:**

```
$ wget http://cfengine.com/inside/binarydownload/download/items/1181 -O cfengine-community-3.5.2-1.x86_64.rpm 
```

## 2. Install CFEngine on a Policy Server 

Install the package on a machine designated as a Policy Server.  A Policy Server is a CFEngine instance that contains promises (business policy)
that get deployed to Hosts. Hosts are instances (clients) that retrieve and execute promises.

Choose the right command for your operating system:

**Ubuntu/Debian 32-bit:**

```
$ sudo dpkg -i cfengine-community_3.5.2-1_i386.deb
```

**Ubuntu/Debian 64-bit:**

```
$ sudo dpkg -i cfengine-community_3.5.2-1_amd64.deb
```

**Redhat/CentOS/SUSE 32-bit:**

```
$ sudo rpm -i cfengine-community_3.5.2-1.i386.rpm
```

**Redhat/CentOS/SUSE 64-bit:**

```
$ sudo rpm -i cfengine-community-3.5.2-1.x86_64.rpm
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

<hr>
## Tutorials

### Create a policy ("hello world")

Step 1. Create a file called **hello_world.cf** and add the following content:

```cf3
body common control
{
  bundlesequence => { "test" };
}

bundle agent test
{
  reports:                   # This is a promise type.

    cfengine_3::           # This means the promise will only
                             # be kept on a CFEngine_3 system.
      "Hello World";         # This is a simple promise; it generates a report
                             # that says "Hello world".

}
```

Step 2. Run the policy: 

```
$ sudo /var/cfengine/bin/cf-agent hello_world.cf
```

The policy displays the following output:

**R: Hello world**  

Find more policy examples [here][Policy].

### Create a distributed policy

Create a policy that ensures (promises) that a file called **example.txt** will always
exist on the Host.

Step 1. On the Policy Server, create a file called **mypolicy.cf** and add it to the **/var/cfengine/masterfiles**
directory:

```
$ sudo <editor> /var/cfengine/masterfiles/mypolicy.cf
```

Step 2. Add the following lines to the file:

```cf3
bundle agent example
{
files:
   cfengine_3::      # This is a class context (the promise will only
                     # be kept on a CFEngine_3 system)

  "/home/vagrant/example.txt"  # Path and name of the file we wish to ensure exists
       create => "true";       # Make sure the file exists; create if it does not
}
```

Step 3. Update **/var/cfengine/masterfiles/promises.cf** to include this new policy. To do so, modify
the **promises.cf** file to ensure that (1 the **mypolicy.cf** file is being included in the next policy 
distribution and that (2 **example** is in the bundlesequence.

```
$ sudo <editor> /var/cfengine/masterfiles/promises.cf
```

```cf3
...
bundlesequence => {
                 # Common bundles first for best practice
                    "def",
                    "example",
...

inputs => {

         # Global common bundles
            "def.cf",
            "mypolicy.cf",
...
```
The process is complete. The next time CFEngine runs on the Host (which by default is every 5 minutes), 
it will pull down the latest policy update and ensure that the **example.txt** file exists (this is the desired 
state). In fact, any Host that has installed CFEngine will contain the **example.txt** file (because we defined 
the cfengine_3:: class above).

### Try these advanced tutorials:

* [Create a standalone policy (Hello World).][Hello World] This Hello World tutorial provides more depth into how to create business policy (promises) on the 
command line. Here, you can get a taste of the CFEngine language as you create standalone and executable scripts.
* [Distribute files from a central location.][Distribute files from a central location] This advanced, command-line tutorial shows 
you how to distribute policy files from the Policy Server to all pertinent Hosts. 

## Recommended Reading

* CFEngine [language concepts][Language Concepts]
* Getting Started Tutorial: [Get CFEngine Up and Running Quickly: A Primer for New Community Users][Up and Running]


## Production Environment

If you plan to use Community in a production environment, complete the following general requirements:

**Host(s) Memory** 

256 MB available memory in order to run the CFEngine agent software (cf-agent).

**Disk Storage** 

A full installation of CFEngine requires 25 MB. Additional disk usage
depends on your specific policies, especially those that concern reporting.

**Network** 

* Verify that the machine’s network connection is working and that port 5308
  (used by CFEngine) is open for both incoming and outgoing connections.

* If iptables are active on your operating system, stop this service or adapt
  it to allow for communication on the above ports. If applicable, type the
  following two commands: /`etc/init.d/iptables stop` and `chkconfig iptables
  off`

<hr>

## Rate your experience

Everyone is a first-time user a some point. We want to make the CFEngine Enterprise installation process easy for all of our new users. 
Before you forget your first-time experience, we would love for you to let us know how we can improve on this process.

<iframe src="https://docs.google.com/forms/d/1wnVR3HQwUNKs5fT0zf_OHjtIQxI_nd00QCFbDZOyXZk/viewform?embedded=true" width="760" height="800" frameborder="0" marginheight="0" marginwidth="0">Loading...</iframe>

