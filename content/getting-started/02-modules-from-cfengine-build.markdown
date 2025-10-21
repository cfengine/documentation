---
layout: default
title: Modules from CFEngine Build
sorting: 20
aliases:
  - "/getting-started-modules-from-cfengine-build.html"
  - "/getting-started/modules-from-cfengine-build"
---

Now that you've installed CFEngine and the tools we need, we can start working with modules from CFEngine Build.
The workflow will look like this:

![](workflow.png)

## Step 0: Creating a new project

Create a folder for you project, for example in your home directory:

```command
mkdir -p ~/cfengine_project
```

Initialize it:

```command
cd ~/cfengine_project && cfbs init
```

When you run `cfbs init` it will prompt you about what to name the project, whether you want to use `git`, etc.
Other commands which you use to edit a CFEngine Build project, such as `cfbs add`, `cfbs remove`, etc. have similar prompts.
Just read the questions/instructions in your terminal, answer as you see fit, and if you are unsure, you can always just press enter to use the default.
For simplicity, we won't keep mentioning the prompts throughout this tutorial.

## Step 1: Explore and add modules

The first module in your project should be `masterfiles`, or a version of it.
This is the default policy which is included in the CFEngine packages, so it is already running on your hub.
It is needed for various features of CFEngine and CFEngine Enterprise to work correctly.
If you didn't add it as part of the previous `cfbs init`, add it now:

```command
cfbs add masterfiles
```

At this point, you can go to [build.cfengine.com](https://build.cfengine.com) and find modules you would like to use.
The command to add them is the same as above.
For the purposes of this tutorial, let's add the git module so we can work with git repositories later:

```command
cfbs add git
```

Additionally, let's add a module to make CFEngine run policy and report collection every minute instead of the default 5 minute interval:

```command
cfbs add every-minute
```

Finally, let's add a report for whether the OS is supported by the OS vendor:

```command
cfbs add compliance-report-os-is-vendor-supported
```

## Step 2: Build

Once we are done adding modules, it is time to build them, combining it all into the policy set which will be deployed to our hub:

```command
cfbs build
```

```output
Modules:
001 masterfiles                              @ a87b7fea6f7a88808b327730a4ba784a3dc664eb (Downloaded)
002 library-for-promise-types-in-python      @ c3b7329b240cf7ad062a0a64ee8b607af2cb912a (Downloaded)
003 promise-type-git                         @ c3b7329b240cf7ad062a0a64ee8b607af2cb912a (Downloaded)
004 every-minute                             @ 74b6776ca4e120285f9c44e68ccf79eef84accfd (Downloaded)
005 compliance-report-imports                @ 06f0894b662befbba4e775884f21cfe8573c32d6 (Downloaded)
006 autorun                                  @ c3b7329b240cf7ad062a0a64ee8b607af2cb912a (Downloaded)
007 compliance-report-os-is-vendor-supported @ d9e0aad225535b2b16ba2126e8302f8ffc5e7d38 (Downloaded)

Steps:
001 masterfiles                              : run './prepare.sh -y'
001 masterfiles                              : copy './' 'masterfiles/'
002 library-for-promise-types-in-python      : copy 'cfengine.py' 'masterfiles/modules/promises/'
003 promise-type-git                         : copy 'git.py' 'masterfiles/modules/promises/'
003 promise-type-git                         : append 'enable.cf' 'masterfiles/services/init.cf'
004 every-minute                             : json 'def.json' 'masterfiles/def.json'
005 compliance-report-imports                : copy './compliance-report-imports.cf' 'masterfiles/services/autorun/'
006 autorun                                  : json 'def.json' 'masterfiles/def.json'
007 compliance-report-os-is-vendor-supported : copy './os-is-vendor-supported.json' 'masterfiles/.no-distrib/compliance-report-definitions/os-is-vendor-supported.json'

Generating tarball...

Build complete, ready to deploy 🐿
 -> Directory: out/masterfiles
 -> Tarball:   out/masterfiles.tgz

To install on this machine: sudo cfbs install
To deploy on remote hub(s): cf-remote deploy
```

Importantly, we see that our policy was built successfully, from 7 different modules.
4 of those are modules we added, and the 3 others were added as dependencies.
The output of the build, the policy set, is available in the `out/` directory.
Feel free to look at some of the files in `out/masterfiles/`, if you want to understand how these modules work.

## Step 3: Deploy

Now, let's deploy what we built to the hub:

```command
cf-remote deploy
```

**Note:** This assumes your hub is saved in `cf-remote`, with the group name _hub_.
We did this in the first part of the series, while installing CFEngine, but if you haven't you can do it like this:

```command
cf-remote save -H root@192.168.56.2 --role hub --name hub
```

(Replace SSH username and IP with what works on your hub).

## Step 4: Observe

Open your web browser and enter the IP address of your hub in the address bar to go the Mission Portal web UI.
For example:

https://192.168.56.2/

(Log in with username `admin` and password `admin`, or whatever you changed it to when you first logged into your hub).

By clicking on _Reports_ and _Compliance_ we can see the report we added, _OS is vendor supported_:

![](os-is-vendor-supported.gif)

(It may take a few minutes before the report shows up).

## What's next

Now that you've successfully added modules and seen the results in Mission Portal, you're ready to look for more modules, or explore Mission Portal further.
Here are some examples of modules you might be interested in:

- [Inventory (reporting) data of who can use sudo on each host](https://build.cfengine.com/modules/inventory-sudoers/)
- [Scan and report on potentially vulnerable log4j installations](https://build.cfengine.com/modules/cve-2021-44228-log4j/)
- [Upgrade all packages with the system's package manager (apt, yum, etc.)](https://build.cfengine.com/modules/upgrade-all-packages/)

To add more modules, just repeat the commands from steps 1-3.
For example, add the `inventory-sudoers` module to your project:

```command
cfbs add inventory-sudoers
```

Then, as usual, build and deploy:

```command
cfbs build && cf-remote deploy
```

In the next tutorial we will look more at the reporting and Web UI, called Mission Portal:

[Reporting and web UI][Reporting and web UI]
