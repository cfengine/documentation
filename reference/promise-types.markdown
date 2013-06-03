---
layout: default
title: Promise Types and Attributes
categories: [Reference, Promise Types]
published: true
alias: reference-promise-types.html
tags: [reference, bundles, common, promises]
---

Within a bundle, the promise types are executed in a round-robin fashion in 
the following 'normal ordering'. Which promise types are available depends on 
the [bundle](manuals-language-concepts-bundles.html) type:

| Promise Type   | common | agent | server | monitor |
|----------------|:------:|:-----:|:------:|:--------|
| [meta](reference-promise-types-meta.html) - information about promise bundles | x      | x     | x      | x       |
| [vars](reference-promise-types-vars.html) - a variable, representing a value | x      | x     | x      | x       |
| [defaults](reference-promise-types-defaults.html) - a default value for bundle parameters | x      | x     | x      | x       |
| [classes](reference-promise-types-classes.html) - a class, representing a state of the system | x      | x     | x      | x       |
| [files](reference-promise-types-files.html) - configure a file |        | x     |        |         |
| [packages](reference-promise-types-packages.html) - install a package |        | x     |        |         |
| [guest_environments](reference-promise-types-guest_environments.html) |        | x     |        |         |
| [methods](reference-promise-types-methods.html) - take on a whole bundle of other promises |        | x     |        |         |
| [processes](reference-promise-types-processes.html) - start or terminate processes |        | x     |        |         |
| [services](reference-promise-types-services.html) - start or stop services |        | x     |        |         |
| [commands](reference-promise-types-commands.html) - execute a command |        | x     |        |         |
| [storage](reference-promise-types-storage.html) - verify attached storage |        | x     |        |         |
| [databases](reference-promise-types-databases.html) - configure a database |        | x     |        |         |
| [access](reference-promise-types-access.html) - grant or deny access to file objects |        |       | x      |         |
| [roles](reference-promise-types-roles.html) - allow certain users to activate certain classes |        |       | x      |         |
| [measurements](reference-promise-types-measurements.html) - measure or sample data from the system |        |       |        | x       |
| [reports](reference-promise-types-reports.html) - report a message | x      | x     | x      | x       |

See each promise type's reference documentation for detailed lists of 
available attributes.

## Common Attributes

The following attributes are available to all promise types.

### action

**Type**: `body action`

#### action_policy

**Type**: (menu option)

**Allowed input range**:   

```cf3
                    fix
                    warn
                    nop
```

**Description**: The `action_policy` menu option policy determines whether 
to repair or report about non-kept promises. The `action` settings allow 
general transaction control to be implemented on promise verification. 
Action bodies place limits on how often to verify the promise and what 
classes to raise in the case that the promise can or cannot be kept.


**Example**:

The following example shows a simple use of transaction control:

```cf3
     
     body action warn_only {
     action_policy => "warn";
     ifelapsed => "60";
     }
     
```

<<<<<<< HEAD
Note that actions can be added to sub-bundles like methods and editing bundles, and that promises within these do not inherit action settings at higher levels. Thus, in the following example there are two levels of action setting:
=======
Note that actions can be added to sub-bundles like methods and editing 
bundles, and that promises within these do not inherit action settings 
at higher levels. Thus, in the following example there are two levels
 of action setting:
>>>>>>> upstream/master

```cf3
     ########################################################
     #
     # Warn if line matched
     #
     ########################################################
     
     body common control
     
     {
     bundlesequence  => { "testbundle" };
     }
     
     ########################################################
     
     bundle agent testbundle
     
     {
     files:
     
       "/var/cfengine/inputs/.*"
     
            edit_line => DeleteLinesMatching(".*cfenvd.*"),
            action => WarnOnly;
     }
     
     ########################################################
     
     bundle edit_line DeleteLinesMatching(regex)
       {
       delete_lines:
     
         "$(regex)" action => WarnOnly;
     
       }
     
     ########################################################
     
     body action WarnOnly
     {
     action_policy => "warn";
     }
```

The `action` setting for the `files` promise means that file edits will
not be committed to disk, only warned about. This is a master-level
promise that overrides anything that happens during the editing. The
`action` setting in the edit\_line bundle means that the internal memory
modelling of the file will only warn about changes rather than
committing them to the memory model. This makes little difference to the
end result, but it means that CFEngine will report

```cf3
          Need to delete line - ... - but only a warning was promised
```

Instead of

```cf3
          Deleting the promised line ... Need to save file - but only a warning was promised
```

In either case, no changes will be made to the disk, but the messages
given by `cf-agent` will differ.   

#### ifelapsed

**Type**: `int`

**Allowed input range**: `0,99999999999`

**Default value:** control body value

<<<<<<< HEAD
**Description**: The number of minutes before next allowed assessment of a promise is set using `ifelapsed`. This overrides the global settings. Promises which take a long time to verify should usually be protected with a long value for this parameter.

This serves as a resource \`spam' protection. A CFEngine check could easily run every 5 minutes provided resource intensive operations are not performed on every run. Using time classes such as `Hr12` is one part of this strategy; using `ifelapsed` is another, which is not tied to a specific time.   

**Example**:  
   
=======
**Description**: The number of minutes before next allowed assessment of 
a promise is set using `ifelapsed`. This overrides the global settings. 
Promises which take a long time to verify should usually be protected 
with a long value for this parameter.

This serves as a resource 'spam' protection. A CFEngine check could 
easily run every 5 minutes provided resource intensive operations are 
not performed on every run. Using time classes such as `Hr12` is one 
part of this strategy; using `ifelapsed` is another, which is not tied 
to a specific time.   

**Example**:
>>>>>>> upstream/master

```cf3
     
     #local
     
     body action example
     {
     ifelapsed   => "120";  # 2 hours
     expireafter => "240";  # 4 hours
     }
     
     # global
     
     body agent control
     {
     ifelapsed   => "180";  # 3 hours
     }
     
```

<<<<<<< HEAD
`expireafter`

**Type**: int
=======
#### expireafter

**Type**: `int`
>>>>>>> upstream/master

**Allowed input range**: `0,99999999999`

**Default value:** control body value

<<<<<<< HEAD
**Description**: The Number of minutes before a repair action is interrupted and retried is set with `expireafter`. This is the locking time after which CFEngine will attempt to kill and restart its attempt to keep a promise.   

**Example**:  
   
=======
**Description**: The Number of minutes before a repair action is interrupted 
and retried is set with `expireafter`. This is the locking time after which 
CFEngine will attempt to kill and restart its attempt to keep a promise.   

**Example**:
>>>>>>> upstream/master

```cf3
     body action example
     {
     ifelapsed   => "120";  # 2 hours
     expireafter => "240";  # 4 hours
     }
```

<<<<<<< HEAD

=======
#### log_string_
>>>>>>> upstream/master

**Type**: `string`

**Allowed input range**: (arbitrary string)

<<<<<<< HEAD
**Description**: The message to be written to the log when a promise verification leads to a repair is determined by the `log_string`. The `log_string` works together with `log_repair`, `log_kept` etc, to define a string for logging to one of the named files depending on promise outcome, or to standard output if the log file is stipulated as stdout. Log strings on standard output are denoted by an L: prefix.

Note that `log_string` does not interact with `log_level`, which is about regular system output messages.
=======
**Description**: The message to be written to the log when a promise 
verification leads to a repair is determined by the `log_string`. The 
`log_string` works together with `log_repair`, `log_kept` etc, to define 
a string for logging to one of the named files depending on promise outcome, 
or to standard output if the log file is stipulated as stdout. Log strings 
on standard output are denoted by an L: prefix.
>>>>>>> upstream/master

Note that `log_string` does not interact with `log_level`, which is about 
regular system output messages.

**Example**:

```cf3
          
          promise-type:
          
           "promiser"
          
             attr = "value",
             action = log_me("checked $(this.promiser) in promise $(this.handle)");
          
          # ..
          
          body action log_me(s)
          {
          log_string = "$(s)";
          }
          
```

<<<<<<< HEAD
**Hint**: The promise handle \$(this.handle) can be a useful referent in a log message, indicating the origin of the message. In CFEngine Nova and above, every promise has a default handle, which is based on the filename and line number (specifying your own handle will probably be more mnemonic).   

`log_level`
=======
**Hint**: The promise handle \$(this.handle) can be a useful referent in a 
log message, indicating the origin of the message. In CFEngine Enterprise, 
every promise has a default handle, which is based on the filename 
and line number (specifying your own handle will probably be more mnemonic).

#### log_level
>>>>>>> upstream/master

**Type**: (menu option)

**Allowed input range**:   

```cf3
                    inform
                    verbose
                    error
                    log
```

<<<<<<< HEAD
**Description**: The `log_level` describes the reporting level sent to syslog. Use this as an alternative to auditing if you wish to use the syslog mechanism to centralize or manage messaging from CFEngine. A backup of these messages will still be kept in WORKDIR/outputs if you are using `cf-execd`.

On the native Windows version of CFEngine (Nova or above), using verbose will include a message when the promise is kept or repaired in the event log.   

=======
**Description**: The `log_level` describes the reporting level sent to 
syslog. Use this as an alternative to auditing if you wish to use the 
syslog mechanism to centralize or manage messaging from CFEngine. A backup
 of these messages will still be kept in WORKDIR/outputs if you are using 
 `cf-execd`.

On the native Windows version of CFEngine Enterprise, using verbose 
will include a message when the promise is kept or repaired in the event 
log.   
>>>>>>> upstream/master


**Example**:

```cf3
     
     body action example
     {
     log_level => "inform";
     }
     
```

<<<<<<< HEAD
`log_kept`
=======
#### log_kept

**Type**: `string`

**Allowed input range**: `stdout|udp_syslog|("?[a-zA-Z]:\\.*)|(/.*)`
>>>>>>> upstream/master

**Description**: The `log_kept` string should be the filename of a 
file to which log\_string will be saved, and if undefined it goes to 
the system logger.

If this option is specified together with `log_string`, the current 
promise will log promise-kept status using the log string to this named
 file. If these log names are absent, the default logging destination 
 for the log string is syslog, but only for non-kept promises. Only the 
 `log_string` is affected by this setting. Other messages destined for 
 logging are sent to syslog.

<<<<<<< HEAD
**Description**: The `log_kept` string should be the filename of a file to which log\_string will be saved, and if undefined it goes to the system logger.

If this option is specified together with `log_string`, the current promise will log promise-kept status using the log string to this named file. If these log names are absent, the default logging destination for the log string is syslog, but only for non-kept promises. Only the `log_string` is affected by this setting. Other messages destined for logging are sent to syslog.

It is intended that named file logs should be different for the three cases: promise kept, promise not kept and promise repaired.
=======
It is intended that named file logs should be different for the three 
cases: promise kept, promise not kept and promise repaired.
>>>>>>> upstream/master

**Example**:

```cf3
     
     body action logme(x)
     {
     log_kept => "/tmp/private_keptlog.log";
     log_failed => "/tmp/private_faillog.log";
     log_repaired => "/tmp/private_replog.log";
     log_string => "$(sys.date) $(x) promise status";
     }
     
```

<<<<<<< HEAD
This string should be the full path to a text file which will contain the log, of one of the following special values:

stdout

Send the log message to the standard output, prefixed with an L: to indicate a log message.   

udp\_syslog

Attempt to connect to the `syslog_server` defined in body common control and log the message there, assuming the server is configured to receive the request.
=======
This string should be the full path to a text file which will contain 
the log, of one of the following special values:

stdout

Send the log message to the standard output, prefixed with an L: to indicate 
a log message.   

udp\_syslog

Attempt to connect to the `syslog_server` defined in body common control and 
log the message there, assuming the server is configured to receive the 
request.
>>>>>>> upstream/master

#### log_priority

**Type**: (menu option)

**Allowed input range**:   

```cf3
                    emergency
                    alert
                    critical
                    error
                    warning
                    notice
                    info
                    debug
```

<<<<<<< HEAD
**Description**: The `log_priority` menu option policy is the priority level of the log message, as interpreted by a syslog server. It determines the importance of messages from CFEngine.   
=======
**Description**: The `log_priority` menu option policy is the priority level 
of the log message, as interpreted by a syslog server. It determines the 
importance of messages from CFEngine.   
>>>>>>> upstream/master

**Example**:

```cf3
     body action low_priority
     {
     log_priority => "info";
     }
```

<<<<<<< HEAD
`log_repaired`

**Type**: string

**Allowed input range**: `stdout|udp_syslog|("?[a-zA-Z]:\\.*)|(/.*)`

**Description**: The `log_repaired` string should contain the filename of a file to which log\_string will be saved, if undefined it goes to the system logger.
=======
#### log_repaired

**Type**: `string`

**Allowed input range**: `stdout|udp_syslog|("?[a-zA-Z]:\\.*)|(/.*)`

**Description**: The `log_repaired` string should contain the filename of a 
file to which log\_string will be saved, if undefined it goes to the system 
logger.
>>>>>>> upstream/master

**Example**:

```cf3
     
     bundle agent test
     {
     vars:
     
       "software" slist => { "/root/xyz", "/tmp/xyz" };
     
     files:
     
       "$(software)"
     
         create => "true",
          action => logme("$(software)");
     
     }
     
     body action logme(x)
     {
     log_kept => "/tmp/private_keptlog.log";
     log_failed => "/tmp/private_faillog.log";
     log_repaired => "/tmp/private_replog.log";
     log_string => "$(sys.date) $(x) promise status";
     }
     
     body action immediate_syslog(x) 
     {
     log_repaired => "udp_syslog";
     log_string => "CFEngine repaired promise $(this.handle) - $(x)";
     }
```

<<<<<<< HEAD
`log_repaired` may be the name of a log to which the `log_string` is written if a promise is repaired. It should be the full path to a text file which will contain the log, of one of the following special values:

stdout

Send the log message to the standard output, prefixed with an L: to indicate a log message.   

udp\_syslog

Attempt to connect to the `syslog_server` defined in body common control and log the message there, assuming the server is configured to receive the request.

`log_failed`
=======
`log_repaired` may be the name of a log to which the `log_string` is 
written if a promise is repaired. It should be the full path to a text 
file which will contain the log, of one of the following special values:

stdout

Send the log message to the standard output, prefixed with an L: to 
indicate a log message.   

udp\_syslog

Attempt to connect to the `syslog_server` defined in body common control 
and log the message there, assuming the server is configured to receive 
the request.

#### log_failed
>>>>>>> upstream/master

**Type**: `string`

**Allowed input range**: `stdout|udp_syslog|("?[a-zA-Z]:\\.*)|(/.*)`

<<<<<<< HEAD
**Description**: The string `log_failed` should contain the filename of a file to which log\_stringvwill be saved, and if undefined it goes to the system logger. If this option is specified together with `log_string`, the current promise will log promise-kept status using the log string to this named file. If these log names are absent, the default logging destination for the log string is syslog, but only for non-kept promises. Only the `log_string` is affected by this setting. Other messages destined for logging are sent to syslog.
=======
**Description**: The string `log_failed` should contain the filename of a 
file to which log\_stringvwill be saved, and if undefined it goes to the 
system logger. If this option is specified together with `log_string`, 
the current promise will log promise-kept status using the log string to 
this named file. If these log names are absent, the default logging 
destination for the log string is syslog, but only for non-kept promises. 
Only the `log_string` is affected by this setting. Other messages 
destined for logging are sent to syslog.
>>>>>>> upstream/master

**Example**:

```cf3
     
     bundle agent test
     {
     vars:
     
       "software" slist => { "/root/xyz", "/tmp/xyz" };
     
     files:
     
       "$(software)"
     
         create => "true",
          action => logme("$(software)");
     
     }
     
     
     body action logme(x)
     {
     log_kept => "/tmp/private_keptlog.log";
     log_failed => "/tmp/private_faillog.log";
     log_repaired => "/tmp/private_replog.log";
     log_string => "$(sys.date) $(x) promise status";
     }
     
```

<<<<<<< HEAD
It is intended that named file logs should be different for the three cases: promise kept, promise not kept and promise repaired. This string should be the full path to a text file which will contain the log, of one of the following special values:

stdout

Send the log message to the standard output, prefixed with an L: to indicate a log message.   

udp\_syslog

Attempt to connect to the `syslog_server` defined in body common control and log the message there, assuming the server is configured to receive the request.

`value_kept`
=======
It is intended that named file logs should be different for the three cases: 
promise kept, promise not kept and promise repaired. This string should be 
the full path to a text file which will contain the log, of one of the 
following special values:

stdout

Send the log message to the standard output, prefixed with an L: to indicate 
a log message.   

udp\_syslog

Attempt to connect to the `syslog_server` defined in body common control 
and log the message there, assuming the server is configured to receive 
the request.

#### value_kept
>>>>>>> upstream/master

**Type**: `real`

**Allowed input range**: `-9.99999E100,9.99999E100`

<<<<<<< HEAD
**Description**: The value of `value_kept` is a real number value attributed to keeping this promise. If nothing is specified, the default value is +1.0. However, nothing is logged unless the agent control body switched on track\_value = "true".
=======
**Description**: The value of `value_kept` is a real number value attributed 
to keeping this promise. If nothing is specified, the default value is 
+1.0. However, nothing is logged unless the agent control body switched 
on track\_value = "true".
>>>>>>> upstream/master

**Example**:

```cf3
     
     body action mydef
     {
     value_kept     => "4.5";   # this promise is worth 4.5 dollars per hour
     value_repaired => "2.5";   # fixing this promise is worth 2.5 dollars per hour
     value_notkept  => "-10.0"; # not keeping this promise costs is 10 dollars per hour
     ifelapsed       => "60";   # one hour
     }
     
```

<<<<<<< HEAD
`value_repaired`
=======
#### value_repaired
>>>>>>> upstream/master

**Type**: `real`

**Allowed input range**: `-9.99999E100,9.99999E100`

<<<<<<< HEAD
**Description**: The value of `value_repaired` is a real number value attributed to repairing a promise. If nothing is specified, the default value is 0.5. However, nothing is logged unless the agent control body switched on track\_value = "true".
  
**Example**:  
   
=======
**Description**: The value of `value_repaired` is a real number value 
attributed to repairing a promise. If nothing is specified, the default 
value is 0.5. However, nothing is logged unless the agent control body 
switched on track\_value = "true".
  
**Example**:
>>>>>>> upstream/master

```cf3
     
     body action mydef
     {
     value_kept     => "4.5";   # this promise is worth 4.5 dollars per hour
     value_repaired => "2.5";   # fixing this promise is worth 2.5 dollars per hour
     value_notkept  => "-10.0"; # not keeping this promise costs is 10 dollars per hour
     ifelapsed       => "60";   # one hour
     }
     
```

<<<<<<< HEAD
`value_notkept`

**Type**: real

**Allowed input range**: `-9.99999E100,9.99999E100`

**Synopsis**: The value of `value_notkept` is a real number value (possibly negative) attributed to not keeping a promise. If nothing is specified, the default value is -1.0. However, nothing is logged unless the agent control body switched on track\_value = "true".
  
**Example**:  
   
=======
#### value_notkept

**Type**: `real`

**Allowed input range**: `-9.99999E100,9.99999E100`

**Description**: The value of `value_notkept` is a real number value (possibly 
negative) attributed to not keeping a promise. If nothing is specified, the 
default value is -1.0. However, nothing is logged unless the agent control 
body switched on track\_value = "true".
  
**Example**:
>>>>>>> upstream/master

```cf3
     
     body action mydef
     {
     value_kept     => "4.5";   # this promise is worth 4.5 dollars per hour
     value_repaired => "2.5";   # fixing this promise is worth 2.5 dollars per hour
     value_notkept  => "-10.0"; # not keeping this promise costs is 10 dollars per hour
     ifelapsed       => "60";   # one hour
     }
     
```


<<<<<<< HEAD
`audit`
=======
#### audit
>>>>>>> upstream/master

**Type**: (menu option)

**Allowed input range**:   

```cf3
                    true
                    false
                    yes
                    no
                    on
                    off
```

<<<<<<< HEAD
**Description**: The `audit` menu option policy is a true/false switch for detailed audit records of a promise. If this is set, CFEngine will perform auditing on this specific promise. This means that all details surrounding the verification of the current promise will be recorded in the audit database.   
=======
**Description**: The `audit` menu option policy is a true/false switch for 
detailed audit records of a promise. If this is set, CFEngine will perform 
auditing on this specific promise. This means that all details surrounding 
the verification of the current promise will be recorded in the audit 
database.   
>>>>>>> upstream/master

**Default value:** false

**Example**:

```cf3
     
     body action example
     {
     # ...
     
     audit => "true";
     }
     
```

<<<<<<< HEAD
`background`
=======
#### background
>>>>>>> upstream/master

**Type**: (menu option)

**Allowed input range**:   

```cf3
                    true
                    false
                    yes
                    no
                    on
                    off
```

<<<<<<< HEAD
**Description**: The `background` menu option policy is a true/false switch for parallelizing the promise repair. If possible, perform the verification of the current promise in the background. This is advantageous only if the verification might take a significant amount of time, e.g. in remote copying of filesystem/disk scans.

On the Windows version of CFEngine Nova, this can be useful if we don't want to wait for a particular command to finish execution before checking the next promise. This is particular for the Windows platform because there is no way that a program can start itself in the background here; in other words, fork off a child process. However, file operations can not be performed in the background on Windows.   
=======
**Description**: The `background` menu option policy is a true/false 
switch for parallelizing the promise repair. If possible, perform the 
verification of the current promise in the background. This is advantageous 
only if the verification might take a significant amount of time, e.g. 
in remote copying of filesystem/disk scans.

On the Windows version of CFEngine Enterprise, this can be useful if we don't
want to wait for a particular command to finish execution before checking 
the next promise. This is particular for the Windows platform because there 
is no way that a program can start itself in the background here; in other 
words, fork off a child process. However, file operations can not be 
performed in the background on Windows.   
>>>>>>> upstream/master

**Default value:** false

**Example**:

```cf3
     
     body action example
     {
     background => "true";
     }
     
```

<<<<<<< HEAD
`report_level`
=======
#### report_level
>>>>>>> upstream/master

**Type**: (menu option)

**Allowed input range**:   

```cf3
                    inform
                    verbose
                    error
                    log
```

**Default value:** none

<<<<<<< HEAD
**Description**: The `report_level` menu option policy defines the reporting level for standard output for this promise. cf-agent can be run in verbose mode (-v), inform mode (-I) and just print errors (no arguments). This attribute allows to set these three output levels on a per promise basis, allowing the promise to be more verbose than the global setting (but not less).

In CFEngine 2 one would say inform=true or syslog=true, and so on. This replaces these levels since they act as encapsulating super-sets.   

**Example**:  
   
=======
**Description**: The `report_level` menu option policy defines the reporting 
level for standard output for this promise. cf-agent can be run in verbose 
mode (-v), inform mode (-I) and just print errors (no arguments). This 
attribute allows to set these three output levels on a per promise basis, 
allowing the promise to be more verbose than the global setting (but not 
less).

**Example**:
>>>>>>> upstream/master

```cf3
     
     body action example
     {
     report_level => "verbose";
     }
     
```


<<<<<<< HEAD
`measurement_class`

**Type**: string

**Allowed input range**: (arbitrary string)

**Description**: The `measurement_class` string, if set, performance will be measured and recorded under this identifier. By setting this string you switch on performance measurement for the current promise, and also give the measurement a name. 
=======
#### measurement_class

**Type**: `string`

**Allowed input range**: (arbitrary string)

**Description**: The `measurement_class` string, if set, performance 
will be measured and recorded under this identifier. By setting this string 
you switch on performance measurement for the current promise, and also 
give the measurement a name. 
>>>>>>> upstream/master

**Example**:  
   
```cf3
     
     
     body action measure
     {
     measurement_class => "$(this.promiser) long job scan of /usr";
     }
     
```

The identifier forms a partial identity for optional performance scanning of promises of the form:

```cf3
          ID:promise-type:promiser.
```


### classes

**Type**: `body classes`


<<<<<<< HEAD

`promise_repaired`
=======
#### promise_repaired
>>>>>>> upstream/master

**Type**: `slist`

**Allowed input range**: `[a-zA-Z0-9_$(){}\[\].:]+`

<<<<<<< HEAD
**Description**: The `promise_repaired` slist contains classes to be defined globally. If a promise is \`repaired' it means that a corrective action had to be taken to keep the promise.

Note that any strings passed to this list are automatically canonified, so it is unnecessary to call a canonify function on such inputs.
=======
**Description**: The `promise_repaired` slist contains classes to be defined 
globally. If a promise is 'repaired' it means that a corrective action had 
to be taken to keep the promise.

Note that any strings passed to this list are automatically canonified, so 
it is unnecessary to call a canonify function on such inputs.
>>>>>>> upstream/master

**Example**:  
   
```cf3
     
     body classes example
     {
     promise_repaired => { "change_happened" };
     }
     
```

<<<<<<< HEAD
**Important**: Complex promises can report misleadingly; for example, `files` promises that set multiple parameters on a file simultaneously.

The classes for different parts of a promise are not separable. Thus, if you promise to create and file and change its permissions, when the file exists with incorrect permissions, `cf-agent` will report that the promise\_kept for the file existence, but promise\_repaired for the permissions. If you need separate reports, you should code two separate promises rather than \`overloading' a single one.   

=======
**Important**: Complex promises can report misleadingly; for example, 
`files` promises that set multiple parameters on a file simultaneously.

The classes for different parts of a promise are not separable. Thus, if 
you promise to create and file and change its permissions, when the file 
exists with incorrect permissions, `cf-agent` will report that the 
promise\_kept for the file existence, but promise\_repaired for the 
permissions. If you need separate reports, you should code two separate 
promises rather than 'overloading' a single one.   

>>>>>>> upstream/master

#### repair_failed

**Type**: `slist`

**Allowed input range**: `[a-zA-Z0-9_$(){}\[\].:]+`

<<<<<<< HEAD
**Description**: A `repair_failed` list contains classes to be defined globally. A promise could not be repaired because the corrective action failed for some reason. Any strings passed to this list are automatically canonified, so it is unnecessary to call a canonify function on such inputs.   
=======
**Description**: A `repair_failed` list contains classes to be defined 
globally. A promise could not be repaired because the corrective action 
failed for some reason. Any strings passed to this list are automatically 
canonified, so it is unnecessary to call a canonify function on such inputs.   
>>>>>>> upstream/master

**Example**:

```cf3
     
     body classes example
     {
     repair_failed => { "unknown_error" };
     }
     
```

<<<<<<< HEAD
`repair_denied`

**Type**: slist

**Allowed input range**: `[a-zA-Z0-9_$(){}\[\].:]+`

**Description**: The `repair_denied` slist contains classes to be defined globally. Note that any strings passed to this list are automatically canonified, so it is unnecessary to call a canonify function on such inputs.   
=======
#### repair_denied

**Type**: `slist`

**Allowed input range**: `[a-zA-Z0-9_$(){}\[\].:]+`

**Description**: The `repair_denied` slist contains classes to be defined 
globally. Note that any strings passed to this list are automatically 
canonified, so it is unnecessary to call a canonify function on such 
inputs.   
>>>>>>> upstream/master


**Example**:  
   
```cf3
     
     body classes example
     {
     repair_denied => { "permission_failure" };
     }
     
```

<<<<<<< HEAD
In the above example, a promise could not be kept because access to a key resource was denied. 
=======
In the above example, a promise could not be kept because access to a key 
resource was denied. 
>>>>>>> upstream/master


#### repair_timeout

**Type**: `slist`

**Allowed input range**: `[a-zA-Z0-9_$(){}\[\].:]+`

<<<<<<< HEAD
**Description**: The `repair_timeout` slist contains classes to be defined globally.
=======
**Description**: The `repair_timeout` slist contains classes to be defined 
globally.
>>>>>>> upstream/master

**Example**:

```cf3
     
     body classes example
     {
     repair_timeout => { "too_slow", "did_not_wait" };
     }
     
``` 

In the above example, a promise maintenance repair timed-out waiting for some dependent resource.   

#### promise_kept

**Type**: `slist`

**Allowed input range**: `[a-zA-Z0-9_$(){}\[\].:]+`

<<<<<<< HEAD
**Description**: The `promise_kept` slist contains classes to be defined globally. Note that any strings passed to this list are automatically canonified, so it is unnecessary to call a canonify function on such inputs.

=======
**Description**: The `promise_kept` slist contains classes to be defined 
globally. Note that any strings passed to this list are automatically 
canonified, so it is unnecessary to call a canonify function on such inputs.
>>>>>>> upstream/master


**Example**:

```cf3
     
     body classes example
     {
     promise_kept => { "success", "kaplah" };
     }
     
```

<<<<<<< HEAD
The class in the above example is set if no action was necessary by `cf-agent`, because the promise concerned was already kept without further action required.

**Important**: complex promises can report misleadingly. For example, `files`promises that set multiple parameters on a file simultaneously.

The classes for different parts of a promise are not separable. Thus, if you promise to create and file and change its permissions, when the file exists with incorrect permissions, `cf-agent` will report that the promise\_kept for the file existence, but promise\_repaired for the permissions. If you need separate reports, you should code two separate promises rather than \`overloading' a single one.   
=======
The class in the above example is set if no action was necessary by 
`cf-agent`, because the promise concerned was already kept without further 
action required.

**Important**: complex promises can report misleadingly. For example, 
`files`promises that set multiple parameters on a file simultaneously.

The classes for different parts of a promise are not separable. Thus, 
if you promise to create and file and change its permissions, when the 
file exists with incorrect permissions, `cf-agent` will report that the 
promise\_kept for the file existence, but promise\_repaired for the 
permissions. If you need separate reports, you should code two separate 
promises rather than 'overloading' a single one.   

#### cancel_kept
>>>>>>> upstream/master

**Type**: `slist`

**Allowed input range**: `[a-zA-Z0-9_$(){}\[\].:]+`

<<<<<<< HEAD
**Description**: A `cancel_kept` slist contains classes to be canceled if the promise is kept. Note that any strings passed to this list are automatically canonified, so it is unnecessary to call a canonify function on such inputs.
=======
**Description**: A `cancel_kept` slist contains classes to be canceled if 
the promise is kept. Note that any strings passed to this list are 
automatically canonified, so it is unnecessary to call a canonify function 
on such inputs.
>>>>>>> upstream/master

**Example**:  
   
```cf3
     
     body classes example
     {
     cancel_kept => { "success", "kaplah" };
     }
     
```

<<<<<<< HEAD
In the above example, if the promise was already kept and nothing was done, cancel (undefine) any of the listed classes so that they are no longer defined.

**History**: This attribute was introduced in CFEngine version 3.0.4 (2010)   

`cancel_repaired`

**Type**: slist

**Allowed input range**: `[a-zA-Z0-9_$(){}\[\].:]+`

**Description**: A `cancel_repaired` slist contains classes to be canceled if the promise is repaired. Note that any strings passed to this list are automatically canonified, so it is unnecessary to call a canonify function on such inputs.
=======
In the above example, if the promise was already kept and nothing was done, 
cancel (undefine) any of the listed classes so that they are no longer 
defined.

**History**: This attribute was introduced in CFEngine version 3.0.4 (2010)   

#### cancel_repaired

**Type**: `slist`

**Allowed input range**: `[a-zA-Z0-9_$(){}\[\].:]+`

**Description**: A `cancel_repaired` slist contains classes to be canceled 
if the promise is repaired. Note that any strings passed to this list are 
automatically canonified, so it is unnecessary to call a canonify function 
on such inputs.
>>>>>>> upstream/master

**Example**:

```cf3
     
     body classes example
     {
     cancel_repaired => { "change_happened" };
     }
     
```

<<<<<<< HEAD
In the above example, if the promise was repaired and changes were made to the system, cancel (undefine) any of the listed classes so that they are no longer defined.
=======
In the above example, if the promise was repaired and changes were made to 
the system, cancel (undefine) any of the listed classes so that they are 
no longer defined.
>>>>>>> upstream/master

**History**: This attribute was introduced in CFEngine version 3.0.4 (2010)   

#### cancel_notkept

**Type**: `slist`

**Allowed input range**: `[a-zA-Z0-9_$(){}\[\].:]+`

<<<<<<< HEAD
**Description**: A `cancel_notkept` slist contains classes to be canceled if the promise is not kept for any reason. Note that any strings passed to this list are automatically canonified, so it is unnecessary to call a canonify function on such inputs.
=======
**Description**: A `cancel_notkept` slist contains classes to be canceled 
if the promise is not kept for any reason. Note that any strings passed 
to this list are automatically canonified, so it is unnecessary to call 
a canonify function on such inputs.
>>>>>>> upstream/master

**Example**:  
   
```cf3
     
     body classes example
     {
     cancel_notkept => { "failure" };
     }
     
```

<<<<<<< HEAD
In the above example, if the promise was not kept but nothing could be done, cancel (undefine) any of the listed classes so that they are no longer defined.
=======
In the above example, if the promise was not kept but nothing could be done, 
cancel (undefine) any of the listed classes so that they are no longer 
defined.
>>>>>>> upstream/master

**History**: This attribute was introduced in CFEngine version 3.0.4 (2010)   

#### kept_returncodes

**Type**: `slist`

**Allowed input range**: `[-0-9_$(){}\[\].]+`

<<<<<<< HEAD
**Synopsis**: A `kept_returncodes` slist contains return codes indicating a kept command-related promise.
=======
**Description**: A `kept_returncodes` slist contains return codes indicating a 
kept command-related promise.
>>>>>>> upstream/master

**Example**:

```cf3
     bundle agent cmdtest
     {
     commands:
       "/bin/false"
        classes => example;
     
     reports:
     waskept::
       "The command-promise was kept!";
     }
     
     body classes example
     {
     kept_returncodes => { "0", "1" };
     promise_kept => { "waskept" };
     }
```

<<<<<<< HEAD
In the above example, a list of integer return codes indicates that a command-related promise has been kept. This can in turn be used to define classes using the `promise_kept` attribute, or merely alter the total compliance statistics.

Currently, the attribute has impact on the following command-related promises:

-   All promises of type `commands:`
-   `files`-promises containing a `transformer`-attribute
-   The package manager change command in `packages`-promises (e.g. the command for add, remove, etc.)

If none of the attributes `kept_returncodes`, `repaired_returncodes`, or `failed_returncodes` are set, the default is to consider a return code zero as promise repaired, and nonzero as promise failed.

Note that the return codes may overlap, so multiple classes may be set from one return code. In Unix systems the possible return codes are usually in the range from 0 to 255.
=======
In the above example, a list of integer return codes indicates that a 
command-related promise has been kept. This can in turn be used to define 
classes using the `promise_kept` attribute, or merely alter the total 
compliance statistics.

Currently, the attribute has impact on the following command-related 
promises:

-   All promises of type `commands:`
-   `files`-promises containing a `transformer`-attribute
-   The package manager change command in `packages`-promises (e.g. the 
command for add, remove, etc.)

If none of the attributes `kept_returncodes`, `repaired_returncodes`, or 
`failed_returncodes` are set, the default is to consider a return code 
zero as promise repaired, and nonzero as promise failed.

Note that the return codes may overlap, so multiple classes may be set 
from one return code. In Unix systems the possible return codes are 
usually in the range from 0 to 255.
>>>>>>> upstream/master

**History**: Was introduced in version 3.1.3, Nova 2.0.2 (2010)   

#### repaired_returncodes

**Type**: `slist`

**Allowed input range**: `[-0-9_$(){}\[\].]+`

<<<<<<< HEAD
**Synopsis**: A `repaired_returncodes` slist contains return codes indicating a repaired command-related promise
=======
**Description**: A `repaired_returncodes` slist contains return codes 
indicating a repaired command-related promise
>>>>>>> upstream/master

**Example**:  
   
```cf3
     bundle agent cmdtest
     {
     commands:
       "/bin/false"
        classes => example;
     
     reports:
     wasrepaired::
       "The command-promise got repaired!";
     }
     
     body classes example
     {
     repaired_returncodes => { "0", "1" };
     promise_repaired => { "wasrepaired" }; 
     }
```

<<<<<<< HEAD
In the above example, a list of integer return codes indicating that a command-related promise has been repaired. This can in turn be used to define classes using the `promise_repaired` attribute, or merely alter the total compliance statistics.

Currently, the attribute has impact on the following command-related promises:

-   All promises of type `commands:`
-   `files`-promises containing a `transformer`-attribute
-   The package manager change command in `packages`-promises (e.g. the command for add, remove, etc.)

If none of the attributes `kept_returncodes`, `repaired_returncodes`, or `failed_returncodes` are set, the default is to consider a return code zero as promise repaired, and nonzero as promise failed.

Note that the return codes may overlap, so multiple classes may be setfrom one return code. In Unix systems the possible return codes are usually in the range from 0 to 255.
=======
In the above example, a list of integer return codes indicating that a 
command-related promise has been repaired. This can in turn be used to 
define classes using the `promise_repaired` attribute, or merely alter the total compliance statistics.

Currently, the attribute has impact on the following command-related 
promises:

-   All promises of type `commands:`
-   `files`-promises containing a `transformer`-attribute
-   The package manager change command in `packages`-promises (e.g. the 
command for add, remove, etc.)

If none of the attributes `kept_returncodes`, `repaired_returncodes`, 
or `failed_returncodes` are set, the default is to consider a return 
code zero as promise repaired, and nonzero as promise failed.

Note that the return codes may overlap, so multiple classes may be set 
from one return code. In Unix systems the possible return codes are usually 
in the range from 0 to 255.
>>>>>>> upstream/master

**History**: Was introduced in version 3.1.3, Nova 2.0.2 (2010)   

#### failed_returncodes

**Type**: `slist`

**Allowed input range**: `[-0-9_$(){}\[\].]+`

<<<<<<< HEAD
**Description**: A `failed_returncodes` slist contains return codes indicating a failed command-related promise.
=======
**Description**: A `failed_returncodes` slist contains return codes 
indicating a failed command-related promise.
>>>>>>> upstream/master

**Example**:

```cf3
     body common control
     {
     bundlesequence => { "cmdtest" };
     }
     
     bundle agent cmdtest
     {
     files:
     "/tmp/test"
       copy_from => copy("/etc/passwd");
     
     
     "/tmp/test"
       classes => example,
       transformer => "/bin/grep -q lkajfo999999 $(this.promiser)";
     
     reports:
     wasfailed::
       "The files-promise failed!";
     }
     
     body classes example
     {
     failed_returncodes => { "1" };
     repair_failed => { "wasfailed" };
     }
     
     body copy_from copy(file)
     {
     source => "$(file)";
     } 
```

<<<<<<< HEAD
The above example contains a list of integer return codes indicating that a command-related promise has failed. This can in turn be used to define classes using the `promise_repaired` attribute, or merely alter the total compliance statistics.

Currently, the attribute has impact on the following command-related promises.

-   All promises of type `commands:`
-   `files`-promises containing a `transformer`-attribute
-   The package manager change command in `packages`-promises (e.g. the     command for add, remove, etc.)

If none of the attributes `kept_returncodes`, `repaired_returncodes`, or `failed_returncodes` are set, the default is to consider a return code zero as promise repaired, and nonzero as promise failed.

Note that the return codes may overlap, so multiple classes may be set from one return code. In Unix systems the possible return codes are usually in the range from 0 to 255.
=======
The above example contains a list of integer return codes indicating 
that a command-related promise has failed. This can in turn be used to 
define classes using the `promise_repaired` attribute, or merely alter 
the total compliance statistics.

Currently, the attribute has impact on the following command-related 
promises.

-   All promises of type `commands:`
-   `files`-promises containing a `transformer`-attribute
-   The package manager change command in `packages`-promises (e.g. the 
command for add, remove, etc.)

If none of the attributes `kept_returncodes`, `repaired_returncodes`, or 
`failed_returncodes` are set, the default is to consider a return code 
zero as promise repaired, and nonzero as promise failed.

Note that the return codes may overlap, so multiple classes may be set from 
one return code. In Unix systems the possible return codes are usually in 
the range from 0 to 255.
>>>>>>> upstream/master

**History**: Was introduced in version 3.1.3, Nova 2.0.2 (2010)   

#### persist_time

**Type**: `int`

**Allowed input range**: `0,99999999999`

<<<<<<< HEAD
**Description**: The value of `persist_time` defines the number of minutes the specified classes should remain active. By default classes are ephemeral entities that disappear when `cf-agent` terminates. By setting a persistence time, they can last even when the agent is not running.   
=======
**Description**: The value of `persist_time` defines the number of minutes 
the specified classes should remain active. By default classes are ephemeral 
entities that disappear when `cf-agent` terminates. By setting a persistence 
time, they can last even when the agent is not running.   
>>>>>>> upstream/master

**Example**:

```cf3
     
     body classes example
     {
     persist_time => "10";
     }
     
```

<<<<<<< HEAD
`timer_policy`
=======
#### timer_policy
>>>>>>> upstream/master

**Type**: (menu option)

**Allowed input range**:   

```cf3
                    absolute
                    reset
```

<<<<<<< HEAD
**Description**: The `timer_policy` menu option policy determines whether a persistent class restarts its counter when rediscovered. In most cases resetting a timer will give a more honest appraisal of which classes are currently important, but if we want to activate a response of limited duration as a rare event then an absolute time limit is useful.
=======
**Description**: The `timer_policy` menu option policy determines whether 
a persistent class restarts its counter when rediscovered. In most cases 
resetting a timer will give a more honest appraisal of which classes are 
currently important, but if we want to activate a response of limited 
duration as a rare event then an absolute time limit is useful.
>>>>>>> upstream/master

**Default value:** reset

**Example**:

```cf3
     
     body classes example
     {
     timer_policy => "reset";
     }
     
```

<<<<<<< HEAD
#### `comment`

**Type**: string

**Allowed input range**: (arbitrary string)

**Description**: The `comment` string describes the real intention of the promise. Comments written in code follow the program, they are not merely discarded; they appear in reports and error messages.
=======
### comment

**Type**: `string`

**Allowed input range**: (arbitrary string)

**Description**: The `comment` string describes the real intention of the 
promise. Comments written in code follow the program, they are not merely 
discarded; they appear in reports and error messages.
>>>>>>> upstream/master

**Example**:

```cf3
comment => "This comment follows the data for reference ...",
```

<<<<<<< HEAD
#### `depends_on`
=======
### depends_on

**Type**: `slist`

**Allowed input range**: (arbitrary string)
>>>>>>> upstream/master

**Description**: A `depends_on` slist contains promise handles that this 
promise builds on or depends on somehow. This is a list of promise handles 
for whom this promise is a promisee. In other words, we acknowledge that 
this promise will be affected by the list of promises whose handles are 
specified. It has the effect of partially ordering promises.

As of version 3.4.0, this feature may be considered short-hand for setting 
classes. If one promise depends on a list of others, it will not be verified 
unless the dependent promises have already been verified and kept: in other 
words, as long as the dependent promises are either kept or repaired the 
dependee can be verified.

<<<<<<< HEAD
**Description**: A `depends_on` slist contains promise handles that this promise builds on or depends on somehow. This is a list of promise handles for whom this promise is a promisee. In other words, we acknowledge that this promise will be affected by the list of promises whose handles are specified. It has the effect of partially ordering promises.

As of version 3.4.0, this feature may be considered short-hand for setting classes. If one promise depends on a list of others, it will not be verified unless the dependent promises have already been verified and kept: in other words, as long as the dependent promises are either kept or repaired the dependee can be verified.

=======
>>>>>>> upstream/master
Handles in other namespaces may be referred to by namespace:handle.

**Example**:

```cf3
body common control
{
bundlesequence => { "one"  };
}

bundle agent one
{
reports:

 cfengine_3::

   "two"
     depends_on => { "handle_one" };

   "one"
     handle => "handle_one";

}

```

<<<<<<< HEAD
#### `handle`
=======
### handle

**Type**: `string`

**Allowed input range**: (arbitrary string)

**Description**: The `handle` string is a unique id-tag string for referring 
to this as a promisee elsewhere.
>>>>>>> upstream/master

A promise handle is like a 'goto' label. It allows you to refer to a promise
as the promisee of `depends_on` client of another promise. Handles are 
essential for mapping dependencies and performing impact analyses.

Handles may consist of regular identifier characters. CFEngine automatically 
`canonifies' the names of handles to conform to this standard.

<<<<<<< HEAD
**Description**: The `handle` string is a unique id-tag string for referring to this as a promisee elsewhere.

A promise handle is like a \`goto' label. It allows you to refer to a promise as the promisee of `depends_on` client of another promise. Handles are essential for mapping dependencies and performing impact analyses. In Enterprise versions of CFEngine, promise handles can also be used in `outputs` promises, See [outputs in agent promises](#outputs-in-agent-promises).

Handles may consist of regular identifier characters. CFEngine automatically \`canonifies' the names of handles to conform to this standard.

**Example**:  
   
=======
**Example**:
>>>>>>> upstream/master

```cf3
access:
 
  "/source"

    handle  => "update_rule",
    admit   => { "127.0.0.1" };
```

**Caution**: If the handle name is based on a variable, and the variable
fails to expand, the handle will be based on the name of the variable
rather than its content.

### ifvarclass

**Type**: `string`

**Allowed input range**: (arbitrary string)

<<<<<<< HEAD
**Description**: The `ifvarclass` string describes extended classes ANDed with context. This is an additional class expression that will be evaluated after the class:: classes have selected promises. It is provided in order to enable a channel between variables and classes.

The result is thus the logical AND of the ordinary classes and the variable classes.
=======
**Description**: The `ifvarclass` string describes extended classes ANDed 
with context. This is an additional class expression that will be evaluated 
after the class:: classes have selected promises. It is provided in order 
to enable a channel between variables and classes.
>>>>>>> upstream/master

The result is thus the logical AND of the ordinary classes and the variable 
classes.

**Example**:

The generic example has the form:

```cf3
     
     promise-type:
     
       "promiser"
     
         ifvarclass = "$(program)_running|($(program)_notfoundHr12)";
     
```

A specific example would be:

```cf3
bundle agent example

{     
commands:

 any::

    "/bin/echo This is linux"

       ifvarclass => "linux";


    "/bin/echo This is solaris"

       ifvarclass => "solaris";

}
```

<<<<<<< HEAD
This function is provided so that one can form expressions that link variables and classes. For example:
=======
This function is provided so that one can form expressions that link 
variables and classes. For example:
>>>>>>> upstream/master

```cf3
# Check that all components are running

vars:

  "component" slist => { "cf-monitord", "cf-serverd" };

processes:

  "$(component)" restart_class => canonify("start_$(component)");

commands:

   "/var/cfengine/bin/$(component)"

       ifvarclass => canonify("start_$(component)");
```

<<<<<<< HEAD
Notice that the function `canonify()` is provided to convert a general variable input into a string composed only of legal characters, using the same algorithm that CFEngine uses.
=======
Notice that the function `canonify()` is provided to convert a general variable 
input into a string composed only of legal characters, using the same algorithm 
that CFEngine uses.
>>>>>>> upstream/master

### meta

**Type**: `slist`

**Allowed input range**: (arbitrary string)

<<<<<<< HEAD
**Description**: The `meta` string describes user-data associated with policy, e.g. key=value strings.

It is sometimes convenient to attach meta-data of a more technical nature to policy. It may be used for arbitrary key=value strings for example.

=======
**Description**: The `meta` string describes user-data associated with policy, 
e.g. key=value strings.
>>>>>>> upstream/master

It is sometimes convenient to attach meta-data of a more technical nature to 
policy. It may be used for arbitrary key=value strings for example.


**Example**:

```cf3
files:

  "/etc/special_file"

    comment => "Special file is a requirement. Talk to Fred X.",
    create => "true",

    meta => { "owner=John",  "version=2.0" };
```

**History**: Was introduced in 3.3.0, Nova 2.2.0 (2012)
