---
layout: default
title: Design Center Overview
published: true
sorting: 60
tags: [design center, cf-sketch, sketches, deploy policy]
---

The Design Center is a public repository for customizable CFEngine design 
patterns and code. [Sketches][Sketch Structure] are ready-to-use components 
(e.g. collections of bundles, support files, etc.) that can be directly 
imported and used in CFEngine policies. Most sketches are specialized for 
achieving specific tasks, or for maintaining a specific piece of software, 
however their scope and capabilities can be varied. They are organized in 
categories according to their functionality. Sketches are managed (installed, 
configured, enabled and uninstalled) through a specialized tool called 
cf-sketch.

[Use Design Center Sketches to Deploy Policy](#use-design-center-sketches-to-deploy-policy)
[The Design Center Sketch Workflow](#the-design-center-sketch-workflow)
[Value of Sketches to Users](#value-of-sketches-to-users)
[Design Center Terminology](#design-center-terminology)
[See Also](#see-also)

## Use Design Center Sketches to Deploy Policy

The CFEngine Design Center is a collection of `sketches` which are reusable, configurable 
policies. Think of sketches as templates that are written in CFEngine policy language; you can 
use these templates to configure and deploy CFEngine policy without mastering the 
CFEngine language. 

The Design Center also contains tools that help you to manipulate and 
manage sketches: 

* Enterprise users manage and deploy sketches in the Design Center app that is located on 
the Mission Portal console. [Deploy your first policy in the Design Center][Deploy your first Policy].

* Community users manage and deploy sketches on the [command line][Command Line Sketches] by using the `cf-sketch` 
tool.

## The Design Center Sketch Workflow

A sketch is installed, configured, and deployed, as shown in the diagram below:

![Sketch Workflow](DCsketchworkflow.png)

1. Install a sketch on a Host from a repository. At this point, the sketch is merely 
a template that cannot do anything because it doesn’t contain parameters.

2. Configure the sketch by providing parameters. Now, you can create sketch 
configurations.  One sketch can have multiple configurations with different parameter sets 
that will get applied under different conditions.

3. Deploy the sketch. This makes the sketch visible to CFEngine, so it can begin to execute.

## Value of Sketches to Users

Sketches provide a time-value in many ways:

* Instead of writing a single policy for each desired state, you can use templated policies 
(sketches) to implement, activate, or enforce policy. Users can configure the sketch for 
the appropriate environment, and then deploy it on your infrastructure, all without 
knowing the intricacies of CFEngine policy language. 

* You can have infinitely flexible configurations of sketches across your infrastructure 
based on static (such as CPU or OS) or dynamic (such as time of day or number of users) 
conditions (classes). Every time CFEngine runs, it chooses which sketch(es) to execute with 
which parameter sets based on those conditions. As conditions change, the execution of 
sketches can change, just as the behavior of regular CFEngine policy can change.

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
to use a sketch to configure and deploy a simple policy by using the Design Center app on 
the Mission Portal console.
* [Configure the Design Center App (Enterprise)][Configure the Design Center App] This section is for Enterprise users who plan to 
manage sketches and possibly write new ones. It also includes advanced topics that provide a 
better look at managing Enterprise sketches in the Design Center app and understanding 
the overall sketch flow.
* [Configure Sketches on the Command Line (Community)][Command Line Sketches] This section is for Community users 
who plan to install, configure, and deploy sketches.
* [Write a new Sketch (Enterprise and Community)][Write a new Sketch] This is an advanced section for both Enterprise 
and Community users who plan to write new sketches.



