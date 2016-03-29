---
layout: default
title: Command Line Sketches
published: true
sorting: 30
tags: [design center, cf-sketch, sketches]
---

The CFEngine Design Center is a repository of pre-made components
called **sketches** that allow you to use the full power of CFEngine
without having to learn the CFEngine policy language. Although
sketches are themselves written in the CFEngine policy language, you
can make use of them by simply installing them, configuring them using
the appropriate parameters, and deploying them on your
infrastructure. For users of the Community edition of CFEngine, this can be easily done
using both a command-line interface called `cf-sketch`.

Please note that CFEngine Enterprise comes with the **Design Center App** to make the work below effortless.

## Overview ##

This page provides instructions on how a Design Center sketch can be
found, installed, configured, and executed as policy, using
command-line tools with CFEngine community. The overview is as follows:

**Before you Begin**

[Requirements][Command Line Sketches#Requirements]

[Basic Concepts][Command Line Sketches#Basic Concepts]

**Instructions**

[Step 1. Check out the Design Center repository][Command Line Sketches#Step 1. Check out the Design Center repository]

[Step 2. Run cf-sketch][Command Line Sketches#Step 2. Run cf-sketch]

[Step 3. Search for sketches][Command Line Sketches#Step 3. Search for sketches]

[Step 4. Install a sketch][Command Line Sketches#Step 4. Install a sketch]

[Step 5. Activate a sketch][Command Line Sketches#Step 5. Activate a sketch]  Define the parameter set and environment, and run the activate command.

[Step 6. Deploy the sketch][Command Line Sketches#Step 6. Deploy the sketch: Generate and execute the runfile]  Generate and execute the runfile.

Additional resources are included at the end of this page.

## Before you Begin ##

Complete the software requirements and review the basic concepts of sketches
before you begin the instructions:

### Requirements ###

To follow these instructions, you will need the following:

- A Unix-like system
- The following programs installed (all of these are either included
  or easily available in the package repositories for most operating system):
  - [Git](http://git-scm.com/downloads), for checking out the Design
    Center repository
  - [Perl](http://www.perl.org/get.html), the Design Center tools are
    written in Perl
  - [Curl](http://curl.haxx.se), used by `cf-sketch` to fetch remote
    files when needed.
- CFEngine Community 3.5.0 or newer, or CFEngine Enterprise 3.5.0 or
  newer. Many of the components will work with CFEngine Community
  3.4.0 or later (Enterprise 3.0.0 or later), but you need 3.5.0 to
  have access to the full range of features and sketches.
- Optional but recommended: the `Term::ReadLine::Gnu` Perl module. On
  many systems it is available in the standard package repositories
  (for example, on Ubuntu Linux you can install it using `apt-get
  install libterm-readline-gnu-perl`). You can also install it using
  the `cpan` utility included with Perl.

### Basic Concepts ###

The following concepts provide a better understanding of how
the Design Center works. The Design Center framework contains the following:

- **Sketches** contain the code that is executed by CFEngine to
   perform some task. Sketches are contributed by the CFEngine
   community and hosted in the Design Center repositories. Most
   sketches take a few parameters to configure their precise
   behavior. For example, the `System::tzconfig` sketch contains the
   code to update the appropriate files in the system to set the
   correct timezone.
- **Parameter sets** contain the parameters that tell a CFEngine sketch
   the details of what to do. For example, the `System::tzconfig`
   sketch takes a parameter that tells it which timezone should be set in
   the system. The Design Center framework can store several parameter
   sets (each one identified by a name) for the same sketch, and from
   which you can choose to apply according to arbitrary circumstances.
- **Environments** contain conditions, expressed as
   [CFEngine Class Expressions](https://github.com/cfengine/documentation/blob/master/manuals/language-concepts/classes.markdown),
   that indicate when and where a particular sketch will be executed
   with a particular set of parameters. Environments also contain
   expressions that determine when and where test and verbose modes
   will be enabled for a sketch. The Design Center can also store
   multiple named environment definitions, which you can combine in
   arbitrary ways to fine tune the execution of each sketch on each
   machine.

Sketches, Parameters and Environments, by themselves, do nothing. They
have to be combined into **Activations**:

An **activation** is a combination of a sketch, a parameter set, and an
environment (all three specified by name) that defines which sketches
must be executed under which conditions, and with which parameters. It is
only through activations that you put sketches to work and make the
decisions as to how different parts of your infrastructure will be
configured. For example, you can have two different parameter sets
for the `System::tzconfig` sketch, one for Linux and another one for
Solaris machines. You can then, on the central CFEngine Policy
Server, create two activations:

- Activation #1: Sketch `System::tzconfig`, parameter set
`tzconfig-linux`, Environment `linux`
- Activation #2: Sketch `System::tzconfig`, parameter set
  `tzconfig-solaris`, Environment `solaris`

When these activations are distributed by the policy server to all the
clients, only Linux and Solaris machines will execute the
`System::tzconfig` sketch, and each one of them will apply the
appropriate parameters.

Other concepts exist that can make your use of the Design
Center even more powerful, but these are enough to get you started and
to be able to follow these instructions.

## Instructions ##

### Step 1. Check out the Design Center repository ###

The Design Center is an open source project and is hosted on
GitHub. Access the repository at
https://github.com/cfengine/design-center.

The best way to get the Design Center at the moment is to check out
its git repository. For these instructions, we check it out
under the `$HOME/source/` directory (you can use any location you
want, just replace it throughout the following instructions):

    mkdir $HOME/source
    cd $HOME/source
    git clone https://github.com/cfengine/design-center.git

A directory called `design-center` is created.  We
call this the **CHECKOUT** directory and henceforth refer to it as
`$CHECKOUT`. In the examples that follow, **CHECKOUT** is
`$HOME/source/design-center`. You can save some typing by typing

    export CHECKOUT=$HOME/source/design-center

at the prompt.  From that point on, all command-line interaction can
use `$CHECKOUT` and it will expand to the installation directory.

### Step 2. Run cf-sketch ###

You can run cf-sketch in interactive mode directly from its directory
under `$CHECKOUT`:

    cd $CHECKOUT/tools/cf-sketch
    ./cf-sketch.pl
    Welcome to cf-sketch version 3.5.0b1.
    CFEngine AS, 2013.

    Enter any command to cf-sketch, use 'help' for help, or 'quit' or '^D' to quit.

    cf-sketch> _

By default, `cf-sketch` provides an interactive prompt where you can
type the commands you want to execute. Type `help` at the prompt
to see the descriptions of all the available commands. You can run
commands non-interactively by passing them as arguments to the
`cf-sketch.pl` script from the command line.

### Step 3. Search for sketches ###

The first step is to find some sketches to install on your system. The
search command provides, without any parameters, a list of all
available sketches:

    cf-sketch> search

    The following sketches are available:

    Applications::Memcached Sketch for installing, configuring, and starting memcached.
    ...
    Yale::stdlib Yale standard library

This is useful for exploration, but might be too much information. You
can also provide a regular expression to search for a particular set
of sketches:

    cf-sketch> search system

    The following sketches match your query:

    System::Logrotate Sets defaults and user permissions in the sudoers file
    System::Routes Sets defaults and user permissions in the sudoers file
    System::Sudoers Sets defaults and user permissions in the sudoers file
    System::Syslog Configures syslog
    System::access Manage access.conf values
    System::config_resolver Configure DNS resolver
    System::cron Manage crontab and /etc/cron.d contents
    System::etc_hosts Manage /etc/hosts
    System::motd Configure the Message of the Day
    System::set_hostname Set system hostname. Domain name is also set on Mac, Red Hat and and Gentoo derived distributions (but not Debian).
    System::sysctl Manage sysctl values
    System::tzconfig Manage system timezone configuration

Use the `info` command to get additional information for a sketch, including details
about its parameters:

    cf-sketch> info -v System::motd

    The following sketches match your query:

    Sketch System::motd
    Description: Configure the Message of the Day
    Authors: Ben Heilman <bheilman@enova.com>
    Version: 1.00
    License: MIT
    Tags: cfdc
    Installed: No
    Parameters:
      For bundle entry
        motd: string
        motd_path: string
        prepend_command: string
        dynamic_path: string
        symlink_path: string

### Step 4. Install a sketch ###

The first step in using a sketch is to install it. As an example, install
the `System::motd` sketch:

    cf-sketch> install System::motd

    Sketch System::motd installed under /home/vagrant/.cfagent/inputs/sketches.
    Sketch README.md installed under System::motd.
    Sketch main.cf installed under System::motd.
    Sketch params/debian_squeeze.json installed under System::motd.
    Sketch params/debian_wheezy.json installed under System::motd.
    Sketch params/example.json installed under System::motd.
    Sketch params/simple.json installed under System::motd.
    Sketch test.cf installed under System::motd.

Verify that the sketch has been installed using the `list` command:

    cf-sketch> list

    The following sketches are installed:

    CFEngine::dclib Design Center standard library
    CFEngine::stdlib The portions of the CFEngine standard library (also known as COPBL) that are compatible with 3.4.0 releases
    System::motd Configure the Message of the Day

Note that the `CFEngine::dclib` and `CFEngine::stdlib` are
automatically installed as dependencies of the `System::motd` sketch.

### Step 5. Activate a sketch ###

Activating sketches includes adding two elements: a parameter set and an environment.

#### Define the parameter set ####

Define the parameter set that contains the values that will
be used by the `System::motd` sketch:

    cf-sketch> define params System::motd

    Please enter a name for the new parameter set (default: System::motd-entry-000): motd_params
    Querying configuration for parameter set 'motd_params' for bundle 'entry'.
    Please enter parameter motd (Message of the Day (aka motd)).
      (enter STOP to cancel)
    motd : Hello there!
    Please enter parameter motd_path (Location of the primary, often only, MotD file).
      (enter STOP to cancel)
    motd_path [/etc/motd]: /etc/motd
    Please enter parameter prepend_command (Command output to prepend to MotD).
      (enter STOP to cancel)
    prepend_command [/bin/uname -snrvm]: /bin/uname -snrvm
    Please enter parameter dynamic_path (Location of the dynamic part of the MotD file).
      (enter STOP to cancel)
    dynamic_path :
    Please enter parameter symlink_path (Location of the symlink to the motd file).
      (enter STOP to cancel)
    symlink_path :
    Defining parameter set 'motd_params' with the entered data.
    Parameter set motd_params successfully defined.

Confirm that the parameter set has been properly defined using
the `list` command:

    cf-sketch> list -v params

    The following parameter sets are defined:

    motd_params: Sketch System::motd
      [System::motd][dynamic_path]:
      [System::motd][motd]: Hello there!
      [System::motd][motd_path]: /etc/motd
      [System::motd][prepend_command]: /bin/uname -snrvm
      [System::motd][symlink_path]:

#### Define an environment ####

For this example, define an
environment that is always active:

    cf-sketch> define environment -n walkthrough any

    Environment 'walkthrough' successfully defined.

Use the `list` command to verify that the environment was
defined:

    cf-sketch> list -v env walk

    The following environments match your query:

    walkthrough
      [activated]: any
      [test]: !any
      [verbose]: !any

Note that the `test` and `verbose` fields are optional and default to
`!any`, which is equivalent to "never" in CFEngine terms.

#### Run the activate command ####

Activate the sketch by tying together the sketch
name, parameter set, and environment:

    cf-sketch> activate System::motd motd_params walkthrough

    Using generated activation ID 'System::motd-1'.
    Using existing parameter definition 'motd_params'.
    Using existing environment 'walkthrough'.
    Activating sketch System::motd with parameters motd_params.

Verify that the activation has been created:

    cf-sketch> list activations

    The following activations are defined:

    Activation ID System::motd-1
      Sketch: System::motd
      Parameter sets: [ motd_params ]
      Environment:  'walkthrough'

This means that when the sketches are deployed, the `System::motd`
sketch will be executed with the values defined in the
`motd_params` parameter set, and on the hosts that satisfy the
conditions defined in the `walkthrough` environment (which includes
all machines for now).

### Step 6. Deploy the sketch: Generate and execute the runfile ###

So far all the definitions of parameters, environments, and activations
are known only to the `cf-sketch` tool. You must deploy these
changes, which creates the appropriate CFEngine policy files for
executing the activated sketches. We have two commands for this:

The `run` command allows you to quickly test the execution of the
sketches on the local host. It generates a standalone runfile that
encodes all the necessary information for the activated sketches, and
then executes it using `cf-agent`:

    cf-sketch> run

    Runfile /var/cfengine/inputs/api-runfile-standalone.cf successfully generated.
    Now executing the runfile with: /var/cfengine/bin/cf-agent  -f /var/cfengine/inputs/api-runfile-standalone.cf

The `deploy` command generates a non-standalone runfile that is meant
to be loaded and executed from your main `promises.cf` file:

    cf-sketch> deploy

    Runfile /var/cfengine/inputs/api-runfile.cf successfully generated.

## More information ##

The Design Center framework provides an API that takes care of
managing all the backend framework, and cf-sketch offers an "expert"
mode in addition to the interactive mode described in these
instructions.

* Once you are familiar with the basic concepts and want to
learn more about how things work internally, visit
the [advanced discussion][Advanced Walkthrough] on configuring sketches.

* Visit the [Design Center API][The Design Center API] for reference.

* Once you are ready to start [writing Design Center sketches][Write a new Sketch], refer to the
[sketch structure][Sketch Structure] documentation.
