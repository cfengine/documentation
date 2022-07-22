---
layout: default
title: Components
published: true
sorting: 10
tags: [Reference, Components]
---

While promises to configure your system are entirely user-defined, the
details of the operational behavior of the CFEngine software is of
course hard-coded. You can still configure the details of this
behavior using the `control` promise bodies. Control behavior is
defined in bodies because the actual promises are fixed and you only
change their details within sensible limits.

See the
[introduction][Overview#CFEngine Component Applications and Daemons]
for a high-level overview of the
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

The `bundlesequence` determines which of the compiled bundles will be executed
by `cf-agent` and in what order they will be executed. The list refers to the
names of bundles (which might be parameterized, function-like objects).


The default value for `bundlesequence` is `{ "main" }`.

A `bundlesequence` may also be specified using the `-b` or
`--bundlesequence` command line option.

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

**Note:** Only `common` and `agent` bundles are allowed to be listed in the
bundlesequence.

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

**History:** The default to `{ "main" }` was introduced in version 3.7.0, so if
you expect your policies to be run by older version, you'll need an explicit
`bundlesequence`.

### bwlimit

**Description:** Coarse control of bandwidth any cf-serverd or cf-agent process
will send *out*. In Bytes/sec.

Bandwidth limit is meant to set an upper bound of traffic coming out of CFEngine
agents or servers, as a countermeasure against network abuse from them. The limit
is applied to all interfaces (in total), a single process at a time. It can
prevent network being flooded by CFEngine traffic when large files or many agents
hit a single cf-serverd.

For more fine-grained control, please use operating system (eg. iptables)
facilities.

**Note:** Bandwidth limiting is currently not supported on Windows.

**Type:** `float`

**Default value:** none (no limit)

**Example:**

```cf3
    body common control

    {
      bwlimit => "10M";
    }
```

In this example,  bwlimit is set to 10MBytes/sec = 80Mbit/s meaning that
CFEngine would only consume up to ~80% of any 100Mbit ethernet interface.


### cache_system_functions

**Description:** Controls the caching of the results of system
functions, e.g. `execresult()` and `returnszero()` for shell execution and
`ldapvalue()` and friends for LDAP queries.  Without this setting,
CFEngine's evaluation model will evaluate functions multiple times,
which is a performance concern.  See [`Functions`][Functions].

Although you can override this to `false`, in practice you should
almost never need to do so.  The effect of having it `true` (the
default) is that the expensive functions will be run just once and
then their result will be cached.

Note that caching is per-process so results will not be cached between
runs of e.g. `cf-agent` and `cf-promises`.

**Type:** [`boolean`][boolean]

**Default value:** true

**Example:**

```cf3
    cache_system_functions => "true";
```

**See also:** [`ifelapsed` in action bodies][Promise Types#ifelapsed]

**History:**
- Introduced in version 3.6.0.


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

**See also:** [`inputs`][file control#inputs] in `body file control`

**Notes:**

If no filenames are specified, no other filenames will be included in the
compilation process.

Library contents are checked for duplication by path and by hash.  For
example, if you put `library.cf` twice in your `inputs`, the duplicate
`library.cf` is noticed because the same path is included twice.  A
verbose-level message is emitted but otherwise there is no error.

In addition, if you include a file once with path `/x/y/z.cf` and
again with path `/x/./y/z.cf`, the duplicate file will be rejected
regardless of any path tricks or symbolic links.  The contents are
hashed, so the same file can't be included twice.

### lastseenexpireafter

**Description:** The value of `lastseenexpireafter` is the number of minutes
after which last-seen entries are purged. It is an **enterprise-only** feature.

**Type:** `int`

**Allowed input range:** `0,99999999999`

**Default value:** One week

**Note:** This value affects the `hostsseen()` function and license counting by
`cf-hub` in the Enterprise edition.

**Example:**

```cf3
    body common control
    {
    lastseenexpireafter => "72";
    }
```

**See also:** [hostsseen()][hostsseen], [cf-hub][cf-hub]

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

### package_inventory

**Description:** List of package module bodies to query for package lists.

Defines the list of [`package module bodies`][packages] which will be queries for
package lists, for use in `packagematching()`, `packageupdatesmatching()` and in
Enterprise inventory reporting.

**Type:** `slist`

**Allowed input range:** (body names)

**Example:**

```cf3
body common control
{
    package_inventory => { "apt_get" };
}
```

### package_module

**Description:** The default package module body to use.

Defines the default package module body to use for [package promises][packages],
if none is specified in the promise.

**Type:** `string`

**Allowed input range:** (body name)

**Example:**

```cf3
body common control
{
    package_module => "apt_get";
}
```

### protocol_version

**Description:** Defines the protocol to use for all outgoing connections.

[%CFEngine_promise_attribute(undefined)%]

**Note:** `protocol_version` can be specified at the individual promise level
using the [`body copy_from protocol_version`][files#protocol_version]
attribute. When undefined (the default) peers automatically negotiate the latest protocol version.

**See also:**  [`body copy_from protocol_version`][files#protocol_version], `allowlegacyconnects`, [`allowtlsversion`][cf-serverd#allowtlsversion], [`allowciphers`][cf-serverd#allowciphers], [`tls_min_version`][Components#tls_min_version], [`tls_ciphers`][Components#tls_ciphers], [`encrypt`][files#encrypt], [`logencryptedtransfers`][cf-serverd#logencryptedtransfers], [`ifencrypted`][access#ifencrypted]

**History:**

* Introduced in CFEngine 3.6.0 with `protocol_version` `1` (`classic`) and `protocol_version` `2` (`tls`)
* Added `protocol_version` `3` (`cookie`) in CFEngine 3.15.0

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

**Default value:** ```localhost```

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

**Default value:** ```514```

**Example:**

```cf3
    body common control
    {
    syslog_host => "syslog.example.org";
    syslog_port => "514";
    }
```

### system_log_level

**Description:** The minimum log level required for log messages to go to the system log (e.g. syslog, Windows Event Log).

**Type:** `string`

**Allowed Input range:** `(critical|error|warning|notice|info)`

**Default value:** ` ` (unspecified)

**Example:**

Prevent messages lower than _critical_ on Windows.

```cf3
body common control
{
@if minimum_version(3.18.1)
  windows::
    system_log_level => "critical";
  cfengine::
@endif
}
```

**History:**

* Introduced in 3.19.0, 3.18.1

### tls_ciphers

**Description:** List of ciphers allowed when making **outgoing** connections.

For a list of possible ciphers, see man page for "openssl ciphers".

[%CFEngine_promise_attribute(undefined)%]

**Example:**

```cf3
body common control
{
    # Use one of these ciphers when making outbound connections
    tls_ciphers => "AES128-SHA";
}
```

**See also:** [`protocol_version`][Components#protocol_version], [`allowciphers`][cf-serverd#allowciphers], [`tls_min_version`][Components#tls_min_version], [`allowtlsversion`][cf-serverd#allowtlsversion], [`encrypt`][files#encrypt], [`logencryptedtransfers`][cf-serverd#logencryptedtransfers], [`ifencrypted`][access#ifencrypted]

**History:** Introduced in CFEngine 3.7.0

### tls_min_version

**Description:** Minimum tls version to allow for **outgoing** connections.

[%CFEngine_promise_attribute(1.0)%]

```cf3
body common control
{
    # Allow only TLSv1.1 or higher for outgoing connections
    tls_min_version => "1.1";
}
```

**See also:** [`protocol_version`][Components#protocol_version], [`allowciphers`][cf-serverd#allowciphers], [`tls_ciphers`][Components#tls_ciphers], [`allowtlsversion`][cf-serverd#allowtlsversion], [`encrypt`][files#encrypt], [`ifencrypted`][access#ifencrypted], [`logencryptedtransfers`][cf-serverd#logencryptedtransfers]

**History:** Introduced in CFEngine 3.7.0

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


## Deprecated attributes in body common control

The following attributes were functional in previous versions
of CFEngine, but today they are deprecated, either because
their functionality is being handled trasparently or because
it doesn't apply to current CFEngine version.

* fips_mode
* host_licenses_paid
