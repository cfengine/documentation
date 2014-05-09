---
title: Quick-Start Guide to Using PuTTY
layout: default
published: true
sorting: 2
tags: [how-to-guides, quick-start guides, putty]
---


Quick-Start Guide to Using PuTTY


This guide is intended for the novice user of CFEngine software. 

It describes how to start using a free, open-source program called PuTTY—to securely connect
a client computer to a CFEngine server, which is called a _hub_. 

Many of the tutorials to follow will refer to using PuTTY, especially if the client computer 
is using the Windows or Unix operating system—including Linux.

The important thing about PuTTY is that it is a _secure_ way to connect a client to a server, 
using the  SSH network protocol.

What is SSH? It is short for “Secure Shell,” which means it creates a _secure channel_ over an 
insecure network—like the internet, for example.

How does SSH do this? By encrypting the communications between the client and the server, using 
public-key cryptography, which means that a key-pair is generated—one of them public, and the other 
private, or secret.

Since CFEngine is a client-server enterprise software system, it is essential to access the servers 
securely. This is true whether the CFEngine system is run on a cloud platform, like Amazon Web Services 
and many others—or on a private network.

That is where PuTTY comes into the picture. The PuTTY software consists of two separate programs: 
PuTTYgen, which is used to generate the encryption key pair—and PuTTY, a command-line interface, 
which is used to secuerely access the CFEngine server, or _hub_, from a remote client machine, which is called 
a _host_ in CFEngine terminology.

PuTTYgen is used only when setting up a new client machine on the CFEngine hub. The CFEngine _hub_ will already 
have a _public-key file_, and PuTTYgen will download this file, by clicking on the _Load_ button. 

![The PuTTYgen Interface](puttygen-interface.png)

The following steps describe how to get the client machine, up and running using PuTTYgen.  It is important
to note that the _public-key_ on the _hub_ will probably be in a file format that is different from the PuTTYgen
file format. For example on Amazon Web Services (AWS) and many other cloud computing services, the format will be
in _.pem_. 

PuTTYgen will be used to create a matching _private-key_ for the specific user—and will save the resulting _key-pair_ 
in the _.ppk_ file format on the user's hard disk.

1. In the Load private key window select All Files (*.*) in the drop down menu next to the 
File name input box.

2. Navigate to the location on disk where the _public-key_ file was downloaded in earlier steps, in this case a _.pem_ file.

3. Enter a _Passphrase_ and confirm the _Passphrase_. If no _Passphrase_ is desired, leave those fields empty.

4. When the key has been loaded click the Save private key button.

![The PuTTYgen Key Generator Window](putty-key-generator-window)

5. If saving without a _Passphrase_ a dialog box will pop up; click _yes_ to save the key without a _Passphrase_.









