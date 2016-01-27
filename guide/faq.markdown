---
layout: default
title: FAQ
published: true
sorting: 90
tags: [getting started, installation, enterprise, faq]
---

* [Enterprise Installation][#Enterprise Installation and Configuration]
	* [What steps should I take after installing CFEngine Enterprise?][#What steps should I take after installing CFEngine Enterprise]
	* [Can I use an existing PostgreSQL installation?][#Can I use an existing PostgreSQL installation]
	* [What is the system user for the CFEngine dedicated PostgreSQL database?][#What is the system user for the CFEngine dedicated PostgreSQL database and Apache server]
	* [Do I need experience with PostgreSQL?][#Do I need experience with PostgreSQL]
	* [What are the requirements for installing CFEngine Enterprise?][#What are the requirements for installing CFEngine Enterprise]
* [Enterprise Scalability][#Enterprise Scalability]
    * [ Is it normal to have many cf-hub processes running?][#Is it normal to have many cf-hub processes running]
* [Policy Distribution][#Policy Distribution]
	* [I have added new files in masterfiles but my remote clients are not getting updates.][#I have added new files in masterfiles but my remote clients are not getting updates]
	* [I have updated some non policy files and changes are not distributed to clients.][#I have updated some non policy files and changes are not distributed to clients]
* [Manual Execution][#Manual Execution]
	* [How do I run a standalone policy file?][#How do I run a standalone policy file]
	* [How do I run a specific bundle?][#How do I run a specific bundle]
	* [How do I define a class for a single run?][#How do I define a class for a single run]
* [Agent Email Reports][#Agent Email Reports]
	* [How do I set the email where agent reports are sent?][#How do I set the email where agent reports are sent]
	* [How do I disable agent email output?][#How do I disable agent email output]
* [Policy Writing][#Policy Writing]
  * [How do I pass a data type variable?][#How do I pass a data type variable]

### Enterprise Installation and Configuration ###

#### What steps should I take after installing CFEngine Enterprise ####

There are general steps to be taken outlined in [Post-Installation Configuration][General Installation#Post-Installation Configuration].

In addition to this, Enterprise 3.6 uses the local mail relay, and it is assumed that the server where CFEngine Enterprise is installed on has proper mail setup.

The default FROM email for all emails sent from the Mission Portal is currently admin@organization.com. This can be changed on the CFEngine Hub in `/var/cfengine/httpd/htdocs/application/config/appsettings.php:$config['appemail']`.

#### Can I use an existing PostgreSQL installation ####

No.  Although CFEngine keeps its assumptions about Postgres to a bare minimum,
CFEngine should use a dedicated PostgreSQL database instance to ensure there is
no conflict with an existing installation.

#### Do I need experience with PostgreSQL ####

PostgreSQL is highly configurable and you should have some in-house
expertise to properly configure your database installation. The
defaults are well tuned for common cases but you may find
optimizations depending on your hardware and OS.

#### What is the system user for the CFEngine dedicated PostgreSQL database and Apache server ####

Starting with CFEngine 3.6 there will be a system user called ```cfpostgres``` for running the dedicated CFEngine PostgreSQL database
installation.

Similarly there will be a ```cfapache``` system user for the Apache web server.

#### What are the requirements for installing CFEngine Enterprise ####

##### General Information #####

* [Pre-Installation Checklist][Pre-Installation Checklist]
* [Supported Platforms and Versions][Supported Platforms and Versions]

##### Users and Permissions #####

* CFEngine Enterprise makes an attempt to create the local users ```cfapache``` and ```cfpostgres```, as well as group ```cfapache``` when installing 3.6. The server must allow creation of these users and groups.


### Enterprise Scalability ###

See: [Enterprise Scalability][Best Practices#Scalability]

#### Is it normal to have many cf-hub processes running

* Yes, it is expected to have ~ 50 cf-hub processes running on your hub

### Policy Distribution ###

#### I have added new files in masterfiles but my remote clients are not getting updates ####

Check that the files you expect to be distributed have matching `leaf_name` pattern.  If newly bootstrapped clients get those files but existing clients don't, this is certainly the problem, because bootstrapping and failsafe operation ignore `leaf_name` and copy everything.

In CFEngine 3.6 masterfiles policy framework this is configurable with
`input_name_patterns` in the `update_def` bundle in `def.cf`.  See [The Policy Framework][The Policy Framework] for more information.

#### I have updated some non policy files and changes are not distributed to clients ###

`cf_promises_validated` gates client updates. This file is only updated on the
policy server when new policy is validated. Edits to non policy files do not
trigger an update of `cf_promises_validated`. You can use a separate promise to
ensure those files are continually distributed, instead of only on policy
updates.

For details see [cf_promises_validated][The Policy Framework#cf_promises_validated] and [cfe_internal_update_policy][The Policy Framework#cfe_internal_update_policy (bundle)]

#### My policy server has changed its IP address and new bootstraps don't work!

(thanks to Dan Langille in https://groups.google.com/forum/#!topic/help-cfengine/jcdIh12_lNI)

Symptom:

After the policy server was restarted with the new IP address, clients would not connect:

    error: Not authorized to trust public key of server '192.168.14.113' (trustkey = false)
    error: Authentication dialogue with '192.168.14.113' failed

Bootstrapping the clients also fails:

```
[root@dev /var/cfengine] /var/cfengine/bin/cf-agent --bootstrap  192.168.14.113
2014-06-23T13:57:07-0400   notice: R: This autonomous node assumes the role of voluntary client
2014-06-23T13:57:07-0400   notice: R: Failed to copy policy from policy server at 192.168.14.113:/var/cfengine/masterfiles
       Please check
       * cf-serverd is running on 192.168.14.113
       * network connectivity to 192.168.14.113 on port 5308
       * masterfiles 'body server control' - in particular allowconnects, trustkeysfrom and skipverify
       * masterfiles 'bundle server' -> access: -> masterfiles -> admit/deny
       It is often useful to restart cf-serverd in verbose mode (cf-serverd -v) on 192.168.14.113 to diagnose connection issues.
       When updating masterfiles, wait (usually 5 minutes) for files to propagate to inputs on 192.168.14.113 before retrying.
2014-06-23T13:57:07-0400   notice: R: Did not start the scheduler
2014-06-23T13:57:07-0400    error: Bootstrapping failed, no input file at '/var/cfengine/inputs/promises.cf' after bootstrap
```

Solution:

Assuming that `661df12c960af9afdde093e0cb339b4d` is the MD5 hostkey and `192.168.14.113` is the new IP address:

```
cd /var/cfengine/ppkeys && mv -i root-MD5=661df12c960af9afdde093e0cb339b4d.pub root-192.168.14.113.pub
```


### Manual Execution ###

#### How do I run a standalone policy file ####

The `--file` or `-f` option to `cf-agent` specifys the policy file. The `-K` or `--no-lock` flag and the `-I` or `--inform`
options are commonly used in combination with the `-f` option to ensure that
all promises are skipped because of locking and for the agent to produce
informational output like successful repairs.

```console
cf-agent -KIf ./my_standalone_policy.cf
```

In 3.6.1 and later, a standalone policy file **may** choose not to
specify a `bundlesequence`. In that case, the `bundlesequence`
defaults to `main` so you'll need a bundle called `main`.

You can avoid that requirement by using the `-b BUNDLENAME` flag which
specifies an explicit `bundlesequence`, see below.

#### Why do I get Undefined body when I try to run my policy ###

`cf-promises -f ./large-files.cf`:
```
./large-files.cf:14:0: error: Undefined body tidy with type delete
./large-files.cf:16:0: error: Undefined body recurse with type depth_search
```

The above errors indicate that the `tidy` and `recurse` bodies are not able
to be found by CFEngine. This is because they are not found in the file or in
one of the files it includes. Either define the body within the same policy
file or include the file that defines the body using inputs in either [body
common control][Components and Common Control#inputs] or [body file
control][file control#inputs].

**Example: Add stdlib via body common control**

```cf3
body common control
{
        bundlesequence => { "file_remover" };
        inputs => { "$(sys.libdir)/stdlib.cf" };
}
```

**Example: Add stdlib via body file control**
Body file control allows you to build modular policy. Body file control inputs
are typically relative to the policy file itself.

```cf3
bundle file_remover_control
{
  vars:
    "inputs" slist => { "$(this.promise_dir)/$(sys.local_libdir)/stdlib.cf" };
}
body file control
{
  inputs => { @(file_remover_control.inputs) };
}
```

This policy will work correctly whether it's included by another
policy file or not. Note the `body file` `control` option is new since
CFEngine 3.6, so you should not use if your policy could be seen by
3.5 or earlier CFEngine clients.

#### How do I run a specific bundle ####

A specific bundle can be activated by passing the `-b` or `--bundlesequence`
options to `cf-agent`. This may be used to activate a specific bundle within a
large policy set or to run a standalone policy that does not include a `body
common control`.

```console
cf-agent -b my_bundle
```

If you want to activate multiple bundles in a sequence simply separate them
with commas (no spaces between).

```console
cf-agent --bundlesequence bundle1,bundle2
```

#### How do I define a class for a single run ####

You can use the `--define` or `-D` options of `cf-agent`.

```console
cf-agent -D my_class
```

And if you want to define multiple, simply separate them with commas (no spaces between).

```console
cf-agent --define my_class,my_other_class
```

Multiple `-D` flags are not supported, you have to put all the classes in one comma-separated list.

### Showing Classes and variables with cf-promsies

`cf-promises --show-classes` and `cf-promises --show-vars` will only show
classes and variables found on a first pass through the policy, since
`cf-promises` does not evaluate agent promises.

### Agent Email Reports ###

#### How do I set the email where agent reports are sent ####

The agent report email functionality is configured in `body executor control`
https://github.com/cfengine/masterfiles/blob/master/controls/cf_execd.cf. It
defaults to `root@$(def.domain)` which is configured in `bundle common def`
https://github.com/cfengine/masterfiles/blob/master/def.cf.

For details see [domain][The Policy Framework#domain (variable)].

#### How do I disable agent email output ####

You can simply remove or comment out the settings.

In 3.6.x there is a convenience class `cfengine_internal_agent_email` avaiable
in `bundle common def` to switch on/off agent email.

For details see [cfengine_internal_agent_email][The Policy Framework#cfengine_internal_agent_email (class)].

### Mustache Templating ###

#### How can I pass a data variable to template_data? ####

Just use `template_data => @(mycontainer)`.

If you need to extract a portion of the container or merge it with another, use 
`template_data => mergedata("mycontainer[piece]", "othercontainer")`.

#### Can I render a Mustache template into a string? ####

Yes, see `string_mustache()`.

#### How do I render a section only if a given class is defined? ####

In this Mustache example the word 'Enterprise' will only be rendered if the class 'enterprise' is defined.

This template should not be passed a data container; it uses the `datastate()` of the CFEngine system.  That's where `classes.enterprise` and `vars.sys.cf_version` came from.

```
Version: CFEngine {{#classes.enterprise}}Enterprise{{/classes.enterprise}} {{vars.sys.cf_version}}
```

#### How do I iterate over a list? ####

This template should not be passed a data container; it uses the `datastate()` of the CFEngine system.  That's where `vars.mon.listening_tcp4_ports` came from.

{% raw %}
```
{{#vars.mon.listening_tcp4_ports}}
  * {{.}}
{{/vars.mon.listening_tcp4_ports}}
```
{% endraw %}

### How do I ensure that a local user is locked? ###

To ensure that a local user exists but is locked (for example a service
account) simply specify `policy => "locked"`.

[%CFEngine_include_snippet(users_type.cf, ### Locked User BEGIN ###, ### Locked User END ###)%]

## Policy Writing ##

Common questions asked about policy writing.

### How do I pass a data type variable ###

Data type variables also known as "data containers" are passed using the same
syntax as passing a list.

```cf3
bundle agent example
{
  vars:
    # First you must have a data type variable, define it inline or read from a
    # file using `readjson()`.
    "data" data => parsejson('[ { "x": 1 }, { "y": 2 } ]');

  methods:
    "use data"
      usebundle => use_data(@(data));
}

bundle agent use_data(dc)
{
  vars:
    # Use the data
    # Get its keys, or its index
    "dc_index" slist => getindices(dc);

  classes:
    "have_x" expression => isvariable("dc[$(dc_index)][x]");
    "have_z" expression => isvariable("dc[$(dc_index)][z]");

  reports:
    "CFEngine version '$(sys.cf_version)'";
    have_x::
      "Index '$(dc_index)' has key for x";

    have_z::
      "Index '$(dc_index)' has key for z";
}
```

```console
$ cf-agent -Kf ./example.cf -b example
R: CFEngine version '3.6.4'
R: Index '0' has key for x
R: Index '1' has key for x
```
