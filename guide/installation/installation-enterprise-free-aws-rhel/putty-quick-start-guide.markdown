---
title: Quick-Start Guide to Using PuTTY
layout: default
published: true
sorting: 2
tags: [how-to-guides, quick-start guides, putty]
---


Quick-Start Guide to Using PuTTY


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

![The Puttygen Interface](puttygen-interface.png)


use the cd command to change directories, for example: `cd /var/cfengine/masterfiles`

to create subdirectory: first sudo su then mkdir name-of-subdirectory

to go into new subdirectory type: cd: name of subdirectory

then go into vi and create file `testing.cf`

1. Create a bundle.

```cf3
bundle agent testing`
{

}
```

2. Insert the promise type `reports`.

```cf3
bundle agent testing
{
  reports:

}
```

3. Add a class expression (optional). The class expression defaults to `any`, but in this example it is explicitly declared.

4. Give attributes required values. In this case only our simple `testing!` message string.

```cf3
bundle agent testing
{
  reports:

    any::

      "testing!";

}
```




exit vi after creating above policy file `testing.cf`

then at subdirectory prompt type: `ls` to see what is there...new file should be there

Can open the file using vi by typing `vi testing`

Now can register the new policy in the promises.cf file

First have to go back to masterfiles directory; type `cd ../` 

then open promises.cf file by typing: `vi promises.cf` Note: may get `E325: ATTENTION` prompt about swap file, press _enter_



Then in the /var/cfengine/masterfiles/promises.cf file you need to add some information so that CFEngine 
will know about your new file and the bundle inside of it That is covered in the four steps in the tutorial.

exit vi; now back in putty go up one directory to `cfengine` by typing: `cd ../`

now go to the `inputs` directory by typing: `cd inputs`

to` see what is there, type: `ls`




