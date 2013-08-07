---
layout: default
title: cf-agent
categories: [Reference, Components, cf-agent]
published: true
alias: reference-components-cfagent.html
tags: [Components, cf-agent]
---

`cf-agent` evaluates policy code and makes changes to the system. Policy 
bundles are evaluated in the order of the provided `bundlesequence` (this is normally specified in the
[`common control body`][Components and Common Control#Common Control]). For 
each bundle, `cf-agent` groups promise statements according to their type. 
Promise types are then evaluated in a preset order to ensure fast system 
convergence to policy.

`cf-agent` keeps the promises made in `common` and `agent` bundles, and is 
affected by `common` and `agent` control bodies.

## Command reference

    --bootstrap, -B
        Bootstrap CFEngine to the given policy server IP, hostname or :avahi (automatic detection)

    --bundlesequence, -b
        Set or override bundlesequence from command line

    --debug, -d
        Enable debugging output

    --define, -D
        Define a list of comma separated classes to be defined at the start of execution

    --self-diagnostics, -x
        Run checks to diagnose a CFEngine agent installation

    --dry-run, -n
        All talk and no action mode - make no changes, only inform of promises not kept

    --file, -f
        Specify an alternative input file than the default

    --help, -h
        Print the help message

    --inform, -I
        Print basic information about changes made to the system, i.e. promises repaired

    --negate, -N
        Define a list of comma separated classes to be undefined at the start of execution

    --no-lock, -K
        Ignore locking constraints during execution (ifelapsed/expireafter) if "too soon" to run

    --verbose, -v
        Output verbose information about the behaviour of the agent

    --version, -V
        Output the version of the software

    --legacy-output, -l
        Use legacy output format

    --color, -C
        Enable colorized output. Possible values: 'always', 'auto', 'never'. Default is 'never'

****

##Automatic Bootstrapping

Automatic bootstrapping allows the user to connect a CFEngine Host to a Policy
Server without specifying the IP address manually. It uses the *Avahi* service
discovery implementation of `zeroconf` to locate the Policy Server, obtain its IP
address, and then connect to it. To use automatic bootstrap, install the
following Avahi libraries:

* libavahi-client
* libavahi-common

To make the CFEngine Server discoverable, it needs to register itself as an 
Avahi service. Run the following command:

```
    $ /var/cfengine/bin/cf-serverd -A
```

This generates the configuration file for Avahi in `/etc/avahi/services` and 
restarts the Avahi daemon in order to register the new service.

From this point on, the Policy Server will be discovered with the Avahi service.
To verify that the server is visible, run the following command (requires
`avahi-utils`):

``` 
    $ avahi-browse -atr | grep cfenginehub
```

The sample output looks like this:

``` 
    eth0 IPv4 CFEngine Community 3.5.0 Policy Server on policy_hub_debian7
    _cfenginehub._tcp local
```

Once the Policy Server is configured with the Avahi service, you can
auto-bootstrap Hosts to it.

``` 
    $ /var/cfengine/bin/cf-agent -B :avahi
```

The Hosts require Avahi libraries to be installed in order to use this 
functionality. By default `cf-agent` looks for libraries in standard install 
locations. Install locations vary from system to system. If Avahi is 
installed in a non-standard location (i.e. compiled from source), set the 
`AVAHI_PATH` environmental variable to specify the path.

``` 
   $ AVAHI_PATH=/lib/libavahi-client.so.3 /var/cfengine/bin/cf-agent -B
```

If more than one server is found, or if the server has more than one IP
address, the list of all available servers is printed and the user is asked to
manually specify the IP address of the correct server by running the standard
bootstrap command of cf-agent:

``` 
   $ /var/cfengine/bin/cf-agent --bootstrap <IP address>
```

If only one Policy Server is found in the network, `cf-agent` performs the
bootstrap without further manual user intervention.

**Note:** Automatic bootstrapping support is ONLY for Linux, and it is limited
only to one subnet.

## Control Promises

Settings describing the details of the fixed behavioral promises
made by `cf-agent`.

```cf3
    body agent control
    {
    123_456_789::

      domain => "mydomain.com";

    123_456_789_111::

      auditing => "true";

    any::

      fullencryption => "true";

    }
```


### abortclasses

**Description:** The `abortclasses` slist contains classes which if defined 
lead to termination of cf-agent.

Regular expressions are used for classes that `cf-agent` will watch out
for. If any matching class becomes defined, it will cause the
current execution of `cf-agent` to be aborted. This may be used for
validation, for example. To handle class expressions, simply create
an alias for the expression with a single name.

**Type:** `slist`

**Allowed input range:** `.*`

**Example:**

```cf3
     body agent control
    
      {
      abortclasses => { "danger.*", "should_not_continue" };
      }
```

### abortbundleclasses

**Description:** The `abortbundleclasses` slist contains classes which 
if defined lead to termination of current bundle.

Regular expressions are used for classes, or class expressions
that `cf-agent` will watch out for. If any of these classes becomes
defined, it will cause the current bundle to be aborted. This may
be used for validation, for example.

**Type:** `slist`

**Allowed input range:** `.*`

**Example:**
This example shows how to use the feature to validate input to a
method bundle.

```cf3
    body common control
    
    {
    bundlesequence  => { "testbundle"  };
    version => "1.2.3";
    }
    
    #################################
    
    body agent control
    
    {
    abortbundleclasses => { "invalid.*" };
    }
    
    #################################
    
    bundle agent testbundle
    {
    vars:
    
     "userlist" slist => { "xyz", "mark", "jeang", "jonhenrik", "thomas", "eben" };
    
    methods:
    
     "any" usebundle => subtest("$(userlist)");
    
    }
    
    #################################
    
    bundle agent subtest(user)
    
    {
    classes:
    
      "invalid" not => regcmp("[a-z]{4}","$(user)");
    
    reports:
    
     !invalid::
    
      "User name $(user) is valid at exactly 4 letters";
    
     # abortbundleclasses will prevent this from being evaluated
     invalid::
    
      "User name $(user) is invalid";
    }
```


### addclasses

**Description:** The `addclasses` slist contains classes to be defined 
always in the current context.

This adds global, literal classes. The only predicates available during 
the control section are hard-classes.

**Type:** `slist`

**Allowed input range:** `.*`

**Example:**

```cf3

    any::
    
      addclasses => { "My_Organization" }
    
    solaris::
    
      addclasses => { "some_solaris_alive", "running_on_sunshine" };
```    

**Notes:**

Another place to make global aliases for system hardclasses.
Classes here are added unequivocally to the system. If classes are
used to predicate definition, then they must be defined in terms of
global hard classes.


### agentaccess

**Description:** A `agentaccess` slist contains user names that are 
allowed to execute cf-agent.

This represents a list of user names that will be allowed to attempt 
execution of the current configuration. This is mainly a sanity check 
rather than a security measure.

**Type:** `slist`

**Allowed input range:** `.*`

**Example:**

```cf3
     agentaccess => { "mark", "root", "sudo" };
```

### agentfacility

**Type:** (menu option)

**Allowed input range:**

       LOG_USER
       LOG_DAEMON
       LOG_LOCAL0
       LOG_LOCAL1
       LOG_LOCAL2
       LOG_LOCAL3
       LOG_LOCAL4
       LOG_LOCAL5
       LOG_LOCAL6
       LOG_LOCAL7

**Default value:** `LOG_USER`

**Description:** The `agentfacility` mentu option policy sets the agent's 
syslog facility level.

**Example:**

```cf3
    agentfacility => "LOG_USER";
```
**Notes:**

This is ignored on Windows, as CFEngine Enterprise creates event logs.

**See Also**: Manual pages for syslog. 

### allclassesreport

**Description:** The `allclassesreport` menu option policy determines
whether to generate the `allclasses.txt` report.

If set to true, the `state/allclasses.txt` file will be written to disk 
during agent execution. 

**Type:** [`boolean`][boolean]

**Default value:** false

**Example:**

```cf3
    body agent control
    {
    allclassesreport => "true";
    }
```

**Notes:**

This functionality is retained only for CFEngine 2 compatibility. As of
CFEngine 3.5, the [`classesmatching()`][classesmatching] function provides
a more convenient way to retrieve a list of set classes at execution time.

**History:** Was introduced in 3.2.4, Enterprise 2.1.4 (2011)

### alwaysvalidate

**Description:** The `alwaysvalidate` menu option policy is a true/false 
flag to determine whether configurations will always be checked before 
executing, or only after updates.

**Type:** [`boolean`][boolean]

**Example:**

```cf3
    body agent control
    {
    Min00_05::
    
      # revalidate once per hour, regardless of change in configuration
    
      alwaysvalidate => "true";
    }
```

**Notes:**

The agents `cf-agent` and `cfserverd` can run `cf-promises` to
validate inputs before attempting to execute a configuration. As of
version 3.1.2 core, this only happens if the configuration file has
changed to save CPU cycles. When this attribute is set, `cf-agent`
will force a revalidation of the input.

**History:** Was introduced in version 3.1.2,Enterprise 2.0.1 (2010)


### auditing

**Deprecated:** This menu option policy is deprecated, does 
nothing and is kept for backward compatibility.

**Type:** [`boolean`][boolean]

**Default value:** false

**Example:**

```cf3
    body agent control
    {
    auditing  => "true";
    }
```


### binarypaddingchar

**Description:** The `binarypaddingchar` contains the character used to 
pad unequal replacements in binary editing.

When editing binary files, it can be dangerous to replace a text
string with one that is longer or shorter as byte references and
jumps would be destroyed. CFEngine will therefore not allow
replacements that are larger in size than the original, but shorter
strings can be padded out to the same length.

**Type:** `string`

**Allowed input range:** (arbitrary string)

**Default value:** space (ASC=32)

**Example:**

```cf3
    body agent control
    {
    binarypaddingchar => "#";
    }
```

**Default value:** empty (i.e., no padding)


### bindtointerface

**Description:** The `bindtointerface` string describes the interface 
to be used for outgoing connections.

On multi-homed hosts, the server and client can bind to a specific
interface for server traffic. The IP address of the interface must
be given as the argument, not the device name.

**Type:** `string`

**Allowed input range:** `.*`

**Example:**

```cf3
    bindtointerface => "192.168.1.1";
```

### hashupdates

**Description:** The `hashupdates` determines whether stored hashes are 
updated when change is detected in source.

If 'true' the stored reference value is updated as soon as a warning 
message has been given. As most changes are benign (package updates 
etc) this is a common setting.

**Type:** [`boolean`][boolean]

**Default value:** false

**Example:**

```cf3
    body agent control
    {
    hashupdates => "true";
    }
```


### childlibpath

**Description:** The `childlibpath` string contains the LD\_LIBRARY\_PATH 
for child processes.

This string may be used to set the internal `LD_LIBRARY_PATH` environment 
of the agent.

**Type:** `string`

**Allowed input range:** `.*`

**Example:**

```cf3
    body agent control
    {
    childlibpath => "/usr/local/lib:/usr/local/gnu/lib";
    }
```


### checksum_alert_time

**Description:** The value of checksum_alert_time represents the 
persistence time for the checksum_alert class.

When checksum changes trigger an alert, this is registered as a
persistent class. This value determines the longevity of that
class.

**Type:** `int`

**Allowed input range:** `0,60`

**Default value:** 10 mins

**Example:**

```cf3
    body agent control
    {
    checksum_alert_time => "30";
    }
```

### defaultcopytype

**Description:** The `defaultcopytype` menu option policy sets the global 
default policy for comparing source and image in copy transactions.

**Type:** (menu option)

**Allowed input range:**

       mtime
       atime
       ctime
       digest
       hash
       binary

**Example:**

```cf3
    body agent control
    {
    #...
    defaultcopytype => "digest";
    }
```


### default_repository

**Description:** The `default_repository` string contains the path to the 
default file repository.

If defined the default repository is the location where versions of
files altered by CFEngine are stored. This should be understood in
relation to the policy for 'backup' in copying, editing etc. If the
backups are time-stamped, this becomes effective a version control
repository. 

**Type:** `string`

**Allowed input range:** `"?(/.*)`

**Default value:** in situ

**Example:**

```cf3
    body agent control
    {
    default_repository => "/var/cfengine/repository";
    }
```

**Notes:** When a repository is specified, the files are stored
using the canonified directory name of the original file,
concatenated with the name of the file. So, for example,
`/usr/local/etc/postfix.conf` would ordinarily be stored in an
alternative repository as `_usr_local_etc_postfix.conf.cfsaved`.

### default_timeout

**Description:** The value of `default_timeout` represents the maximum 
time a network connection should attempt to connect.

The time is in seconds. It is not a guaranteed number, since it
depends on system behavior. 

**Type:** `int`

**Allowed input range:** `0,99999999999`

**Default value:** 10 seconds

**Example:**

```cf3
    body agent control
    {
    default_timeout => "10";
    }
```

**Notes:** Under Linux, the kernel version plays a role, since not all system 
calls seem to respect the signals.

### dryrun

**Description:** The `dryrun` menu option, if set, makes no changes to 
the system, and will only report what it needs to do.

**Type:** [`boolean`][boolean]

**Default value:** false

**Example:**

```cf3
    body agent control
    {
    dryrun => "true";
    }
```


### editbinaryfilesize

**Description:** The value of `editbinaryfilesize` represents the limit 
on maximum binary file size to be edited.

This is a global setting for the file-editing safety-net for binary files,
and may be overridden on a per-promise basis with `max_file_size`. 

**Type:** `int`

**Allowed input range:** `0,99999999999`

**Default value:** `100k`

**Example:**

```cf3
    body agent control
    {
    edibinaryfilesize => "10M";
    }
```

**Notes:**
When setting limits, the limit on editing binary files should
generally be set higher than for text files.

### editfilesize

**Description:** The value of `editfilesize` is the limit on maximum text 
file size to be edited.

This is a global setting for the file-editing safety-net, and may be 
overridden on a per-promise basis with `max_file_size`.

**Type:** `int`

**Allowed input range:** `0,99999999999`

**Default value:** 100000

**Example:**

```cf3
    body agent control
    {
    editfilesize => "120k";
    }
```

### environment

**Description:** The `environment` slist contains environment variables 
to be inherited by children.

This may be used to set the runtime environment of the agent process. 
The values of environment variables are inherited by child commands. 

**Type:** `slist`

**Allowed input range:** `[A-Za-z0-9_]+=.*`

**Example:**

```cf3
    body common control
    {
    bundlesequence => { "one" };
    }
    
    body agent control
    {
    environment => { "A=123", "B=456", "PGK_PATH=/tmp"};
    }
    
    bundle agent one
    {
    commands:
    
      "/usr/bin/env";
    }
```

Some interactive programs insist on values being set, for example:

```cf3
    # Required by apt-cache, debian
    
    environment => { "LANG=C"};
```


### expireafter

**Description:** The value of `expireafter` is a global default for time 
before on-going promise repairs are interrupted.

This represents the locking time after which CFEngine will attempt to 
kill and restart its attempt to keep a promise.

**Type:** `int`

**Allowed input range:** `0,99999999999`

**Default value:** 1 min

**Example:**

```cf3
    body action example
    {
    ifelapsed   => "120";   # 2 hours
    expireafter => "240";   # 4 hours
    }
```

### files_single_copy

**Description:** The `files_single_copy` slist contains filenames to be 
watched for multiple-source conflicts.

This list of regular expressions will ensure that files matching
the patterns of the list are never copied from more than one source
during a single run of `cf-agent`. This may be considered a
protection against accidential overlap of copies from diverse
remote sources, or as a first-come-first-served disambiguation tool
for lazy-evaluation of overlapping file-copy promises.

**Type:** `slist`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
    body agent control
    {
    files_single_copy => { "/etc/.*", "/special/file" };
    }
```

### files_auto_define

**Description:** The `files_auto_define` slist contains filenames to 
define classes if copied.

Classes are automatically defined by the files that are copied. The
file is named according to the prefixed 'canonization' of the file
name. Canonization means that non-identifier characters are
converted into underscores. Thus `/etc/passwd` would canonize to
`_etc_passwd`. The prefix `auto_` is added to clarify the origin
of the class. Thus in the example the copying of `/etc/passwd` would
lead to the class `auto__etc_passwd` being defined
automatically.

**Type:** `slist`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
    body agent control
    {
    files_auto_define => { "/etc/syslog\.c.*", "/etc/passwd" };
    }
```

### hostnamekeys

**Deprecated:** Host identification is now handled transparently.

**Description:** The `hostnamekeys` menu option policy determines whether 
to label ppkeys by hostname not IP address.

This represents a client side choice to base key associations on host 
names rather than IP address. This is useful for hosts with dynamic 
addresses.

**Type:** [`boolean`][boolean]

**Default value:** false

**Example:**

```cf3
    body server control
    {
    hostnamekeys => "true";
    }
```

### ifelapsed

**Description:** The value of `ifelapsed` is a global default representing 
the time that must elapse before a promise will be rechecked.

This overrides the global settings. Promises which take a long time
to verify should usually be protected with a long value for this
parameter. This serves as a resource 'spam' protection. A CFEngine
check could easily run every 5 minutes provided resource intensive
operations are not performed on every run. Using time classes like
`Hr12` etc., is one part of this strategy; using `ifelapsed` is
another which is not tied to a specific time.

**Type:** `int`

**Allowed input range:** `0,99999999999`

**Default value:** 1

**Example:**

```cf3
    #local
    
    body action example
    {
    ifelapsed   => "120";   # 2 hours
    expireafter => "240";   # 4 hours
    }
    
    # global
    
    body agent control
    {
    ifelapsed   => "180";   # 3 hours
    }
```

### inform

**Description:** The `inform` menu option policy sets the default  output 
level 'permanently' within the class context indicated.

It is equivalent to (and when present, overrides) the command line option
'-I'. 

**Type:** [`boolean`][boolean]

**Default value:** false

**Example:**

```cf3
    body agent control
    {
    inform => "true";
    }
```

### intermittency

**Deprecated:** This attribute does nothing and is kept for backward  
compatibility.

**Type:** [`boolean`][boolean]

**Default value:** false


### max_children

**Description:** The value of `max_children` represents the maximum number 
of background tasks that should be allowed concurrently.

For the run-agent this is the maximum number of forked background 
processes allowed when parallelizing connections to servers. 
For the agent it represents the number of background jobs allowed 
concurrently. Background jobs often lead to contention of the disk 
resources slowing down tasks considerably; there is thus a law of 
diminishing returns.

**Type:** `int`

**Allowed input range:** `0,99999999999`

**Default value:** 1 concurrent agent promise

**Example:**

```cf3
    body agent control
    {
    max_children => "10";
    }
```


### maxconnections

**Description:** The value of `maxconnections` represents the maximum 
number of outgoing connections to `cf-serverd`.

**Type:** `int`

**Allowed input range:** `0,99999999999`

**Default value:** 30 remote queries

**Example:**

```cf3
    # client side 
    
    body agent control
    {
    maxconnections => "1000";
    }
```

**Notes:**

Watch out for kernel limitations for maximum numbers of open file
descriptors which can limit this.


### mountfilesystems

**Description:** The `mountfilesystems` menu option policy determines 
whether to mount any filesystems promised.

It issues the generic command to mount file systems defined in the
file system table.

**Type:** [`boolean`][boolean]

**Default value:** false

**Example:**

```cf3
    body agent control
    {
    mountfilesystems => "true";
    }
```

### nonalphanumfiles

**Description:** The `nonalphanumfiles` menu option policy determines 
whether to warn about filenames with no alphanumeric content.

This test is applied in all recursive/depth searches.

**Type:** [`boolean`][boolean]

**Default value:** false

**Example:**

```cf3
    body agent control
    {
    nonalphanumfiles => "true";
    }
```

### repchar

**Description:** The `repchar` string represents a character used to 
canonize pathnames in the file repository.

**Type:** `string`

**Allowed input range:** `.`

**Default value:** `_`

**Example:**

```cf3
    body agent control
    {
    repchar => "_";
    }
```

**Notes:**

### refresh_processes

**Description:** The `refresh_processes` slist contains bundles to reload 
the process table before verifying the bundles named in this list 
(lazy evaluation).

If this list of regular expressions is non-null and an existing
bundle is mentioned or matched in this list, CFEngine will reload
the process table at the start of the named bundle, each time is is
scheduled. If the list is null, the process list will be reloaded
at the start of every scheduled bundle.

**Type:** `slist`

**Allowed input range:** `[a-zA-Z0-9_$(){}\[\].:]+`

**Example:**

```cf3
    body agent control
    {
    refresh_processes => { "mybundle" };
    #refresh_processes => { "none" };
    }
```

This examples uses a non-empty list with the name 'none'. This is not a 
reserved word, but as long as there are no bundles with the name 'none' this 
has the effect of *never* reloading the process table. This keeps improves the 
efficiency of the agent.

**History:** Was introduced in version 3.1.3, Enterprise 2.0.2 (2010)

### secureinput

**Description:** The `secureinput` menu option policy checks whether 
input files are writable by unauthorized users.

If this is set, the agent will not accept an input file that is not
owned by a privileged user.

**Type:** [`boolean`][boolean]

**Default value:** false

**Example:**

```cf3
    body agent control
    {
    secureinput => "true";
    }
```

### sensiblecount

**Description:** The value of `sensiblecount` represents the minimum 
number of files a mounted filesystem is expected to have.

**Type:** `int`

**Allowed input range:** `0,99999999999`

**Default value:** 2 files

**Example:**

```cf3
    body agent control 
    {
    sensiblecount => "20";
    }
```

### sensiblesize

**Description:** The value of `sensiblesize` represents the minimum 
number of bytes a mounted filesystem is expected to have.

**Type:** `int`

**Allowed input range:** `0,99999999999`

**Default value:** 1000 bytes

**Example:**

```cf3
    body agent control
    {
    sensiblesize => "20K";
    }
```


### skipidentify

**Description:** The `skipidentify` menu option policy determines whether 
to send an IP/name during server connection because address resolution is 
broken.

Hosts that are not registered in DNS cannot supply reasonable
credentials for a secondary confirmation of their identity to a
CFEngine server. This causes the agent to ignore its missing DNS
credentials.

**Type:** [`boolean`][boolean]

**Default value:** false

**Example:**

```cf3
    body agent control
    {
    skipidentify => "true";
    }
```

### suspiciousnames

**Description:** The `suspiciousnames` slist contains names to warn about 
if found during any file search.

If CFEngine sees these names during recursive (depth) file searches
it will warn about them.

**Type:** `slist`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
    body agent control
    {
    suspiciousnames => { ".mo", "lrk3", "rootkit" };
    }
```

### syslog

**Description:** The `syslog` menu option policy determines wether to 
switch on output to syslog at the inform level.

**Type:** [`boolean`][boolean]

**Default value:** false

**Example:**

```cf3
    body agent control
    {
    syslog => "true";
    }
```

### track_value

**Description:** The `track_value` menu option policy determines whether 
to switch on tracking of promise valuation.

If true, CFEngine generates a log in `WORKDIR/state/cf_value.log` of the 
estimated 'business value' of the system automation as a running log, 
`value_kept`, etc. The format of the file is date, sum value kept, sum value 
repaired, sum value notkept.

**Type:** [`boolean`][boolean]

**Default value:** false

**Example:**

```cf3
    body agent control
    {
    track_value => "true";
    }
```


### timezone

**Description:** The `timezone` slist contains allowed timezones this 
machine must comply with.

**Type:** `slist`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
    body agent control
    {
    timezone => { "MET", "CET", "GMT+1" };
    }
```


### verbose

**Description:** The `verbose` menu option policy determines whether to 
switch on verbose standard output.

It is equivalent to (and when present, overrides) the command line option
'-v'. Sets the default output level 'permanently' for this
promise.

**Type:** [`boolean`][boolean]

**Default value:** false

**Example:**

```cf3
    body agent control
    {
    verbose => "true";
    }
```

