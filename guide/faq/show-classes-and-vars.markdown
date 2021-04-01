---
layout: default
title: How can I tell what Classes and Variables are defined?
published: true
sorting: 90
tags: [getting started, installation, faq]
---

You can see a high level overview of the first order classes and variables using
`cf-promises --show-classes` and `cf-promises --show-vars`.

Both of those commands will take an optional regular expression you can use to
filter the classes or variables. For example `cf-promises --show-classes=MT`
will show all the classes that contain `MT` like `GMT_July`.

You can see the variables and namespace scoped classes defined at the end of an
agent execution by using the ```--show-evaluated-vars``` or
```--show-evaluated-classes``` options to `cf-agent`. In addition to the
variables and classes shown by `cf-promsies --show-classes` or `cf-promises
--show-vars` this will show variables and namespace scoped classes that get
defined during a full agent run where the system may be modified and more policy
is evaluated.

# Show first order classes with cf-promises

```console
cf-promises --show-classes
```

[%CFEngine_include_snippet(cf-promises_--show-classes.txt, [\w], ^$)%]

# Show first order variables with cf-promises

```console
cf-promises --show-vars
```

[%CFEngine_include_snippet(cf-promises_--show-classes.txt, [\w], ^$)%]


