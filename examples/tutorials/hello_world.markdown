---
layout: default
title: Hello World 
sorting: 10
categories: [Examples, Tutorials]
published: true
alias: examples-tutorials-hello-world.html
tags: [Examples, Tutorials, hello-world, stand-alone]
---

While CFEngine typically runs automatically, it can also be invoked manually
with standalone policy. In this tutorial you will learn how to write a
standalone policy that reports the obligitory "Hello World".

CFEngine policy files by convention are suffixed with the `.cf` or `.cf3` file
extensions. Learn more about writing CFEngine policy from the [Policy Style
Guide][Policy Style Guide].

## Overview
Create hello_world
Make hello_world stand-alone
Make hello_world.cf a script


## Create hello_world

Create hello_world.cf with the following content:

```cf3
bundle agent hello_world
# @brief Say Hi to everyone and introduce yourself
{
  reports:

    any::
      
      "Hello World! I am $(sys.fqhost) and its $(sys.date)"
        comment => "It's nice to introduce yourself when you say hello";


}
```

Bundles are collections of promises. They allow related promises to be grouped
together. Here we have defined an agent bundle named `hello_world`. Agent
bundles are only evaluated by the [agent component][cf-agent] of CFEngine
(cf-agent).

This bundle [promises][Promises] to [report][reports] on any [class of
hosts][Classes and Decisions] `Hello World! I am $(sys.fqhost) and its
$(sys.date)`. [$(sys.fqhost)][sys#sys-fqhost] and [$(sys.date)][sys#sys-date]
are [special variables][Special Variables] that are automatically defined
during an agent run that expand to the fully qualified hostname and todays date
respectively.

Take special note of the `comment` attribute attached to the report promise.
Comments are intended to follow the promise and provide insight into the reason
a promise is used. When writing comments its good practice to try and answer
*why* the promise exists.

Lets activate the bundle manually.
```
# /var/cfengine/bin/cf-agent --no-lock --file ./hello_world.cf --bundlesequence hello_world
2013-08-20T14:03:43-0500   notice: R: Hello World! I am thinkpad-w520 and its Tue Aug 20 14:03:32 2013
```

Here we are instructing CFEngine to ignore [locks][Controlling Frequency], load
the `hello_world.cf` policy, and activate the `hello_world` bundle.

## Make hello_world stand-alone

Instead of specifying the bundlesequence on the command line, a [body common
control][Components and Common Control#Common Control] section can be added to
the policy file. It's important to note that only one `body common control` is
allowed per agent activation.

Add body common control to `hello_world.cf`.

```cf3
body common control
{
  bundlesequence => { "hello_world" };
}

bundle agent hello_world
# @brief Say Hi to everyone and introduce yourself
{
  reports:

    any::
      
      "Hello World! I am $(sys.fqhost) and its $(sys.date)"
        comment => "It's nice to introduce yourself when you say hello";


}
```

Lets run the policy.

```
# cf-agent --no-lock --file ./hello_world.cf
2013-08-20T14:25:36-0500   notice: R: Hello World! I am thinkpad-w520 and its Tue Aug 20 14:25:25 2013
```


## Make hello_world an executable script

This is a handy little trick. It allows you to take CFEngine policy and invoke
it as an executable script.

Add a shebang to `hello_world.cf`.

```cf3
#!/var/cfengine/bin/cf-agent -Kf
body common control
{
  bundlesequence => { "hello_world" };
}

bundle agent hello_world
# @brief Say Hi to everyone and introduce yourself
{
  reports:

    any::
      
      "Hello World! I am $(sys.fqhost) and its $(sys.date)"
        comment => "It's nice to introduce yourself when you say hello";


}
```

Make the policy file executable, and run it.

```
# chmod +x ./hello_world.cf
# ./hello_world.cf
2013-08-20T14:39:34-0500   notice: R: Hello World! I am thinkpad-w520 and its Tue Aug 20 14:39:22 2013
```
