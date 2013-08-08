---
layout: default
title: Advanced Walkthrough
categories: [Manuals, Design Center, Advanced Walkthrough]
published: true
sorting: 35
alias: manuals-design-center-advanced.html
tags: [design center, walkthrough, cf-sketch, sketches]
---

This walkthrough will show how a Design Center sketch can be found,
installed, configured, and executed as policy.

It requires a Unix that can run Perl and, of course, CFEngine itself.

### Checkout Design Center

You can browse the source for examples, tools, sketches (generic
reusable policy), or read through the Design Center wiki by browsing
https://github.com/cfengine/design-center

After you have explored and you are ready to go, change to a directory
that will not be cleaned up automatically (don't use `/tmp` for
example; here we used `~/source`) and run:

    git clone git@github.com:cfengine/design-center.git
    
or, if the Git native protocol is blocked at your site:

    git clone https://github.com/cfengine/design-center.git

You should end up with a directory called `design-center`.  We'll call
this directory the *CHECKOUT* directory and refer to it as
`$(CHECKOUT)` from here on.  In the examples that follow, *CHECKOUT*
is `~/source/design-center` (the tilde `~` refers to the current
user's home directory).

You can save some typing by saying

    export CHECKOUT=~/source/design-center
    
at the prompt.  From that point on, all command-line interaction can
use `$CHECKOUT` and it will expand to the installation directory.

You also need to make sure [curl](http://curl.haxx.se) is installed on
your system, since it is used by `cf-sketch` for accessing remote
files when needed. Curl is readily available as a package in most
Unix/Linux systems, and even installed by default on many of them.

### Prepare config.json

To interact with Design Center, you need to tell its API where things
were installed.  Copy the `config.json` file to your CFEngine personal
directory:

    mkdir ~/.cfagent
    cp $CHECKOUT/tools/cf-sketch/config.json ~/.cfagent/dc-api-config.json

(Note that there's also a `config-root.json` intended for privileged
(root) usage.  It sets things up under `/var/cfengine` but still
expects the checkout under `~/source/design-center`.)

Now if you look at this file, you'll see that it has some JSON data:

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

You can change any setting you want but it's probably safer to leave
them all at the default.

The paths you see are all relative to your home directory.  The `log`
can be set to a file.  The `log_level` can be lowered to 1 if you want
less noise (here we'll work with it at 4).

`vardata` is where the Design Center API stores all the configuration.

`runfile` describes where the Design Center API will save an
executable policy with all the sketches you have installed and
activated.

The `repolist` is where sketches will be *installed*.

The `recognized_sources` is where sketches will be *found*.  It can be
a URL such as
`https://github.com/cfengine/design-center/blob/master/sketches/cfsketches.json`.

You can save some typing by saying

    export DCJ=~/.cfagent/dc-api-config.json    

at the prompt.  From that point on, all command-line interaction can
use `$DCJ` and it will expand to the filename above.

From this point on, we'll refer to this command

    $CHECKOUT/tools/cf-sketch/cf-dc-api.pl

as `$CFAPI` for brevity.

You can save some typing by saying

    export CFAPI=$CHECKOUT/tools/cf-sketch/cf-dc-api.pl
    
at the prompt.  From that point on, all command-line interaction can
use `$CFAPI` and it will expand to the command above.

### Search for sketches

Time to search for sketches!!!  This section will explain many details
that the later sections in the walkthrough will skip for brevity.

#### Search for sketches with the Design Center API

This is what all the other Design Center tools use.  You don't need to
know this protocol or know that it's used.

	echo '{ dc_api_version: "0.0.1", request: {search: true } }' | $CFAPI $DCJ

If you get errors here, you may be missing Perl modules or the
CFEngine agent.  Look at the Design Center wiki for possible solutions
to your problem, at https://github.com/cfengine/design-center/wiki

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
essential errors will be shown.  Now for the actual API response:

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

The response says (with many sketch names omitted for brevity): here, these are all my sketches.

Again, this is not what you would use daily.

#### Search for sketches with `cf-sketch` in expert mode

    $CHECKOUT/tools/cf-sketch/cf-sketch.pl --expert --cfpath=/var/cfengine/bin --apiconfig $DCJ --search | sort

Output:

```
Applications::Memcached Sketch for installing, configuring, and starting memcached.
...
Yale::stdlib Yale standard library
```

You piped the command above through the standard `sort` command to
sort the results.  You can omit the `sort`.

#### Search for sketches with `cf-sketch` in interactive mode

Run

    $CHECKOUT/tools/cf-sketch/cf-sketch.pl --apiconfig $DCJ

You'll see this prompt, or something like it:

```
Welcome to cf-sketch version 3.5.0b1.
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

Obviously that's easiest but you may want the expert or direct API
interaction for specific purposes.  We'll show all three along the
way, don't worry.

### Install a sketch

#### Install a sketch with the Design Center API

    echo '{ dc_api_version: "0.0.1", request: {install: {sketch:"System::motd", force:true} } }' | $CFAPI $DCJ
    
The `force` parameter tells the Design Center API to overwrite the
sketch even if it's installed already.

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

After lots of fireworks (again, remember to drop down to `log_level` 1 or 0 if you want to skip all these messages) the sketch is installed!

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

OK, so we need to force it...

    $CHECKOUT/tools/cf-sketch/cf-sketch.pl --expert --cfpath=/var/cfengine/bin --install System::motd --apiconfig $DCJ --force

Output: nothing!  In expert mode, when everything is OK, nothing is
printed.  Only the command return code will tell you if everything
went well.

OK, so we need to make it verbose...

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

Run

    $CHECKOUT/tools/cf-sketch/cf-sketch.pl --apiconfig $DCJ

Now enter the `uninstall System::motd` and `install System::motd`
commands, because just installing an already-installed sketch won't do
anything interesting:

```
cf-sketch> uninstall System::motd

Deactivated System::motd.
Sketch 'System::motd' was uninstalled.

cf-sketch> install System::motd

Sketch System::motd installed under /home/tzz/.cfagent/inputs/sketches.

cf-sketch> 
```

Oh, and if you miss all that verbose output, you can still use
`--verbose` with the interactive `cf-sketch` call and see all that
wonderful output.

### Activate a sketch

#### Activate a sketch with the Design Center API

We are going to define a run environment, which will tell the Design
Center API that we want an activated sketch, not in test mode, and
with verbose output:

	echo '{ dc_api_version: "0.0.1", request: {define_environment: { walkthrough: { activated: true, test: false, verbose: true } } } }' | $CFAPI $DCJ

Then we will define the parameters for the `System::motd` sketch:

    echo '{ dc_api_version: "0.0.1", request: {define: { "motd_params": { "System::motd": { "motd": "\\n ! System is under the control of CFEngine, local changes may by overwritten.\\n", "prepend_command": null } } } } }' | $CFAPI $DCJ

and finally, use the run environment and the parameters to activate the sketch:

	echo '{ dc_api_version: "0.0.1", request: {activate: { "System::motd": { environment: "walkthrough", params: [ "motd_params" ] } } } }' | $CFAPI $DCJ

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
You can look at that file, it's the same as the `motd_params` above.

    $CHECKOUT/tools/cf-sketch/cf-sketch.pl --expert --apiconfig $DCJ --activate System::motd=$CHECKOUT/sketches/system/motd/params/simple.json --verbose --activated

Output:

    ...
    DCAPI::log(DCAPI.pm:1061): Activations for sketch System::motd are now [{"params":["motd_params"],"environment":"walkthrough"},{"params":["parameter definition from /home/tzz/source/design-center/sketches/system/motd/params/simple.json"],"environment":"cf_sketch_testing","target":"/home/tzz/.cfagent/inputs/sketches"}]

This says we now have two activations!  One from the API call above
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
There's also a `--test` flag, but we won't use it here.

#### Activate a sketch with `cf-sketch` in interactive mode

Run

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

As you can see the expert and interactive modes have completely
different usage patterns.

### Generate and execute the runfile

#### Generate and execute the runfile with the Design Center API

Generating the runfile is easy:

	echo '{ dc_api_version: "0.0.1", request: {regenerate: { } } }' | $CFAPI $DCJ

Output:

    DCAPI::log(DCAPI.pm:249): Saving runfile /home/tzz/.cfagent/inputs/api-runfile.cf
    {"api_ok":{"warnings":[],"success":true,"errors":[],"error_tags":{},"data":{},"log":[],"tags":{}}}

Note there is no user control over the location of the runfile, it's
entirely defined in the API's `config.json` file.  This is by design.

Time to run the policy!!!  We know the name of the runfile, let's go!

    cf-agent -KI -f ~/.cfagent/inputs/api-runfile.cf

We are not in test mode, so we'll get errors if we run as a non-privileged user.

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

That's it!

#### Generate and execute the runfile with `cf-sketch` in expert mode

    $CHECKOUT/tools/cf-sketch/cf-sketch.pl --expert --apiconfig $DCJ --generate

Output:

    ...
    DCAPI::log(DCAPI.pm:249): Saving runfile /home/tzz/.cfagent/inputs/api-runfile.cf

Run the runfile!  Do it!!!

    cf-agent -KI -f ~/.cfagent/inputs/api-runfile.cf

The output will be the same as in the previous section.

#### Generate and execute the runfile with `cf-sketch` in interactive mode

Run

    $CHECKOUT/tools/cf-sketch/cf-sketch.pl

You'll see:

```
cf-sketch> generate

...
DCAPI::log(DCAPI.pm:249): Saving runfile /home/tzz/.cfagent/inputs/api-runfile.cf
Runfile /home/tzz/.cfagent/inputs/api-runfile.cf successfully generated.
```

There you go.  Run it.  Do it.

    cf-agent -KI -f ~/.cfagent/inputs/api-runfile.cf

The output will be the same as in the previous section.
