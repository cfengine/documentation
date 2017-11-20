---
layout: default
title: Deploy your first Policy
published: false
sorting: 10
tags: [design center, sketches]
---

### Enterprise Users can Deploy Policies through the Design Center App

**Note:** This tutorial walks you
through configuring and deploying ("activating") a sketch to make it part of your site policy. You must be an authenticated Enterprise user who has authorized access
to the CFEngine Mission Portal console. CFEngine must be up and running in order to complete
this tutorial.

## Overview

A **sketch** defines data-driven configurable and reusable policy. You can use sketches to implement,
activate, or enforce policy. Sketches are written in the CFEngine
policy language; you can use them simply by installing them, configuring them
using the appropriate parameters and environments, and then deploying them on your infrastructure ("activating" them).

In this tutorial, we want to implement the following policy:

The **iscsi-initatior-utils** software package must be present/installed on all hosts.

Since CFEngine includes a sketch (the **Packages** sketch) that can generate this
policy, we do not do not need to write a policy. Instead, we can use the **Packages** sketch
to deploy our policy. (Note that you may use an alternate package from your
system's package repository if necessary.)

## Configure and deploy a policy using sketches
We will activate the **Packages** sketch which allows you to install selected software
packages on specific hosts. A sketch must include a **parameter set** and an **environment(s)**, both of which
we will set in the example below. Make certain that the packages you select are included in the
package repository. (The package in our example below is available in the CentOS package repository. You
can select any package that is available through your operating system's package repository.)

1. Log in to the Mission Portal. Select **Design Center** from the left sidebar.

2. Select the **Packages::installed** sketch. Use the following values:

	a. **Descriptive name:** Enter **Install iSCSI**. This allows you to recognize the activation
   (and its goal) later, as the Design Center uses this name when it commits changes to Git.

	b. **Packages that should be installed:** Fill in the name of the package that must be installed.
   For this example, use **iscsi-initiator-utils**. This is the **parameter set**.

	c. **Hosts to activate on:** Click **Select category** to display host options. Select **All hosts**
   for our example. All host names appear. This is the **environment** in which the sketch
   must be activate.

   Here is an example:

   ![Sketch Configuration](Sketch.png)

3. Click **Activate**. This deploys the sketch to all hosts.

4. Enter a description in the **Commit your changes** window that appears. The Design Center
   uses this comment for version control when it commits changes to Git.
   Click **Commit** to complete the change.

**When a sketch is activated, the following occurs:**

* The policy that is generated when the sketch is activated gets committed to your Git repository.
This allows you to keep track of who has made what changes, and when, and why.

* The **policy server** is typically configured to check the Git repository every five minutes to ensure
that it is running the latest version of available policies. This process can be handled manually as well.

* The **hosts** check with the policy server for updated policy. They also work on default intervals of five minutes.

* The policy server collects information from the agents on the hosts to obtain insight
   into the progress with executing the sketch. The information it collects is used to update
   the information in the Design Center.

In total, this process might take a few minutes to converge to the correct state for all hosts.
The process is designed to be scalable: even though it takes a few minutes for the two servers in this
example to be updated, it does not take much longer to update 2,000 servers.
If you check back with the Packages sketch in the middle of the activation process, you will
see a message that reads **Status: Being Activated**. Upon successful completion, the window
should look like this:

![Activated Sketch](Activated-sketch.png)

Now that the sketch is deployed, CFEngine continuously verifies that it is maintained. It checks
365 days per year, 24 hours per day, 12 times per hour to make certain this package is on all of the hosts.
If the package is removed, it is added within five minutes, and CFEngine creates reports that it
made a _repair_. Thus, the state of the overall system is known and stable and system drift is avoided.
This works for 2, 200, or 20,000 servers.
