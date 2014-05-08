Quick-Start Guide to PuTTY


This guide is designed for the novice user of CFEngine software. 

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
which is used to access the CFEngine server, or _hub_.

PuTTYgen is used only when setting up a new client machine on the CFEngine hub. The hub will already 
have a key-pair file, and PuTTYgen will download this file, by clicking on the _Load_ button.

![The Puttygen Interface](Puttygen Interface.png)





