---
layout: default
title: Configure CFEngine Policy Server
sorting: 100
categories: [Getting Started, Policy Server]
published: true
alias: getting-started-policy-server.html
tags: [getting started, policy server]
---

## What is the Policy Server 

The policy server makes important files available to client machines.

## How Does it Work ##

The policy server itself only makes the files available on the network. It is up to the clients for which the server is responsible to pull the files themselves. The server will not do this on their behalf.

## Basic Policy Server Configuration ##

### def.cf ###

### controls/cf_execd.cf ###

### Configuring a Promise in promises.cf ###

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

### Alternative Configuration Approach for promises.cf ###





