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
with standalone policy. This tutorial describes how to write a
standalone policy that reports the obligatory __Hello World__.

CFEngine policy files by convention are suffixed with the `.cf` or `.cf3` file
extensions. Learn more about writing CFEngine policy from the [Policy Style
Guide][Policy Style Guide].

## Overview
This tutorial provides instructions for the following:

* Create a hello_world policy file

* Make hello_world standalone

* Make hello_world.cf an executable script


## Create hello_world

Policies contain bundles, which are collections of promises. A promise is a declaration of
intent. Bundles allow related promises to be grouped together, as illustrated in the tutorial below.

Create a policy file called __hello_world.cf__ with the following content:

```cf3
bundle agent hello_world
# @brief Say Hi to everyone and introduce yourself
{
  reports:

    any::
      
      "Hello World! I am $(sys.fqhost) and it is $(sys.date)"
        comment => "It's nice to introduce yourself when you say hello";


}
```

In the policy file above, we have defined an agent bundle named `hello_world`. Agent
bundles are only evaluated by the [agent component][cf-agent] of CFEngine
(cf-agent).

This bundle [promises][Promises Types and Attributes] to [report][reports] on any [class of
hosts][Classes and Decisions] from `Hello World! I am $(sys.fqhost) and it is
$(sys.date)`. [$(sys.fqhost)][sys#sys.fqhost] and [$(sys.date)][sys#sys.date]
are [special variables][Special Variables] that are automatically defined
during an agent run and expand to the fully-qualified hostname and today's date
respectively.

Take special note of the `comment` attribute that is attached to the report promise.
Comments are intended to follow the promise and provide insight into the reason
a promise is used. When writing comments, it's good practice to answer *why* the promise exists.

Activate the bundle manually by adding the following on the command line:
```
/var/cfengine/bin/cf-agent --no-lock --file ./hello_world.cf --bundlesequence hello_world
```
This command instructs CFEngine to ignore [locks][Controlling Frequency], load
the `hello_world.cf` policy, and activate the `hello_world` bundle. See the output below:

```
# /var/cfengine/bin/cf-agent --no-lock --file ./hello_world.cf --bundlesequence hello_world
2013-08-20T14:03:43-0500   notice: R: Hello World! I am thinkpad-w520 and it is Tue Aug 20 14:03:32 2013
```

## Make hello_world standalone

Instead of specifying the bundlesequence on the command line (as it was above), a [body common
control][Components and Common Control#Common Control] section can be added to
the policy file. The common body control refers to those promises that are hard-coded into
all CFEngine components and therefore affect the behavior of all components. Note that only
 one `body common control` is allowed per agent activation.

Add __body common control__ to `hello_world.cf`. Place it above __bundle agent hello_world__, as 
shown in the following example:

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
      
      "Hello World! I am $(sys.fqhost) and it is $(sys.date)"
        comment => "It's nice to introduce yourself when you say hello";


}
```

Run the policy by adding the following on the command line: 
```
cf-agent --no-lock --file ./hello_world.cf
```

The output is shown below:

```
# cf-agent --no-lock --file ./hello_world.cf
2013-08-20T14:25:36-0500   notice: R: Hello World! I am thinkpad-w520 and it is Tue Aug 20 14:25:25 2013
```


## Make hello_world an executable script

Add a shebang to `hello_world.cf` in order to invoke CFEngine policy as an executable script:
```
#!/var/cfengine/bin/cf-agent -Kf
```

Add it before __body common control__, as shown below:

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
      
      "Hello World! I am $(sys.fqhost) and it is $(sys.date)"
        comment => "It's nice to introduce yourself when you say hello";


}
```

Make the policy file executable, and then run it by adding the following on the command line:
```
chmod +x ./hello_world.cf
./hello_world.cf
```
See the output below:

```
# chmod +x ./hello_world.cf
# ./hello_world.cf
2013-08-20T14:39:34-0500   notice: R: Hello World! I am thinkpad-w520 and it is Tue Aug 20 14:39:22 2013
```
