---
layout: default
title: Components and Common Control
categories: [Reference, Components]
published: true
sorting: 10
alias: reference-components.html
tags: [Reference, Components]
---

While promises to configure your system are entirely user-defined, the
details of the operational behavior of the CFEngine software is of
course hard-coded. You can still configure the details of this
behavior using the `control` promise bodies. Control behavior is
defined in bodies because the actual promises are fixed and you only
change their details within sensible limits.

See the [manual][The CFEngine Components] for a high-level overview of the 
CFEngine components, and each component's reference documentation for the 
details about the specific control bodies.

## Common Control

The `common` control body refers to those promises that are
hard-coded into all the components of CFEngine, and therefore
affect the behavior of all the components.


```cf3 
     body common control
     
     {
     inputs  => {
                "update.cf",
                "library.cf"
                };
     
     bundlesequence  => {
                        update("policy_host.domain.tld"),
                        "main",
                        "cfengine2"
                        };
     
     goal_categories => { "goals", "targets", "milestones" };
     goal_patterns   => { "goal_.*", "target.*" };
     
     output_prefix => "cfengine>";
     version => "1.2.3";
     }
```


### bundlesequence

**Description:** The `bundlesequence` contains promise bundles
to verify, in a specific order.

The `bundlesequence` determines which of the compiled bundles will
be executed and in what order they will be executed. The list
refers to the names of bundles (which might be parameterized,
function-like objects).

There is no default value for `bundlesequence`, and the absence of
a `bundlesequence` will cause a compilation error. A `bundlesequence`
may also be specified using the `-b` or `--bundlesequence` command
line option.

**Type:** `slist`

**Allowed input range:** `.*`

**Example:**

```cf3
    body common control
    
    {
    bundlesequence  => {
                       update("policy_host.domain.tld"),
                       "main",
                       "cfengine2"
                       };
    }
```

The order in which you execute bundles can affect the outcome of
your promises. In general you should always define variables before
you use them.

The `bundlesequence` is like a genetic makeup of a machine. The
bundles act like characteristics of the systems. If you want
different systems to have different `bundlesequences`, distinguish
them with classes

```cf3
    webservers::
    
      bundlesequence => { "main", "web" };
    
    others::
    
      bundlesequence => { "main", "otherstuff" };
```

If you want to add a basic common sequence to all sequences, then
use global variable lists to do this:

```cf3
    body common control
    {
    webservers::
    
      bundlesequence => { @(g.bs), "web" };
    
    others::
    
      bundlesequence => { @(g.bs), "otherstuff" };
    
    }
    
    bundle common g
    {
    vars:
    
      "bs" slist => { "main", "basic_stuff" }; 
    }
```

### cache_system_functions

**Description:** Controls the caching of the results of system
functions, e.g. `execresult` and `returnszero` for shell execution and
`ldapvalue` and friends for LDAP queries.  Without this setting,
CFEngine's evaluation model will evaluate functions multiple times,
which is a performance concern.  See [`Functions`][Functions].

Although you can override this to `false`, in practice you should
almost never need to do so.  The effect of having it `true` (the
default) is that the expensive functions will be run just once and
then their result will be cached.

**Type:** [`boolean`][boolean]

**Default value:** true

**Example:**

```cf3
    cache_system_functions => "true";
```

**History:** Was introduced in version 3.6.0.

### goal_patterns

**Description:** Contains regular expressions that match promisees/topics 
considered to be organizational goals

It is used as identifier to mark business and organizational goals in
CFEngine Enterprise. CFEngine uses this to match promisees that represent 
business goals in promises.

**Type:** `slist`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
    body common control
    {
    goal_patterns => { "goal_.*", "target.*" };
    }
```

**History:** Was introduced in version 3.1.5, Nova 2.1.0 (2011)


### ignore_missing_bundles

**Description:** Determines whether to ignore missing bundles.

If `ignore_missing_bundles` is set to true, if any bundles in the bundle 
sequence do not exist, ignore and continue.

**Type:** [`boolean`][boolean]

**Default value:** false

**Example:**

```cf3
    ignore_missing_bundles => "true";
```

**Notes:**

This authorizes the bundlesequence to contain possibly
"nonexistent" pluggable modules. It defaults to false, whereupon
undefined bundles cause a fatal error in parsing, and a transition
to failsafe mode.


### ignore_missing_inputs

**Description:** If any input files do not exist, ignore and continue

The inputs lists determines which files are parsed by CFEngine.
Normally stringent security checks are made on input files to
prevent abuse of the system by unauthorized users. 

Sometimes however, it is appropriate to consider the automatic plug-in of
modules that might or might not exist. This option permits CFEngine
to list possible files that might not exist and continue 'best
effort' with those that do exist. The default of all Booleans is
false, so the normal behavior is to signal an error if an input is
not found.

**Type:** [`boolean`][boolean]

**Default value:** false

**Example:**

```cf3
    ignore_missing_inputs => "true";
```

### inputs

**Description:** The `inputs` slist contains additional filenames to parse for promises.

The filenames specified are all assumed to be in the same directory
as the file which references them (this is usually
`$(sys.workdir)/inputs`, but may be overridden by the `-f` or
`--file` command line option.

**Type:** `slist`

**Allowed input range:** `.*`

**Example:**

```cf3
    body common control
    {
    inputs  => {
               "update.cf",
               "library.cf"
               };
    }
```

**Notes:**

If no filenames are specified, no other filenames will be included in the 
compilation process.

### version

**Description:** The `version` string contains the scalar version of the 
configuration. 

It is is used in error messages and reports.

**Type:** `string`

**Allowed input range:** (arbitrary string)

This string should not contain the colon ':' character, as this has
a special meaning in the context of knowledge management. This
restriction might be lifted later.

**Example:**

```cf3
    body common control
    {
    version => "1.2.3";
    }
```

### lastseenexpireafter

**Description:** The value of `lastseenexpireafter` is the number of minutes 
after which last-seen entries are purged.

**Type:** `int`

**Allowed input range:** `0,99999999999`

**Default value:** One week

**Example:**

```cf3
    body common control
    {
    lastseenexpireafter => "72";
    }
```

### output_prefix

**Description:** The string prefix for standard output

**Type:** `string`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
    body common control
    {
    output_prefix => "my_cf3";
    }
```

**Notes:**

On native Windows versions of CFEngine (Enterprise), this
string is also prefixed messages in the event log.

### domain

**Description:** The `domain` string specifies the domain name for this host.

There is no standard, universal or reliable way of determining the
DNS domain name of a host, so it can be set explicitly to simplify
discovery and name-lookup.

**Type:** `string`

**Allowed input range:** `.*`

**Example:**

```cf3
    body common control
    {
    domain => "example.org";
    }
```

### require_comments

**Description:** The `require_comments` menu option policy warns about 
promises that do not have comment documentation.

When true, `cf-promises` will report loudly on promises that do not have
comments. Variables promises are exempted from this rule, since
they may be considered self-documenting. This may be used as a policy Quality 
Assurance measure, to remind policy makers to properly document their 
promises.

**Type:** [`boolean`][boolean]

**Default value:** false

**Example:**

```cf3
    body common control
    
    {
    common::
    
    require_comments => "true";
    }
```


### host_licenses_paid

**Deprecated: 3.5**

**Description:** The value of `host_licenses_paid` represents the number
of licenses that you promise to have paid for by setting this value 
(legally binding for CFEngine Enterprise).

Licensees of CFEngine Enterprise have to make a promise in acceptance of 
contract terms by setting this value to the number of licenses they have paid 
for. This is tallied with the number of licenses granted. This declaration 
should be placed in all separate configuration files, e.g. failsafe.cf, 
promises.cf.

**Type:** `int`

**Allowed input range:** `0,99999999999`

**Default value:** 25

**Example:**

```cf3
    body common control
    {
    host_licenses_paid => "1000";
    }
```

### site_classes

**Description:** A `site_classes` contains classes that will represent 
geographical site locations for hosts. These should be defined elsewhere in 
the configuration in a classes promise.

This list is used to match against topics when connecting
inferences about host locations in the knowledge map. Normally any
CFEngine classes promise whose name is defined as a thing or topic
under class `locations::` will be assumed to be a location defining
classifier. This list will add alternative class contexts for
interpreting location.

**Type:** `slist`

**Allowed input range:** `[a-zA-Z0-9_!&@@$|.()\[\]{}:]+`

Each string is expected to be a class.

**Example:**

```cf3
    body common control
    {
    site_classes => { "datacenters","datacentres"  }; # locations is by default
    }
```

**History:** Was introduced in version 3.2.0, Nova 2.1.0 (2011)


### syslog_host

**Description:** The `syslog_host` contains the name or address of a 
host to which syslog messages should be sent directly by UDP.

This is the hostname or IP address of a local syslog service to which all
CFEngine's components may promise to send data. 

**Type:** `string`

**Allowed input range:** `[a-zA-Z0-9_$(){}.:-]+`

**Default value:** 514

**Example:**

```cf3
    body common control
    {
    syslog_host => "syslog.example.org";
    syslog_port => "514";
    }
```

### syslog_port

**Description:** The value of `syslog_port` represents the port number 
of a UDP syslog service.

It is the UDP port of a local syslog service to which all CFEngine's
components may promise to send data. 

**Type:** `int`

**Allowed input range:** `0,99999999999`

**Example:**

```cf3
    body common control
    {
    syslog_host => "syslog.example.org";
    syslog_port => "514";
    }
```

### fips_mode

**Description:** The `fips_mode` menu option policy determines whether 
to activate full FIPS mode restrictions.

In CFEngine Enterprise, this value may be set to avoid the use of old 
deprecated algorithms that are no longer FIPS 140-2 compliant. If not set, 
there is some degree of compatibility with older versions and algorithms. 
During an upgrade, setting this parameter can cause a lot of recomputation of 
checksums etc. Government bodies starting with CFEngine Enterprise 2.0 or  
higher should set this to 'true' from the start.

**Type:** [`boolean`][boolean]

**Default value:** false

**Example:**

```cf3
    body common control
    {
    fips_mode => "true";
    }
```
