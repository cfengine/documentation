---
title: Quick-Start Guide to Using PuTTY
layout: default
published: true
sorting: 2
tags: [how-to-guides, quick-start guides, putty, puttygen]
---

* [Using PuTTY in Simple Steps][Quick-Start Guide to Using PuTTY#Using PuTTY in Simple Steps]
* [Accessing AWS Virtual Machines via SSH on Windows Using PuTTY and PuTTYgen][Quick-Start Guide to Using PuTTY#Accessing AWS Virtual Machines via SSH on Windows Using PuTTY and PuTTYgen]

## Using PuTTY in Simple Steps ##

This guide is intended for Windows users who are not accustomed to using SSH, or need some additional support for understanding how to work with SSH from their machine (e.g. challenges with key pairs).

It describes how to start using the free, open-source program PuTTY, to securely connect
a client computer to a remote Linux/Unix server.

Many of the tutorials to follow will refer to using PuTTY, which is a popular SSH client for Windows workstations.

The important thing about PuTTY is that it is a _secure_ way to connect a client to a server,
using the  SSH network protocol. It has a powerful and easy-to-use graphical user interface (GUI) and is used
to run a remote session over a network.

What is SSH? It is short-form for “Secure Shell,” which means it creates a _secure channel_ over an
insecure network—like the internet, for example.

How does SSH do this? By encrypting the communications between the client and the server, using
public-key cryptography, which means that a key-pair is generated—one of them public, and the other
private, or secret, known only to the user.

Since CFEngine is a client-server enterprise software system, it is essential to access the servers
securely. This is true whether the CFEngine system is run on a cloud platform, like Amazon Web Services
and many others—or on a private network.

That is where PuTTY comes into the picture, since it uses  SSH protocol for connecting a client to a server.

The PuTTY software consists of two separate programs PuTTY and PuTTYgen:
They can be downloaded at http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html

PuTTYgen is used to generate the encryption key pair while PuTTY, a command-line interface,
 is used to securely access the CFEngine server, or _hub_, from a remote client machine, which is called
a _host_ in CFEngine terminology.

PuTTYgen is used only when setting up a new client machine on the CFEngine hub. The CFEngine _hub_ will already
have an encrypted _key-pair_ that was created when setting up the _hub_. (See the tutorial, [Installing CFEngine on RHEL Using AWS][Using Amazon Web Services])

The following steps describe how to get the client machine, up and running using PuTTYgen and PuTTY. There are two distinct
steps to this process:

Step 1. Use PuTTYgen to create an encrypted _key-pair_ in the _.ppk_ file format that PuTTY uses.

(It is important to note that the _key-pair_ on the _hub_ will probably be in a file format that is different from the PuTTYgen
_.ppk_ file format. For example on Amazon Web Services (AWS) and many other cloud computing services, the _key-pair_ file format created
when setting up the server (_hub_) will be in the _.pem_ file format.)

Step 2. Configure the PuTTY application in order to securely access the CFEngine _hub_.

Step 1. consists of the following sequence: First, launch PuTTYgen by double-clicking on the puTTygen icon in the Windows programs menu tree;
(It should be inside the PuTTY folder that was created when the PuTTY was downloaded and installed.)

Next, download the _key-pair_ and save it on the local hard disk in the _.ppk_ file format.

![The PuTTYgen Interface](puttygen-interface.png)

a. Click _Load_. The following _Load private key_ window will pop up:

![The PuTTYgen "Load private key" pop-up window](puttygen-load-private-key-window.png)

b. In the Load private key window select All Files (*.*) in the drop down menu next to the
File name input box.

c. Navigate to the location on disk where the _public-key_ file was downloaded in earlier steps, in this
case a _.pem_ file. Click _Open_. The following window will appear:

![The PuTTYgen Key Generator Window; note  that the actual key and key fingerprint has been blanked out](putty-key-generator-window)

d. Enter a _Passphrase_ and confirm the _Passphrase_. If no _Passphrase_ is desired, leave those fields empty.

e. When the key has been loaded click the _Save private key_ button.

f. If saving without a _Passphrase_ a dialog box will pop up; click _yes_ to save the key without a _Passphrase_

g. Now close PuTTYgen.

## Accessing AWS Virtual Machines via SSH on Windows Using PuTTY and PuTTYgen ##

### Get PuTTY and PuTTYgen ###

* To get PuTTY and PuTTYgen, first go to
http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html and either:
 * Download and install using the PuTTY binaries installer
 * Or, download PuTTY and PuTTYgen individually

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


