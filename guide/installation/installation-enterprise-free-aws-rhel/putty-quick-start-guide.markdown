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

Many of the tutorials to follow will refer to using PuTTY, especially if the client computer 
is using the Windows or Unix operating system—including Linux.

The important thing about PuTTY is that it is a _secure_ way to connect a client to a server, 
using the  SSH network protocol.

What is SSH? It is short-form for “Secure Shell,” which means it creates a _secure channel_ over an 
insecure network—like the internet, for example.

How does SSH do this? By encrypting the communications between the client and the server, using 
public-key cryptography, which means that a key-pair is generated—one of them public, and the other 
private, or secret, known only to the user.

Since CFEngine is a client-server enterprise software system, it is essential to access the servers 
securely. This is true whether the CFEngine system is run on a cloud platform, like Amazon Web Services 
and many others—or on a private network.

That is where PuTTY comes into the picture, since it uses  SSHo protocol for connecting a client to a server. 

The PuTTY software consists of two separate programs: 

PuTTYgen, which is used to generate the encryption key pair—and PuTTY, a command-line interface, 
which is used to securely access the CFEngine server, or _hub_, from a remote client machine, which is called 
a _host_ in CFEngine terminology.

PuTTYgen is used only when setting up a new client machine on the CFEngine hub. The CFEngine _hub_ will already 
have an encrypted _key-pair_ that was created when setting up the _hub_. (See the tutorial, "Installing CFEngine on RHEL Using AWS")

First, PuTTYgen will download this _key-pair_ file, by clicking on the _Load_ button, as shown below. 

![The PuTTYgen Interface](puttygen-interface.png)

The following steps describe how to get the client machine, up and running using PuTTYgen. There are two distinct 
steps to this process: 

Step 1. is to use PuTTYgen to create an encrypted _key-pair_ in file format (_.ppk_) that PuTTY works with.
It is important to note that the _key-pair_ on the _hub_ will probably be in a file format that is different from the PuTTYgen
file format. For example on Amazon Web Services (AWS) and many other cloud computing services, the format will be
in _.pem_.

Step 2. is to configure the PuTTY application in order to securely access the CFEngine _hub_.

Step 1. consists of the following sequence: First, PuTTYgen will be used to download the _key-pair_ 
and save it on the user's hard disk in the _.ppk_ file format. 

a. Click _Load_. The following _Load private key_ window will pop up:

![The PuTTYgen "Load private key" pop-up window](puttygen-load-private-key-window.png)

b. In the Load private key window select All Files (*.*) in the drop down menu next to the 
File name input box.

c. Navigate to the location on disk where the _public-key_ file was downloaded in earlier steps, in this 
case a _.pem_ file. Click _Open_. The following window will appear:

![The PuTTYgen Key Generator Window; note  that the actual key and key fingerprint has been blanked out](putty-key-generator-window)

d. Enter a _Passphrase_ and confirm the _Passphrase_. If no _Passphrase_ is desired, leave those fields empty.

e. When the key has been loaded click the Save private key button.

f. If saving without a _Passphrase_ a dialog box will pop up; click _yes_ to save the key without a _Passphrase_

g. Now close PuTTYgen. 

Step 2. Configuring PuTTY.















