---
layout: default
title: Manage Network Time Protocol
published: true
sorting: 3
tags: [getting started, tutorial]
---

In this tutorial we will write a simple policy to ensure that the latest version of the NTP service is installed on your system. Once the NTP software is installed, we will extend the policy to manage the service state as well as the software configuration.

Note: For simplicity, in this tutorial we will work directly on top of the Masterfiles Policy Framework (MPF) in `/var/cfengine/masterfiles` (*masterfiles*) and we will not use version control.

## Ensuring the NTP package is installed


```cf3
bundle agent ntp
{
   vars:
       "ntp_package_name" string => "ntp";

   packages:
       "$(ntp_package_name)"   -> { "StandardsDoc 3.2.1" } 
       policy          => "present",
       handle          => "ntp_packages_$(ntp_package_name)",
       classes         => results("bundle", "ntp_package");
}
```

What does this policy do?

Let's walk through the different sections of the code do see how it works.

### bundle agent ntp

You can think of bundles as a collection of desired states. You can have as many bundles as you would like, and also reference them from within themselves. In fact, they are somewhat similar to function calls in other programming languages. Let's dive deeper into the code in the ntp bundle.

#### vars

```cf3
vars:
```

`vars` is a promise type that ensures the presence of variables that hold specific values. `vars:` starts a promise type block which ends when the next promise type block is declared.

##### ntp_package_name

```cf3
    "ntp_package_name" string => "ntp";
```

A variable with the name `ntp_package_name` is declared and it is assigned a value, `ntp`. This string variable will be referenced in the other sections of the bundle.

#### packages

```cf3
   packages:
       "$(ntp_package_name)"   -> { "StandardsDoc 3.2.1" } 
         policy          => "present",
         handle          => "ntp_packages_$(ntp_package_name)",
         classes         => results("bundle", "ntp_package");
```

`packages` is a promise type that ensures the presence or absence of a package on a system.

##### $(ntp_package_name)

```
       "$(ntp_package_name)"   -> { "StandardsDoc 3.2.1" } 
```

Notice the `ntp_package_name` variable is referenced here, which evaluates to `ntp` as the promiser. You can also associate a stakeholder aka promisee to this promiser. The stakeholder association is optional, but is particularly useful in when you wish to provide some structure in your policy to tie it to a business rule. In this example, what we are stating is this – "Make sure NTP is installed as it is described in StandardsDoc 3.2.1".

This promiser has a number of additional attributes defined:

###### policy

```cf3
       policy          => "present",
```

    The package_policy attribute describes what you want to do the package. In this case you want to ensure that it is present on the system. Other valid values of this attribute include delete, update, patch, reinstall, addupdate, and verify. Because of the self-healing capabilities of CFEngine, the agents will continuously check to make sure the package is installed. If it is not installed, CFEngine will try to install it according to its policy.

###### handle

```cf3
       handle          => "ntp_packages_$(ntp_package_name)",
```

The handle uniquely identifies a promise within a policy. A recommended naming scheme for the handle is `bundle_name_promise_type_class_restriction_promiser`. It is often used for documentation and compliance purposes. As shown in this example, you can easily substitute values of variables for the handle.

###### classes

```cf3
       classes         => results("bundle", "ntp_package_");
```

`classes` provide context which can help drive the logic in your policies. In this example, classes for each promise outcome are defined prefixed with `ntp_package_`, for details check out the implementation of `body classes results` in the stdlib. For example, `ntp_package_repaired` will be defined if cf-agent did not have the ntp package installed and had to install it. `ntp_package_kept` would be defined if the ntp package is already installed and `ntp_package_notkept` would be defined. 

On your hub create `services/ntp.cf` inside *masterfiles* with the following content:

```cf3
bundle agent ntp
{
   vars:
       "ntp_package_name" string => "ntp";

   packages:
       "$(ntp_package_name)"   -> { "StandardsDoc 3.2.1" } 
         policy          => "present",
         handle          => "ntp_packages_$(ntp_package_name)",
         classes         => results("bundle", "ntp_package");

}
```

Now, check the syntax, it's always a good idea any time you edit policy.

```
[root@hub masterfiles]# cf-promises -f ./services/ntp.cf 
[root@hub masterfiles]# echo $?
0
```

Now, we need to make sure the agent knows it should use this policy file and bundle. Create `def.json` an Augments file with the following content: 

```json
{
  "inputs": [ "services/ntp.cf" ],
  "vars": {
    "control_common_bundlesequence_end": [ "ntp" ]
  }
}
```

Validate it.

```console
[root@hub masterfiles]# python -m json.tool < def.json
{
    "inputs": [
        "services/ntp.cf"
    ],
    "vars": {
        "control_common_bundlesequence_end": [
            "ntp"
        ]
    }
}
```

Force a policy update. Remember, CFEngine is running in the background, so it's possible that by the time you force a policy update and run the agent may have already done it and your output may differ.

```
cf-agent -KIf update.cf
```

In the output, you should see something like:

```
info: Updated '/var/cfengine/inputs/services/ntp.cf' from source '/var/cfengine/masterfiles/services/ntp.cf' on 'localhost'
```

Now force a policy run.

```console
[root@hub masterfiles]# cf-agent -KI
```

```
info: Successfully installed package 'ntp'
```

Now that we have successfully promised the package, let's move on to the *service*.

## Manage NTP service

Now we will extend the policy to ensure that the NTP service is running.

Now that the NTP service has been installed on the system, we need to make sure that it is running.

```cf3
bundle agent ntp
{
   vars:
       "ntp_package_name" string => "ntp";

     redhat::
         "ntp_service_name" string => "ntpd";

     debian::
         "ntp_service_name" string => "ntp";

   packages:
       "$(ntp_package_name)"   -> { "StandardsDoc 3.2.1" } 
         policy          => "present",
         handle          => "ntp_packages_$(ntp_package_name)",
         classes         => results("bundle", "ntp_package");

  services:
     "$(ntp_service_name)" -> { "StandardsDoc 3.2.2" } 
       service_policy => "start",
       classes => results( "bundle", "ntp_service")

   reports:
     ntp_service_repaired.inform_mode::
       "NTP service repaired";

}
```

### What does this policy do?

Let's dissect this policy and review the differences in the policy.

#### vars

```cf3
   redhat::
       "ntp_service_name" string => "ntpd";
   debian::
       "ntp_service_name" string => "ntp";
```

The first thing that you will notice is that the variable declarations section has been expanded. Recall that you completed part 1 of this tutorial by creating packages promises that works across Debian and redhat. While the package name for NTP is the same between Debian and Red Hat, the service names are actually different. Therefore, classes introduced here to distinguish the service name for NTP between these two environments. The CFEngine agents automatically discover environment properties and defines [*hard classes*][language-concepts-classes-hard] that can be used – this includes classes such as `debian` and `redhat` that define the host's operating system.

#### reports

```cf3
   reports:
     ntp_service_repaired.inform_mode::
       "NTP service repaired";
```

The reports promise type emits information from the agent. Most commonly and by default, information is emitted to standard out. Reports are useful when tracking or reporting on the progress of the policy execution.

```
ntp_service_repaired.inform_mode::
```

This line restricts the context for the promises that follow to hosts that have `ntp_service_repaired` and `inform_mode` defined. Note: `inform_mode` is defined when information level logging is requested, e.g.  the `-I`, `--inform`, or `--log-level inform` options are given to `cf-agent` defined.

```cf3
       "NTP service repaired";
```

This defines the line that should be emitted by the `reports` promise type.

Messages printed to standard out from reports promises are prefixed with the letter `R` to distinguish them from other output.

```
R: NTP service repaired
```

### Modify and run the policy

On your hub modify `services/ntp.cf` introducing the new promises as described previously.

After making changes it's always a good idea to validate the policy file you modified, as well as the full policy set:

```console
[root@hub masterfiles]# cf-promises -KI -f ./services/ntp.cf
[root@hub masterfiles]# cf-promises -KI -f ./promises.cf
```

If the code has no syntax error, you should see no output.


Perform a manual policy run and review the output to ensure that the policy executed successfully. Upon a successful run you should expect to see an output similar to this (depending on the init system your OS is using):

```console
[root@hub masterfiles]# cf-agent -KIf update.cf;
    info: Copied file '/var/cfengine/masterfiles/services/ntp.cf' to '/var/cfengine/inputs/services/ntp.cf.cfnew' (mode '600')

[root@hub masterfiles]# cf-agent -KI
    info: Executing 'no timeout' ... '/sbin/chkconfig ntpd on'
    info: Command related to promiser '/sbin/chkconfig ntpd on' returned code defined as promise kept 0
    info: Completed execution of '/sbin/chkconfig ntpd on'
    info: Executing 'no timeout' ... '/etc/init.d/ntpd start'
    info: Completed execution of '/etc/init.d/ntpd start'
R: NTP service repaired
```

You have now written a complete policy to ensure that the NTP package is installed, and that the service is up and running.

## Manage NTP configuration

Now we will manage the configuration file using the built-in mustache templating engine, set up appropriate file permissions, and restart the service when necessary.

By default, the NTP service leverages configuration properties specified in /etc/ntp.conf. In this tutorial, we introduce the concept of the files promise type. With this promise type, you can create, delete, and edit files using CFEngine policies. The example policy below illustrates the use of the files promise.

```cf3
bundle agent ntp
{
   vars:
     linux::
       "ntp_package_name" string => "ntp";
       "config_file" string => "/etc/ntp.conf";
       "driftfile" string => "/var/lib/ntp/drift";
       "servers" slist => { "time.nist.gov" };

      # For brevity, and since the template is small, we define it in-line
       "config_template_string"
         string => "# NTP Config managed by CFEngine
driftfile {{{driftfile}}}
restrict default kod nomodify notrap nopeer noquery
restrict -6 default kod nomodify notrap nopeer noquery
restrict 127.0.0.1
restrict -6 ::1
{{#servers}} 
server {{{.}}} iburst
{{/servers}}
includefile /etc/ntp/crypto/pw
keys /etc/ntp/keys
";

     redhat::
         "ntp_service_name" string => "ntpd";

     debian::
         "ntp_service_name" string => "ntp";

   packages:
       "$(ntp_package_name)"   -> { "StandardsDoc 3.2.1" } 
         policy          => "present",
         handle          => "ntp_packages_$(ntp_package_name)",
         classes         => results("bundle", "ntp_package");

   files:
    "$(config_file)"
      create                => "true",
      handle                => "ntp_files_conf",
      perms                 => mog( "644", "root", "root" ),
      template_method       => "inline_mustache",
      edit_template_string  => "$(config_template_string)",
      template_data         => mergedata( '{ "driftfile": "$(driftfile)", "servers": servers }' ),
      classes               => results( "bundle", "ntp_config" );

   services:
     "$(ntp_service_name)" -> { "StandardsDoc 3.2.2" } 
       service_policy => "start",
       classes => results( "bundle", "ntp_service_running" );

    ntp_config_repaired::
     "$(ntp_service_name)" -> { "StandardsDoc 3.2.2" } 
       service_policy => "restart",
       classes => results( "bundle", "ntp_service_config_change" );


   reports:
     ntp_service_running_repaired.inform_mode::
       "NTP service started";

     ntp_service_config_change_repaired.inform_mode::
       "NTP service restarted after configuration change";

}
```

What does this policy do?

Let's review the different sections of the code, starting with the variable declarations which makes use of operating system environment for classification of the time servers.

#### vars


```cf3
   vars:
     linux::
       "ntp_package_name" string => "ntp";
       "config_file" string => "/etc/ntp.conf";
       "driftfile" string => "/var/lib/ntp/drift";
       "servers" slist => { "utcnist.colorado.edu", "utcnist2.colorado.edu" };

      # For brevity, and since the template is small, we define it in-line
       "config_template_string"
         string => "# NTP Config managed by CFEngine
driftfile {{{driftfile}}}
restrict default kod nomodify notrap nopeer noquery
restrict -6 default kod nomodify notrap nopeer noquery
restrict 127.0.0.1
restrict -6 ::1
{{#servers}} 
server {{{.}}} iburst
{{/servers}}
includefile /etc/ntp/crypto/pw
keys /etc/ntp/keys
";

```

A few new variables are defined. The variables `ntp_package_name`, `config_file`, `driftfile`, `servers`, and `config_template_string` are defined under the `linux` context (so only linux hosts will define them). `config_file` is the path to the ntp configuration file, `driftfile` and `servers` are both variables that will be used when rendering the configuration file and `config_template_string` is the template that will be used to render the configuration file. While both `driftfile` and `servers` are set the same for all linux hosts, those variables could easily be set to different values under different contexts.

#### files

Now let's walk through the files promise in detail.

```cf3
   files:
    "$(config_file)"
      create                => "true",
      handle                => "ntp_files_conf",
      perms                 => mog( "644", "root", "root" ),
      template_method       => "inline_mustache",
      edit_template_string  => "$(config_template_string)",
      template_data         => mergedata( '{ "driftfile": "$(driftfile)", "servers": servers }' ),
      classes               => results( "bundle", "ntp_config" );
```

The promiser here is referenced by the `config_file` variable. In this case, it is the configuration file for the NTP service. There are a number of additional attributes that describe this promise.

##### create

```cf3
      create                => "true",
```

Valid values for this attribute are `true` or `false` to instruct the agent whether or not to create the file. In other words, the file must exist. If it does not exist, it will be created.

##### perms

```cf3
      perms                 => mog( "644", "root", "root" ),
```

This attribute sets the permissions and ownership of the file. [`mog()`][stdlib-mog] is a `perms` body in the CFEngine standard library that sets the ```mode```, ```owner```, and ```group``` of the file. In this example, the permissions for the NTP configuration file are set to ```644``` with *owner* and *group* both assigned to ```root```.

##### handle

```cf3
      handle                => "ntp_files_conf",
```

A handle uniquely identifies a promise within a policy set. The [policy style guide][Policy Style Guide#promise handles] recommends a naming scheme for the handles e.g. `bundle_name_promise_type_class_restriction_promiser`. Handles are optional, but can be very useful when reviewing logs and can also be used to influence promise ordering with `depends_on`.

##### classes

```cf3
      classes               => results( "bundle", "ntp_config" );
```

The classes attribute here uses the [`results()`][lib/common.cf#results] classes body from the standard library. The `results()` body defines classes for every outcome a promise has. Every time this promise is executed classes will be defined bundle scoped classes prefixed with `ntp_config`. If the promise changes the file content or permissions the class `ntp_config_repaired` will be set.

##### template_method

```cf3
      template_method       => "inline_mustache",
```

CFEngine supports multiple templating engines, the [template_method][files#template_method] attribute specifies how the promised file content will be resolved. The value `inline_mustache` indicates that we will use the mustache templating engine and specify the template in-line, instead of in an external file.

##### edit_template_string

```cf3
      edit_template_string  => "$(config_template_string)",
```

The `edit_template_string` attribute is set to `$(config_template_string)` which holds the mustache template used to render the file content.

##### template_data

```cf3
      template_data         => mergedata( '{ "driftfile": "$(driftfile)", "servers": servers }' ),
```

`template_data` is assigned a data container that is in this case constructed by [`mergedata()`][mergedata] so that only the necessary data is provided to the template. If `template_data` is not explicitly provided, CFEngine uses `datastate()` by default. It is considered best practice to provide explicit data as this makes it easier to delegate responsibility of the template and that data to different entities where neither are required to know anything about CFEngine itself and it's *much* more efficient to send the templating engine only the data the template actually uses.

Note, `mergedata()` tries to expand bare values from CFEngine variables, so `servers` will expand to the entire list of servers. The result of `mergedata()` in the example is equivalent to this json:

```json
{
  "driftfile": "/var/lib/ntp/drift",
  "servers": [ "time.nist.gov" ]
}
```

Now that we have dissected the policy, let's go ahead and give it a whirl.

### Modify and run the policy

```console
[root@hub masterfiles]# cf-agent -KIf update.cf;
    info: Copied file '/var/cfengine/masterfiles/services/ntp.cf' to '/var/cfengine/inputs/services/ntp.cf.cfnew' (mode '600')

[root@hub masterfiles]# cf-agent -KI
    info: Updated rendering of '/etc/ntp.conf' from mustache template 'inline'
    info: files promise '/etc/ntp.conf' repaired
    info: Executing 'no timeout' ... '/etc/init.d/ntpd restart'
    info: Completed execution of '/etc/init.d/ntpd restart'
R: NTP service restarted after configuration change
```

More interestingly, if you examine the configuration file `/etc/ntp.conf`, you will notice that it has been updated with the time `server`(s) and `driftfile` you had specified in the policy, for that specific operating system environment. This is the configuration that the NTP service has been restarted with.

```console
[root@hub masterfiles]# grep -P "^(driftfile|server)" /etc/ntp.conf
driftfile /var/lib/ntp/drift
server time.nist.gov iburst
```

Mission Accomplished!

## Instrumenting for tunability via Augments

Next we will augment file/template management with data sourced from a JSON data file. This is a simple extension of what we have done previously illustrating how tunables in policy can be exposed and leveraged from a data feed.

CFEngine offers out-of-the-box support for reading and writing JSON data structures. In this tutorial, we will default the NTP configuration properties in policy, but provide a path for the properties to be overridden from Augments.

```cf3
bundle agent ntp
{
   vars:
     linux::
       "ntp_package_name" string => "ntp";
       "config_file" string => "/etc/ntp.conf";

       # Set the default value for driftfile
       "driftfile"
         string => "/var/lib/ntp/drift";

       # Overwrite driftfile with value defined from Augments if it's provided
       "driftfile"
         string => "$(def.ntp[config][driftfile])",
         if => isvariable( "def.ntp[config][driftfile]" );

       # Set the default value for servers
       "servers"
         slist => { "time.nist.gov" };

       # Overwrite servers with value defined from Augments if it's provided
       "servers"
         slist => getvalues( "def.ntp[config][servers]" ),
         if => isvariable( "def.ntp[config][servers]" );

      # For brevity, and since the template is small, we define it in-line
       "config_template_string"
         string => "# NTP Config managed by CFEngine
driftfile {{{driftfile}}}
restrict default kod nomodify notrap nopeer noquery
restrict -6 default kod nomodify notrap nopeer noquery
restrict 127.0.0.1
restrict -6 ::1
{{#servers}} 
server {{{.}}} iburst
{{/servers}}
includefile /etc/ntp/crypto/pw
keys /etc/ntp/keys
";

     redhat::
         "ntp_service_name" string => "ntpd";

     debian::
         "ntp_service_name" string => "ntp";

   packages:
       "$(ntp_package_name)"   -> { "StandardsDoc 3.2.1" } 
         policy          => "present",
         handle          => "ntp_packages_$(ntp_package_name)",
         classes         => results("bundle", "ntp_package");

   files:
    "$(config_file)"
      create                => "true",
      handle                => "ntp_files_conf",
      perms                 => mog( "644", "root", "root" ),
      template_method       => "inline_mustache",
      edit_template_string  => "$(config_template_string)",
      template_data         => mergedata( '{ "driftfile": "$(driftfile)", "servers": servers }' ),
      classes               => results( "bundle", "ntp_config" );

   services:
     "$(ntp_service_name)" -> { "StandardsDoc 3.2.2" } 
       service_policy => "start",
       classes => results( "bundle", "ntp_service_running" );

    ntp_config_repaired::
     "$(ntp_service_name)" -> { "StandardsDoc 3.2.2" } 
       service_policy => "restart",
       classes => results( "bundle", "ntp_service_config_change" );


   reports:
     ntp_service_running_repaired.inform_mode::
       "NTP service started";

     ntp_service_config_change_repaired.inform_mode::
       "NTP service restarted after configuration change";

}
```

What does this policy do?

Let's review the changes to the vars promises as they were the only changes made.

#### vars

```cf3
bundle agent ntp
{
   vars:
     linux::
       "ntp_package_name" string => "ntp";
       "config_file" string => "/etc/ntp.conf";

       # Set the default value for driftfile
       "driftfile"
         string => "/var/lib/ntp/drift";

       # Overwrite driftfile with value defined from Augments if it's provided
       "driftfile"
         string => "$(def.ntp[config][driftfile])",
         if => isvariable( "def.ntp[config][driftfile]" );

       # Set the default value for servers
       "servers"
         slist => { "time.nist.gov" };

       # Overwrite servers with value defined from Augments if it's provided
       "servers"
         slist => getvalues( "def.ntp[config][servers]" ),
         if => isvariable( "def.ntp[config][servers]" );
```

Notice two promises were introduced, one setting `driftfile` to the value of `$(def.ntp[config][driftfile])` if it is defined and one setting servers to the list of values for `def.ntp[config][servers]` if it is defined. [Augments][Augments] allows for variables to be set in the *def* bundle scope very early before policy is evaluated.

### Modify and run the policy

First modify `services/ntp.cf` as shown previously (don't forget to check syntax with `cf-promises` after modification), then run the policy.


```console
[root@hub masterfiles]# cf-agent -KIf update.cf
    info: Copied file '/var/cfengine/masterfiles/services/ntp.cf' to '/var/cfengine/inputs/services/ntp.cf.cfnew' (mode '600')
    info: Copied file '/var/cfengine/masterfiles/def.json' to '/var/cfengine/inputs/def.json.cfnew' (mode '600')

[root@hub masterfiles]# cf-agent -KI
```

We do not expect to see the ntp configuration file modified or the service to be restarted since we have only instrumented the policy so far.

Now, let's modify `def.json` (in the root of masterfiles) and define some different values for `driftfile` and `servers`.
Modify `def.json` so that it looks like this:

```json
{
  "inputs": [ "services/ntp.cf" ],
  "vars": {
    "control_common_bundlesequence_end": [ "ntp" ],
    "ntp": {
      "config": {
        "driftfile": "/tmp/drift",
        "servers": [ "0.north-america.pool.ntp.org", "1.north-america.pool.ntp.org",
                     "2.north-america.pool.ntp.org", "3.north-america.pool.ntp.org" ]
      }
    }
  }
}
```

Now, let's validate the JSON and force a policy run and inspect the result.


```console
[root@hub masterfiles]# python -m json.tool < def.json
{
    "inputs": [
        "services/ntp.cf"
    ], 
    "vars": {
        "control_common_bundlesequence_end": [
            "ntp"
        ], 
        "ntp": {
            "config": {
                "driftfile": "/tmp/drift", 
                "servers": [
                    "0.north-america.pool.ntp.org", 
                    "1.north-america.pool.ntp.org", 
                    "2.north-america.pool.ntp.org", 
                    "3.north-america.pool.ntp.org"
                ]
            }
        }
    }
}

[root@hub masterfiles]# cf-agent -KI
    info: Updated rendering of '/etc/ntp.conf' from mustache template 'inline'
    info: files promise '/etc/ntp.conf' repaired
    info: Executing 'no timeout' ... '/etc/init.d/ntpd restart'
    info: Completed execution of '/etc/init.d/ntpd restart'
R: NTP service restarted after configuration change
    info: Can not acquire lock for 'ntp' package promise. Skipping promise evaluation
    info: Can not acquire lock for 'ntp' package promise. Skipping promise evaluation

[root@hub masterfiles]# grep -P "^(driftfile|server)" /etc/ntp.conf
driftfile /tmp/drift
server 0.north-america.pool.ntp.org iburst
server 1.north-america.pool.ntp.org iburst
server 2.north-america.pool.ntp.org iburst
server 3.north-america.pool.ntp.org iburst
```

Mission Accomplished!

You have successfully completed this tutorial that showed you how to write a simple policy to ensure that NTP is installed, running and configured appropriately.

