---
layout: default
title: access
categories: [Reference, Promise Types, access]
published: true
alias: reference-promise-types-access.html
tags: [reference, bundle server, cf-serverd, access, server, promise types, acl, trust, encryption]
---

Access promises are conditional promises made by the server about file
objects. The promise has two consequences. For file copy requests, the
file becomes transferable to the remote client according to the
conditions specified in the server promise; in other words, if the
connection encryption requirements are met, and if the client has been
granted appropriate privileges with `maproot` (like its NFS counterpart)
to be able to see file objects not owned by the server process owner.

The promise has two mutally exclusive attributes admit and deny. Use of
admit is preferred as mistakes and omissions can easily be made when
excluding from a group.

When access is granted to a directory, the promise is automatically
given about all of its contents and sub-directories. The access promise
allows overlapping promises to be made, and these are kept on a
first-come-first-served basis. Thus file objects (promisers) should be
listed in order of most-specific file first. In this way, specific
promises will override less specific ones.

```cf3
      access:
     
         "/path/file_object"
     
           admit   = { "hostname", "ipv4_address", "ipv6_address"  };
     
```

  

**Example:**

```cf3
body server control 
{
allowconnects         => { "127.0.0.1" , "::1" };
allowallconnects      => { "127.0.0.1" , "::1" };
trustkeysfrom         => { "127.0.0.1" , "::1" };
}

bundle server access_rules()
{
access:

  "/source/directory"
          comment => "Access to file transfer",
          admit   => { "127.0.0.1" };

  # Grant orchestration communication

  "did.*"
          comment => "Access to class context (enterprise)",
    resource_type => "context",
            admit => { "127.0.0.1" };


  "value of my test_scalar, can expand variables here - $(sys.host)"
          comment => "Grant access to the string in quotes, by name test_scalar",
           handle => "test_scalar",
    resource_type => "literal",
            admit => { "127.0.0.1" };

  "XYZ"
          comment => "Grant access to contents of persistent scalar variable XYZ",
    resource_type => "variable",
            admit => { "127.0.0.1" };

  # Client grants access to CFEngine hub access

  "delta"
               comment => "Grant access to cfengine hub to collect report deltas",
         resource_type => "query",
    report_data_select => report_filter,
                 admit => { "127.0.0.1"  };
  "full"
               comment => "Grant access to cfengine hub to collect full report dump",
         resource_type => "query",
    report_data_select => report_filter,
                 admit => { "127.0.0.1"  };

  policy_hub::

  "collect_calls"
          comment => "Grant access to cfengine client to request the collection of its reports",
    resource_type => "query",
            admit => { "10.1.2.*" };


}

body report_data_select report_filter
{
    variables_include => { "sys..*", "mon..*" };
    variables_exclude => { "sys.host" };
}

```

Entries may be literal addresses of IPv4 or IPv6, or any name registered
in the POSIX `gethostbyname` service.

****

## Attributes

### admit

**Description:** The `admit` slist contains host names or IP addresses 
to grant access to file objects.

Admit promises grant access to file objects on the server. Arguments may
be IP addresses or hostnames, provided DNS name resolution is active. In
order to reach this stage, a client must first have passed all of the
standard connection tests in the control body.

The lists may contain network addresses in CIDR notation or regular
expressions to match the IP address or name of the connecting host.

[%CFEngine_promise_attribute()%]

**Example:**

```cf3
access:

  "/home/mark/LapTop"

    admit   => { "127.0.0.1", "192.168.0.1/24", ".*\.domain\.tld"  };
```

### deny

**Description:** The `deny` slist contains host names or IP addresses 
to deny access to file objects.

Denial is for special exceptions. A better strategy is always to grant
on a need to know basis. A security policy based on exceptions is a weak
one.

[%CFEngine_promise_attribute()%]

**Example:**

```cf3
bundle server access_rules()
{
access:

  "/path"

    admit   => { ".*\.example\.org" },
    deny    => { "badhost_1\.example\.org", "badhost_1\.example\.org" };
}
```

**Notes:**
Only regular expressions or exact matches are allowed in this list, 
as non-specific matches are too greedy for denial.

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

       admit => { "backup_host.example.org" },
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

If this flag is true a client cannot access the file object unless its
connection is encrypted.

[%CFEngine_promise_attribute(false)%]

**Example:**

```cf3
access:

   "/path/file"

    admit     => { ".*\.example\.org" },
    ifencrypted => "true";
```


### resource_type

**Description:** The `resource_type` is the type of object being granted 
access.

By default, access to resources granted by the server are files.
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
tunneling.

**Example:**

```cf3
bundle server access_rules()
{
access:

  "value of my test_scalar, can expand variables here - $(sys.host)"
    handle => "test_scalar",
    comment => "Grant access to contents of test_scalar VAR",
    resource_type => "literal",
    admit => { "127.0.0.1" };

  "XYZ"
    resource_type => "variable",
    handle => "XYZ",
    admit => { "127.0.0.1" };


  # On the policy hub

  "collect_calls"
     resource_type => "query",
           admit   => { "127.0.0.1" };

  # On the isolated client in the field


 "delta"
    comment => "Grant access to cfengine hub to collect report deltas",
    resource_type => "query",
          admit   => { "127.0.0.1"  };
  "full"
          comment => "Grant access to cfengine hub to collect full report dump",
    resource_type => "query",
          admit   => { "127.0.0.1"  };
}
```

### report_data_select

**This body is only available in CFEngine Enterprise.**

**Description:** The `report_data_select` body restricts access to data 
for the specified query types reported to the CFEngine Enterprise Database.

This body template allows users to control the content of reports collected 
by the Enterprise Database Server, and allows users to strip unwanted data 
(e.g. temporary variables from reporting).

Report content can be differentiated between hosts that are controlled
by the class expression on access promiser.

If more than one select statement applies to the same host, all of them are applied.

Usage of this body is only allowed in conjunction with using 
`resource_type => "query"`, as this is the resource type that is being affected.

[%CFEngine_promise_attribute()%]

**Example:**

```cf3

body report_data_select
{
    variables_include => { "sys..*" };
    monitoring_exclude => { ".*" };
}
```

**History:** Introduced in Enterprise 3.5.0

#### classes_include

**Description:** The `classes_include` attribute is used to filter content 
of the class report collected by Enterprise Hub, to include classes matching 
specified regular expressions on the list.

Only classes matching the specified regular expressions on the list will 
be sent back in the report. 

If this attribute is not used, the report content is not reduced.

[%CFEngine_promise_attribute()%]

**Example:**

```cf3

body report_data_select
{
    classes_include => { "report_only_my_classes_.*" };
}
```

**History:** Introduced in Enterprise 3.5.0

#### classes_exclude

**Description:** The `classes_exclude` attribute is used to filter content 
of the class report collected by Enterprise Hub, to exclude classes matching 
specified regular expressions on the list.

If this attribute is used in conjunction with `classes_include` it will 
exclude entries from the subset selected by the include expression.

[%CFEngine_promise_attribute()%]

**Example:**

```cf3

body report_data_select
{
    classes_exclude => { "my_tmp_class.*" };
}
```

**Notes:**

**History:** Introduced in Enterprise 3.5.0

#### variables_include

**Description:** The `variables_include` attribute is used to filter 
content of the variables report collected by Enterprise Hub, to contain 
only variables matching specified regular expressions on the list.

If the attribute is not used, the report content is not reduced.

[%CFEngine_promise_attribute()%]

Regular expressions for this attribute use the form `<scope>.<variable_name>`.

**Example:**

```cf3

body report_data_select
{
    variables_include => { "my_bundle.my_variable_prefix_.*" };
}
```

**History:** Introduced in Enterprise 3.5.0


#### variables_exclude

**Description:** The `variables_exclude` attribute is used to filter 
content of the variable report collected by Enterprise Hub, to exclude 
variables matching specified regular expression list.

[%CFEngine_promise_attribute()%]

Regular expressions for this attribute use the form `<scope>.<variable_name>`.
  
**Example:**

```cf3

body report_data_select
{
    variables_exclude => { "my_bundle.tmp_var_test.*" };
}
```

**Notes:**
If this attribute is used in conjunction with `variables_include`, it will 
exclude entries from the subset selected by the include expression.

**History:** Introduced in Enterprise 3.5.0

#### promise_notkept_log_include

**Description:** The `promise_notkept_log_include` attribute is used to 
filter content of the not kept log report collected by Enterprise Hub, 
to contain promise handles matching specified regular expressions on 
the list.

Only those handles matching the regular expressions on the list will 
be sent back in the report.

If the attribute is not used, the report content will not be reduced.

[%CFEngine_promise_attribute()%]

**Example:**

```cf3

body report_data_select
{
    promise_notkept_log_include => { "my_none_important_promises_.*" };
}
```

**History:** Introduced in Enterprise 3.5.0

#### promise_notkept_log_exclude

**Description:** The `promise_notkept_log_exclude` attribute is used to 
filter content of the not kept log report collected by Enterprise Hub, 
to exclude promise handles matching specified regular expressions on the 
list.

Only those handles matching regular expression on the list will be excluded 
from the report.

[%CFEngine_promise_attribute()%]

**Example:**

```cf3

body report_data_select
{
    promise_notkept_log_exclude => { "my_tmp_promise_handle.*" };
}
```

**Notes:** If this attribute is used in conjunction with the 
`promise_notkept_log_include` attribute, it will exclude entries 
from the subset selected by the include expression.

**History:** Introduced in Enterprise 3.5.0

#### promise_repaired_log_include

**Description:** The `promise_repaired_log_include` attribute is used to 
filter content of the repaired log report collected by Enterprise Hub, 
to include regular expressions matched on the list.

Only those handles matching the regular expression on the list will be 
sent back in the report. If attribute is not used, the report content 
will not be filtered.

[%CFEngine_promise_attribute()%]

**Example:**

```cf3

body report_data_select
{
    promise_repaired_log_include => { "my_none_important_promises_.*" };
}
```

**History:** Introduced in Enterprise 3.5.0

#### promise_repaired_log_exclude

**Description:** The `promise_repaired_log_exclude` attribute is used to 
filter content of the repaired log report collected by Enterprise Hub, 
to exclude promise handles matching regular expression on the list.

Only those handles matching regular expression on the list will be excluded 
from the report.

[%CFEngine_promise_attribute()%]

**Example:**

```cf3

body report_data_select
{
    promise_repaired_log_exclude => { "my_tmp_promise_handle.*" };
}
```

**Notes:**
If this attribute is used in conjunction with `promise_repaired_log_include`, 
it will exclude entries from the subset selected by the include expression.

**History:** Introduced in Enterprise 3.5.0


#### monitoring_include

**Description:** The `monitoring_include` attribute is used to filter 
content of the monitoring report collected by Enterprise Hub, to contain 
only observed objects matching regular expressions on the list.

Only object names matching regular expression on the list will be sent 
back in the report. If the attribute is not used, the report content will 
not be filtered.

[%CFEngine_promise_attribute()%]

**Example:**

```cf3

body report_data_select
{
    monitoring_include => { "mem_.*" };
}
```

**History:** Introduced in Enterprise 3.5.0

#### monitoring_exclude

**Description:** The `monitoring_exclude` attribute is used to filter 
content of the monitoring report collected by Enterprise Hub, to exclude 
observed objects matching specified regular expressions on the list.

Only object names matching regular expression list will be excluded from 
the report.

[%CFEngine_promise_attribute()%]

**Example:**

```cf3

body report_data_select
{
    monitoring_exclude => { "mem_swap", "mem_freeswap" };
}
```

**Notes:**

If this attribute is used in conjunction with `monitoring_include` it will 
exclude entries from the subset selected by the include expression.

**History:** Introduced in Enterprise 3.5.0
