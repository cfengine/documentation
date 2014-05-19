---
layout: default
title: Installing CFEngine on RHEL Using AWS
published: true
sorting: 10
tags: [getting started, installation, enterprise free, aws, rhel]
---

This guide describes how to install CFEngine on two Red Hat® Enterprise Linux® (RHEL) virtual machines using Amazon Web Services™ (AWS) and SSH. At the time of writing, under certain conditions, setting up an AWS account and using micro-instances is free.

One of the two machines will be a `policy server` (see [Policy Server Overview][Policy Server Overview]), while the other will be a `host` (see [Host Overview][Host Overview]).

Although these instructions walk through the steps needed to install CFEngine Enterprise on two machines, up to 25 machines can be set up using the same procedure and scripts. 

This tutorial will cover the following steps:

1. Initial Configuration of the AWS Virtual Machines.
2. Configuring the Security Group.
3. Configuring SSH Access to the Virtual Machines Using PuTTY (for Windows machines).
4. Configuring the Firewall on the Policy Server.
5. Installing CFEngine on both the Policy Server and Host Virtual Machines.

## Initial Configuration of the Virtual Machines in AWS ##

### Configure 2 RHEL Virtual Machine Instances in AWS ###

* Login to AWS.
* Under `Create Instance` click on `Launch Instance`.
* On the line `Red Hat Enterprise Linux 64 Bit Free tier eligible` press the `Select` button.
* On the `Choose Instance Type` screen ensure the `Micro Instances` tab on the left is selected.

### Configure Instance Details ###

* Press `Next: Configure Instance Details`.
* On the `Configure Instance Details` screen change the number of instances to 2.
* Leave `Network` as the default.
* `Subnet` can be `No preference`.
* Ensure `Public IP` is checked.
* Leave all else at their default values.

### Review and Launch ###
* Click `Review and Launch`.
* Make a note of `Security group` name on the `Review Instance Launch` screen.
* Click `Launch`.
* Select `Create a new key` pair in the first drop down menu.
* Enter anything as the `Key pair name`.
* Click the `Download Key Pair` button and save the .pem file to your local computer.
* After the .pem file is saved click the `Launch Instance` button.
* On the `Launch Status` screen click the `View Instances` button.

### Configure the Security Group ###

* On the left hand side of the AWS console click `NETWORK & SECURITY > Security Groups`
* Remembering the `Security group` name from earlier, click on the appropriate line item in the list.
* Below the list of security group names will display details for the current security group.
* Click the `Inbound` tab.
* Click "Edit" button. A popup window will appear with "SSH" rule already present. 
* Click the `+Add Rule` button. Select `HTTP` from the drop-down list. Click "Add Rule" button again.
* Select `Custom TCP rule` and enter `5308` in the `Port range` text entry. Select "Custom IP" from the drop-down menu in the "Source" column.
* Copy the "Group ID" from the line containing your "Group Name" and copy the "Group ID" into the text entry in the last column. Click "Save."
* Click the "Edit" button again. On the "Custom TCP" Rule, select "Anywhere" from the "Source" drop-down list. Click "Save."

## Accessing AWS Virtual Machines via SSH on Windows Using PuTTY and PuTTYgen ##

### Get PuTTY and PuTTYgen ###

* To get PuTTY and PuTTYgen, first go to
http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html and either:
 * Download and install using the PuTTY binaries installer
  * At the time of writing the exact download url was
http://the.earth.li/~sgtatham/putty/latest/x86/putty0.63installer.exe
 * Or, download PuTTY and PuTTYgen individually
  * At the time of writing http://the.earth.li/~sgtatham/putty/latest/x86/putty.exe
and http://the.earth.li/~sgtatham/putty/latest/x86/puttygen.exe respectively.

### Prepare Private Key Using PuTTYgen ###
* After the binaries have been downloaded and/or installed either:
 * Double click `puttygen.exe` from the download location, if downloaded directly.
 * Or, if the PuTTY installer was used above, one of either:
  * Press the `Windows` key + `R` key and then type `puttygen` in the field named `Open`. Then press the `Enter` key or click `OK`.
  * Alternatively, double click puttygen.exe under `C:\Program Files (x86)\PuTTY` (when using Windows 64 bit) or `C:\Program Files\PuTTY` (when using Windows 32 bit).

![The Puttygen Interface](Installing-CFE-on-AWS-1.png)

The Puttygen Interface. You will load the .pem file that you created in AWS.

* On the PuTTYgen interface click the load button.
* In the Load private key window select All Files (*.*) in the drop down menu next to the
File name input box.
* Navigate to the location on disk where the .pem file was downloaded in earlier steps.
* When the key has been loaded click the Save private key button.
* When prompted with a warning about saving without a passphrase, click yes.

![The Puttygen popup window](Installing-CFE-on-AWS-2.png)

The Puttygen popup window. Click `Yes`, to proceed without a passphrase. You can also protect your private key with a passphrase that you enter into `Key Passprhase` and `Confirm Key Passphrase`.

* Finally, navigate to a good location on disk to save the key file, enter a name for the private key, ensure PuTTY Private Key Files (*.ppk) type is selected, and then click the Save button.
* You can now close the Puttygen application. You will call up the .ppk file when you configure the virtual machines using PuTTY.

### Configure PuTTY ###

* Before configuring PuTTY, go back to your AWS Console, then navigate to INSTANCES > Instances.
* Make a note of the 2 different Public DNS entries for the virtual machines that were setup earlier (e.g. ec2xxxxxxxxxxxx.uswest1.compute.amazonaws.com, where the x's represent numbers).
* Launch PuTTY by either:
 * Double clicking `putty.exe` from the download location, if downloaded directly.
 * Or, if the PuTTY installer was used above, one of either:
  * Press the `Windows` key + `R` key and then type `putty` in the field named `Open`. Then press the `Enter` key or click `OK`.
  * Alternatively, double click `putty.exe` under `C:\Program Files (x86)\PuTTY` (when using Windows 64 bit) or `C:\Program Files\PuTTY` (when using Windows 32 bit).
 * On the PuTTY interface, select `Category > Session` on the left side navigation tree:

![The Puttygen Interface](Installing-CFE-on-AWS-3.png)

The Putty interface, with `Session` selected on the left-side navigation tree.

* Now, we will configure the Putty application, which we will use to set up the two AWS virtual machines.
 * The first step is to create a Host Name for the first VM.
  * The Host Name consists mainly of the public DNS entry that was created for one of the two virtual machines in AWS. But the DNS is preceded by a user name, `ec2-user`, followed by the `@` symbol, which is then followed by the DNS entry.

![Setting up the PuTTY configuration](Installing-CFE-on-AWS-4.png)

Setting up the PuTTY configuration with the Host Name, and a Saved Sessions Name.

  * Port should be set to `22`.
  * Connection type should be set to `SSH`.
  * `Saved Sessions` can be any label.

Once we have entered our Host Name and our Saved Sessions name, we take the following steps:
 * Select `Connection > SSH > Auth` on the left side navigation tree.
 * Click the `Browse` button to select the `Private key for authentication`.
 * In the `Select private key file` window, navigate to the .ppk private key file created earlier, and double-click on it to enter it into PuTTY. Your PuTTY screen should look like this:

![Setting up the PuTTY configuration](Installing-CFE-on-AWS-5.png)

Note that `Auth` has been selected on left-side tree, in order to bring up this screen.

 * Now we go back and select `Category > Session` on the left side navigation tree and then press the `Save` button.
 * Repeat the steps for the second virtual machine, starting from setting the Host Name through pressing the Save button (as described above). Your PuTTY screen should show the two saved virtual machines, which are here named `Examples 1 and 2.`
 * Note: It may be necessary to redo the steps from selecting `Connection > SSH > Auth` through selecting the .ppk private key file. In other words, when configuring the connection the private key file may not be persistently saved.
 * Wait a moment, and select `Yes` if prompted.
 * This prompt will generally only be necessary when trying to login for the very first time.

![The PuTTY interface with the two virtual machines saved](Installing-CFE-on-AWS-6.png)

The PuTTY interface with the two virtual machines saved. We can now proceed to configure those virtual machines with CFEngine.

### Login to Virtual Machines Using PuTTY ###

* If one of the two virtual machines is configured and its details loaded in the PuTTY interface, first select the machine, then click the Open button. This will close the above PuTTY interface and open a command-line window, from which we will setup CFEngine on each of the two machines. One machine will act as the Server and the other as the client, and they will each be set up with different software.
* Once the first virtual machine is logged into, right click the top of PuTTY's application window (e.g. the part of the window decoration displaying the virtual machine name).
* In the contextual menu that then shows click New Session.
* Select the second virtual machine entry in the Saved Sessions list.
* Click Load and then Open.
* Both virtual machines should now be accessed in two different PuTTY command-line windows. Below is an example of what the command-line window will look like.

![The PuTTY command-line window](Installing-CFE-on-AWS-7.png)

The PuTTY command-line window, which we will use to configure the virtual machines with CFEngine.

## Install and Configure the Firewall ##

### Install the Firewall ###

* Ensure you are logged into both virtual machines.
* In both enter `sudo yum install system-config-firewall` to install.
* Hit 'y' if prompted.

### Configure the Firewall on the Policy Server (AKA hub) ###

The following steps are only necessary for one of the two virtual machines, the one that is designated as the policy server; these steps can be omitted on the second (client machine). Note that CFEngine refers to a client machine by the name `Host`:

* When system-config-firewall is installed, enter `sudo system-config-firewall`
* In the `Firewall Configuration` screen use the `Tab` key to go to Customize.
* Hit the `Enter` key. Below is the `Firewall Configuration` window that comes up:

![The firewall Configuration window](Installing-CFE-on-AWS-8.png)

#### Open Port 80 (HTTPD) ####

* On the `Trusted Services` screen, scroll down to `WWW (HTTP)`, AKA port 80.
* Hit the `Space Bar` to toggle the `WWW` entry (i.e. ensure it is on, showing an asterisk beside the name).

#### Open Port 5308 (CFEngine) ####

* Hit the `Tab` key again until `Forward` is highlighted, then hit `Enter`.
* Hit the `Tab` key until `Add` is highlighted, then hit `Enter`.
* Enter `5308` in the `Port` section.
* Hit the `Tab` key and enter `tcp` in the `Protocol` section.
* Hit the `Tab` key until OK is highlighted, and hit `Enter`.

![Configuring a forward](Installing-CFE-on-AWS-9.png)

The `Port and Protocol` are entered in the blue boxes, with entries of `5308` and `tcp` respectively.
Then the `Tab` key is used to highlight the `OK` button, and the user presses `Enter`.


#### Wrapping Up Firewall Configuration ####

* Hit the `Tab` key until `Close` is highlighted, and hit `Enter`.
* Hit the `Tab` key or arrow keys until `OK` is highlighted, and hit `Enter`.

#### Disabling Firewall on a Host (Warning: Only Do This If Absolutely Necessary) ####

For the second virtual machine, which is the client machine (also called `host`), you may need to do the following if you see an error when bootstrapping this virtual machine in later steps:
* In the `Firewall Configuration` screen use the `Tab` key to go to Firewall.
* Turn off the firewall by toggling the entry with the `Space` bar.

Note: Turning off the firewall in a production environment is considered unsafe.

## CFEngine Installation Overview ##

We ready now ready to install the CFEngine software on both the server and client virtual machines. These also referred to as the “hub” and “host” machines, respectively. During the course of the instructions outlined in this guide, you will perform the following tasks:

* Install CFEngine Enterprise onto a Policy Server and onto Hosts. A Policy Server (hub) is a CFEngine instance that contains promises (business policy) that get deployed to Hosts. Hosts are clients that retrieve and execute promises.
* Bootstrap the Policy Server to itself and then bootstrap each of the Hosts to the Policy Server. Bootstrapping establishes a trust relationship between the Policy Server and all Hosts. Thus, business policy that you create in the Policy Server can be deployed to Hosts throughout your company. Bootstrapping completes the installation process.
* Log in to the Mission Portal. The Mission Portal is a graphical user interface that allows you to verify the the actual state of all your Hosts, thus ensuring that your promises are being executed. By using the Design Center inside the Mission Portal, you can also define new desired states (business policies) for your infrastructure.
* Try out the Tutorials. Links to three tutorials give you a head start on learning CFEngine.

### Step 1. Download and install Enterprise on a Policy Server ###

Run the following script on your designated Policy Server (hub), the virtual machine with the
configured firewall from earlier steps:

`$ wget http://s3.amazonaws.com/cfengine.packages/quick-install-cfengine-enterprise.sh && sudo bash ./quick-install-cfengine-enterprise.sh hub`

This script installs the latest CFEngine Enterprise Policy Server on your server machine.

### Step 2. Bootstrap the Policy Server ###

* The Policy Server must be bootstrapped to itself. Find the IP address of your Policy Server:
	`$ ifconfig`.
* Run the bootstrap command: `sudo /var/cfengine/bin/cf-agent --bootstrap <IP address of policy server>`

Example: `$ sudo /var/cfengine/bin/cf-agent --bootstrap 172.31.3.25`

![Bootstrap the policy server](Installing-CFE-on-AWS-10.png)

Upon successful completion, a confirmation message appears: "Bootstrap to '172.31.3.25' completed successfully!"

* Type the following to check which version of CFEngine your are running:

	`/var/cfengine/bin/cf-promises --version`

* The Policy Server is now installed.

### Step 3. Install Enterprise on Host (Client) ###

* Ensure you are logged into the host machine setup earlier.
* Install CFEngine client version using the following:

`$ wget http://s3.amazonaws.com/cfengine.packages/quick-install-cfengine-enterprise.sh && sudo`
`$ bash ./quick-install-cfengine-enterprise.sh client`

Note: The installation will work on 64-bit and 32-bit client machines (the host requires a 64-bit machine).

![Bootstrap the policy server](Installing-CFE-on-AWS-11.png)

The client software (host), has been installed on the second virtual machine.

Note: You can install CFEngine Enterprise on up to 25 hosts using the script above.

### Step 4. Bootstrap the Host to the Policy Server ###

* All hosts must be bootstrapped to the Policy Server in order to establish a connection between the `Host` and the `Policy Server`. 
* Run the same commands that you ran in Step 2, `$ sudo /var/cfengine/bin/cfagent bootstrap <IP address of policy server>`.

Example: `$ sudo /var/cfengine/bin/cfagent bootstrap 172.31.3.25`

* The installation process is complete and CFEngine Enterprise is up and running on your system. 

### Step 5. Log in to the Mission Portal ###

* The Mission Portal is immediately accessible. Connect to the Policy Server through your web browser at: http://<External IP address of your Policy Server> (Note: The External IP address is available in the AWS console).
* The default username for the Mission Portal is `admin`, and the password is also `admin`.
* The Mission Portal runs TCP port 80 by default. [Configure mission portal to use HTTPS instead of HTTP][Configure Mission Portal to use HTTPS instead of HTTP].
* During the initial setup, the Host(s) might take a few minutes to show up in the Mission Portal. Refresh the web page and login again if necessary.

## What Next? ##

### Tutorials ###

* [Configure and deploy a policy using sketches in the Design Center.][Configure and Deploy a Policy Using Sketches (Enterprise Only)] This tutorial
teaches you how to configure and deploy business policy by using the Design Center application in the Mission Portal. Next, it shows you how to verify
that your business policy is being activated by viewing the Reports in the Mission Portal.
* [Create a standalone policy (Hello World).][Hello World] Whereas the above tutorial uses pre-defined policy (called sketches) that you can modify in the Mission Portal, this
tutorial teaches you how to create business policy (promises) on the command line. Here, you
can get a taste of the CFEngine language as you create standalone and executable scripts.
* [Distribute files from a central location.][Distribute files from a central location] Whereas the first tutorial in this list teaches you how to deploy business policy
through the Mission Portal, this advanced, command-line tutorial shows you how to distribute policy files from the Policy Server to all pertinent Hosts.

### Recommended Reading ###

* CFEngine [manuals][Learning CFEngine].
* Additional [tutorials, examples, and documentation][Learning Resources].