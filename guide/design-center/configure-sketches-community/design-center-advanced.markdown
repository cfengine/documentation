---
layout: default
title: Advanced Walkthrough
published: false
sorting: 10
tags: [design center, walkthrough, cf-sketch, sketches]
---

This walkthrough illustrates how a Design Center sketch can be found,
installed, configured, and executed as policy. Many items are already discussed at
[Command Line Sketches][Command Line Sketches].
This Walkthrough provides a more advanced look at sketches in that it describes internal and backend processes.

Please note the following instructions will work with CFEngine Enterprise as well, but the Mission Portal **Design Center App** is a better user interface for most of the topics covered here.

## Before you Begin

Make certain you have installed all necessary software and have checked out the Design Center repository:

[Complete the software requirements][Command Line Sketches#Requirements]

[Review the basics concepts of sketches][Command Line Sketches#Basic Concepts]

[Check out the Design Center repository][Command Line Sketches#Step 1. Check out the Design Center repository]

## Overview

The following topics are discussed in this Walkthrough:

[Prepare the config.json file][Advanced Walkthrough#Prepare the config.json file]

[Search for sketches][Advanced Walkthrough#Search for sketches]

* Search for sketches with the Design Center API
* Search for sketches with cf-sketch in expert mode
* Search for sketches with cf-sketch in interactive mode

[Install a sketch][Advanced Walkthrough#Install a sketch]

* Install a sketch with the Design Center API
* Install a sketch with cf-sketch in expert mode
* Install a sketch with cf-sketch in interactive mode

[Activate a sketch][Advanced Walkthrough#Activate a sketch]

* Activate a sketch with the Design Center API
* Activate a sketch with cf-sketch in expert mode
* Activate a sketch with cf-sketch in interactive mode

[Generate and execute the runfile][Advanced Walkthrough#Generate and execute the runfile]

* Generate and execute the runfile with the Design Center API
* Generate and execute the runfile with cf-sketch in expert mode
* Generate and execute the runfile with cf-sketch in interactive mode

### Prepare the config.json file

To interact with the Design Center, you must tell its API where things
are installed. Copy the `config.json` file to your CFEngine personal
directory:

    mkdir ~/.cfagent
    cp $CHECKOUT/tools/cf-sketch/config.json ~/.cfagent/dc-api-config.json

**Note:** A `config-root.json` file exists that is intended for privileged
(root) usage.  It sets things up under `/var/cfengine` but still
expects the checkout under `~/source/design-center`.

Open the config.json file. It contains the following JSON data:

```
{
 log: "STDERR",
 log_level: 4,
 repolist: [ "~/.cfagent/inputs/sketches" ],
 recognized_sources: [ "~/source/design-center/sketches" ],
 runfile: { location: "~/.cfagent/inputs/api-runfile.cf", standalone: true, relocate_path: "sketches", filter_inputs: [] },
 vardata: "~/.cfagent/vardata.conf",
}
```

You can change any setting you want but keeping the default values is recommended.

The paths you see are all relative to your home directory. The `log`
can be set to a file.  The `log_level` can be lowered to 1 if you want
less noise (the level is set to 4 in this example).

`vardata`: is where the Design Center API stores all configurations.

`runfile`: describes where the Design Center API will save an
executable policy with all the sketches you have installed and
activated.

`repolist`: is where sketches will be **installed**.

`recognized_sources`: is where sketches will be **found**. It can be
a URL such as
`https://github.com/cfengine/design-center/blob/master/sketches/cfsketches.json`.

You can save some typing by entering

    export DCJ=~/.cfagent/dc-api-config.json

at the prompt. From that point on, all command-line interaction can
use `$DCJ` and it will expand to the filename above.

From this point on, refer to this command

    $CHECKOUT/tools/cf-sketch/cf-dc-api.pl

as `$CFAPI` for brevity.

You can save some typing by entering

    export CFAPI=$CHECKOUT/tools/cf-sketch/cf-dc-api.pl

at the prompt.  From that point on, all command-line interaction can
use `$CFAPI` and it will expand to the command above.

### Search for sketches

This section explains many details
that the later sections in the Walkthrough will skip for brevity.

#### Search for sketches with the Design Center API

This is what all the other Design Center tools use. You do not need to
know this protocol or know that it is used.

	echo '{ dc_api_version: "3.6.0", request: {search: true } }' | $CFAPI $DCJ

If you get errors here, you might be missing Perl modules or the
CFEngine agent. Look at the [Design Center Wiki](https://github.com/cfengine/design-center/wiki)
for possible solutions to your problem.

Output:

```
DCAPI::log3(DCAPI.pm:173): Successfully loaded vardata file /home/tzz/.cfagent/vardata.conf
DCAPI::log(DCAPI.pm:376): Searching location ~/source/design-center/sketches for terms true
DCAPI::Sketch::matches(Repo.pm:118): sketch Applications::Memcached matched terms true
...
DCAPI::Sketch::matches(Repo.pm:118): sketch Webserver::Install matched terms true
```

All of the above is debugging output.  With `log` set to a file name,
the output will go to that file.  With `log_level` set to 1, only the
essential errors will be shown. The actual API response is:

```
{
  "api_ok":
  {
    "warnings":[],"success":true,"errors":[],"error_tags":{},
    "data":
    {
        "search":
        {
            "/home/tzz/source/design-center/sketches":
            {
              "System::config_resolver":"System::config_resolver", ... ,"System::set_hostname":"System::set_hostname"
            }
        }
    },
    "log":[],"tags":{}
  }
}
```

The response says (with many sketch names omitted for brevity): Here, these are all my sketches.

Note that this is not what you would use daily.

#### Search for sketches with `cf-sketch` in expert mode

    $CHECKOUT/tools/cf-sketch/cf-sketch.pl --expert --cfpath=/var/cfengine/bin --apiconfig $DCJ --search | sort

Output:

```
Applications::Memcached Sketch for installing, configuring, and starting memcached.
...
```

You piped the command above through the standard `sort` command to
sort the results. You can omit the `sort`.

#### Search for sketches with `cf-sketch` in interactive mode

Run:

    $CHECKOUT/tools/cf-sketch/cf-sketch.pl --apiconfig $DCJ

You'll see this prompt, or something like it:

```
Welcome to cf-sketch version 3.6.0.
CFEngine AS, 2013.

Enter any command to cf-sketch, use 'help' for help, or 'quit' or '^D' to quit.

cf-sketch>

```

Now enter the `search` command:

```
cf-sketch> search

The following sketches are available:

Applications::Memcached Sketch for installing, configuring, and starting memcached.
...
Yale::stdlib Yale standard library

cf-sketch>
```

This is the easiest method but you might want the expert or direct API
interaction for specific purposes.  All three are shown throughout this Walkthrough.

### Install a sketch

#### Install a sketch with the Design Center API

    echo '{ dc_api_version: "3.6.0", request: {install: {sketch:"System::motd", force:true} } }' | $CFAPI $DCJ

The `force` parameter tells the Design Center API to overwrite the
sketch even if it is installed already.

Output:

```
DCAPI::log3(DCAPI.pm:173): Successfully loaded vardata file /home/tzz/.cfagent/vardata.conf
...
DCAPI::log(DCAPI.pm:576): Installing sketch: {"source":["~/source/design-center/sketches"],"target":"~/.cfagent/inputs/sketches","sketch":"System::motd","force":true}
DCAPI::log4(Repo.pm:179): Installing sketch System::motd: copying /home/tzz/source/design-center/sketches/system/motd/README.md to /home/tzz/.cfagent/inputs/sketches/system/motd/README.md
DCAPI::log4(Repo.pm:179): Installing sketch System::motd: copying /home/tzz/source/design-center/sketches/system/motd/main.cf to /home/tzz/.cfagent/inputs/sketches/system/motd/main.cf
DCAPI::log4(Repo.pm:179): Installing sketch System::motd: copying /home/tzz/source/design-center/sketches/system/motd/params/debian_squeeze.json to /home/tzz/.cfagent/inputs/sketches/system/motd/params/debian_squeeze.json
DCAPI::log4(Repo.pm:179): Installing sketch System::motd: copying /home/tzz/source/design-center/sketches/system/motd/params/debian_wheezy.json to /home/tzz/.cfagent/inputs/sketches/system/motd/params/debian_wheezy.json
DCAPI::log4(Repo.pm:179): Installing sketch System::motd: copying /home/tzz/source/design-center/sketches/system/motd/params/example.json to /home/tzz/.cfagent/inputs/sketches/system/motd/params/example.json
DCAPI::log4(Repo.pm:179): Installing sketch System::motd: copying /home/tzz/source/design-center/sketches/system/motd/params/simple.json to /home/tzz/.cfagent/inputs/sketches/system/motd/params/simple.json
DCAPI::log4(Repo.pm:179): Installing sketch System::motd: copying /home/tzz/source/design-center/sketches/system/motd/test.cf to /home/tzz/.cfagent/inputs/sketches/system/motd/test.cf
```

After lots of activity (again, remember to drop down to `log_level` 1 or 0 if you want to skip all these messages) the sketch is installed.

Finally the API returns:

```
{
  "api_ok":
  {
    "warnings":[],"success":true,"errors":[],"error_tags":{},
    "data":
    {
        "install":
        {
          "System::motd":
          {
            "test.cf":"/home/tzz/.cfagent/inputs/sketches/system/motd/test.cf",
            "params/debian_squeeze.json":"/home/tzz/.cfagent/inputs/sketches/system/motd/params/debian_squeeze.json",
            "README.md":"/home/tzz/.cfagent/inputs/sketches/system/motd/README.md",
            "params/example.json":"/home/tzz/.cfagent/inputs/sketches/system/motd/params/example.json",
            "params/debian_wheezy.json":"/home/tzz/.cfagent/inputs/sketches/system/motd/params/debian_wheezy.json",
            "main.cf":"/home/tzz/.cfagent/inputs/sketches/system/motd/main.cf",
            "params/simple.json":"/home/tzz/.cfagent/inputs/sketches/system/motd/params/simple.json"
          },
          "~/.cfagent/inputs/sketches":{"System::motd":1}
        },
        "inventory_save":1
    },
    "log":[],"tags":{"System::motd":1,"installation":8}
  }
}
```

The above output says that `System::motd` was installed in
`/home/tzz/.cfagent/inputs/sketches/system/motd/` (because my
`config.json` says so), and that the sketch inventory was saved
afterwards.

#### Install a sketch with `cf-sketch` in expert mode

    $CHECKOUT/tools/cf-sketch/cf-sketch.pl --expert --cfpath=/var/cfengine/bin --install System::motd --apiconfig $DCJ

Output:

    Sketch System::motd is already in target repo; you must uninstall it first

So, we need to force it...

    $CHECKOUT/tools/cf-sketch/cf-sketch.pl --expert --cfpath=/var/cfengine/bin --install System::motd --apiconfig $DCJ --force

Output: nothing!  In expert mode, when everything is OK, nothing is
printed.  Only the command return code will tell you if everything
went well.

So, we need to make it verbose...

    $CHECKOUT/tools/cf-sketch/cf-sketch.pl --expert --cfpath=/var/cfengine/bin --install System::motd --apiconfig $DCJ --force --verbose

Output:

```
... lots of verbose output, including the API interaction, omitted ...
OK: Got successful result: ... the API result is here, omitted for brevity
```

The `cf-sketch` expert mode is a thin layer over the API for testing
and unattended work, so the above verbose output is not really meant
for everyday use.

#### Install a sketch with `cf-sketch` in interactive mode

Run:

    $CHECKOUT/tools/cf-sketch/cf-sketch.pl --apiconfig $DCJ

Now enter the `uninstall System::motd` and `install System::motd`
commands, because just installing an already-installed sketch will not do
anything interesting:

```
cf-sketch> uninstall System::motd

Deactivated System::motd.
Sketch 'System::motd' was uninstalled.

cf-sketch> install System::motd

Sketch System::motd installed under /home/tzz/.cfagent/inputs/sketches.

cf-sketch>
```

To view verbose output, use
`--verbose` with the interactive `cf-sketch` call and view the output.

### Activate a sketch

#### Activate a sketch with the Design Center API

We are going to define a run environment, which will tell the Design
Center API that we want an activated sketch, not in test mode, and
with verbose output:

	echo '{ dc_api_version: "3.6.0", request: {define_environment: { walkthrough: { activated: true, test: false, verbose: true } } } }' | $CFAPI $DCJ

Then we will define the parameters for the `System::motd` sketch:

    echo '{ dc_api_version: "3.6.0", request: {define: { "motd_params": { "System::motd": { "motd": "\\n ! System is under the control of CFEngine, local changes may by overwritten.\\n", "prepend_command": null } } } } }' | $CFAPI $DCJ

and finally, use the run environment and the parameters to activate the sketch:

	echo '{ dc_api_version: "3.6.0", request: {activate: { "System::motd": { environment: "walkthrough", params: [ "motd_params" ] } } } }' | $CFAPI $DCJ

Output (omitting log lines and reformatted):

    {"api_ok":{"warnings":[],"success":true,"errors":[],"error_tags":{},
               "data":{"define_environment":{"walkthrough":1}},
               "log":[],"tags":{"walkthrough":1}}}

    {"api_ok":{"warnings":[],"success":true,"errors":[],"error_tags":{},
               "data":{"define":{"motd_params":1}},
               "log":[],"tags":{"motd_params":1}}}

    {"api_ok":{"warnings":[],"success":true,"errors":[],"error_tags":{},
               "data":{"activate":{"System::motd":{"params":["motd_params"],"environment":"walkthrough"}}},
               "log":[],"tags":{"System::motd":1}}}

This tells us that the API has recorded that we want the sketch
`System::motd` to run with the run environment `walkthrough` and the
parameters `motd_params`.

#### Activate a sketch with `cf-sketch` in expert mode

We'll try the `simple.json` parameters that come with `System::motd`.
You can look at that file; it is the same as the `motd_params` above.

    $CHECKOUT/tools/cf-sketch/cf-sketch.pl --expert --apiconfig $DCJ --activate System::motd=$CHECKOUT/sketches/system/motd/params/simple.json --verbose --activated

Output:

    ...
    DCAPI::log(DCAPI.pm:1061): Activations for sketch System::motd are now [{"params":["motd_params"],"environment":"walkthrough"},{"params":["parameter definition from /home/tzz/source/design-center/sketches/system/motd/params/simple.json"],"environment":"cf_sketch_testing","target":"/home/tzz/.cfagent/inputs/sketches"}]

This says we now have two activations.  One from the API call above
and one we just created.  Let's undo the activations:

    $CHECKOUT/tools/cf-sketch/cf-sketch.pl --expert --apiconfig $DCJ --deactivate-all
    $CHECKOUT/tools/cf-sketch/cf-sketch.pl --expert --apiconfig $DCJ --activate System::motd=$CHECKOUT/sketches/system/motd/params/simple.json  --verbose --activated

Output:

    ...
    DCAPI::log(DCAPI.pm:1403): Deactivating all activations: {"System::motd":[{"params":["motd_params"],"environment":"walkthrough"},{"params":["parameter definition from /home/tzz/source/design-center/sketches/system/motd/params/simple.json"],"environment":"cf_sketch_testing","target":"/home/tzz/.cfagent/inputs/sketches"}]}
    ...
    OK: Got successful result: {"success":true,"warnings":[],"errors":[],"error_tags":{},"log":[],"data":{"activate":{"System::motd":{"environment":"cf_sketch_testing","params":["parameter definition from /home/tzz/source/design-center/sketches/system/motd/params/simple.json"],"target":"/home/tzz/.cfagent/inputs/sketches"}}},"tags":{"System::motd":1}}

Looks like it worked!  The `cf_sketch_testing` environment is created
by `cf-sketch` on the fly and will include the same things as the
`walkthrough` run environment.  The `--activated` and `--verbose`
flags turn on the environment `activated` and `verbose` flags.
There's also a `--test` flag, but we will not use it here.

#### Activate a sketch with `cf-sketch` in interactive mode

Run:

    $CHECKOUT/tools/cf-sketch/cf-sketch.pl

Then:

```
cf-sketch> define params System::motd

Please enter a name for the new parameter set (default: System::motd-entry-000): motd_params
Querying configuration for parameter set 'motd_params' for bundle 'entry'.

Please enter parameter motd (Message of the Day (aka motd), ).
motd : Hello there!

Please enter parameter motd_path (Location of the primary, often only, MotD file, ).
motd_path [/etc/motd]: /etc/motd

Please enter parameter prepend_command (Command output to prepend to MotD, ).
prepend_command [/bin/uname -snrvm]: /bin/uname -snrvm

Please enter parameter dynamic_path (Location of the dynamic part of the MotD file, ).
dynamic_path : null

Please enter parameter symlink_path (Location of the symlink to the motd file, ).
symlink_path : null

Defining parameter set 'motd_params' with the entered data.
Parameter set motd_params successfully defined.

cf-sketch> activate System::motd motd_params walkthrough
Using existing parameter definition 'motd_params'.
Using existing environment 'walkthrough'.
Activating sketch System::motd with parameters motd_params.
...
DCAPI::log(DCAPI.pm:1061): Activations for sketch System::motd are now [{"params":["parameter definition from /home/tzz/source/design-center/sketches/system/motd/params/simple.json"],"environment":"cf_sketch_testing","target":"/home/tzz/.cfagent/inputs/sketches"},{"params":["motd_params"],"environment":"walkthrough","target":"/home/tzz/.cfagent/inputs/sketches","identifier":"System::motd-1"}]

cf-sketch>
```

As you can see, the expert and interactive modes have completely
different usage patterns.

### Generate and execute the runfile

#### Generate and execute the runfile with the Design Center API

Generating the runfile is easy:

	echo '{ dc_api_version: "3.6.0", request: {regenerate: { } } }' | $CFAPI $DCJ

Output:

    DCAPI::log(DCAPI.pm:249): Saving runfile /home/tzz/.cfagent/inputs/api-runfile.cf
    {"api_ok":{"warnings":[],"success":true,"errors":[],"error_tags":{},"data":{},"log":[],"tags":{}}}

Note there is no user control over the location of the runfile, it's
entirely defined in the API's `config.json` file.  This is by design.

Time to run the policy!!!  We know the name of the runfile, so we can run it.

    cf-agent -KI -f ~/.cfagent/inputs/api-runfile.cf

We are not in test mode, so we will get errors if we run as a non-privileged user.

```
2013-06-04T20:12:04-0400     info: This agent is not bootstrapped
2013-06-04T20:12:04-0400     info: Running full policy integrity checks
2013-06-04T20:12:04-0400    error: Unable to open destination file '/etc/motd.cf-after-edit' for writing. (fopen: Permission denied)
2013-06-04T20:12:04-0400    error: /cfsketch_run/methods/'___001_System_motd_entry'/cfdc_motd:entry/files/'$(main_path)': Unable to save file '/etc/motd' after editing
2013-06-04T20:12:04-0400    error: chmod failed on '/etc/motd'. (chmod: Operation not permitted)
2013-06-04T20:12:04-0400   notice: R: cfdc_motd:entry: System::motd license = MIT
2013-06-04T20:12:04-0400   notice: R: cfdc_motd:entry: System::motd dependencies = CFEngine::dclib, CFEngine::stdlib
2013-06-04T20:12:04-0400   notice: R: cfdc_motd:entry: System::motd version 1.00 by Ben Heilman <bheilman@enova.com> starting up...
2013-06-04T20:12:04-0400   notice: R: cfdc_motd:entry: imported environment 'cf_sketch_testing' var 'activated' with value '1'
2013-06-04T20:12:04-0400   notice: R: cfdc_motd:entry: imported environment 'cf_sketch_testing' var 'test' with value ''
2013-06-04T20:12:04-0400   notice: R: cfdc_motd:entry: imported environment 'cf_sketch_testing' var 'verbose' with value '1'
2013-06-04T20:12:04-0400   notice: R: cfdc_motd:entry: imported environment 'cf_sketch_testing' class 'activated' because 'default:runenv_cf_sketch_testing_activated' was defined
2013-06-04T20:12:04-0400   notice: R: cfdc_motd:entry: imported environment 'cf_sketch_testing' class 'verbose' because 'default:runenv_cf_sketch_testing_verbose' was defined
2013-06-04T20:12:04-0400   notice: R: cfdc_motd:entry: running in verbose mode
```

Complete.

#### Generate and execute the runfile with `cf-sketch` in expert mode

    $CHECKOUT/tools/cf-sketch/cf-sketch.pl --expert --apiconfig $DCJ --generate

Output:

    ...
    DCAPI::log(DCAPI.pm:249): Saving runfile /home/tzz/.cfagent/inputs/api-runfile.cf

Run the runfile:

    cf-agent -KI -f ~/.cfagent/inputs/api-runfile.cf

The output will be the same as in the previous section.

#### Generate and execute the runfile with `cf-sketch` in interactive mode

Run:

    $CHECKOUT/tools/cf-sketch/cf-sketch.pl

You'll see:

```
cf-sketch> generate

...
DCAPI::log(DCAPI.pm:249): Saving runfile /home/tzz/.cfagent/inputs/api-runfile.cf
Runfile /home/tzz/.cfagent/inputs/api-runfile.cf successfully generated.
```

Run it:

    cf-agent -KI -f ~/.cfagent/inputs/api-runfile.cf

The output will be the same as in the previous section.
