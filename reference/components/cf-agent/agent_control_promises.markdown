---
layout: default
title: cf-agent control promises
categories: [Reference, Components, cf-agent, cfagent control promises]
published: true
alias: reference-components-cf-agent-control-promises.html
tags: [Reference, Components, cf-agent, control promises]
---

    body agent control
    {
    123_456_789::

      domain => "mydomain.com";

    123_456_789_111::

      auditing => "true";

    any::

      fullencryption => "true";

    }

Settings describing the details of the fixed behavioural promises
made by `cf-agent`.


#### `abortclasses`

**Type**: slist

**Allowed input range**: `.*`

**Synopsis**: A list of classes which if defined lead to
termination of cf-agent

     body agent control
    
      {
      abortclasses => { "danger.*", "should_not_continue" };
      }

**Notes**:

A list of class regular expressions that `cf-agent` will watch out
for. If any matching class becomes defined, it will cause the
current execution of `cf-agent` to be aborted. This may be used for
validation, for example. To handle class expressions, simply create
an alias for the expression with a single name.



## `abortbundleclasses`

**Type**: slist

**Allowed input range**: `.*`

**Synopsis**: A list of classes which if defined lead to
termination of current bundle


This example shows how to use the feature to validate input to a
method bundle.

    body common control
    
    {
    bundlesequence  => { "testbundle"  };
    version => "1.2.3";
    }
    
    ###########################################
    
    body agent control
    
    {
    abortbundleclasses => { "invalid.*" };
    }
    
    ###########################################
    
    bundle agent testbundle
    {
    vars:
    
     "userlist" slist => { "xyz", "mark", "jeang", "jonhenrik", "thomas", "eben" };
    
    methods:
    
     "any" usebundle => subtest("$(userlist)");
    
    }
    
    ###########################################
    
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

**Notes**:

A list of regular expressions for classes, or class expressions
that `cf-agent` will watch out for. If any of these classes becomes
defined, it will cause the current bundle to be aborted. This may
be used for validation, for example.



## `addclasses`

**Type**: slist

**Allowed input range**: `.*`

**Synopsis**: A list of classes to be defined always in the current
context


Add classes adds global, literal classes. The only predicates
available during the control section are hard-classes.

    any::
    
      addclasses => { "My_Organization" }
    
    solaris::
    
      addclasses => { "some_solaris_alive", "running_on_sunshine" };
    

**Notes**:

Another place to make global aliases for system hardclasses.
Classes here are added unqeuivocally to the system. If classes are
used to predicate definition, then they must be defined in terms of
global hard classes.



## `agentaccess`

**Type**: slist

**Allowed input range**: `.*`

**Synopsis**: A list of user names allowed to execute cf-agent

     agentaccess => { "mark", "root", "sudo" };

**Notes**:

A list of user names that will be allowed to attempt execution of
the current configuration. This is mainly a sanity check rather
than a security measure.



## `agentfacility`

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

**Synopsis**: The syslog facility for cf-agent

    agentfacility => "LOG_USER";

**Notes**:

Sets the agent's syslog facility level. See the manual pages for
syslog. This is ignored on Windows, as CFEngine Enterprise creates event
logs.



## `allclassesreport`

**Type**: (menu option)

**Allowed input range**:

       true
       false
       yes
       no
       on
       off

**Synopsis**: Generate allclasses.txt report

    body agent control
    {
    allclassesreport => "true";
    }

**Notes**:

*History*: Was introduced in 3.2.0, Enterprise 2.1.0 (2011)

This option determines whether state/allclasses.txt file is written
to disk during agent execution. This functionality is retained only
for CFEngine 2 compatibility as more convenient facilities exist in
CFEngine 3 language to achieve similar results.

This option is turned off by default.



## `alwaysvalidate`

**Type**: (menu option)

**Allowed input range**:

       true
       false
       yes
       no
       on
       off

**Synopsis**: true/false flag to determine whether configurations
will always be checked before executing, or only after updates

    body agent control
    {
    Min00_05::
    
      # revalidate once per hour, regardless of change in configuration
    
      alwaysvalidate => "true";
    }

**Notes**:

*History*: Was introduced in version 3.1.2,Enterprise 2.0.1 (2010)

The agents `cf-agent`, and `cfserverd` etc can run `cf-promises` to
validate inputs before attempting to execute a configuration. As of
version 3.1.2 core, this only happens if the configuration file has
changed to save CPU cycles. When this attribute is set, `cf-agent`
will force a revalidation of the input.



## `auditing`

**Type**: (menu option)

**Allowed input range**:

       true
       false
       yes
       no
       on
       off

**Default value:** false

**Synopsis**: This option is deprecated, does nothing and is kept
for backward compatibility

    body agent control
    {
    auditing  => "true";
    }

**Notes**:

If this is set, CFEngine will perform auditing on promises in the
current configuration. This means that all details surrounding the
verification of the current promise will be recorded in the audit
database.

## `binarypaddingchar`

**Type**: string

**Allowed input range**: (arbitrary string)

**Default value:** space (ASC=32)

**Synopsis**: Character used to pad unequal replacements in binary
editing

    body agent control
    {
    binarypaddingchar => "#";
    }

**Notes**:

When editing binary files, it can be dangerous to replace a text
string with one that is longer or shorter as byte references and
jumps would be destroyed. CFEngine will therefore not allow
replacements that are larger in size than the original, but shorter
strings can be padded out to the same length.

**Default value**:

The `binarypaddingchar` defaults to the empty string (i.e., no
padding)



## `bindtointerface`

**Type**: string

**Allowed input range**: `.*`

**Synopsis**: Use this interface for outgoing connections

    bindtointerface => "192.168.1.1";

**Notes**:

On multi-homed hosts, the server and client can bind to a specific
interface for server traffic. The IP address of the interface must
be given as the argument, not the device name.



## `hashupdates`

**Type**: (menu option)

**Allowed input range**:

       true
       false
       yes
       no
       on
       off

**Default value:** false

**Synopsis**: true/false whether stored hashes are updated when
change is detected in source

    body agent control
    {
    hashupdates => "true";
    }

**Notes**:

If 'true' the stored reference value is updated as soon as a
warning message has been given. As most changes are benign (package
updates etc) this is a common setting.



## `childlibpath`

**Type**: string

**Allowed input range**: `.*`

**Synopsis**: LD\_LIBRARY\_PATH for child processes

    body agent control
    {
    childlibpath => "/usr/local/lib:/usr/local/gnu/lib";
    }

**Notes**:

This string may be used to set the internal `LD_LIBRARY_PATH`
environment of the agent.



## `checksum_alert_time`

**Type**: int

**Allowed input range**: `0,60`

**Default value:** 10 mins

**Synopsis**: The persistence time for the checksum\_alert class

    body agent control
    {
    checksum_alert_time => "30";
    }

**Notes**:

When checksum changes trigger an alert, this is registered as a
persistent class. This value determines the longevity of that
class.



## `defaultcopytype`

**Type**: (menu option)

**Allowed input range**:

       mtime
       atime
       ctime
       digest
       hash
       binary

**Synopsis**: ctime or mtime differ

    body agent control
    {
    #...
    defaultcopytype => "digest";
    }

**Notes**:

Sets the global default policy for comparing source and image in
copy transactions.



## `default_repository`

**Type**: string

**Allowed input range**: `"?(/.*)`

**Default value:** in situ

**Synopsis**: Path to the default file repository

    body agent control
    {
    default_repository => "/var/cfengine/repository";
    }

**Notes**:

If defined the default repository is the location where versions of
files altered by CFEngine are stored. This should be understood in
relation to the policy for 'backup' in copying, editing etc. If the
backups are time-stamped, this becomes effective a version control
repository. See also [repository](#repository-in-files) for a way
to locally override the global repository.

Note that when a repository is specified, the files are stored
using the canonified directory name of the original file,
concatenated with the name of the file. So, for example,
/usr/local/etc/postfix.conf would ordinarily be stored in an
alternative repository as \_usr\_local\_etc\_postfix.conf.cfsaved.

## `default_timeout`

**Type**: int

**Allowed input range**: `0,99999999999`

**Default value:** 10 seconds

**Synopsis**: Maximum time a network connection should attempt to
connect

    body agent control
    {
    default_timeout => "10";
    }

**Notes**:

The time is in seconds. It is not a guaranteed number, since it
depends on system behaviour. under Linux, the kernel version plays
a role, since not all system calls seem to respect the signals.

## `dryrun`

**Type**: (menu option)

**Allowed input range**:

       true
       false
       yes
       no
       on
       off

**Default value:** false

**Synopsis**: All talk and no action mode

    body agent control
    {
    dryrun => "true";
    }

**Notes**:

If set in the configuration, CFEngine makes no changes to a system,
only reports what it needs to do.



## `editbinaryfilesize`

**Type**: int

**Allowed input range**: `0,99999999999`

**Default value:** 100000

**Synopsis**: Integer limit on maximum binary file size to be
edited

    body agent control
    {
    edibinaryfilesize => "10M";
    }

**Notes**:

The global setting for the file-editing safety-net for binary files
(this value may be overridden on a per-promise basis with
`max_file_size`, See
[edit\_defaults in files](#edit_005fdefaults-in-files). The default
value for `editbinaryfilesize` is `100k`. Note the use of special
units is allowed, See
[Datatypes in CFEngine 3](#Datatypes-in-CFEngine-3), for a list of
permissible suffixes.

When setting limits, the limit on editing binary files should
generally be set higher than for text files.



## `editfilesize`

**Type**: int

**Allowed input range**: `0,99999999999`

**Default value:** 100000

**Synopsis**: Integer limit on maximum text file size to be edited

    body agent control
    {
    editfilesize => "120k";
    }

**Notes**:

The global setting for the file-editing safety-net (this value may
be overridden on a per-promise basis with `max_file_size`, See
[edit\_defaults in files](#edit_005fdefaults-in-files). Note the
use of special units is allowed, See
[Datatypes in CFEngine 3](#Datatypes-in-CFEngine-3), for a list of
permissible suffixes.



## `environment`

**Type**: slist

**Allowed input range**: `[A-Za-z0-9_]+=.*`

**Synopsis**: List of environment variables to be inherited by
children

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

**Notes**:

This may be used to set the runtime environment of the agent
process. The values of environment variables are inherited by child
commands. Some interactive programs insist on values being set,
e.g.
    # Required by apt-cache, debian
    
    environment => { "LANG=C"};



## `expireafter`

**Type**: int

**Allowed input range**: `0,99999999999`

**Default value:** 1 min

**Synopsis**: Global default for time before on-going promise
repairs are interrupted

    body action example
    {
    ifelapsed   => "120";   # 2 hours
    expireafter => "240";   # 4 hours
    }

**Notes**:

The locking time after which CFEngine will attempt to kill and
restart its attempt to keep a promise.



## `files_single_copy`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: List of filenames to be watched for multiple-source
conflicts

    body agent control
    {
    files_single_copy => { "/etc/.*", "/special/file" };
    }

**Notes**:

This list of regular expressions will ensure that files matching
the patterns of the list are never copied from more than one source
during a single run of `cf-agent`. This may be considered a
protection against accidential overlap of copies from diverse
remote sources, or as a first-come-first-served disambiguation tool
for lazy-evaluation of overlapping file-copy promises.



## `files_auto_define`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: List of filenames to define classes if copied

    body agent control
    {
    files_auto_define => { "/etc/syslog\.c.*", "/etc/passwd" };
    }

**Notes**:

Classes are automatically defined by the files that are copied. The
file is named according to the prefixed \`canonization' of the file
name. Canonization means that non-identifier characters are
converted into underscores. Thus /etc/passwd would canonize to
'\_etc\_passwd'. The prefix 'auto\_' is added to clarify the origin
of the class. Thus in the example the copying of /etc/passwd would
lead to the class 'auto\_\_etc\_passwd' being defined
automatically.



## `hostnamekeys`

**Type**: (menu option)

**Allowed input range**:

       true
       false
       yes
       no
       on
       off

**Default value:** false

**Synopsis**: true/false label ppkeys by hostname not IP address


    body server control
    {
    hostnamekeys => "true";
    }

**Notes**:

Client side choice to base key associations on host names rather
than IP address. This is useful for hosts with dynamic addresses.

**This feature has been deprecated since 3.1.0.** Host
identification is now handled transparently.



## `ifelapsed`

**Type**: int

**Allowed input range**: `0,99999999999`

**Default value:** 1

**Synopsis**: Global default for time that must elapse before
promise will be rechecked

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

**Notes**:

This overrides the global settings. Promises which take a long time
to verify should usually be protected with a long value for this
parameter. This serves as a resource \`spam' protection. A CFEngine
check could easily run every 5 minutes provided resource intensive
operations are not performed on every run. Using time classes like
`Hr12` etc., is one part of this strategy; using `ifelapsed` is
another which is not tied to a specific time.



## `inform`

**Type**: (menu option)

**Allowed input range**:

       true
       false
       yes
       no
       on
       off

**Default value:** false

**Synopsis**: true/false set inform level default

    body agent control
    {
    inform => "true";
    }

**Notes**:

Equivalent to (and when present, overrides) the command line option
'-I'. Sets the default output level \`permanently' within the class
context indicated.

Every promiser makes an implicit default promise to use output
settings declared using `outputs` promises.



## `intermittency`

**Type**: (menu option)

**Allowed input range**:

       true
       false
       yes
       no
       on
       off

**Default value:** false

**Synopsis**: This option is deprecated, does nothing and is kept
for backward compatibility


**Notes**:



## `max_children`

**Type**: int

**Allowed input range**: `0,99999999999`

**Default value:** 1 concurrent agent promise

**Synopsis**: Maximum number of background tasks that should be
allowed concurrently

    body runagent control
    {
    max_children => "10";
    }
    
    # or
    
    body agent control
    {
    max_children => "10";
    }

**Notes**:

For the run-agent this represents the maximum number of forked
background processes allowed when parallelizing connections to
servers. For the agent it represents the number of background jobs
allowed concurrently. Background jobs often lead to contention of
the disk resources slowing down tasks considerably; there is thus a
law of diminishing returns.



## `maxconnections`

**Type**: int

**Allowed input range**: `0,99999999999`

**Default value:** 30 remote queries

**Synopsis**: Maximum number of outgoing connections to cf-serverd

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

**Notes**:

Watch out for kernel limitations for maximum numbers of open file
descriptors which can limit this.



## `mountfilesystems`

**Type**: (menu option)

**Allowed input range**:

       true
       false
       yes
       no
       on
       off

**Default value:** false

**Synopsis**: true/false mount any filesystems promised

    body agent control
    {
    mountfilesystems => "true";
    }

**Notes**:

Issues the generic command to mount file systems defined in the
file system table.



## `nonalphanumfiles`

**Type**: (menu option)

**Allowed input range**:

       true
       false
       yes
       no
       on
       off

**Default value:** false

**Synopsis**: true/false warn about filenames with no alphanumeric
content

    body agent control
    {
    nonalphanumfiles => "true";
    }

**Notes**:

This test is applied in all recursive/depth searches.



## `repchar`

**Type**: string

**Allowed input range**: `.`

**Default value:** \_

**Synopsis**: The character used to canonize pathnames in the file
repository

    body agent control
    {
    repchar => "_";
    }

**Notes**:



## `refresh_processes`

**Type**: slist

**Allowed input range**: `[a-zA-Z0-9_$(){}\[\].:]+`

**Synopsis**: Reload the process table before verifying the bundles
named in this list (lazy evaluation)

    body agent control
    {
    refresh_processes => { "mybundle" };
    #refresh_processes => { "none" };
    }

**Notes**:

*History*: Was introduced in version 3.1.3, Enterprise 2.0.2 (2010)

If this list of regular expressions is non-null and an existing
bundle is mentioned or matched in this list, CFEngine will reload
the process table at the start of the named bundle, each time is is
scheduled. If the list is null, the process list will be reloaded
at the start of every scheduled bundle.

In the example above we use a non-empty list with the name \`none'.
This is not a reserved word, but as long as there are no bundles
with the name \`none' this has the effect of *never* reloading the
process table. This keeps improves the efficiency of the agent.



## `secureinput`

**Type**: (menu option)

**Allowed input range**:

       true
       false
       yes
       no
       on
       off

**Default value:** false

**Synopsis**: true/false check whether input files are writable by
unauthorized users

    body agent control
    {
    secureinput => "true";
    }

**Notes**:

If this is set, the agent will not accept an input file that is not
owned by a privileged user.



## `sensiblecount`

**Type**: int

**Allowed input range**: `0,99999999999`

**Default value:** 2 files

**Synopsis**: Minimum number of files a mounted filesystem is
expected to have

    body agent control 
    {
    sensiblecount => "20";
    }

**Notes**:



## `sensiblesize`

**Type**: int

**Allowed input range**: `0,99999999999`

**Default value:** 1000 bytes

**Synopsis**: Minimum number of bytes a mounted filesystem is
expected to have

    body agent control
    {
    sensiblesize => "20K";
    }

**Notes**:



## `skipidentify`

**Type**: (menu option)

**Allowed input range**:

       true
       false
       yes
       no
       on
       off

**Default value:** false

**Synopsis**: Do not send IP/name during server connection because
address resolution is broken

    body agent control
    {
    skipidentify => "true";
    }

**Notes**:

Hosts that are not registered in DNS cannot supply reasonable
credentials for a secondary confirmation of their identity to a
CFEngine server. This causes the agent to ignore its missing DNS
credentials.



## `suspiciousnames`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: List of names to warn about if found during any file
search

    body agent control
    {
    suspiciousnames => { ".mo", "lrk3", "rootkit" };
    }

**Notes**:

If CFEngine sees these names during recursive (depth) file searches
it will warn about them.



## `syslog`

**Type**: (menu option)

**Allowed input range**:

       true
       false
       yes
       no
       on
       off

**Default value:** false

**Synopsis**: true/false switches on output to syslog at the inform
level

    body agent control
    {
    syslog => "true";
    }

**Notes**:



## `track_value`

**Type**: (menu option)

**Allowed input range**:

       true
       false
       yes
       no
       on
       off

**Default value:** false

**Synopsis**: true/false switches on tracking of promise valuation

    body agent control
    {
    track_value => "true";
    }

**Notes**:

If this is true, CFEngine generates a log in
WORKDIR/state/cf\_value.log of the estmated \`business value' of
the system automation as a running log, `value_kept`, etc. The
format of the file is
    date,sum value kept,sum value repaired,sum value notkept



## `timezone`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: List of allowed timezones this machine must comply
with

    body agent control
    {
    timezone => { "MET", "CET", "GMT+1" };
    }

**Notes**:



## `verbose`

**Type**: (menu option)

**Allowed input range**:

       true
       false
       yes
       no
       on
       off

**Default value:** false

**Synopsis**: true/false switches on verbose standard output

    body agent control
    {
    verbose => "true";
    }

**Notes**:

Equivalent to (and when present, overrides) the command line option
'-v'. Sets the default output level \`permanently' for this
promise.

Every promiser makes an implicit default promise to use output
settings declared using `outputs` promises.

