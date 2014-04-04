---
layout: default
title: Up and Running
sorting: 13
published: true
tags: [Examples, Tutorials, Community]
---


## Get Up and Running Quickly with CFEngine 3.5 Community Edition
by [Erik Schwartz](http://www.linkedin.com/pub/erik-schwartz/7/257/ba9), CFEngine Contributor

v0.1, 2013-10

*This information is reprinted with Erik's permission and thanks. Content and formatting modifications have been made where necessary.*

## Overview

This document includes the following:

[CFEngine Basics][Up and Running#CFEngine Basics]

[Install and configure the CFEngine server][Up and Running#Install and configure the CFEngine server]

[Set up your promise management files][Up and Running#Set up your promise management files]

[Set up your first promise][Up and Running#Set up your first promise]

[Start your CFEngine server][Up and Running#Start your CFEngine Server]

[Install and configure CFEngine agent systems][Up and Running#Install and configure CFEngine agent systems]

[Dissect the "hello world" promise][Up and Running#Dissect the "hello world" promise]

[Set up a global classes promise][Up and Running#Set up a global classes promise]

[Add some more useful promises][Up and Running#Add some more useful promises]

[Commands for controlling CFEngine][Up and Running#Commands for controlling CFEngine]

[CFEngine official resources][Up and Running#CFEngine official resources]


## Preface

This document assumes the following:

* You are a competent sysadmin, well-versed in administrating GNU/Linux.
* You are running RHEL or Debian (or perhaps a close derivative).
* You are brand new to CFEngine.

**Note:** Perform due diligence with testing and tinkering, and in a proper test environment, before deploying anything to production. This document assumes no responsibility if you use (or misuse) the advice here, and it causes data loss, service problems, or other system mayhem.


## CFEngine basics
CFEngine is a configuration management system. That means, roughly, it's a collection of applications that is used to get your host (or group of hosts) configured to a desired state. You--the sysadmin--describe that state, and CFEngine makes it happen, and in an automated fashion.

For a more detailed overview:

* http://cfengine.com/what-is-cfengine
* http://en.wikipedia.org/wiki/CFEngine


#### Useful Terms

* `promise`: One or more descriptions (written by you, the sysadmin) of a system state you wish to get to.
* `bundle`: A collection of promises, usually contained within a single file.
* `convergent`: Describes a promise that may be executed in a several-step, sequential fashion. CFEngine may make several passes at completing a single promise, performing a few of the steps each pass.
* `agent`: A CFEngine instance that a) retrieves its promises from a `server` over TCP; b) validates and executes those promises, configuring itself to the desired state.
* `server`: A CFEngine instance that a) contains promises that get deployed to agents; and b) listens on a TCP socket for agent connections. A `server` is also known as a `policy hub` (for the purposes of this primer).

[Back to top of page.][Up and Running#Overview] 

## Install and configure the CFEngine server


### Download and install

Download the latest CFEngine 3.5 Community Edition packages from: http://cfengine.com/community

Decide on a RHEL or Debian system that will act as your CFEngine `server`, and install the package using `rpm(8)`, `dpkg(1)`, or whatever method you prefer.

**Note**: The same package is used for both `server` and `agent` installs.


**IMPORTANT!**
You will likely see a message that reads:

_Policy is not found in /var/cfengine/inputs, not starting CFEngine_

This is fine. No worries for the time being.


### Set up master directories


Navigate to `/var/cfengine/masterfiles`. This directory is where your CFEngine server keeps everything it will be sharing with agents. In other words, the changes we make here will ultimately be made on the agents as well.

```
cd /var/cfengine/masterfiles
```


Within /var/cfengine/masterfiles, create two new directories. These directories will contain your promise files, and your configuration templates, respectively.

```
mkdir myPromises
   
mkdir myTemplates
```

Here is (for the purposes of this primer) how the propagation of promise changes happen from the CFEngine server to the CFEngine agent:

* You make a change within `/var/cfengine/masterfiles` or its subdirectories
* Agent systems connect to the server, and copy `/var/cfengine/masterfiles` into their local `/var/cfengine/inputs` directory


### Customize your server configuration


#### def.cf

Configure `/var/cfengine/masterfiles/def.cf`: This contains two variables of interest: `domain` and `acl`. 

These variables allow us to manage access control, so what we specify here determines which agents have access. Set `domain` to your organization's domain; when an agent attempts to connect to the server, the server does a reverse DNS lookup. For the connection to proceed, the agent's domain should match what you specify here.

**Tip**: If your agent hostnames are `web.me.local` and `mongo.me.local`, then you should set `domain` to `me.local`.


Set `acl` to a comma-separated, quoted (see the example below) list of subnets your agents will be connecting from. Same idea: for the connection to proceed, the agent must be on one of those subnets.

`def.cf`

```cf3
# This is just a snippet from def.cf. Search for and
# modify the appropriate sections.


vars:

    "domain"  string    => "your.domain.here",

# ...

   "acl" slist          => {
        "172.16.31.0/24", 
        "10.5.28.0/24",
   },
```


#### controls/cf_execd.cf


Configure `/var/cfengine/masterfiles/controls/cf_execd.cf`: This tells the CFEngine server what email address to notify about certain events and about reports designed by you, the sysadmin.

Set `mailto` to an email address that you will read and monitor. Set `mailfrom` as shown below. Set `smtpserver` as appropriate for your environment.


**Tip:** Most RHEL and Debian servers have an SMTP service listening on localhost by default. If your agent systems do not, consult with your mail administrator about what to specify here.


`controls/cf_execd.cf`

```cf3
# This is just a snippet from controls/cf_execd.cf. Search for and
# modify the appropriate sections.

body executor control
{

 any::

  splaytime             => "1";
  mailto                => "some-admin-list@me.local";
  mailfrom              => "root@$(sys.fqhost)";
  smtpserver            => "localhost";

# ...
```


#### update.cf


Configure `/var/cfengine/masterfiles/update.cf`: This file controls what files the agents receive from the server. Before changing it, create your `failsafe.cf` from it:

```
  # cd /var/cfengine/masterfiles
  # cp update.cf failsafe.cf
```

**Tip:** failsafe.cf is a safety mechanism: If `update.cf` somehow becomes damaged, CFEngine agents know to fall back to failsafe.cf. After you fix update.cf, CFEngine then begins working from update.cf again.


Two separate sections will be updated in update.cf: `body file&#95;select u&#95;input&#95;files` and `body copy&#95;from u&#95;rcp()`. Take extra care to edit the correct sections, and pay close attention to quotes, commas, brackets, and semicolons. 

`update.cf`

```cf3
# This is just a snippet from update.cf. Search for and
# modify the appropriate sections.

# .. add values to the leaf_name key

body file_select u_input_files
{

leaf_name               => { ".*.cf",".*.dat",".*.txt",".*.conf" };
file_result             => "leaf_name";

}

# ..

# .. add the purge key, with value of "true"

body copy_from u_rcp(from,server)
{

source                  => "$(from)";
compare                 => "digest";
trustkey                => "false";
purge                   => "true" ;

# ..

```

#### promises.cf

Configure `/var/cfengine/masterfiles/promises.cf`: This file drives the agent promise execution. In other words, the agent reads this file to figure out what instructions you have for it.

Under `body common control`, add the lines that follow to `bundlesequence`. Take care to add the lines just before the closing bracket.

Add the lines that follow to inputs. (Same caveat about respecting the closing bracket.)

`promises.cf`

```cf3

# .. snippet from the promises.cf config file

body common control
{

bundlesequence          => {

# ..

        # Agent bundles from here
        "main",


# .. just adding the next three content lines; not removing anything!

        # MY org's stuff
        "z01_promise_setup",
        @(z01_promise_setup.bundles),

    };
                   
    inputs              => {

# ..

        # User services from here
        "services/init_msg.cf",


# .. just adding the next three content lines; not removing anything!

        # MY org's stuff
        "myPromises/z01PromiseSetup.cf",
        @(z01_promise_setup.promise_files),

    };
```

[Back to top of page.][Up and Running#Overview] 

## Set up your promise management files


Within the `/var/cfengine/masterfiles/myPromises` directory, create a skeleton promise file, and name it `z01PromiseSetup.cf`. (Doing so will make adding new promises in the future a lot easier.)

`myPromises/z01PromiseSetup.cf`

```cf3
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


**The bottom line:** From this point forward, we will edit this file (and not `promises.cf`) to add new promises.

[Back to top of page.][Up and Running#Overview] 

## Set up your first promise 


### Create a "hello world" promise file


Within the `/var/cfengine/masterfiles/myPromises` directory, create a file called `a01SayHello.cf`, with the following contents:

#### a01SayHello.cf


```cf3
bundle agent a01_say_hello
{

methods:
    "a01sayhello" usebundle
                        => a01_run ;

}

bundle agent a01_run
{

vars:
    "myfile" string     => "/tmp/helloFromCfengine.txt" ;

files:
    "$(myfile)"
    edit_line           => a01_edit,
    edit_defaults       => empty,
    perms               => mog("644","root","root"),
    create              => "true", 
    classes             => if_repaired("make_some_noise") ;

reports:
    make_some_noise::
    "Heads up - the $(this.promise_filename) promise did its thing." ;

}


bundle edit_line a01_edit
{

vars:
    "hello" string           =>
"If you are reading this, your promise worked on $(sys.fqhost)
Nice going!" ;

insert_lines:
    "$(hello)" ;

}
```


### Make CFEngine aware of the new promise


Now edit `/var/cfengine/masterfiles/myPromises/z01PromiseSetup.cf` as follows.

```cf3
bundle common z01_promise_setup
{
vars:
    "bundles" slist     => {
                             "a01_say_hello",
    } ;

    "promise_files" slist
                        => {
                             "myPromises/a01SayHello.cf",
    } ;

}
```

[Back to top of page.][Up and Running#Overview] 

## Start your CFEngine server


#### Do a quick syntax check


Make sure you don't have any typos up to this point.

```
  # cf-promises -f /var/cfengine/masterfiles/promises.cf
```

If you see any error output, carefully review the messages for line numbers that are causing the problem. Reread earlier steps in this primer, and try to fix them.


#### Fire up your newly configured CFEngine server

The server is configured and ready to start. We will step through a couple one-time commands to get it going.

```
  # cp -fr /var/cfengine/masterfiles/* /var/cfengine/inputs/

  # /etc/init.d/cfengine3 start
```


**TIPS**

* Don't forget to poke a hole in your firewall (and/or router ACL), so that any agents you add can reach the CFEngine server.
* CFEngine server listens for TCP connections on port 5308.


#### Fire up an agent on the CFEngine server

Assuming you wish for the CFEngine server to manage itself (i.e. by running a CFEngine agent daemon, in addition to the server daemon), also run the following command.

```
  # cf-agent --bootstrap cfmaster.me.local
```

(Of course, replace `cfmaster.me.local` with your CFEngine server hostname. You are bootstrapping the server to itself.)


You now have both a CFEngine server and a CFEngine agent running on your server system.

* CFEngine server files live in /var/cfengine/masterfiles
* CFEngine agent files live in /var/cfengine/inputs

[Back to top of page.][Up and Running#Overview] 

## Install and configure CFEngine agent systems


#### Download and install


Download the latest CFEngine 3.5 Community Edition packages from: http://cfengine.com/community

On each of your agent systems (the systems you want managed by CFEngine), install the appropriate RHEL or Debian package using `rpm(8)`, `dpkg(1)`, or whatever method you prefer.


**Note:** The same package is used for both `server` and `agent` installs. Use the same CFEngine version on the agents that you installed on the server.


#### Start the agent
 

Getting the agent started is easy! We've already done most of the work on the server. The agent will get everything it needs from the server's `masterfiles`, and keep them locally in `/var/cfengine/inputs`. Run the following on the agent system:

```
  # cf-agent --bootstrap cfmaster.me.local
```

(Of course, replace `cfmaster.me.local` with your CFEngine `server` hostname.)

That's it! Your agent will soon begin executing the promises it receives from the server.

[Back to top of page.][Up and Running#Overview] 

## Dissect the "hello world" promise


Before continuing with further promise examples, let's back up a step and walk through notable lines in our first promise.

`a01SayHello.cf`

```cf3
bundle agent a01_say_hello                                     # <1>
{

methods:                                                       # <2>
    "a01sayhello" usebundle
                        => a01_run ;                           # <3>

}

bundle agent a01_run
{

vars:                                                          # <4>
    "myfile" string     => "/tmp/helloFromCfengine.txt" ;

files:                                                         # <5>
    "$(myfile)"                                                # <6>
    edit_line           => a01_edit,                           # <7>
    edit_defaults       => empty,                              # <8>
    perms               => mog("644","root","root"),           # <9>
    create              => "true",                             # <10>
    classes             => if_repaired("make_some_noise") ;    # <11>

reports:                                                       # <12>
    make_some_noise::                                          # <13>
    "Heads up - the $(this.promise_filename) promise ran." ;   # <14>

}


bundle edit_line a01_edit                                      # <15>
{

vars:
    "hello" string           =>                                # <16>
"If you are reading this, your promise worked on $(sys.fqhost)
Nice going!"

insert_lines:                                                  # <17>
    "$(hello)" ;

}
```

**Point by Point:**

<1> The `a01&#95;say&#95;hello` bundle is called by `promises.cf`, by way of the `z01PromiseSetup.cf` file we created. Recall that we specified `a01&#95;say&#95;hello` within the `z01&#95;promise&#95;setup` bundle.

<2> CFEngine bundles can have a `methods` section. It is used to call other bundles.

<3> Here we call the `a01_run` bundle, which is defined a few lines below.

<4> CFEngine bundles can have a `vars` section. It defines variables of type `string` or `slist` (roughly, string type and array type, respectively).

<5> CFEngine bundles can have a `files` section for specifying files and describing how they must be changed.

<6> The expanded value of `$(myfile)` is `/tmp/helloFromCfengine.txt`. This is the file we will be editing.

<7> The ```edit_line``` directive says to call bundle `a01_edit`.

<8> This directive says to empty the file before editing it.

<9> The `perms` directive sets the file (m)ode to 644, the file (o)wner to root, and the file (g)roup owner to root.

<10> This directive says to create the file if it does not already exist.

<11> This directive says to set a `class` called `make_some_noise` to the value true, _if_ CFEngine discovers that the file is not in the state it expected and therefore needs to edit it (either its content or its permissions). We will get to more examples of `classes` later, and they are further enumerated by URL references at the end of this primer.

<12> Remember when we set up a mailto address in the `controls/cf_execd.cf` server configuration? The `reports` section utilizes that address to send an email on anything we report about here. (It also logs a message, via syslog.)

<13> We are checking the `make&#95;some&#95;noise` class. If it's set to `true`, we generate the report (which gets emailed and logged). If it's set to `false`, we don't.

<14> This value is the message we report. The `$(this.promise&#95;filename)` is a special CFEngine variable. The `$(this)` variables are enumerated by a URL at the end of this primer.

<15> Another bundle, this time of type `edit&#95;line`.

<16> We define a variable, and assign it some text, including a special CFEngine variable called `$(sys.fqhost)`, which contains the system's fully-qualified hostname. The `$(sys)` variables are enumerated by a URL at the end of this primer.

<17> The `edit&#95;line` bundles can have an `insert&#95;lines` section. As you can probably guess, they insert into the file the text we specify.

[Back to top of page.][Up and Running#Overview] 



## Set up a global classes promise


To add flexibility to our promise files, we are going to set up a promise that provides `global` classes to our CFEngine environment. That means we can group hosts together arbitrarily, as needed.

Within `/var/cfengine/masterfiles/myPromises`, create the `z02GlobalClasses.cf` file.


`.z02GlobalClasses.cf`

```cf3
bundle common z02_global_classes
{

classes:

    # Define a single host using 'expression'.
    #
    "my_loghost" expression
                        => "zeus" ;

    # Define multiple hosts using 'or'.
    #
    "my_mongo_hosts" or => { 
                              "hypnos",
                              "athena",
                              "ares",
    } ;

    "my_web_hosts" or => { 
                              "pluto",
                              "nyx",
    } ;

}
```


#### Make CFEngine aware of the new promise


Update `/var/cfengine/masterfiles/myPromises/z01PromiseSetup.cf` as shown.

`.z01PromiseSetup.cf`

```cf3
bundle common z01_promise_setup
{
vars:
    "bundles" slist     => {
                             "z02_global_classes",
                             "a01_say_hello",
    } ;

    "promise_files" slist
                        => {
                             "myPromises/z02GlobalClasses.cf",
                             "myPromises/a01SayHello.cf",
    } ;

}
```

[Back to top of page.][Up and Running#Overview] 

## Add some more useful promises


Let's get serious now. You are probably loosely, incompletely familiar with the anatomy of a promise file at this point. If you think the way I do, you're ready for a lot more examples to pore over and learn from.

Read through the promise files in this section, and then create them as they're labeled here, all within `var/cfengine/masterfiles/myPromises` on your CFEngine server.


**Tip:** Leave the `/var/cfengine/masterfiles` directory alone on agent systems. Only the server uses `masterfiles`. Agents read and execute promises from `/var/cfengine/inputs`.



#### Install packages, based on OS


As always, create the new promise file in `/var/cfengine/masterfiles/myPromises`.

`.b01BaselinePackages.cf`

```cf3
bundle agent b01_baseline_packages
{

methods:
    redhat_6|debian_6|debian_7::                       # <1>
    "b01basepackages" usebundle
                        => b01_run ;

}

bundle agent b01_run
{

vars:

    redhat_6::
    "desired_packages" slist
                        => {
                             "nc",
                             "rcs",
                             "sysstat",
                             "dump",
    } ;

    debian_6|debian_7::
    "desired_packages" slist
                        => {
                             "ntp",
                             "netcat",
                             "tcpdump",
                             "rcs",
                             "sysstat",
                             "sudo",
                             "dump",
    } ;

packages:                                             # <2>

    redhat::                                          # <3>
    "$(desired_packages)"
    package_policy      => "add",
    package_method      => generic ;                  # <4>

    debian::                                          # <5>
    "$(desired_packages)"
    package_policy      => "add",
    package_method      => apt ;                      # <6>

}
```

**Point by Point:**

<1> Our next taste of CFEngine `classes`, and checking for true or false value. In this case, we are testing: Is this a RHEL 6 system, or a Debian 6 system, or a Debian 7 system? (The pipe '|' operator means OR in this context.) If it's one of those operating systems, we call the `b01_run` bundle.

<2> CFEngine bundles can have a `packages` section for managing packages.

<3> Another `class` test. This time, we are testing: Is this a RHEL system (of any major/minor version)? If so, we install the packages defined in `$(desired_packages)`.

<4> This directive chooses a suitable package installation method for us. Don't worry about it until you are ready to dig deeper into CFEngine.

<5> Another `class` test. Is this a Debian system (of any major/minor version)? If so, install the packages.

<6> This directive says to use `apt(8)`.


#### Make CFEngine aware of the new promise

Update `/var/cfengine/masterfiles/myPromises/z01PromiseSetup.cf` as shown.

`.z01PromiseSetup.cf`

```cf3
bundle common z01_promise_setup
{
vars:
    "bundles" slist     => {
                             "z02_global_classes",
                             "a01_say_hello",
                             "b01_baseline_packages",
    } ;

    "promise_files" slist
                        => {
                             "myPromises/z02GlobalClasses.cf",
                             "myPromises/a01SayHello.cf",
                             "myPromises/b01BaselinePackages.cf",
    } ;

}
```

#### Manage a config file, based on a template


Before creating this next promise in `/var/cfengine/masterfiles/myPromises`, create a `/var/cfengine/masterfiles/myTemplates/motd.txt` file, with the text `Hey, this is a template` inside.

`.b21ManageConfig.cf`

```cf3
bundle agent b21_manage_config
{

methods:
    my_mongo_hosts::                                              # <1>
    "b21manageconf" usebundle
                        => b21_run ;

}

bundle agent b21_run
{

vars:

    "source_dir" string
                        => "/var/cfengine/inputs/myTemplates" ;   # <2>

    "source_file" string
                        => "$(source_dir)/motd.txt" ;


files:

    "/tmp/motd"
    perms               => mog("640","root","root"),
    create              => "true",
    edit_defaults       => empty,
    edit_line           => expand_template("$(source_file)") ;    # <3>

}
```

**Point by Point:**

<1> This test utilizes the `my_mongo_hosts` class, which we defined earlier in `z02GlobalClasses.cf`.

<2> Notice how we have specified a path under the `inputs` directory? This is because agents use the `/var/cfengine/inputs` directory, NOT `/var/cfengine/masterfiles`!

<3> Here is something new and significant. This is how we are going to manage almost all configuration files in this primer. We create a template within `myTemplates`, and we use the `edit&#95;line` and `expand&#95;template` directive to populate it on agent systems. In this case, `/var/cfengine/inputs/myTemplates/motd.txt` will be created as `/tmp/motd` on agent systems.


**Remember:** We create CFEngine server promise files within `/var/cfengine/masterfiles`. The CFEngine agents consume those files within `/var/cfengine/inputs`.

#### Make CFEngine aware of the new promise


Update `/var/cfengine/masterfiles/myPromises/z01PromiseSetup.cf` as shown.

`.z01PromiseSetup.cf`

```cf3
bundle common z01_promise_setup
{
vars:
    "bundles" slist     => {
                             "z02_global_classes",
                             "a01_say_hello",
                             "b01_baseline_packages",
                             "b21_manage_config",
    } ;

    "promise_files" slist
                        => {
                             "myPromises/z02GlobalClasses.cf",
                             "myPromises/a01SayHello.cf",
                             "myPromises/b01BaselinePackages.cf",
                             "myPromises/b21ManageConfig.cf",
    } ;

}
```


You understand how we're using `z01PromiseSetup.cf` now, right? For every promise we want to make CFEngine aware of, we need to:

* Add the bundle name to the `bundles` slist.
* Add the promise file name to the `promise_files` slist.


#### Manage a config file, on a per-host basis


Before creating this next promise in `/var/cfengine/masterfiles/myPromises`, create a `/var/cfengine/masterfiles/myTemplates/motd.HOSTNAME.txt` file, with the text `Hey, this is a per-host template` inside.

Replace `HOSTNAME` in the file path with your agent's unqualified hostname. (So `pluto.me.local` has an unqualified hostname of `pluto`.)

`.b22ManageConfigByHostname.cf`


```cf3
bundle agent b22_manage_config_by_hostname
{

methods:
    my_mongo_hosts::
    "b22manageconfbyhost" usebundle
                        => b22_run ;

}

bundle agent b22_run
{

vars:

    "source_dir" string
                        => "/var/cfengine/inputs/myTemplates" ;

    "source_file" string
       => "$(source_dir}/motd.$(sys.uqhost).txt" ;		        # <1>


files:

    "/tmp/motd_again"
    perms               => mog("640","root","root"),
    create              => "true",
    edit_defaults       => empty,
    edit_line           => expand_template("$(source_file)") ;

}
```

**Point by Point:**

<1> Another special CFEngine variable example. The `$(sys.uqhost)` variable expands to the agent's unqualified hostname. This is a good strategy for customizing configurations on a per-host basis. For instance, the `iris.me.local` host (unqualified name `iris`) would look for the file `/var/cfengine/inputs/myTemplates/motd.iris.txt`.

**Note:** Update `myPromises/z01PromiseSetup.cf` to include this promise.


#### Manage a config file, and restart a service


As always, create the new promise file in `/var/cfengine/masterfiles/myPromises`.


`.b23ManageConfigAndServiceRestart.cf`

```cf3
bundle agent b23_manage_config_and_restart_service
{

methods:
    my_mongo_hosts::
    "b23manageconfrestart" usebundle
                        => b23_run ;

}

bundle agent b23_run
{

vars:

    "source_dir" string
                        => "/var/cfengine/inputs/myTemplates" ;

    "source_file" string
                        => "$(source_dir}/baz_service.txt" ;        # <1>


files:

   "/etc/baz/."                                                     # <2>
    handle              => "b23_create_bazdir",                     # <3>
    create              => "true",
    perms               => mog("0750","root","bazgroup") ;

    "/etc/baz/main.conf"
    depends_on          => { "b23_create_bazdir" },                 # <4>
    perms               => mog("640","root","bazgroup"),
    create              => "true",
    edit_defaults       => empty,
    edit_line           => expand_template("$(source_file)"),       # <5>
    classes		 => if_repaired("restart_baz_service") ;

commands:                                                           # <6>

    restart_baz_service::
    "/etc/init.d/baz restart" ;

reports:

    restart_baz_service::
    "baz was configured and restarted" ;

}
```

**Point by Point:**

<1> The config file template. Again, notice that it's looking in the `inputs` directory, because that is where agents look!

<2> Directories need a dot (.) at the end. They just do.

<3> The `handle` directive is used to identify this part of the promise to later parts of the promise. We can handle flow control this way.

<4> The `depends&#95;on` directive works hand-in-hand with the earlier `handle` directive. It means that this part of the promise will only run if `b23&#95;create&#95;bazdir` has already successfully completed. The convergent nature of CFEngine means this may take several passes of the promise file for it to complete.

<5> Our `edit&#95;line` and `expand&#95;template` combo again. Manage your config files this way. It is reliable and easy to understand from a sysadmin perspective.

<6> CFEngine bundles can have a `commands` section which can issue commands directly to the system's shell. In CFEngine culture, these are to be used sparingly. But a service restart is a good candidate for appropriate use.


**Note:** Update `myPromises/z01PromiseSetup.cf` to include this promise.

#### Add a group to /etc/group


As always, create the new promise file in `/var/cfengine/masterfiles/myPromises`.

`.b31AddGroup.cf`

```cf3
bundle agent b31_add_group
{

methods:
    debian.my_mongo_hosts::                             # <1>
    "b31addgroup" usebundle
                        => b31_run ;

}

bundle agent b31_run
{

vars:

    "group[dbas]" string                                # <2>
                        => "dbas:x:15101:" ;            # <3>

    "group[nodedevs]" string
                        => "devs:x:16101:" ;            # <4>


files:

    "/etc/group"
    edit_line
      => append_groups_starting("b31_run.group") ;      # <5>

}
```

**Point by Point:**

<1> Another nice `classes` example. Here, we are testing whether the agent system is a Debian (of any version) OS, and is also in the `my&#95;mongo&#95;hosts` class we defined in `z02GlobalClasses.cf`. The dot '.' operator means AND in this context.

<2> This is a different type of variable naming than we are accustomed to seeing. Suffice it to say, it allows us to add multiple name/value pairs to the `$(group)` variable. It acts like an associative array, or hash.

<3> This string of text is formatted exactly the way we want it to appear in `/etc/group`.

<4> Another string of text we want to appear in `/etc/group`.

<5> Insert the group[] entries into `/etc/group`.


**Tip:** We specify `b31&#95;run.group`, and not `$(b31&#95;run.group)`. That's not a typo; it's just the way we qualify this type of variable. Try to not think about it too hard (until you are ready to dig deeper into CFEngine).


**Note:** Update `myPromises/z01PromiseSetup.cf` to include this promise.


#### Add a shell user

As always, create the new promise file in `/var/cfengine/masterfiles/myPromises`.

`.b32AddShellUser.cf`

```cf3
bundle agent b32_add_shell_user
{

methods:
    nyx|iris|pluto::                                             # <1>
    "b32addshelluser" usebundle
                        => b32_run ;

}

bundle agent b32_run
{

vars:

    "pwd[qing]" string
       => "qing:x:18055:15101::/home/qing:/bin/bash" ;           # <2>

    "pwd[liu]" string
       => "liu:x:18056:15101::/home/liu:/bin/bash" ;

    # --------

    "shadow[qing]" string
       => "qing:$6$VyKJ5BZv$bfOvuqigJEB:15904:0:99999:7:::" ;    # <3>

    "shadow[liu]" string
       => "liu:$6$kNtT24lu$RtfPROpqbaw:15904:0:99999:7:::" ;

files:

    "/home/qing/."
    create              => "true",
    perms               => mog("0755","18055","15101") ;

    "/home/liu/."
    create              => "true",
    perms               => mog("0755","18056","15101") ;

    "/etc/shadow"
    handle              => "b32_create_shadow_entry",            # <4>
    edit_line
      => append_users_starting("b32_run.shadow") ;               # <5>

    "/etc/passwd"
    depends_on      => { "b32_create_shadow_entry" },            # <6>
    edit_line       => append_users_starting("b32_run.pwd") ;    # <7>

}
```

**Point by Point:**

<1> Another classes example. This is testing the unqualified hostname, and evaluating to true if hostname is `iris` or `nyx` or `pluto`.

<2> A string that's formatted exactly the way we want it to appear in `/etc/passwd`.

<3> A string that's formatted the way we want it to appear in `/etc/shadow`. (The salted password digest has been truncated for the sake of brevity!)

<4> Another handle example. It will allow this part of the promise to be identified by later promise parts that run.

<5> Insert the shadow[] entries into `/etc/shadow`.

<6> Only run this part of the promise after `b32&#95;create&#95;shadow&#95;entry` has already completed.

<7> Insert pwd[] entries into `/etc/passwd`.


**Note:** Update `myPromises/z01PromiseSetup.cf` to include this promise.



#### Report on existence of files and users


As always, create the new promise file in `/var/cfengine/masterfiles/myPromises`.

`.b41ReportOnExistence.cf`

```cf3
bundle agent b41_report_on_existence
{

methods:

    (my_mongo_hosts|my_web_hosts).!debian::                       # <1>
    "b41report" usebundle
                        => b41_run ;

}

bundle agent b41_run
{

vars:

    "important_dir" string
                        => "/usr/local/etc/my_stuff" ;

    "annoying_file" string
                        => "/tmp/large_nonsense_data" ;

    "banned_user" string
                        => "george" ;

classes:

    "dir_test01" expression
                        => fileexists("$(important_dir)/.") ;     # <2>

    "file_test01" expression
                        => fileexists("$(annoying_file)") ;

    "user_test01" expression
                        => userexists("$(banned_user)") ;         # <3>

reports:

    !dir_test01::                                                 # <4>
    "$(important_dir) does not exist on $(sys.fqhost)!" ;

    file_test01::
    "Please clean up $(file_test01)" ;

    user_test01::
    "$(banned_user) needs to be removed from $(sys.fqhost)" ;

}
```

**Point by Point:**

<1> A more advances `classes` test from which to learn. In this case, we logically group '()' two classes together, and utilize the negation '!' operator. So, if the agent is in our defined `my&#95;mongo&#95;hosts` OR in our defined `my&#95;web&#95;hosts` AND it's not a Debian host, it evaluates to true, and we run the `b41&#95;run` bundle.

<2> The `fileexists()` function, as you can probably deduce, checks for the presence of a file on the filesystem. There are a number of CFEngine built-in functions which are enumerated in a URL in this primer's appendix.

<3> Another function. This one tests for the existence of a shell user.

<4> Another example of using a negation operator on a class. If `dir_test01` is false, then we run this report.

**Note:** Update `myPromises/z01PromiseSetup.cf` to include this promise.

[Back to top of page.][Up and Running#Overview] 

## Commands for controlling CFEngine


### Useful server commands


So you've just updated your promises, and you want to make them immediately available to your agents? (In your test environment. Because we test before deploying anywhere important.) You can wait for CFEngine to run through its normal procedures (in which case it can take five, ten, or fifteen minutes before the agents execute the promises, for reasons beyond the scope of this primer). Or you can speed things up a bit.

#### Validate your promise changes

```
  # cf-promises -f /var/cfengine/masterfiles/promises.cf
```

If there is a syntactical problem with your promises, CFEngine will complain here and point you to a file and line number. Do not proceed until you've fixed any problems.

#### Update what's available for your agents to pull

```
  # cf-agent -IKf /var/cfengine/masterfiles/update.cf
```

That's that. Now observe one of your agents, or speed things up there too..


### Useful agent commands


#### Immediately pull the latest promise updates from the server

```
  # cf-agent -IKf /var/cfengine/inputs/update.cf
```

Remember, this is only if you wish to speed things up and not wait for CFEngine to take care of it naturally via its daemon processes. Notice how we are using the `inputs` directory here. Agents care only about `inputs`, not `masterfiles`.

#### Immediately execute promises

```
  # cf-agent -IKf /var/cfengine/inputs/promises.cf
```

That's that.


### More useful agent commands


#### Query the status of a single promise bundle

```
  # cf-agent -vnb *b21_manage_config*
```

#### Print the percentage of promises currently kept

```
  # cf-agent -vn
```

The percentage of currently-kept promises gives us the percentage of promises that have successfully executed, the percentage that will be fixed on the next CFEngine run, and the percentage that were unable to execute. (You may be able to drill down on details by carefully reviewing the output from this command.)

#### Print only promises that are currently unable to execute

```
  # cf-agent -n
```

[Back to top of page.][Up and Running#Overview] 

***


License
--------
**Get Up and Running Quickly with CFEngine 3.5 Community Edition** by Erik Schwartz is licensed under a http://creativecommons.org/licenses/by-sa/3.0/.
