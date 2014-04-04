---
layout: default
title: Policy Server Overview
sorting: 100
published: true
tags: [overviews, system overview, policy server]
---

## What is the Policy Server 

The policy server makes important files available to client machines.

## How Does it Work ##

The policy server itself only makes important files available on the network. It is up to the clients for which the server is responsible to pull the files themselves. The server will not do this on behalf of its clients.

### Basic Policy Server Setup ###

There are two essential things that need to be taken care of when setting up a simple policy server:

1. Bootstrapping
2. Configuration

#### 1. Bootstrap the Policy Server ####

The Policy Server must be bootstrapped to itself. 

(**1**) Find the IP address of your Policy Server:

``` 
$ ifconfig
```

(**2**) Run the bootstrap command:

```
$ sudo /var/cfengine/bin/cf-agent --bootstrap <IP address of policy server>
```

Note: The bootstrap command must also be run on any client attaching itself to this server, using the ip address of the policy server (i.e. exactly the same as the command run on the policy server itself).

#### 2. Basic Policy Server Configuration ####

##### def.cf #####

(**1**) Find the following line:
```
"domain"  string    => "your.domain.here",
```
(**2**) Change **your.domain.here** to your domain name, e.g. **example.com**.

##### controls/cf_execd.cf #####

(**1**) Find the following line:
```
mailto                => "some-admin-list@me.local";
```
(**2**) Change **some-admin-list@me.local** to your email address.

Note: On some systems this modification should hopefully work without needing to make any additional changes elsewhere. However, any emails sent from the system might also end up flagged as spam and sent directly to a user's junk mailbox.


##### Configuring a Promise in promises.cf #####

Assuming there is a promise called "**hello_world**" defined in a file located at **/var/cfengine/masterfiles/hello_world.cf**:

(**1**) On the policy server, open the file **/var/cfengine/masterfiles/promises.cf** in a text editor.
(**2**) At the end of the **bundlesequence** section add the following line:

```
"hello_world",
```
(**3**) At the end of the **inputs** section add the following line:

```
"hello_world.cf",
```

##### Alternative Configuration Approach for promises.cf #####

Bundles and promises can be included in files outside of **promises.cf**.

(**1**) Create a file called **/var/cfengine/masterfiles/z01PromiseSetup.cf**
(**2**) In it add the following content:
```
bundle common z01_promise_setup
{
vars:
    "bundles" slist     => {
                             "",
    } ;

    "promise_files" slist
                        => {
                             "",
    } ;

}
```
(**3**) Assuming there is a promise called "**hello_world**" defined in a file located at **/var/cfengine/masterfiles/hello_world.cf**, modify **/var/cfengine/masterfiles/z01PromiseSetup.cf**:
```
bundle common z01_promise_setup
{
vars:
    "bundles" slist     => {
                             "hello_world",
    } ;

    "promise_files" slist
                        => {
                             "hello_world.cf",
    } ;

}
```
(**4**) In **promises.cf**, at the end of the **bundlesequence** section, replace **"hello_world",** with the following two lines:

```
"z01_promise_setup",
@(z01_promise_setup.bundles),
```
(**5**) Also in **promises.cf**, at the end of the **inputs** section, replace **"hello_world.cf",** with the following two lines:

```
"z01PromiseSetup.cf",
@(z01_promise_setup.promise_files),
```

Note: It can take up to 10 minutes for these changes to propogate across the entire system.
