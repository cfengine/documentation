---
layout: default
title: Using Sketches in Mission Portal's Design Center App
sorting: 100
published: true
tags: [overviews, mission portal, sketches, design center, design center app]
---

## Design Center App ##

The CFEngine `Design Center` includes a number of templates, so called `sketches`, that let you configure and deploy CFEngine `policies` without requiring detailed knowledge of the CFEngine language. You can select `sketches` from a categorized list, and configure them in the interface.

Every organization using CFEngine can add their own custom `sketches` which will consequently be shown in the app's list of sketches.

Note: The `Design Center App` requires a dedicated git repository. If you have admin rights to the `Mission Portal`, you can configure it in `Settings`.

### Configuration ###

After selecting a sketch, you need to configure a number of parameters. Start with giving your current configuration a unique name which will make it easier for your to recognize it again later. Then fill in the mandatory fields below. All of them show examples and a descriptive text.

You also need to define the hosts you want to activate your configured sketch on. You can select host categories of varying size by following the step-by-step selection presented in the drop-down menus. These categories are based on categorizations defined for example in the `Hosts App`.

### Activation ###

When you're done configuring your `sketch` you need to activate it. This will trigger a commit to your configured git repository, and transform your configured sketch into CFEngine `policy`. You will then be able to follow-up on the state of your activation (`In Progress`, `OK`, and `Failed`), and report on potential issues.

Note: `Sketches` can be activated multiple times with varying configuration and on different sets of hosts. The `Design Center App` indicates which sketches have been activated in your environment.


### See Also ###

* [Design Center Sketches Guide][Design Center Sketches]
* [Write a new Sketch][Write a new Sketch]

