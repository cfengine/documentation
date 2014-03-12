---
layout: default
title: Installing Enterprise 25 Free with AWS™ and RHEL Using Micro Instances
categories: [Getting Started, Installation, Installing Enterprise Free 25, AWS, RHEL]
published: true
sorting: 20
alias: getting-started-installation-installing-enterprise-free-aws-rhel.html
tags: [getting started, installation, enterprise free, aws, rhel]
---

These instructions describe how to install the latest version of CFEngine Enterprise 25 Free with Amazon Web Services™ (AWS™) and Red Hat® Enterprise Linux® (RHEL) using Micro Instances. 

The tutorial will cover the following steps:

1. Initial Configuration of the Virtual Machines.
2. Configure the Security Group.
3. Configure SSH Access to the Virtual Machines Using PuTTY (for Windows machines).
4. Configuration of the Firewall on the Policy Server.
5. Install CFEngine on the Policy Server and Host Virtual Machines. 

This is the full version of CFEngine Enterprise, but the number of Hosts (clients) is limited to 25.

## Initial Configuration in AWS™ ##

### Configure 2 RHEL Virtual Machine Instances in AWS™ ###

* Login to AWS™.
* Under **Create Instance** click on **Launch Instance**.
* On the line **Red Hat Enterprise Linux 64 Bit - Free tier eligible** press the **Select** button.
* On the **Choose Instance Type** screen ensure the **Micro Instances** tab on the left is selected.

#### Configure Instance Details ####
* Press **Next: Configure Instance Details**. 
* On the **Configure Instance Details** screen change the **Number of instances** to 2.
* Leave **Network** as the default.
* **Subnet** can be **No preference**.
* Ensure **Public IP** is checked.
* Leave all else at their default values.

#### Review and Launch ####
* Click **Review and Launch**.
* Make a note of **Security group name** on the **Review Instance Launch** screen.
* Click **Launch**.
* In the **Select an existing key pair or create a new key pair** select **Create a new key pair** in the first drop down menu.
* Enter anything as the **Key pair name**.
* Click the **Download Key Pair** button and save the **.pem** file to your local computer.
* After the **.pem** file is saved click the **Launch Instance** button.
* On the **Launch Status** screen click the **View Instances** button.

## Configure the Security Group ##

* On the left hand side of the AWS™ console click **NETWORK & SECURITY > Security Groups**
* Remembering the **Security group name** from earlier, click on the appropriate line item in the list.
* Below the list of security group names will display details for the current security group.
* Click the **Inbound** tab.
* Select **HTTP** from the **Create a new rule** list.
* Click the **+Add Rule** button.
* Select **Custom TCP rule** and enter **5308** in the **Port range** text entry.
* Click the **+Add Rule** button.
* Click **Apply Rule Changes**.

## Accessing AWS™ VMs via SSH on Windows Using PuTTY and PuTTYgen ##

### Get PuTTY and PuTTYgen ###

* To get PuTTY and PuTTYgen, first go to http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html and either:
	* Download and install using the PuTTY binaries installer 
		* At the time of writing the exact download url was http://the.earth.li/~sgtatham/putty/latest/x86/putty-0.63-installer.exe
	* Or, download PuTTY and PuTTYgen individually
		* At the time of writing http://the.earth.li/~sgtatham/putty/latest/x86/putty.exe and http://the.earth.li/~sgtatham/putty/latest/x86/puttygen.exe respectively.

### Prepare Private Key Using PuTTYgen ###

* After the binaries have been downloaded and/or installed either:
	* Double click **puttygen.exe** from the download location, if downloaded directly.
	* Or, if the PuTTY installer was used above, one of either:
		* Press the **Windows** key + **R** key and then type **puttygen** in the field named **Open**. Then press the enter key or click **OK**.
		* Alternatively, double click **puttygen.exe** under **C:\Program Files (x86)\PuTTY** (when using Windows 64 bit) or **C:\Program Files\PuTTY** (when using Windows 32 bit).
* On the PuTTYgen interface click the **load** button.
* In the **Load private key** window select **All Files (\*.\*)** in the drop down menu next to the **File name** input box. 
* Navigate to the location on disk where the **.pem** file was downloaded in earlier steps.
* When the key has been loaded click the **Save private key** button.
* When prompted with a warning about saving without a passphrase, click **yes**.
* Finally, navigate to a good location on disk to save the key file, enter a name for the private key, ensure **PuTTY Private Key Files (\*.ppk)** type is selected, and then click the **Save** button.

### Configure PuTTY ###

* In the AWS™ Console, navigate to **INSTANCES > Instances**.
* Make a note of the 2 different **Public DNS** entries for the virtual machines that were setup earlier (e.g. ec2-xxx-xxx-xxx-xxx.us-west-1.compute.amazonaws.com, where the x's represent numbers).
* Launch PuTTY by either:
	* Double clicking **putty.exe** from the download location, if downloaded directly.
	* Or, if the PuTTY installer was used above, one of either:
		* Press the **Windows** key + **R** key and then type **putty** in the field named **Open**. Then press the enter key or click **OK**.
		* Alternatively, double click **putty.exe** under **C:\Program Files (x86)\PuTTY** (when using Windows 64 bit) or **C:\Program Files\PuTTY** (when using Windows 32 bit).
	* On the PuTTY interface, with **Category > Session** on the left side navigation tree selected:
		* **Host Name** should consist of a user name ('**ec2-user**'), the '**@**' mark, and the public DNS entry for one of the two virtual machines created earlier. For example, **ec2-user@ec2-xxx-xxx-xxx-xxx.us-west-1.compute.amazonaws.com**. 
		* **Port** should be set to **22**.
		* **Connection type** should be set to **SSH**.
		* **Saved Sessions** can be any label.
	* Select **Connection > SSH > Auth** on the left side navigation.
	* Click the **Browse** button to select the **Private key for authentication**.
	* In the **Select private key file** window, navigate to the **.ppk** private key file created earlier. 
	* Select **Category > Session** on the left side navigation tree and then press the **Save** button.
	* Repeat the steps for the second virtual machine, starting from setting the **Host Name** through pressing the **Save** button (as described above).

### Login to Virtual Machines Using PuTTY ###

* If one of the two virtual machines is configured and its details loaded in the PuTTY interface, click the **Open** button.
	* Note: It may be necessary to redo the steps from selecting **Connection > SSH > Auth** through selecting the **.ppk** private key file. In other words, when configuring the connection the private key file may not be persistently saved.
* Wait a moment, and select **Yes** if prompted.
	* This prompt will generally only be necessary when trying to login for the very first time 
* Once the first virtual machine is logged into, right click the top of PuTTY's application window (e.g. the part of the window decoration displaying the virtual machine name).
* In the contextual menu that then shows click **New Session**.
* Select the second virtual machine entry in the **Saved Sessions** list.
* Click **Load** and then **Open**.
* Both virtual machines should now be accessed in two different PuTTY application windows.

### Configure RHEL Firewall ###

#### Install the Firewall ####

* Ensure you are logged into both virtual machines. 
* In both enter **sudo yum install system-config-firewall** to install.
* Hit '**y**' if prompted.

#### Configure the Firewall on the Policy Server (AKA hub) ####

The following is only necessary for one of the two virtual machines:

* When **system-config-firewall** is installed, next enter **sudo system-config-firewall**
* In the **Firewall Configuration** screen use the **Tab** key to go to **Customize**.
* Hit the **Enter** key.

##### Open Port 80 (HTTPD) #####
* On the **Trusted Services** screen, scroll down to **WWW (HTTPD)**, AKA port 80.
* Hit the **Space Bar** to toggle the **WWW** entry (i.e. ensure it is on, showing an asterisk beside the name).

##### Open Port 5308 (CFEngine) #####
* Hit the **Tab** key again until **Forward** is highlighted, then hit **Enter**.
* Hit the **Tab** key until **Add** is highlighted, then hit **Enter**.
* Enter '**5308**' in the **Port** section.
* Hit the **Tab** key and enter '**tcp**' in the **Protocol** section. 
* Hit the **Tab** key until **OK** is highlighted, and hit **Enter**.

##### Wrapping Up Firewall Configuration #####

* Hit the **Tab** key until **Close** is highlighted, and hit **Enter**.
* Hit the **Tab** key or **arrow** keys until **OK** is highlighted, and hit **Enter**.

##### Disabling Firewall on a Host (Warning: Only Do This If Absolutely Necessary) #####

For the other virtual machine you may need to do the following if you see an error when bootstrapping this virtual machine in later steps:

* In the **Firewall Configuration** screen use the **Tab** key to go to **Firewall**.
* Turn off the firewall by toggling the entry with the **Space** bar.

Note: Turning off the firewall in a production environment is considered unsafe.

## CFEngine Installation Overview

During the course of the instructions outlined in this guide, you will perform the following tasks:

* **Install CFEngine Enterprise onto a Policy Server and onto Hosts.**
A Policy Server (hub) is a CFEngine instance that contains promises (business policy) that get deployed to Hosts.
Hosts are clients that retrieve and execute promises.
* **Bootstrap the Policy Server to itself and then bootstrap each of the Hosts to the Policy Server.** Bootstrapping establishes a trust relationship between the Policy Server
and all Hosts. Thus, business policy that you create in the Policy Server can be deployed to Hosts throughout your company.
Bootstrapping completes the installation process.
* **Log in to the Mission Portal.** The Mission Portal is a graphical user interface that allows you to verify the
the actual state of all your Hosts, thus ensuring that your promises are being executed. By using the **Design Center** inside the Mission Portal, you
can also define new desired states (business policies) for your infrastructure.
* **Try out the Tutorials.** Links to three tutorials give you a head start on learning CFEngine.


## 1. Download and install Enterprise on a Policy Server

Run the following script on your designated Policy Server (hub), the virtual machine with the configured firewall from earlier steps:

```
$ wget http://s3.amazonaws.com/cfengine.packages/quick-install-cfengine-enterprise.sh  && sudo bash ./quick-install-cfengine-enterprise.sh hub
```

This script installs the latest CFEngine Enterprise Policy Server on your machine.

## 2. Bootstrap the Policy Server

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

## 3. Install Enterprise on Hosts

Install Enterprise on your designated Host (the second of the two virtual machines, without the configured firewall) by running the script below. Per the **Free 25** agreement, you can
install Enterprise on 25 Hosts. Note that the Hosts must be
on the same network as the Policy Server that you just installed in Step 2.

```
wget http://s3.amazonaws.com/cfengine.packages/quick-install-cfengine-enterprise.sh  && sudo bash ./quick-install-cfengine-enterprise.sh client
```

Note that this installation works on 64- and 32-bit machines (but in this tutorial only 64-bit machines are being used).

## 4. Bootstrap the Host to the Policy Server

All Hosts must be bootstrapped to the Policy Server in order to establish a connection between the Host and
the Policy Server. Run the same commands that you ran in Step 3.

```
$ sudo /var/cfengine/bin/cf-agent --bootstrap <IP address of policy server>
```

**Example: $ sudo /var/cfengine/bin/cf-agent --bootstrap 192.168.1.12**

The installation process is complete and CFEngine Enterprise is up and running on your system.

## 5. Log in to the Mission Portal

The Mission Portal is immediately accessible. Connect to the Policy Server
through your web browser at:

http://`<External IP address of your Policy Server>`

Note: The External IP address is available in the AWS™ console.

username: admin
password: admin

The Mission Portal runs TCP port 80 by default. (Click [here] (https://cfengine.zendesk.com/entries/25005193-Configure-Mission-Portal-to-use-HTTPS-instead-of-HTTP)
to configure the Mission Portal to use HTTPS instead of HTTP.) During the initial setup, the Host(s) might take a few minutes to show up in the Mission Portal. Simply refresh the web page
and login again if necessary.

Note: If you are running Enterprise with Vagrant, you must add the
correct port: http://localhost:<port> in your browser.  The <port> is the port-forwarder
number you use in your **Vagrantfile** (e.g. policyserver.vm.network "forwarded_port", guest: 80, host: 8080; the port will be 8080).

<hr>

## Tutorials

* [Configure and deploy a policy using sketches in the Design Center.][Configure and Deploy a Policy Using Sketches (Enterprise Only)] This tutorial
teaches you how to configure and deploy business policy by using the Design Center application in the Mission Portal. Next, it shows you how to verify
that your business policy is being activated by viewing the Reports in the Mission Portal.
* [Create a standalone policy (Hello World).][Hello World] Whereas the above tutorial uses pre-defined policy (called sketches) that you can modify in the Mission Portal, this
tutorial teaches you how to create business policy (promises) on the command line. Here, you
can get a taste of the CFEngine language as you create standalone and executable scripts.
* [Distribute files from a central location.][Distribute files from a central location] Whereas the first tutorial in this list teaches you how to deploy business policy
through the Mission Portal, this advanced, command-line tutorial shows you how to distribute policy files from the Policy Server to all pertinent Hosts.

## Recommended Reading

* CFEngine [manuals][Learning CFEngine].
* Additional [tutorials, examples, and documentation][Learning Resources].

<hr>

## Rate your experience

Everyone is a first-time user a some point. We want to make the CFEngine Enterprise installation process easy for all of our new users.
Before you forget your first-time experience, we would love for you to let us know how we can improve on this process.

<iframe src="https://docs.google.com/forms/d/1-D5ny2_5HDmPBpRR69aZeC-dVY08VlDouCsdGXBCnyc/viewform?embedded=true" width="760" height="800" frameborder="0" marginheight="0" marginwidth="0">Loading...</iframe>
