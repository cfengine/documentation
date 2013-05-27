---
layout: default
title: common control
categories: [Reference, Components, commmon control]
published: true
alias: reference-components-common-control.html
tags: [body, bodies, components, common, control, promises, bundlesequence]
---

# `common` control promises
 
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

The `common` control body refers to those promises that are
hard-coded into all the components of CFEngine, and therefore
affect the behaviour of all the components.




## `bundlesequence`

**Type**: slist

**Allowed input range**: `.*`

**Synopsis**: List of promise bundles to verify in order

    body common control
    
    {
    bundlesequence  => {
                       update("policy_host.domain.tld"),
                       "main",
                       "cfengine2"
                       };
    }

**Notes**:

The `bundlesequence` determines which of the compiled bundles will
be executed and in what order they will be executed. The list
refers to the names of bundles (which might be parameterized
function-like objects).

The order in which you execute bundles can affect the outcome of
your promises. In general you should always define variables before
you use them.

The `bundlesequence` is like a genetic makeup of a machine. The
bundles act like characteristics of the systems. If you want
different systems to have different bundlesequences, distinguish
them with classes

    webservers::
    
      bundlesequence => { "main", "web" };
    
    others::
    
      bundlesequence => { "main", "otherstuff" };

If you want to add a basic common sequence to all sequences, then
use global variable lists to do this

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

**Default value**:

There is no default value for `bundlesequence`, and the absence of
a `bundlesequence` will cause a compilation error. A bundlesequence
may also be specified using the `-b` or `--bundlesequence` command
line option.





## `goal_patterns`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: A list of regular expressions that match
promisees/topics considered to be organizational goals

    body common control
    {
    goal_patterns => { "goal_.*", "target.*" };
    }

**Notes**:

*History*: Was introduced in version 3.1.5, Nova 2.1.0 (2011)

Used as identifier to mark business and organizational goals in
commercial versions of CFEngine. CFEngine uses this to match
promisees that represent business goals in promises.





## `ignore_missing_bundles`

**Type**: (menu option)

**Allowed input range**

                   true
                   false
                   yes
                   no
                   on
                   off

**Default value:** false

**Synopsis**: If any bundles in the bundlesequence do not exist,
ignore and continue

    ignore_missing_bundles => "true";

**Notes**:

This authorizes the bundlesequence to contain possibly
"nonexistent" pluggable modules. It defaults to false, whereupon
undefined bundles cause a fatal error in parsing, and a transition
to failsafe mode.





## `ignore_missing_inputs`

**Type**: (menu option)

**Allowed input range**

                   true
                   false
                   yes
                   no
                   on
                   off

**Default value:** false

**Synopsis**: If any input files do not exist, ignore and continue

    ignore_missing_inputs => "true";

**Notes**:

The inputs lists determines which files are parsed by CFEngine.
Normally stringent security checks are made on input files to
prevent abuse of the system by unauthorized users. Sometimes
however, it is appropriate to consider the automatic plug-in of
modules that might or might not exist. This option permits CFEngine
to list possible files that might not exist and continue \`best
effort' with those that do exist. The default of all Booleans is
false, so the normal behaviour is to signal an error if an input is
not found.





## `inputs`

**Type**: slist

**Allowed input range**: `.*`

**Synopsis**: List of additional filenames to parse for promises

    body common control
    {
    inputs  => {
               "update.cf",
               "library.cf"
               };
    }

**Notes**:  
The filenames specified are all assumed to be in the same directory
as the file which references them (this is usually
`$(sys.workdir)/inputs`, but may be overridden by the `-f` or
`--file` command line option.

**Default value**:

There is no default value. If no filenames are specified, no other
filenames will be included in the compilation process.





## `version`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: Scalar version string for this configuration

    body common control
    {
    version => "1.2.3";
    }

**Notes**:

The version string is used in error messages and reports.

This string should not contain the colon ':' character, as this has
a special meaning in the context of knowledge management. This
restriction might be lifted later.





## `lastseenexpireafter`

**Type**: int

**Allowed input range**: `0,99999999999`

**Default value:** One week

**Synopsis**: Number of minutes after which last-seen entries are
purged

    body common control
    {
    lastseenexpireafter => "72";
    }

**Notes**:

Default time is one week.





## `output_prefix`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: The string prefix for standard output

    body common control
    {
    output_prefix => "my_cf3";
    }

**Notes**:

On native Windows versions of CFEngine (Enterprise), this
string is also prefixed messages in the event log.





## `domain`

**Type**: string

**Allowed input range**: `.*`

**Synopsis**: Specify the domain name for this host

    body common control
    {
    domain => "example.org";
    }

**Notes**:

There is no standard, universal or reliable way of determining the
DNS domain name of a host, so it can be set explicitly to simplify
discovery and name-lookup.





## `require_comments`

**Type**: (menu option)

**Allowed input range**

                   true
                   false
                   yes
                   no
                   on
                   off

**Default value:** false

**Synopsis**: Warn about promises that do not have comment
documentation

    body common control
    
    {
    common::
    
    require_comments => "true";
    }

**Notes**:

This may be used as a policy Quality Assurance measure, to remind
policy makers to properly document their promises. When true,
`cf-promises` will report loudly on promises that do not have
comments. Variables promises are exempted from this rule, since
they may be considered self-documenting.





## `host_licenses_paid`

**Type**: int

**Allowed input range**: `0,99999999999`

**Default value:** 25

**Synopsis**: The number of licenses that you promise to have paid
for by setting this value (legally binding for commercial license)

    body common control
    {
    host_licenses_paid => "1000";
    }

**Notes**:

Licensees of the commercial CFEngine releases have to make a
promise in acceptance of contract terms by setting this value to
the number of licenses they have paid for. This is tallied with the
number of licenses granted. This declaration should be placed in
all separate configuration files, e.g. failsafe.cf, promises.cf.





## `site_classes`

**Type**: clist

**Allowed input range**: `[a-zA-Z0-9_!&@@$|.()\[\]{}:]+`

**Synopsis**: A list of classes that will represent geographical
site locations for hosts. These should be defined elsewhere in the
configuration in a classes promise.

    body common control
    {
    site_classes => { "datacenters","datacentres"  }; # locations is by default
    }

**Notes**:

*History*: Was introduced in version 3.2.0, Nova 2.1.0 (2011)

This list is used to match against topics when connecting
inferences about host locations in the knowledge map. Normally any
CFEngine classes promise whose name is defined as a thing or topic
under class `locations::` will be assumed to be a location defining
classifier. This list will add alternative class contexts for
interpreting location.





## `syslog_host`

**Type**: string

**Allowed input range**: `[a-zA-Z0-9_$(){}.:-]+`

**Default value:** 514

**Synopsis**: The name or address of a host to which syslog
messages should be sent directly by UDP

    body common control
    {
    syslog_host => "syslog.example.org";
    syslog_port => "514";
    }

**Notes**:

The hostname or IP address of a local syslog service to which all
CFEngine's components may promise to send data. This feature is
provided in CFEngine Nova and above.





## `syslog_port`

**Type**: int

**Allowed input range**: `0,99999999999`

**Synopsis**: The port number of a UDP syslog service

    body common control
    {
    syslog_host => "syslog.example.org";
    syslog_port => "514";
    }

**Notes**:

The UDP port of a local syslog service to which all CFEngine's
components may promise to send data. This feature is provided in
CFEngine Nova and above.





## `fips_mode`

**Type**: (menu option)

**Allowed input range**

                   true
                   false
                   yes
                   no
                   on
                   off

**Default value:** false

**Synopsis**: Activate full FIPS mode restrictions

    body common control
    {
    fips_mode => "true";
    }

**Notes**:

Appears as of Nova 2.0. If CFEngine commercial editions this value
may be set to avoid the use of old deprecated algorithms that are
no longer FIPS 140-2 compliant. If not set, there is some degree of
compatibility with older versions and algorithms. During an
upgrade, setting this parameter can cause a lot of recomputation of
checksums etc. Government bodies starting with Nova 2.0 or higher
should set this to 'true' from the start.

