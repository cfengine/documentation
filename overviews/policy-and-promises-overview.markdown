---
layout: default
title: Policy and Promises Overview
sorting: 2 
categories: [Overviews, Policy and Promises Overview]
published: true
alias: overviews-promises.html
tags: [overviews, promises overview]
---

Central to CFEngine's effectiveness in system administration is an intuitive tool called a **promise**, which defines the intent and expectation of how some part of an overall system should behave. 

CFEngine is a system that emphasizes the promises a client makes to the overall CFEngine network. Combining promises with patterns to describe where and when promises should apply is what CFEngine is all about.

This document describes in brief what a promise is and what a promise does. There are other resources for finding out additional details about **promises** in the See Also section at the end of this document.

## What Are Promises ##

A promise is the documentation or definition of an intention to act or behave in some manner. They are the rules which CFEngine clients are responsible for implementing. 

### The Value of a Promise ###

When you make a promise it is an effort to improve trust, which is an economic time-saver. If you have trust then there is less need to verify, which in turn saves time and money.

When individual components are empowered with clear guidance, independent decision making power, and the trust that they will fulfil their duties, then systems that are complex and scalable, yet still manageable, become possible. 

### Anatomy of a Promise ###

```cf3
bundle agent hello_world
{
  reports:

    any::

      "Hello World!"
        comment => "This is a simple promise saying hello to the world.";

}
```

## How Promises Work ##

Everything in CFEngine can be thought of as a promise to be kept by different resources in the system. In a system that delivers a web site with Apache httpd, an important promise may be to make sure that httpd is installed, running, and accessible on port 80. 

In the simple **hello_world** example shown above, the **promise** is that the **Hello World** message will be sent to the log, which will then trigger other events that will be described below. 

### Summary for Making a Promise ###

Making a CFEngine **promise** will generally follow these simple steps:

1. Open a text editor and create a new file (e.g. **hello_world.cf**).
2. Create the **promise** in the file (see **Defining the Promise**).
3. Save the file on **policy server** somewhere under **/var/cfengine/masterfiles** (can be under a sub-directory).
4. Let CFEngine know about the **promise** on the **policy server**, generally in the file **/var/cfengine/masterfiles/promises.cf**, or a file elsewhere but referred to in **promises.cf**.

### Steps to Create a Promise ###

(**1**) Create a bundle.

```cf3
bundle agent hello_world
{

}
```

(**2**) Insert the promise type **reports**.

```cf3
bundle agent hello_world
{
  reports:

}
```

(**3**) Add a class expression (optional). The class expression defaults to '**any**', but in this example it is explicitly declared.

```cf3
bundle agent hello_world
{
  reports:

    any::

}
```

(**4**) Give attributes required values. In this case only our simple "**Hello World!**" message string.

```cf3
bundle agent hello_world
{
  reports:

    any::

      "Hello World!"

}
```

### Observing the Promise in Action ###

#### Manually Executing the Promise ####

(**1**) Assuming the promise file is located at **/var/cfengine/masterfiles/hello_world.cf**, on the command line type the following: 

```# /var/cfengine/bin/cf-agent --no-lock --file /var/cfengine/masterfiles/hello_world.cf --bundlesequence hello_world```

(**2**) The output will include something similar to the following:

```notice: R: Hello World!```


#### Registering the Promise ####

Registering the promise with CFEngine consists of some simple steps:

(**1**) On the policy server, open the file **/var/cfengine/masterfiles/promises.cf** in a text editor.
(**2**) At the end of the **bundlesequence** section add the following line:

```
"hello_world",
```
(**3**) At the end of the **inputs** section add the following line:

```
"hello_world.cf",
```

With the above information CFEngine will then do the following:

1. The policy server copies the **hello_world promise** defined in **promises.cf** to its own **/var/cfengine/inputs** directory.
2. Hosts pull their own copy of the same **hello_world promise** into its own **/var/cfengine/inputs** directory.
3. The **promise** is executed.
4. In the **hello_world** example an adminstrator, defined in the file **controls/cf_execd.cf**, will be emailed the message "**Hello World!**". 

## See Also ##
* [Promises][Promises]



