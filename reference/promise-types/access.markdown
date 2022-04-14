---
layout: default
title: access
published: true
tags: [reference, bundle server, cf-serverd, access, server, promise types, acl, trust, encryption]
---

Access promises are conditional promises made by resources living on the server.

The promiser is the name of the resource affected and is interpreted to be a path, unless a
different `resource_type` is specified. Access is then granted to hosts listed in `admit_ips`,
`admit_keys` and `admit_hostnames`, or denied using the counterparts `deny_ips`, `deny_keys`
and `deny_hostnames`.

You layer the access policy by denying all access and then allowing it
only to selected clients, then denying to an even more restricted set.

```cf3
bundle server my_access_rules()
{
access:

  "/source/directory"
    comment => "Access to file transfer",
    admit_ips   => { "192.168.0.1/24" };
}
```

For file copy requests, the file becomes transferable to the remote client according to the
conditions specified in the access promise. Use `ifencrypted` to grant access only if the
transfer is encrypted in the "classic" CFEngine protocol (the TLS protocol is always encrypted).

When access is granted to a directory, the promise is automatically
made about all of its contents and sub-directories.

Use the `maproot` attribute (like its NFS counterpart) to control
which hosts can see file objects not owned by the server process
owner.

File resources are specified using an absolute filepath, but can set a `shortcut` through
which clients can access the resource using a logical name, without having any detailed
knowledge of the filesystem layout on the server. Specifically in access promises about
files, a special variable context `connection` is available with variables `ip`, `key`
and `hostname`, containing information about the connection through which access is attempted.

```cf3
   "/var/cfengine/cmdb/$(connection.key).json"
      shortcut   => "me.json",
      admit_keys => { "$(connection.key)" };
```

In this example, requesting the file `me.json` will transfer the file stored on the
server under the name `/var/cfengine/cmdb/SHA=....json` to the requesting host,
where it will be received as `me.json`.
Note that the usage of the `$(connection.*)` variables is strictly
limited to literal strings within the promiser and admit/deny lists; they cannot be
passed to functions or stored in other variables.

With CFEngine Enteprise, access promises can be made about additional query data for
reporting and orchestration.

```cf3
  # Grant orchestration communication

  "did.*"
          comment => "Access to class context (enterprise)",
    resource_type => "context",
        admit_ips => { "127.0.0.1" };


  "value of my test_scalar, can expand variables here - $(sys.host)"
          comment => "Grant access to the string in quotes, by name test_scalar",
           handle => "test_scalar",
    resource_type => "literal",
        admit_ips => { "127.0.0.1" };

  "XYZ"
          comment => "Grant access to contents of persistent scalar variable XYZ",
    resource_type => "variable",
        admit_ips => { "127.0.0.1" };

  # Client grants access to CFEngine hub access

  "delta"
               comment => "Grant access to cfengine hub to collect report deltas",
         resource_type => "query",
    report_data_select => default_data_select_host,
                 admit_ips => { "127.0.0.1"  };
  "full"
               comment => "Grant access to cfengine hub to collect full report dump",
         resource_type => "query",
    report_data_select => default_data_select_host,
             admit_ips => { "127.0.0.1"  };

  policy_server::

  "collect_calls"
          comment => "Grant access to cfengine client to request the collection of its reports",
    resource_type => "query",
        admit_ips => { "10.1.2.0/24" };


}

```

Using the built-in `report_data_select` body `default_data_select_host`:

[%CFEngine_include_snippet(controls/reports.cf, .+default_data_select_host, \})%]


The access promise allows overlapping promises to be made, and these are kept on a
first-come-first-served basis. Thus file objects (promisers) should be
listed in order of most-specific file first. In this way, specific
promises will override less specific ones.

****

## Attributes ##


### admit_hostnames

**Description:** A list of hostnames or domains that should have access to the object.

[%CFEngine_promise_attribute()%]

**Note:** The host trying to access the object is identified using a
reverse DNS lookup on the connecting IP. This introduces latency for
*every* incoming connection. If possible, avoid this penalty by
leaving `admit_hostnames` empty and only specifying numeric addresses
and subnets in `admit_ips`.

To admit an entire domain, start the string with a dot `.`.  This
includes every hostname ending with the domain, but not a machine
named after the domain itself.

For example, here we'll admit the entire domain `.cfengine.com` and
the host `www.cfengine3.com`.  A machine named `cfengine.com` would be
refused access because it's not in the `cfengine.com` domain.

```cf3
access:

   "/path/file"
   admit_hostnames => { ".cfengine.com", "www.cfengine3.com" };
```

**See also:** `deny_hostnames`, `admit_ips`, `admit_keys`

**History:** Introduced in CFEngine 3.6.0

### admit_ips

**Description:** A list of IP addresses that should have access to the object.

Subnets are specified using CIDR notation.  For example, here we'll
admit one host, then a subnet, then everyone:

```cf3
access:

   "/path/file"
   admit_ips => {"192.168.0.1", "192.168.0.0/24", "0.0.0.0/0"};
```

[%CFEngine_promise_attribute()%]

**See also:** `deny_ips`, `admit_hostnames`, `admit_keys`

**History:** Introduced in CFEngine 3.6.0

### admit_keys

**Description:** A list of RSA keys of hosts that should have access to the object.

For example, here we'll admit the fictitious SHA key `abcdef`:

```cf3
access:

   "/path/file"
   admit_keys => {"SHA=abcdef"};
```

In Community, MD5 keys are used, so similarly we can admit the
fictitious MD5 key `abcdef`:

```cf3
access:

   "/path/file"
   admit_keys => {"MD5=abcdef"};
```

[%CFEngine_promise_attribute()%]

**See also:** `deny_keys`, `admit_hostnames`, `admit_ips`, `copyfrom_restrict_keys`

**History:** Introduced in CFEngine 3.6.0

### deny_hostnames

**Description:** A list of hostnames that should be denied access to the object.

This overrides the grants in `admit_hostnames`, `admit_ips` and `admit_keys`.

To deny an entire domain, start the string with a dot `.`.  This
includes every hostname ending with the domain, but not a machine
named after the domain itself.

For example, here we'll deny the entire domain `.cfengine.com` and the
host `www.cfengine3.com`.  A machine named `cfengine.com` would be
allowed access (unless it's denied by other promises) because it's not
in the `cfengine.com` domain.

```cf3
access:

   "/path/file"
   deny_hostnames => { ".cfengine.com", "www.cfengine3.com" };
```

[%CFEngine_promise_attribute()%]

**Notes:** Failure to resolve a hostname or it's reverse results in a denial.
Since this control is sensitive to temporary DNS failures, and cases, where
reverse DNS is not present, it should be used with extreme scrutiny.

**See also:** `admit_hostnames`, `deny_ips`, `deny_keys`

**History:** Introduced in CFEngine 3.6.0

### deny_ips

**Description:** A list of IP addresses that should be denied access to the object.

Subnets are specified using CIDR notation.

This overrides the grants in `admit_hostnames`, `admit_ips` and `admit_keys`.

For example, here we'll deny one host, then a subnet, then everyone:

```cf3
access:

   "/path/file"
   deny_ips => {"192.168.0.1", "192.168.0.0/24", "0.0.0.0/0"};
```

[%CFEngine_promise_attribute()%]

**See also:** `admit_ips`, `deny_hostnames`, `deny_keys`

**History:** Introduced in CFEngine 3.6.0

### deny_keys

**Description:** A list of RSA keys of hosts that should be denied access to the object.

This overrides the grants in `admit_hostnames`, `admit_ips` and `admit_keys`.

[%CFEngine_promise_attribute()%]

For example, here we'll deny the fictitious SHA key `abcdef`:

```cf3
access:

   "/path/file"
   deny_keys => {"SHA=abcdef"};
```

In Community, MD5 keys are used, so similarly we can deny the
fictitious MD5 key `abcdef`:

```cf3
access:

   "/path/file"
   deny_keys => {"MD5=abcdef"};
```

**See also:** `admit_keys`, `deny_hostnames`, `deny_ips`

**History:** Introduced in CFEngine 3.6.0

### admit

**Description:** The `admit` slist can contain a mix of entries in the
syntax of `admit_ips`, `admit_hostnames` and `admit_keys`, and offers
the same functionality. It's a legacy attribute that was split in the
aforementioned attributes, and it's **not recommended** to use in new
policy.

### deny

**Description:** The `deny` slist can contain a mix of entries in the
syntax of `deny_ips`, `deny_hostnames` and `deny_keys`, and offers the
same functionality. It's a legacy attribute that was split in the
aforementioned attributes, and it's **not recommended** to use in new
policy. Example:

```cf3
bundle server my_access_rules()
{
access:

  "/directory/"

    admit   => { "127.0.0.1", ".example.org" },
    deny    => { "badhost_1.example.org", "badhost_1.example.org" };
}
```

The best way to write the same policy would be the following:

```cf3
bundle server my_access_rules()
{
access:

  "/directory/"

    admit_ips       => { "127.0.0.1" },
    admit_hostnames => { ".example.org" },
    deny_hostnames  => { "badhost_1.example.org", "badhost_1.example.org" };
}
```


**Notes:**
Only regular expressions or exact matches are allowed in this list,
as non-specific matches are too greedy for denial.

`deny` will be deprecated in CFEngine 3.7 in favor of `deny_ips`,
`deny_hostnames`, and `deny_keys`.

### maproot

**Description:** The `maproot` slist contains host names or IP addresses
to grant full read-privilege on the server.

Normally users authenticated by the server are granted access only to
files owned by them and no-one else. Even if the `cf-serverd` process
runs with root privileges on the server side of a client-server
connection, the client is not automatically granted access to download
files owned by non-privileged users. If `maproot` is true then remote
`root` users are granted access to all files.

A typical case where mapping is important is in making backups of many
user files.

[%CFEngine_promise_attribute()%]

**Example:**

```cf3
access:

 "/home"

     admit_hostnames => { "backup_host.example.org" },
 ifencrypted => "true",

     # Backup needs to have access to all users

     maproot => { "backup_host.example.org" };
```

**Notes:**

On Windows, `cf-serverd`, `maproot` is required to read files if the
connecting user does not own the file on the server.

### ifencrypted

**Description:** The `ifencrypted` menu option determines whether the
current file access promise is conditional on the connection from the
client being encrypted.

This option has no effect with the TLS CFEngine protocol, where
encryption is always enabled.

If this flag is true a client cannot access the file object unless its
connection is encrypted.

[%CFEngine_promise_attribute(false)%]

**Example:**

```cf3
access:

   "/path/file"

    admit_hostnames => { ".example.org" },
    ifencrypted => "true";
```

**Note:** This attribute is a noop when used with
[`protocol_version`][Components#protocol_version] 2 or
greater.

**See also:** [`protocol_version`][Components#protocol_version], [`allowtlsversion`][cf-serverd#allowtlsversion], [`allowciphers`][cf-serverd#allowciphers], [`tls_min_version`][Components#tls_min_version], [`tls_ciphers`][Components#tls_ciphers], [`encrypt`][files#encrypt], [`logencryptedtransfers`][cf-serverd#logencryptedtransfers], [`ifencrypted`][access#ifencrypted]

### report_data_select

**This body is only available in CFEngine Enterprise.**

**Description:** The `report_data_select` body restricts which data is included
for [query][access#resource_type] resources, and allows filtering of data reported to the
CFEngine Enterprise server.

Use this body template to control the content of reports collected by the
CFEngine Enterprise server, and to strip unwanted data (e.g. temporary variables)
from reporting.

By default, no filtering is applied. If include and exclude rules are combined, then the
exclude statement is applied to the subset from the include statement.

If more than one `report_data_select` body applies to the same host, all of them are applied.

Usage of this body is only allowed in conjunction with using
[`resource_type => "query"`][access#resource_type], as this is the resource type that is being affected.

[%CFEngine_promise_attribute()%]

**Example:**

```cf3
body report_data_select report_data
{
    metatags_include => { "inventory", "compliance" };
    promise_handle_exclude => { "_.*" };
    monitoring_exclude => { "mem_.*swap" };
}
```

**Example:**

Here are the built-in `report_data_select` bodies `default_data_select_host()` and
`default_data_select_policy_hub()`:

[%CFEngine_include_snippet(controls/reports.cf, .+default_data_select_host, \})%]

[%CFEngine_include_snippet(controls/reports.cf, .+default_data_select_policy_hub, \})%]

**See also:** [Common Body Attributes][Promise Types#Common Body Attributes]

**History:**

* Introduced in Enterprise 3.5.0

* `metatags_exclude`, `metatags_include`, `promise_handle_exclude`, and
  `promise_handle_include` body attributes added in 3.6.0.

* `classes_exclude`, `classes_include`, `promise_notkept_log_exclude`,
  `promise_notkept_log_include`, `promise_repaired_log_exclude`,
  `promise_repaired_log_include`, `variables_exclude`, and `variables_include`
  body attributes removed in 3.6.0

#### metatags_exclude

**Description:** List of [anchored][anchored] regular expressions matching
metatags of classes or vars to exclude from reporting.

Classes and variables with metatags matching any entry of that list will not be
reported to the CFEngine Enterprise server.

When combined with `metatags_include`, this list is applied to the selected
subset.

[%CFEngine_promise_attribute()%]

**See also:** `metatags_include`, `promise_handle_exclude`, `monitoring_exclude`

**History:** Introduced in CFEngine 3.6.0

#### metatags_include

**Description:** List of [anchored][anchored] regular expressions matching
metatags of classes or vars to include in reporting.

Classes and variables with metatags matching any entry of that list will be
reported to the CFENgine Enterprise server.

When combined with `metatags_exclude`, the exclude list is applied to the subset
from this list.

[%CFEngine_promise_attribute()%]

**See also:** `metatags_exclude`, `promise_handle_include`, `monitoring_include`

**History:** Introduced in CFEngine 3.6.0

#### promise_handle_exclude

**Description:** List of [anchored][anchored] regular expressions matching
promise handles to exclude from reporting.

Information about promises with handles that match any entry in that list will
not be reported to the CFEngine Enterprise server.

When combined with `promise_handle_include`, this list is applied to the
selected subset.

[%CFEngine_promise_attribute()%]

**See also:** `promise_handle_include`, `metatags_exclude`, `monitoring_exclude`

**History:** Introduced in CFEngine 3.6.0

#### promise_handle_include

**Description:** List of [anchored][anchored] regular expressions matching
promise handles to include in reporting.

Information about promises with handles that match any entry in that list will
be reported to the CFEngine Enterprise server.

When combined with `promise_handle_exclude`, the exclude list is applied to the
subset from this list.

[%CFEngine_promise_attribute()%]

**See also:** `promise_handle_exclude`, `metatags_include`, `monitoring_include`

**History:** Introduced in CFEngine 3.6.0

#### monitoring_include

**Description:** List of [anchored][anchored] regular expressions matching
monitoring objects to include in reporting.

Monitoring objects with names matching any entry in that list will be reported
to the CFEngine Enterprise server.

When combined with `monitoring_exclude`, the exclude list is applied to the
subset from this list.

[%CFEngine_promise_attribute()%]

**See also:** `monitoring_exclude`, `promise_handle_include`, `metatags_include`

**History:** Introduced in Enterprise 3.5.0

#### monitoring_exclude

**Description:** List of [anchored][anchored] regular expressions matching monitoring objects
to exclude from reporting.

Monitoring objects with names matching any entry in that list will not be
reported to the CFEngine Enterprise server.

When combined with `monitoring_include`, this list is applied to the selected
subset.

[%CFEngine_promise_attribute()%]

**See also:** `monitoring_include`, `promise_handle_exclude`, `metatags_exclude`

**History:** Introduced in Enterprise 3.5.0

### resource_type

**Description:** The `resource_type` is the type of object being granted
access.

By default, access to resources granted by the server are files
(`resource_type => "path"`).
However, sometimes it is useful to cache `literal` strings, hints and
data on the server for easy access (e.g. the contents of variables or
hashed passwords). In the case of literal data, the promise handle
serves as the reference identifier for queries. Queries are instigated
by function calls by any agent.

[%CFEngine_promise_attribute()%]

If the resource type is `literal`, CFEngine will grant access to a
literal data string. This string is defined either by the promiser
itself, but the name of the variable is the identifier given by the
promise handle of the access promise, since the promiser string might be
complex.

If the resource type is `variable` then the promiser is the name of a
persistent scalar variable defined on the server-host. Currently
persistent scalars are only used internally by Enterprise CFEngine to
hold enumerated classes for orchestration purposes.

If you want to send the value of a policy defined variable in the server
host (which for some reason is not available directly through policy on
the client, e.g. because they have different policies), then you could
use the following construction:

```cf3
access:

  "$(variable_name)"

         handle => "variable_name",
  resource_type => "literal";
```

If the resource type is `context`, the promiser is treated as a regular
expression to match persistent classes defined on the server host. If
these are matched by the request from the client, they will be
transmitted (See `remoteclassesmatching()`).

The term `query` may also be used in CFEngine Enterprise to query the server
for data from embedded databases. This is currently for internal use only, and
is used to grant access to report 'menus'. If the promiser of a query request
is called `collect_calls`, this grants access to server peering collect-call
tunneling (see also `call_collect_interval`).

If the resource type is `bundle` then the specific bundles are allowed
to be remotely executed with `cf-runagent --remote-bundles` from the
specified hosts. The promiser is an anchored regular expression.


**Example:**

```cf3
bundle server my_access_rules()
{
access:

  "value of my test_scalar, can expand variables here - $(sys.host)"
    handle => "test_scalar",
    comment => "Grant access to contents of test_scalar VAR",
    resource_type => "literal",
    admit_ips => { "127.0.0.1" };

  "XYZ"
    resource_type => "variable",
    handle => "XYZ",
    admit_ips => { "$(sys.policy_hub)" };

 "delta"
    comment => "Grant access to cfengine hub to collect report deltas",
    resource_type => "query",
    admit_ips   => { "$(sys.policy_hub)"  };

 "full"
          comment => "Grant access to cfengine hub to collect full report dump",
    resource_type => "query",
        admit_ips => { "$(sys.policy_hub)"  };

 "magic_bundle"
          comment => "Grant access to the hub to activate magic_bundle with cf-runagent",
    resource_type => "bundle",
        admit_ips => { "$(sys.policy_hub)" };

 am_policy_hub::

  "collect_calls"
     comment       => "Enable call-collect report collection for the specific client",
     resource_type => "query",
     admit_ips     => { "1.2.3.4" };
}
```

**See also:** [--remote-bundles option for cf-runagent][cf-runagent], [cfruncommand in body server control][cf-serverd#cfruncommand]

**History:**

- ```bundle``` `resource_type` added in 3.9.0

### shortcut

**Description:** For file promisers, the server will give access to the file under
its shortcut name.

[%CFEngine_promise_attribute()%]

**Example:**

```cf3
  "/var/cfengine/cmdb/$(connection.key).json"
    shortcut   => "me.json",
    admit_keys => { "$(connection.key)" };
```

In this example, requesting the file `me.json` will transfer the file stored on the
server under the name `/var/cfengine/cmdb/SHA=....json` to the requesting host,
where it will be received as `me.json`.

**History:** Introduced in CFEngine 3.6.0
