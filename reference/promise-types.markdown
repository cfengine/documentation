---
layout: default
title: Promise Types
published: true
sorting: 20
tags: [reference, bundles, common, promises]
---

Within a bundle, the promise types are executed in a round-robin fashion in the
following [normal ordering][Normal Ordering]. Which promise types are available
depends on the [bundle][bundles] type:

| Promise Type   | common | agent | server | monitor |
|----------------|:------:|:-----:|:------:|:--------|
| [defaults][defaults] - a default value for bundle parameters | x      | x     | x      | x       |
| [classes][classes] - a class, representing a state of the system | x      | x     | x      | x       |
| [meta][meta] - information about promise bundles | x      | x     | x      | x       |
| [reports][reports] - report a message | x      | x     | x      | x       |
| [vars][vars] - a variable, representing a value | x      | x     | x      | x       |
| [commands][commands] - execute a command |        | x     |        |         |
| [databases][databases] - configure a database |        | x     |        |         |
| [files][files] - configure a file |        | x     |        |         |
| [packages][packages] - install a package |        | x     |        |         |
| [guest_environments][guest_environments] |        | x     |        |         |
| [methods][methods] - take on a whole bundle of other promises |        | x     |        |         |
| [processes][processes] - start or terminate processes |        | x     |        |         |
| [services][services] - manage services or define new abstractions |        | x     |        |         |
| [storage][storage] - verify attached storage |        | x     |        |         |
| [users][users] - add or remove users |        | x     |        |         |
| [access][access] - grant or deny access to file objects |        |       | x      |         |
| [roles][roles] - allow certain users to activate certain classes |        |       | x      |         |
| [measurements][measurements] - measure or sample data from the system |        |       |        | x       |

See each promise type's reference documentation for detailed lists of available
attributes.

## Common Promise Attributes

The following attributes are available to all promise types.

### action

**Type:** `body action`

The `action` settings allow general transaction control to be implemented on
promise verification. Action bodies place limits on how often to verify the
promise and what classes to raise in the case that the promise can or cannot be
kept.

#### action_policy

**Description:** Determines whether to repair or report about non-kept promises

**Type:** (menu option)

**Allowed input range:**

* ```fix``` makes changes to move toward the desired state
* ```warn``` does not make changes, emits a warning level log message about non-compliance, raise repair_failed (not-kept)
* ```nop``` alias for warn

**Default value:** ```fix```

**Example:**

Policy:

[%CFEngine_include_example(action_policy.cf, #\+begin_src\s+cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(action_policy.cf, #\+begin_src\s+mock_example_output\s*, .*end_src)%]

#### ifelapsed

**Description:** The number of minutes before next allowed assessment of a
promise is set using `ifelapsed`. This overrides the global settings.  Promises
which take a long time to verify should usually be protected with a long value
for this parameter.

This serves as a resource 'spam' protection. A CFEngine check could easily run
every 5 minutes provided resource intensive operations are not performed on
every run. Using time classes such as `Hr12` is one part of this strategy;
using `ifelapsed` is another, which is not tied to a specific time.

`ifelapsed => "0"` disables [function caching][Functions#function caching]
for the specific promise it's attached to.

**Type:** `int`

**Allowed input range:** `0,99999999999`

**Default value:** [body agent control ifelapsed value][cf-agent#ifelapsed]

**Example:**

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

**See also:** [promise locking][Promises#Promise Locking], [ifelapsed in body agent control][cf-agent#ifelapsed],
[`ifelapsed` and function caching][Functions#function caching]

**History:**

* `ifelapsed => "0"` disables function caching for specific promise introduced in 3.19.0, 3.18.1

#### expireafter

**Description:** The Number of minutes a promise is allowed to run before the
agent is terminated.

**Note**: Not to be confused
with [`body contain exec_timeout`][commands#exec_timeout] in commands type
promises, the original agent does **not** terminate the promise. When a
subsequent agent notices that a promise actuation has persisted for longer than
`expireafter` the subsequent agent will kill the agent that appears to be stuck
on the long running promise.

**Type:** `int`

**Allowed input range:** `0,99999999999`

**Default value:** [control body value][cf-agent#expireafter]

**Example:**

```cf3
body action example
{
  ifelapsed   => "120";  # 2 hours
  expireafter => "240";  # 4 hours
}
```

**See also:** [`body contain exec_timeout`][commands#exec_timeout], [`body agent control expireafter`][cf-agent#expireafter], [`body executor control agent_expireafter`][cf-execd#agent_expireafter]

#### log_string

**Description:** The message to be written to the log when a promise
verification leads to a repair.

The `log_string` works together with `log_kept`, `log_repaired`, and
`log_failed` to define a string for logging to one of the named files depending
on promise outcome, or to standard output if the log file is stipulated as
`stdout`. Log strings on standard output are denoted by an `L:` prefix.

Note that `log_string` does not interact with `log_level`, which is about
regular system output messages.

**Type:** `string`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
  promise-type:

      "promiser"

        attr => "value",
        action => log_me("checked $(this.promiser) in promise $(this.handle)");

    # ..

  body action log_me(s)
{
  log_string => "$(s)";
}
```

**Hint**: The promise handle [`$(this.handle)`][this#this.handle] can be a
useful referent in a log message, indicating the origin of the message. In
[CFEngine Enterprise](https://cfengine.com/product-overview/), promise handles make it easy to interpret report data.

#### log_kept
#### log_repaired
#### log_failed

**Description:** The names of files to which `log_string` will be saved
for kept, repaired and failed promises.

When used together with `log_string`, the current promise will log its status
using the log string to the respective file.

If these log names are absent, the default logging destination for the log
string is syslog, but only for non-kept promises. Only the `log_string` is
affected by this setting. Other messages destined for logging are sent to
syslog.

**Type:** `string`

**Allowed input range:** `stdout|udp_syslog|("?[a-zA-Z]:\\.*)|(/.*)`

This string should be the full path to a text file which will contain the log,
or one of the following special values:

* `stdout`

Send the log message to the standard output, prefixed with an L: to indicate a
log message.

* `udp_syslog`

Log messages to [syslog_host][Components#syslog_host] as
defined in body common control over UDP. Please note
[UDP is unreliable](http://en.wikipedia.org/wiki/Syslog#Limitations).

**Example:**

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

It is intended that named file logs should be different for the three cases:
promise kept, promise not kept and promise repaired.

#### log_level

**Description:** Describes the reporting level sent to syslog.

Use this as an alternative to auditing if you wish to use the syslog mechanism
to centralize or manage messaging from CFEngine. A backup of these messages
will still be kept in `WORKDIR/outputs` if you are using `cf-execd`.

On the native Windows version of CFEngine Enterprise, using verbose will
include a message when the promise is kept or repaired in the event log.

**Type:** (menu option)

**Allowed input range:**

```
    inform
    verbose
    error
    log
```

**Example:**

```cf3
body action example
{
  log_level => "inform";
}
```

**Note**: This attribute can not make the logging for an individual promise less
verbose than specified by an agent option ( `-v`, `--verbose`, `-I`, `--inform`,
`-d`, `--debug` ).

#### log_priority

**Type:** (menu option)

**Allowed input range:**

```
    emergency
    alert
    critical
    error
    warning
    notice
    info
    debug
```

**Description:** The `log_priority` menu option policy is the priority level
of the log message, as interpreted by a syslog server. It determines the
importance of messages from CFEngine.

**Example:**

```cf3
body action low_priority
{
  log_priority => "info";
}
```

#### value_kept

**Deprecated:** This menu option policy is deprecated as of 3.6.0. It performs
no action and is kept for backward compatibility.

#### value_repaired

**Deprecated:** This menu option policy is deprecated as of 3.6.0. It performs
no action and is kept for backward compatibility.

#### value_notkept

**Deprecated:** This menu option policy is deprecated as of 3.6.0. It performs
no action and is kept for backward compatibility.

#### audit

**Deprecated:** This menu option policy is deprecated as of 3.6.0. It performs
no action and is kept for backward compatibility.

#### background

**Description:** A true/false switch for parallelizing the promise repair.

If possible, perform the verification of the current promise in the background (up to [`max_children` in body agent control][cf-agent#max_children]).
This is advantageous only if the verification might take a significant amount
of time, e.g. in remote copying of filesystem/disk scans.

On the Windows version of CFEngine Enterprise, this can be useful if we don't
want to wait for a particular command to finish execution before checking the
next promise. This is particular for the Windows platform because there is
no way that a program can start itself in the background here; in other words,
fork off a child process. However, file operations can not be performed in the
background on Windows.

**Type:** [`boolean`][boolean]

**Default value:** false

**Example:**

```cf3
bundle agent main
{
  commands:

    "/bin/sleep 10"
      action  => background;

    "/bin/sleep"
      args => "20",
      action  => background;

}
body action background
{
  background => "true";
}
```

**See also:** [`max_children` in body agent control][cf-agent#max_children]

#### report_level

**Description:** Defines the reporting level for standard output for this promise.

`cf-agent` can be run in verbose mode (-v), inform mode (-I) and just print
errors (no arguments). This attribute allows to set these three output levels
on a per promise basis, allowing the promise to be more verbose than the global
setting (but not less).

**Type:** (menu option)

**Allowed input range:**

```
    inform
    verbose
    error
    log
```

**Default value:** none

**Example:**

```cf3
body action example
{
  report_level => "verbose";
}
```

#### measurement_class

**Description:** If set, performance will be measured and recorded under this
identifier.

By setting this string you switch on performance measurement for the current
promise, and also give the measurement a name.

**Type:** `string`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
body action measure
{
  measurement_class => "$(this.promiser) long job scan of /usr";
}
```

The identifier forms a partial identity for optional performance scanning of
promises of the form:

```cf3
    ID:promise-type:promiser.
```


### classes

**Type:** `body classes`

#### scope

**Description:** Scope of the class set by this body.

**Type:** (menu option)

**Allowed input range:**

```
    namespace
    bundle
```

**Default value:** namespace

**Example:**

```cf3
body classes bundle_class
{
  scope => "bundle";
  promise_kept => { "bundle_context" };
}
```

**History:** This attribute was introduced in CFEngine 3.5

**See also:** [`scope` in `classes` promises][classes#scope]

#### promise_repaired

**Description:** Classes to be defined globally if the promise was 'repaired'.

If the classes are set, a corrective action had to be taken to keep the
promise.

**Type:** `slist`

**Allowed input range:** `[a-zA-Z0-9_$(){}\[\].:]+`

Note that any strings passed to this list are automatically canonified, so it
is unnecessary to call a canonify function on such inputs.

**Example:**

```cf3
body classes example
{
  promise_repaired => { "change_happened" };
}
```

**Important**: Complex promises can report misleadingly; for example, `files`
promises that set multiple parameters on a file simultaneously.

The classes for different parts of a promise are not separable. Thus, if you
promise to create and file and change its permissions, when the file exists
with incorrect permissions, `cf-agent` will report that the `promise_kept` for
the file existence, but `promise_repaired` for the permissions. If you need
separate reports, you should code two separate promises rather than
'overloading' a single one.


#### repair_failed

**Description:** Classes to be defined globally if the promise could not be
kept.

If the classes are set, the corrective action to keep the promise failed for
some reason.

**Type:** `slist`

**Allowed input range:** `[a-zA-Z0-9_$(){}\[\].:]+`

Note that any strings passed to this list are automatically canonified, so it
is unnecessary to call a canonify function on such inputs.

**Example:**

```cf3
body classes example
{
  repair_failed => { "unknown_error" };
}
```

#### repair_denied

**Description:** Classes to be defined globally if the promise could not be
repaired due to denied access to required resources.

**Type:** `slist`

**Allowed input range:** `[a-zA-Z0-9_$(){}\[\].:]+`

Note that any strings passed to this list are automatically canonified, so it
is unnecessary to call a canonify function on such inputs.

**Example:**

```cf3
body classes example
{
  repair_denied => { "permission_failure" };
}
```

In the above example, a promise could not be kept because access to a key
resource was denied.

#### repair_timeout

**Description:** Classes to be defined globally if the promise could not be
repaired due to timeout.

**Type:** `slist`

**Allowed input range:** `[a-zA-Z0-9_$(){}\[\].:]+`

Note that any strings passed to this list are automatically canonified, so it
is unnecessary to call a canonify function on such inputs.

**Example:**

```cf3
body classes example
{
  repair_timeout => { "too_slow", "did_not_wait" };
}
```

In the above example, a promise maintenance repair timed-out waiting for some
dependent resource.

#### promise_kept

**Description:** Classes to be defined globally if the promise was kept without
any corrective action.

**Type:** `slist`

**Allowed input range:** `[a-zA-Z0-9_$(){}\[\].:]+`

Note that any strings passed to this list are automatically canonified, so it
is unnecessary to call a canonify function on such inputs.

**Example:**

```cf3
body classes example
{
  promise_kept => { "success", "kaplah" };
}
```

The class in the above example is set if no action was necessary by `cf-agent`,
because the promise concerned was already kept without further action required.

**Note**: Complex promises can report misleadingly. For example,
`files`promises that set multiple parameters on a file simultaneously.

The classes for different parts of a promise are not separable. Thus, if you
promise to create and file and change its permissions, when the file exists
with incorrect permissions, `cf-agent` will report that the `promise_kept` for
the file existence, but `promise_repaired` for the permissions. If you need
separate reports, you should code two separate promises rather than
'overloading' a single one.

#### cancel_kept

**Description:** Classes to be canceled if the promise is kept.

**Type:** `slist`

**Allowed input range:** `[a-zA-Z0-9_$(){}\[\].:]+`

Note that any strings passed to this list are automatically canonified, so it
is unnecessary to call a canonify function on such inputs.

**Example:**

```cf3
body classes example
{
  cancel_kept => { "success", "kaplah" };
}
```

In the above example, if the promise was already kept and nothing was done,
cancel (undefine) any of the listed classes so that they are no longer defined.

**History:** This attribute was introduced in CFEngine version 3.0.4 (2010)

#### cancel_repaired

**Description:** Classes to be canceled if the promise is repaired.

**Type:** `slist`

**Allowed input range:** `[a-zA-Z0-9_$(){}\[\].:]+`

Note that any strings passed to this list are automatically canonified, so
it is unnecessary to call a canonify function on such inputs.

**Example:**

```cf3
body classes example
{
  cancel_repaired => { "change_happened" };
}
```

In the above example, if the promise was repaired and changes were made to the
system, cancel (undefine) any of the listed classes so that they are no longer
defined.

**History:** This attribute was introduced in CFEngine version 3.0.4 (2010)

#### cancel_notkept

**Description:** Classes to be canceled if the promise is not kept for any
reason.

**Type:** `slist`

**Allowed input range:** `[a-zA-Z0-9_$(){}\[\].:]+`

Note that any strings passed to this list are automatically canonified, so
it is unnecessary to call a canonify function on such inputs.

**Example:**

```cf3
body classes example
{
  cancel_notkept => { "failure" };
}
```

In the above example, if the promise was not kept but nothing could be done,
cancel (undefine) any of the listed classes so that they are no longer
defined.

**History:** This attribute was introduced in CFEngine version 3.0.4 (2010)

#### kept_returncodes

**Description:** Return codes that indicate a kept `commands` promise.

Currently, the attribute has impact on the following command-related promises:

* All promises of type `commands:`
* `files`-promises containing a `transformer`-attribute
* The package manager change command in `packages`-promises (e.g. the command
  for add, remove, etc.)

If none of the attributes `kept_returncodes`, `repaired_returncodes`, or
`failed_returncodes` are set, the default is to consider a return code zero as
promise repaired, and nonzero as promise failed.

**Type:** `slist`

**Allowed input range:** `[-0-9_$(){}\[\].]+`

Note that the return codes may overlap, so multiple classes may be set from one
return code. In Unix systems the possible return codes are usually in the range
from 0 to 255.

**Example:**

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

In the above example, a list of integer return codes indicates that a
command-related promise has been kept. This can in turn be used to define
classes using the `promise_kept` attribute, or merely alter the total
compliance statistics.

**History:** Was introduced in version 3.1.3, Nova 2.0.2 (2010)

#### repaired_returncodes

**Description:** Return codes that indicate a repaired `commands` promise

Currently, the attribute has impact on the following command-related promises:

* All promises of type `commands:`
* `files`-promises containing a `transformer`-attribute
* The package manager change command in `packages`-promises (e.g. the command
  for add, remove, etc.)

If none of the attributes `kept_returncodes`, `repaired_returncodes`, or
`failed_returncodes` are set, the default is to consider a return code zero as
promise repaired, and nonzero as promise failed.

**Type:** `slist`

**Allowed input range:** `[-0-9_$(){}\[\].]+`

Note that the return codes may overlap, so multiple classes may be set from one
return code. In Unix systems the possible return codes are usually in the range
from 0 to 255.

**Example:**

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

In the above example, a list of integer return codes indicating that a
command-related promise has been repaired. This can in turn be used to define
classes using the `promise_repaired` attribute, or merely alter the total
compliance statistics.

**History:** Was introduced in version 3.1.3, Nova 2.0.2 (2010)

#### failed_returncodes

**Description:** A `failed_returncodes` slist contains return codes indicating
a failed command-related promise.

Currently, the attribute has impact on the following command-related promises:

* All promises of type `commands:`
* `files`-promises containing a `transformer`-attribute
* The package manager change command in `packages`-promises (e.g. the command
  for add, remove, etc.)

If none of the attributes `kept_returncodes`, `repaired_returncodes`, or
`failed_returncodes` are set, the default is to consider a return code zero as
promise repaired, and nonzero as promise failed.

**Type:** `slist`

**Allowed input range:** `[-0-9_$(){}\[\].]+`

Note that the return codes may overlap, so multiple classes may be set from one
return code. In Unix systems the possible return codes are usually in the range
from 0 to 255.

**Example:**

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
      hasfailed::
        "The files-promise failed!";
}

body classes example
{
  failed_returncodes => { "1" };
  repair_failed => { "hasfailed" };
}

body copy_from copy(file)
{
  source => "$(file)";
}
```

The above example contains a list of integer return codes indicating that a
command-related promise has failed. This can in turn be used to define classes
using the `promise_repaired` attribute, or merely alter the total compliance
statistics.

**History:** Was introduced in version 3.1.3, Nova 2.0.2 (2010)

#### persist_time

**Description:** The number of minutes the specified classes should remain
active.

By default classes are ephemeral entities that disappear when `cf-agent`
terminates. By setting a persistence time, they can last even when the agent is
not running. When a persistent class is activated it gets `scope` namespace.

**Type:** `int`

**Allowed input range:** `0,99999999999`

**Example:**

```cf3
body classes example
{
  persist_time => "10";
}
```

**See also:** [`persistance` classes attribute][classes#persistence], [`persist_time` in classes body][Promise Types#persist_time]

#### timer_policy

**Description:** Determines whether a persistent class restarts its counter
when rediscovered.

In most cases resetting a timer will give a more honest appraisal of which
classes are currently important, but if we want to activate a response of
limited duration as a rare event then an absolute time limit is useful.

**Type:** (menu option)

**Allowed input range:**

```
    absolute
    reset
```

**Default value:** reset

**Example:**

```cf3
body classes example
{
  timer_policy => "reset";
}
```

### comment

**Description:** Describes the real intention of the promise.

Comments written in code follow the program, they are not merely discarded;
they appear in verbose logs and error messages.

**Type:** `string`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
  comment => "This comment follows the data for reference ...",
```

### depends_on

**Description:** A list of promise handles for promises that must have an outcome of KEPT or REPAIRED in order for the promise to be actuated.

This is a list of promise handles for whom this promise is a promisee. In other
words, we acknowledge that this promise will be affected by the list of
promises whose handles are specified. It has the effect of partially ordering
promises.

As of version 3.4.0, this feature may be considered short-hand for setting
classes. If one promise depends on a list of others, it will not be verified
unless the dependent promises have already been verified and kept: in other
words, as long as the dependent promises are either kept or repaired the
dependee can be verified.

Handles in other namespaces may be referred to by namespace:handle.

**Type:** `slist`

**Allowed input range:** (arbitrary string)

**Example:**

[%CFEngine_include_example(depends_on.cf)%]

### handle

**Description:** A unique id-tag string for referring to this as a promisee
elsewhere.

A promise handle allows you to refer to a promise as the promisee of
`depends_on` client of another promise. Handles are essential for mapping
dependencies and performing impact analyses.

**Type:** `string`

**Allowed input range:** (arbitrary string)

Handles may consist of regular identifier characters. If the handle is likely to
contain non-identifier characters, you can use `canonify()` to turn them into
such characters.

**Example:**

```cf3
  access:

      "/source"
        handle  => "update_rule",
        admit   => { "127.0.0.1" };
```

**Notes:** If the handle name is based on a variable, and the variable
fails to expand, the handle will be based on the name of the variable
rather than its content.

### if

**Description:** Class expression to further restrict the promise context.
Previously called `ifvarclass`.

This is an additional class expression that will be evaluated after the
`class::` classes have selected promises. It is provided in order to enable a
channel between variables and classes.

The result is thus the logical AND of the ordinary classes and the variable
classes.

**Type:** `string`

**Allowed input range:** (arbitrary string)

**Example:**

The generic example has the form:

```cf3
  promise-type:

      "promiser"
        if => "$(program)_running|($(program)_notfoundHr12)";
```

A specific example would be:

```cf3
bundle agent example
{
  commands:

      any::

        "/bin/echo This is linux"
          if => "linux";

        "/bin/echo This is solaris"
          if => "solaris";
}
```

This function is provided so that one can form expressions that link variables
and classes. For example:

```cf3
  # Check that all components are running

  vars:

      "component" slist => { "cf-monitord", "cf-serverd" };

  processes:

      "$(component)" restart_class => canonify("$(component)_not_runnning");

  commands:

      "/var/cfengine/bin/$(component)"
        if => canonify("$(component)_not_runnning");
```

**Notes:**

While strings are automatically canonified during class definition, they are not
automatically canonified when checking. You may need to use `canonify()` to
convert strings containing invalid class characters into a valid class.

In most cases, `if => something` and `if => not(something)` are opposite,
but because of [function skipping](Funcions#Function_Skipping), both of these
will be skipped if `something` is never resolved:

```cf3
bundle agent main
{
  classes:
      "a" if => "$(no_such_var)";      # Will be skipped
      "b" if => not("$(no_such_var)"); # Will be skipped
}
```

If you need a condition which defaults to _not skipping_ in the cases above,
`unless` does this; for any expression where `if` will skip, `unless` will not
skip.

`if` and `unless` both make choices about whether to _skip_ a promise. Both
`if` and `unless` can _force_ a promise to be skipped - if a promise has both
`if` and `unless` constraints, _skipping_ takes precedence.

**History:** In 3.7.0 `if` was introduced as a shorthand for `ifvarclass` (and
`unless` as an opposite).

### ifvarclass

**Description:** Deprecated, use [`if`][Promise Types#if] instead.

**History:** New name `if` was introduced in 3.7.0, `ifvarclass` deprecated in 3.17.0.

### meta

**Description:** A list of strings to be associated with the promise for knowledge management purposes.
The strings are usually called "meta tags" or simply "tags."

Any promise (of any type) can be given a "meta" attribute.
Since the right hand side for this attribute is an slist, multiple strings (tags) can be associated with the same promise.

Note that the inventory reporting of CFEngine Enterprise 3.6 and later uses the meta attributes `inventory` and `attribute_name=`, so these should be considered reserved for this purpose.

A "meta" attribute can likewise be added into any body (of any type).

**Type:** `slist`

**Allowed input range:** (arbitrary string list)

**Example:**

```cf3
  files:

      "/etc/special_file"

        comment => "Special file is a requirement. Talk to John.",
        create => "true",

        meta => { "owner=John",  "version=2.0", "ticket=CFE-1234" };
```

Another example:

```cf3
  some_promise_type:
      any::
        "my_promiser"
          meta => { "Team Foo", "workaround", "non-critical" };
```

The meta tags may be referred to programmatically in various ways, or may be solely for human consumption.
Meta tags on vars promises and classes promises are particularly suited for programmatic interpretation;
meta tags on other promise types (or in bodies) are more likely to be intended only for human consumption.

Relevant CFEngine functions are:
`classesmatching()`, `classmatch()`, `countclassesmatching()`, `getclassmetatags()`, `getvariablemetatags()`, `variablesmatching()`, `variablesmatching_as_data()`.

Also see [meta promises][meta]: While "meta" attribute can be added to a promise of any type, there can also be promises of promise type "meta" added to any bundle.
If mention is made of "tags" on a *bundle*, what is actually meant is meta *promises* in that bundle.
(This is just a terminology point.)

**Note:** When a variable is re-defined the associated meta tags are also re-defined.

**History:** Was introduced in 3.3.0, Nova 2.2.0 (2012)


### unless

**Description:** Class expression to further restrict the promise context. This
is exactly like `if` but logically inverted; see its description
for details. For any case where `if` would skip the promise, unless should
evaluate the promise.

**Type:** `string`

**Allowed input range:** (arbitrary string)

**Example:**

The generic example has the form:

```cf3
  promise-type:
      "promiser"
        unless => "forbidden";
```

A specific example would be:

```cf3
bundle agent example
{
  commands:
      any::
        "/bin/echo This is NOT linux"
          unless => "linux";
}
```

**Notes:**

While strings are automatically canonified during class definition, they are not
automatically canonified when checking. You may need to use `canonify()` to
convert strings containing invalid class characters into a valid class.

`if` and `unless` both make choices about whether to _skip_ a promise. Both
`if` and `unless` can _force_ a promise to be skipped - if a promise has both
`if` and `unless` constraints, _skipping_ takes precedence.

`unless` will skip a promise, only if the class expression is evaluated to
false. If the class expression is true, or not evaluated (because of
unexpanded variables, or unresolved function calls) it will not cause the
promise to be skipped. Since `if` defaults to skipping in those cases,
`unless` defaults to _not skipping_.

```cf3
bundle agent main
{
  classes:
      "a"     if => "any";            # Will be evaluated
      "b" unless => "any";            # Will be skipped

      "c"     if => "$(no_such_var)"; # Will be skipped
      "d" unless => "$(no_such_var)"; # Will be evaluated
}
```

**History:** Was introduced in 3.7.0.

### with

**Description:** Reusable promise attribute to avoid repetition.

Very often, it's handy to refer to a single value in many places in a promise,
especially in the promiser. Especially when iterating over a list, the `with`
attribute can save you a lot of work and code.

Another use of the `with` attribute is when in `reports` you want to use
`format()` or other functions that produce lots of text, but don't want to
create an intermediate variable.

Another common use of `with` is to avoid canonifying a value. In that case,
you'd use `with => canonify("the value")` so you don't have to create a
"canonification" array.

**Type:** `string`

**Allowed input range:** (arbitrary string)

**Example:**

[%CFEngine_include_snippet(with.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(with.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**History:** Was introduced in 3.11.0

## Common Body Attributes

The following attributes are available to all body types.

### inherit_from

**Description:** Inherits all attributes from another body of the same
type as a function call. For a detailed description, see
[**Bodies**][bodies].

**Type:** `fncall`

**Allowed input range:** (arbitrary body invocation)

**Examples:**

[%CFEngine_include_example(inherit_from.cf)%]

[%CFEngine_include_example(inherit_from_classes.cf)%]

**History:** Was introduced in 3.8.0.

### meta

**Description:** A list of strings to be associated with the body for knowledge management purposes.
The strings are usually called "meta tags" or simply "tags."

Any body can be given a "meta" attribute.
Since the right hand side for this attribute is an slist, multiple strings (tags) can be associated with the same body.

**Type:** `slist`

**Allowed input range:** (arbitrary string list)

**Example:**

```cf3
body ANYTYPE mybody
{
  meta => { "deprecated" , "CFE-1234", "CVE-2020-1234" };
}
```

**Note:** When a variable is re-defined the associated meta tags are also re-defined.

**History:** Was introduced in 3.7.0.
