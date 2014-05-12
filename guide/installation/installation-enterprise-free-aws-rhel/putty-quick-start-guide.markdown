---
title: Quick-Start Guide to Using PuTTY
layout: default
published: true
sorting: 2
tags: [how-to-guides, quick-start guides, putty, puttygen]
---


Quick-Start Guide to Using PuTTY


This guide is intended for the novice user of CFEngine software. 

It describes how to start using a free, open-source program called PuTTY, to securely connect
a client computer to a CFEngine server, which is called a _hub_. 

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
have an encrypted _key-pair_ that was created when setting up the _hub_. (See the tutorial, "Installing CFEngine on RHEL Using AWS")

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

Step 2. Configure PuTTY.

a. Launch PuTTY by double-clicking on the PuTTY icon in the Windows programs menu tree. 

b. 











