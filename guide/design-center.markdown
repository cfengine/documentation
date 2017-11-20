---
layout: default
title: Design Center Overview
published: false
sorting: 70
tags: [design center, cf-sketch, sketches, deploy policy]
---

The Design Center is a public repository for data-driven policy
templates called *sketches* that is deeply integrated with CFEngine
Enterprise.

[Sketches][Sketch Structure] are ready-to-use components (e.g.
collections of bundles, support files, etc.) that can be directly
imported and used in CFEngine policies. Most sketches are specialized
for achieving specific tasks, or for maintaining a specific piece of
software, but their scope and capabilities can range beyond. They are
organized in categories and tagged according to their functionality.

Sketches are managed (installed, configured, enabled and uninstalled)
through a specialized tool called `cf-sketch` which in turn talks to a
specialized Design Center API. That API is available for third-party
integrations.

In CFEngine Enterprise, the Design Center interactions are driven by
the Mission Portal **Design Center App** for great ease of use.

This is a guide to the Design Center functionality. For the reference
pages for its API and code structure, start with
[Design Center][Design Center].

* [Use Design Center Sketches to Deploy Policy](#use-design-center-sketches-to-deploy-policy)
* [The Design Center Sketch Workflow](#the-design-center-sketch-workflow)
* [Value of Sketches to Users](#value-of-sketches-to-users)
* [Design Center Terminology](#design-center-terminology)
* [See Also](#see-also)

## Use Design Center Sketches to Deploy Policy

The CFEngine Design Center is a collection of data-driven policy
templates called *sketches*. Sketches can be configured and deployed
("activated") without prior knowledge of the CFEngine language.

The Design Center also contains tools that help you to manipulate and
manage sketches:

* Enterprise users manage and deploy sketches in the Mission Portal **Design Center App**. [Deploy your first policy in the Design Center][Deploy your first Policy].

* Community users manage and deploy sketches on the [command line][Command Line Sketches] by using the `cf-sketch`
tool.

* third-part integrators can use the Design Center API from the
command line or through the CFEngine Enterprise API. For more information, see [The Design Center API][The Design Center API].
<!-- (??? LINK TO Enterprise DC API depends on https://dev.cfengine.com/issues/6011 ???) -->


## The Design Center Sketch Workflow

A sketch is installed, configured, and deployed (the whole process is called an "activation"), as shown in the diagram below:

![Sketch Workflow](DCsketchworkflow.png)

1. Install a sketch from a master repository. At this point, the
sketch is merely a template that cannot do anything because it doesn’t
contain parameters. With CFEngine Enterprise, installations are
handled invisibly.

2. Configure the sketch by providing parameters. Now, you can create
sketch configurations. One sketch can have multiple configurations
with different parameter sets that will get applied under different
conditions. With CFEngine Enterprise, you do this from a GUI screen.

3. Deploy the runfile. This makes the sketch visible to CFEngine, so
it can begin to execute. Typically the intermediate stage here is to
generate a runfile (the policy glue that enables all the Design Center
magic) and check it into your version control repository. With
CFEngine Enterprise, this step is handled invisibly, you just enter a
commit message for the change you've made.

## Value of Sketches to Users

Sketches provide value to CFEngine users, especially Enterprise customers:

* Instead of writing a single policy for each desired state, you can
use data-driven policies (sketches) to implement, activate, or enforce
policy. Users can configure the sketch for the appropriate environment
and then deploy it to specific hosts or groups of hosts without knowing the
intricacies of CFEngine policy language.

* You can have infinitely flexible configurations of sketches across your infrastructure
based on static (such as CPU or OS) or dynamic (such as time of day or number of users)
conditions (classes). Every time CFEngine runs, it chooses which sketch(es) to execute with
which parameter sets based on those conditions. As conditions change, the execution of
sketches can change, just as the behavior of regular CFEngine policy can change.

* There's a large list of sketches you can use already and the list is growing.  You can use them as they are, or learn from their techniques and write your own.

## Design Center Terminology

* `Design Center`  Refers to the collection of sketches and the tools that allow you to
manipulate and manage them.
* `Design Center app (UI)` Refers to the Design Center user interface app that is
located on the Mission Portal console for CFEngine Enterprise users.
* `Design Center in GitHub` Refers to the [CFEngine github][github design-center] repository of sketches, tools,
and policy examples.
* `Design Center API` Refers to the [API][The Design Center API] which performs all operations related to
sketches, parameter sets, environments, validations, and deployment.

## See Also ##

* [Deploy your first Policy (Enterprise)][Deploy your first Policy] This Enterprise-specific tutorial illustrates how
to use a sketch to configure and deploy a simple policy by using the **Design Center App** on
the Mission Portal console.
* [Configure Sketches on the Command Line (Community)][Command Line Sketches] This section is for Community users
who plan to install, configure, and deploy sketches.
* [Write a new Sketch (Enterprise and Community)][Write a new Sketch] This is an advanced section for both Enterprise
and Community users who plan to write new sketches.
