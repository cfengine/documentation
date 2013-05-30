---
layout: default
title: cf-agent control promises
categories: [Reference, Components, cf-agent, cfagent control promises]
published: true
alias: reference-components-cf-agent-control-promises.html
tags: [Reference, Components, cf-agent, control promises]
---

Settings describing the details of the fixed behavioural promises
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

**Type**: slist

**Allowed input range**: `.*`

**Description**: The `abortclasses` slist contains classes which if defined 
lead to termination of cf-agent.

Regular expressions are used for classes that `cf-agent` will watch out
for. If any matching class becomes defined, it will cause the
current execution of `cf-agent` to be aborted. This may be used for
validation, for example. To handle class expressions, simply create
an alias for the expression with a single name.

**Example**:
```cf3
     body agent control
    
      {
      abortclasses => { "danger.*", "should_not_continue" };
      }
```


### abortbundleclasses

**Type**: slist

**Allowed input range**: `.*`

**Description**: The `abortbundleclasses` slist contains classes which 
if defined lead to termination of current bundle.

Regular expressions are used for classes, or class expressions
that `cf-agent` will watch out for. If any of these classes becomes
defined, it will cause the current bundle to be aborted. This may
be used for validation, for example.

**Example**:
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

**Type**: slist

**Allowed input range**: `.*`

**Description**: The `addclasses` slist contains classes to be defined 
always in the current context.

This adds global, literal classes. The only predicates available during 
the control section are hard-classes.

**Example**:
```cf3

    any::
    
      addclasses => { "My_Organization" }
    
    solaris::
    
      addclasses => { "some_solaris_alive", "running_on_sunshine" };
```    

**Notes**:

Another place to make global aliases for system hardclasses.
Classes here are added unqeuivocally to the system. If classes are
used to predicate definition, then they must be defined in terms of
global hard classes.


### agentaccess

**Type**: slist

**Allowed input range**: `.*`

**Description**: A `agentaccess` slist contains user names that are 
allowed to execute cf-agent.

This represents a list of user names that will be allowed to attempt 
execution of the current configuration. This is mainly a sanity check 
rather than a security measure.

**Example**:
```cf3
     agentaccess => { "mark", "root", "sudo" };
```

### agentfacility

**Type**: (menu option)

**Allowed input range**:

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

**Default value:** LOG\_USER

**Description**: The `agentfacility` mentu option policy sets the agent's 
syslog facility level.

**Example**:
```cf3
    agentfacility => "LOG_USER";
```
**Notes**:

This is ignored on Windows, as CFEngine Enterprise creates event logs.

**See Also**: Manual pages for syslog. 

### allclassesreport

**Type**: (menu option)

**Allowed input range**:

       true
       false
       yes
       no
       on
       off

**Default value**: off

**Description**: The `allclassesreport` menu option policy determines
whether to generate the allclasses.txt report.

If set to true, the state/allclasses.txt file will be written to disk 
during agent execution. 

**Example**:
```cf3
    body agent control
    {
    allclassesreport => "true";
    }
```

**Notes**:

This functionality is retained only for CFEngine 2 compatibility as more 
convenient facilities exist in CFEngine 3 language to achieve similar 
results.

*History*: Was introduced in 3.2.0, Enterprise 2.1.0 (2011)


### alwaysvalidate

**Type**: (menu option)

**Allowed input range**:

       true
       false
       yes
       no
       on
       off

**Description**: The `alwaysvalidate` menu option policy is a true/false 
flag to determine whether configurations will always be checked before 
executing, or only after updates.

**Example**:
```cf3
    body agent control
    {
    Min00_05::
    
      # revalidate once per hour, regardless of change in configuration
    
      alwaysvalidate => "true";
    }
```

**Notes**:

The agents `cf-agent`, and `cfserverd` etc can run `cf-promises` to
validate inputs before attempting to execute a configuration. As of
version 3.1.2 core, this only happens if the configuration file has
changed to save CPU cycles. When this attribute is set, `cf-agent`
will force a revalidation of the input.

*History*: Was introduced in version 3.1.2,Enterprise 2.0.1 (2010)


### auditing

**Deprecated*: Yes. This menu option policy is deprecated, does 
nothing and is kept for backward compatibility.

**Type**: (menu option)

**Allowed input range**:

       true
       false
       yes
       no
       on
       off

**Default value:** false

**Example**:
```cf3
    body agent control
    {
    auditing  => "true";
    }
```


### binarypaddingchar

**Type**: string

**Allowed input range**: (arbitrary string)

**Default value:** space (ASC=32)

**Description**: The `binarypaddingchar` contains the character used to 
pad unequal replacements in binary editing.

When editing binary files, it can be dangerous to replace a text
string with one that is longer or shorter as byte references and
jumps would be destroyed. CFEngine will therefore not allow
replacements that are larger in size than the original, but shorter
strings can be padded out to the same length.

**Example**:
```cf3
    body agent control
    {
    binarypaddingchar => "#";
    }
```

**Default value**: empty (i.e., no padding)


### bindtointerface

**Type**: string

**Allowed input range**: `.*`

**Description**: The `bindtointerface` string describes the interface 
to be used for outgoing connections.

On multi-homed hosts, the server and client can bind to a specific
interface for server traffic. The IP address of the interface must
be given as the argument, not the device name.

**Example**:
```cf3
    bindtointerface => "192.168.1.1";
```


### hashupdates

**Type**: (menu option)

**Allowed input range**:

       true
       false
       yes
       no
       on
       off

**Default value:** false

**Description**: The `hashupdates` determines whether stored hashes are 
updated when change is detected in source.

If 'true' the stored reference value is updated as soon as a warning 
message has been given. As most changes are benign (package updates 
etc) this is a common setting.

**Example**:
```cf3
    body agent control
    {
    hashupdates => "true";
    }
```


### childlibpath

**Type**: string

**Allowed input range**: `.*`

**Description**: The `childlibpath` string contains the LD\_LIBRARY\_PATH 
for child processes.

This string may be used to set the internal `LD_LIBRARY_PATH` environment 
of the agent.

**Example**:
```cf3
    body agent control
    {
    childlibpath => "/usr/local/lib:/usr/local/gnu/lib";
    }
```


### checksum_alert_time

**Type**: int

**Allowed input range**: `0,60`

**Default value:** 10 mins

**Description**: The value of checksum_alert_time represents the 
persistence time for the checksum\_alert class.

When checksum changes trigger an alert, this is registered as a
persistent class. This value determines the longevity of that
class.

**Example**:
```cf3
    body agent control
    {
    checksum_alert_time => "30";
    }
```


### defaultcopytype

**Type**: (menu option)

**Allowed input range**:

       mtime
       atime
       ctime
       digest
       hash
       binary

**Description**: The `defaultcopytype` menu option policy sets the global 
default policy for comparing source and image in copy transactions.

**Example**:
```cf3
    body agent control
    {
    #...
    defaultcopytype => "digest";
    }
```


### default_repository

**Type**: string

**Allowed input range**: `"?(/.*)`

**Default value:** in situ

**Description**: The `default_repository` string contains the path to the 
default file repository.

If defined the default repository is the location where versions of
files altered by CFEngine are stored. This should be understood in
relation to the policy for 'backup' in copying, editing etc. If the
backups are time-stamped, this becomes effective a version control
repository. 

**Example**:
```cf3
    body agent control
    {
    default_repository => "/var/cfengine/repository";
    }
```

**Notes**: When a repository is specified, the files are stored
using the canonified directory name of the original file,
concatenated with the name of the file. So, for example,
/usr/local/etc/postfix.conf would ordinarily be stored in an
alternative repository as \_usr\_local\_etc\_postfix.conf.cfsaved.

**See also**: [repository](#repository-in-files) for a way
to locally override the global repository.


### default_timeout

**Type**: int

**Allowed input range**: `0,99999999999`

**Default value:** 10 seconds

**Description**: The value of `default_timeout` represents the maximum 
time a network connection should attempt to connect.

The time is in seconds. It is not a guaranteed number, since it
depends on system behaviour. 

**Example**:
```cf3
    body agent control
    {
    default_timeout => "10";
    }
```

**Notes**: Under Linux, the kernel version plays a role, 
since not all system calls seem to respect the signals.


### dryrun

**Type**: (menu option)

**Allowed input range**:

       true
       false
       yes
       no
       on
       off

**Default value:** false

**Description**: The `dryrun` menu option, if set, makes no changes to 
the system, and will only report what it needs to do.

**Example**:
```cf3
    body agent control
    {
    dryrun => "true";
    }
```


### editbinaryfilesize

**Type**: int

**Allowed input range**: `0,99999999999`

**Default value:** `100k`

**Description**: The value of `editbinaryfilesize` represents the limit 
on maximum binary file size to be edited.

This is a global setting for the file-editing safety-net for binary files,
and may be overridden on a per-promise basis with `max_file_size`. 

**Example**:
```cf3
    body agent control
    {
    edibinaryfilesize => "10M";
    }
```

**Notes**:

The use of special units is allowed (See [Datatypes in CFEngine 3]
(#Datatypes-in-CFEngine-3), for a list of permissible suffixes).

When setting limits, the limit on editing binary files should
generally be set higher than for text files.

**See Also**: [edit\_defaults in files](#edit_005fdefaults-in-files)


### editfilesize

**Type**: int

**Allowed input range**: `0,99999999999`

**Default value:** 100000

**Description**: The value of `editfilesize` is the limit on maximum text 
file size to be edited.

This is a global setting for the file-editing safety-net, and may be 
overridden on a per-promise basis with `max_file_size`.

**Example**:
```cf3
    body agent control
    {
    editfilesize => "120k";
    }
```

**Notes**:

Use of special units is allowed (See [Datatypes in CFEngine 3]
(#Datatypes-in-CFEngine-3) for a list of permissible suffixes).

**See Also**: [edit\_defaults in files](#edit_005fdefaults-in-files)


### environment

**Type**: slist

**Allowed input range**: `[A-Za-z0-9_]+=.*`

**Description**: The `environment` slist contains environment variables 
to be inherited by children.

This may be used to set the runtime environment of the agent process. 
The values of environment variables are inherited by child commands. 

**Example**:
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

**Type**: int

**Allowed input range**: `0,99999999999`

**Default value:** 1 min

**Description**: The value of `expireafter` is a global default for time 
before on-going promise repairs are interrupted.

This represents the locking time after which CFEngine will attempt to 
kill and restart its attempt to keep a promise.

**Example**:
```cf3
    body action example
    {
    ifelapsed   => "120";   # 2 hours
    expireafter => "240";   # 4 hours
    }
```


### files_single_copy

**Type**: slist

**Allowed input range**: (arbitrary string)

**Description**: The `files_single_copy` slist contains filenames to be 
watched for multiple-source conflicts.

This list of regular expressions will ensure that files matching
the patterns of the list are never copied from more than one source
during a single run of `cf-agent`. This may be considered a
protection against accidential overlap of copies from diverse
remote sources, or as a first-come-first-served disambiguation tool
for lazy-evaluation of overlapping file-copy promises.

**Example**:
```cf3
    body agent control
    {
    files_single_copy => { "/etc/.*", "/special/file" };
    }
```


### files_auto_define

**Type**: slist

**Allowed input range**: (arbitrary string)

**Description**: The `files_auto_define` slist contains filenames to 
define classes if copied.

Classes are automatically defined by the files that are copied. The
file is named according to the prefixed \`canonization' of the file
name. Canonization means that non-identifier characters are
converted into underscores. Thus /etc/passwd would canonize to
'\_etc\_passwd'. The prefix 'auto\_' is added to clarify the origin
of the class. Thus in the example the copying of /etc/passwd would
lead to the class 'auto\_\_etc\_passwd' being defined
automatically.

**Example**:
```cf3
    body agent control
    {
    files_auto_define => { "/etc/syslog\.c.*", "/etc/passwd" };
    }
```


### hostnamekeys

**Deprecated**: Yes, since 3.1.0. Host identification is now handled 
transparently.

**Type**: (menu option)

**Allowed input range**:

       true
       false
       yes
       no
       on
       off

**Default value:** false

**Description**: The `hostnamekeys` menu option policy determines whether 
to label ppkeys by hostname not IP address.

This represents a client side choice to base key associations on host 
names rather than IP address. This is useful for hosts with dynamic 
addresses.

**Example**:
```cf3
    body server control
    {
    hostnamekeys => "true";
    }
```


### ifelapsed

**Type**: int

**Allowed input range**: `0,99999999999`

**Default value:** 1

**Description**: The value of `ifelapsed` is a global default representing 
the time that must elapse before a promise will be rechecked.

This overrides the global settings. Promises which take a long time
to verify should usually be protected with a long value for this
parameter. This serves as a resource \`spam' protection. A CFEngine
check could easily run every 5 minutes provided resource intensive
operations are not performed on every run. Using time classes like
`Hr12` etc., is one part of this strategy; using `ifelapsed` is
another which is not tied to a specific time.

**Example**:
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

**Type**: (menu option)

**Allowed input range**:

       true
       false
       yes
       no
       on
       off

**Default value:** false

**Description**: The `inform` menu option policy sets the default  output 
level \`permanently' within the class context indicated.

It is equivalent to (and when present, overrides) the command line option
'-I'. 

**Example**:
```cf3
    body agent control
    {
    inform => "true";
    }
```

**Notes**:

Every promiser makes an implicit default promise to use output
settings declared using `outputs` promises.


### intermittency

**Deprecated**: Yes. This menu option policy does nothing and is 
kept for backward  compatibility.

**Type**: (menu option)

**Allowed input range**:

       true
       false
       yes
       no
       on
       off

**Default value:** false


### max_children

**Type**: int

**Allowed input range**: `0,99999999999`

**Default value:** 1 concurrent agent promise

**Description**: The value of `max_children` represents the maximum number 
of background tasks that should be allowed concurrently.

For the run-agent this is the maximum number of forked background 
processes allowed when parallelizing connections to servers. 
For the agent it represents the number of background jobs allowed 
concurrently. Background jobs often lead to contention of the disk 
resources slowing down tasks considerably; there is thus a law of 
diminishing returns.

**Example**:
```cf3
    body runagent control
    {
    max_children => "10";
    }
    
    # or
    
    body agent control
    {
    max_children => "10";
    }
```


### maxconnections

**Type**: int

**Allowed input range**: `0,99999999999`

**Default value:** 30 remote queries

**Description**: The value of `maxconnections` represents the maximum 
number of outgoing connections to cf-serverd.

**Example**:
```cf3
    # client side 
    
    body agent control
    {
    maxconnections => "1000";
    }
    
    # server side
    
    body server control
    {
    maxconnections => "1000";
    }
```

**Notes**:

Watch out for kernel limitations for maximum numbers of open file
descriptors which can limit this.


### mountfilesystems

**Type**: (menu option)

**Allowed input range**:

       true
       false
       yes
       no
       on
       off

**Default value:** false

**Description**: The `mountfilesystems` menu option policy determines 
whether to mount any filesystems promised.

It issues the generic command to mount file systems defined in the
file system table.

**Example**:
```cf3
    body agent control
    {
    mountfilesystems => "true";
    }
```


### nonalphanumfiles

**Type**: (menu option)

**Allowed input range**:

       true
       false
       yes
       no
       on
       off

**Default value:** false

**Description**: The `nonalphanumfiles` menu option policy determines 
whether to warn about filenames with no alphanumeric content.

This test is applied in all recursive/depth searches.

**Example**:
```cf3
    body agent control
    {
    nonalphanumfiles => "true";
    }
```

### repchar

**Type**: string

**Allowed input range**: `.`

**Default value:** \_

**Description**: The `repchar` string represents a character used to 
canonize pathnames in the file repository.

**Example**:
```cf3
    body agent control
    {
    repchar => "_";
    }
```

**Notes**:


### refresh_processes

**Type**: slist

**Allowed input range**: `[a-zA-Z0-9_$(){}\[\].:]+`

**Description**: The `refresh_processes` slist contains bundles to reload 
the process table before verifying the bundles named in this list 
(lazy evaluation).

If this list of regular expressions is non-null and an existing
bundle is mentioned or matched in this list, CFEngine will reload
the process table at the start of the named bundle, each time is is
scheduled. If the list is null, the process list will be reloaded
at the start of every scheduled bundle.

**Example**:
```cf3
    body agent control
    {
    refresh_processes => { "mybundle" };
    #refresh_processes => { "none" };
    }
```

**Notes**:

In the example above we use a non-empty list with the name \`none'.
This is not a reserved word, but as long as there are no bundles
with the name \`none' this has the effect of *never* reloading the
process table. This keeps improves the efficiency of the agent.

*History*: Was introduced in version 3.1.3, Enterprise 2.0.2 (2010)


### secureinput

**Type**: (menu option)

**Allowed input range**:

       true
       false
       yes
       no
       on
       off

**Default value:** false

**Description**: The `secureinput` menu option policy checks whether 
input files are writable by unauthorized users.

If this is set, the agent will not accept an input file that is not
owned by a privileged user.

**Example**:
```cf3
    body agent control
    {
    secureinput => "true";
    }
```


### sensiblecount

**Type**: int

**Allowed input range**: `0,99999999999`

**Default value:** 2 files

**Description**: The value of `sensiblecount` represents the minimum 
number of files a mounted filesystem is expected to have.

**Example**:
```cf3
    body agent control 
    {
    sensiblecount => "20";
    }
```


### sensiblesize

**Type**: int

**Allowed input range**: `0,99999999999`

**Default value:** 1000 bytes

**Description**: The value of `sensiblesize` represents the minimum 
number of bytes a mounted filesystem is expected to have.

**Example**:
```cf3
    body agent control
    {
    sensiblesize => "20K";
    }
```


### skipidentify

**Type**: (menu option)

**Allowed input range**:

       true
       false
       yes
       no
       on
       off

**Default value:** false

**Description**: The `skipidentify` menu option policy determines whether 
to send an IP/name during server connection because address resolution is 
broken.

Hosts that are not registered in DNS cannot supply reasonable
credentials for a secondary confirmation of their identity to a
CFEngine server. This causes the agent to ignore its missing DNS
credentials.

**Example**:
```cf3
    body agent control
    {
    skipidentify => "true";
    }
```


### suspiciousnames

**Type**: slist

**Allowed input range**: (arbitrary string)

**Description**: The `suspiciousnames` slist contains names to warn about 
if found during any file search.

If CFEngine sees these names during recursive (depth) file searches
it will warn about them.

**Example**:
```cf3
    body agent control
    {
    suspiciousnames => { ".mo", "lrk3", "rootkit" };
    }


### syslog

**Type**: (menu option)

**Allowed input range**:

       true
       false
       yes
       no
       on
       off

**Default value:** false

**Description**: The `syslog` menu option policy determines wether to 
switch on output to syslog at the inform level.

**Example**:
```cf3
    body agent control
    {
    syslog => "true";
    }
```


### track_value

**Type**: (menu option)

**Allowed input range**:

       true
       false
       yes
       no
       on
       off

**Default value:** false

**Description**: The `track_value` menu option policy determines whether 
to switch on tracking of promise valuation.

If this is true, CFEngine generates a log in
WORKDIR/state/cf\_value.log of the estmated \`business value' of
the system automation as a running log, `value_kept`, etc. The
format of the file is date, sum value kept, sum value repaired, 
sum value notkept.

**Example**:
```cf3
    body agent control
    {
    track_value => "true";
    }
```


### timezone

**Type**: slist

**Allowed input range**: (arbitrary string)

**Description**: The `timezone` slist contains allowed timezones this 
machine must comply with.

**Example**:
```cf3
    body agent control
    {
    timezone => { "MET", "CET", "GMT+1" };
    }
```


### verbose

**Type**: (menu option)

**Allowed input range**:

       true
       false
       yes
       no
       on
       off

**Default value:** false

**Description**: The `verbose` menu option policy determines whether to 
switch on verbose standard output.

It is equivalent to (and when present, overrides) the command line option
'-v'. Sets the default output level \`permanently' for this
promise.

**Example**:
```cf3
    body agent control
    {
    verbose => "true";
    }
```

**Notes**:

Every promiser makes an implicit default promise to use output
settings declared using `outputs` promises.

