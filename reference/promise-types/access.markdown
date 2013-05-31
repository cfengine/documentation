---
layout: default
title: access
categories: [Reference, Promise Types, access]
published: true
alias: reference-promise-types-access.html
tags: [reference, bundles, server, cf-serverd, access, server, promise types, acl, trust, encryption]
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

  

Example:

```cf3
#########################################################
# Server config
#########################################################

body server control 

{
allowconnects         => { "127.0.0.1" , "::1" };
allowallconnects      => { "127.0.0.1" , "::1" };
trustkeysfrom         => { "127.0.0.1" , "::1" };
}

#########################################################

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

  "collect call"
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

-   [admit in access](#admit-in-access)
-   [deny in access](#deny-in-access)
-   [maproot in access](#maproot-in-access)
-   [ifencrypted in access](#ifencrypted-in-access)
-   [resource\_type in access](#resource_005ftype-in-access)
-   [report\_data\_select in access](#report_data_select-in-access)

#### `admit`

**Type**: `slist`

**Allowed input range**: (arbitrary string)

**Synopsis**: List of host names or IP addresses to grant access to file
objects

**Example**:  
   

```cf3
access:

  "/home/mark/LapTop"

    admit   => { "127.0.0.1", "192.168.0.1/24", ".*\.domain\.tld"  };
```

**Notes**:  
   

Admit promises grant access to file objects on the server. Arguments may
be IP addresses or hostnames, provided DNS name resolution is active. In
order to reach this stage, a client must first have passed all of the
standard connection tests in the control body.

The lists may contain network addresses in CIDR notation or regular
expressions to match the IP address or name of the connecting host.

#### `deny`

**Type**: `slist`

**Allowed input range**: (arbitrary string)

**Synopsis**: List of host names or IP addresses to deny access to file
objects

**Example**:  
   

```cf3
bundle server access_rules()

{
access:

  "/path"

    admit   => { ".*\.example\.org" },
    deny    => { "badhost_1\.example\.org", "badhost_1\.example\.org" };
}
```

**Notes**:  
   

Denial is for special exceptions. A better strategy is always to grant
on a need to know basis. A security policy based on exceptions is a weak
one.

Note that only regular expressions or exact matches are allowed in this
list, as non-specific matches are too greedy for denial.

#### `maproot`

**Type**: `slist`

**Allowed input range**: (arbitrary string)

**Synopsis**: List of host names or IP addresses to grant full
read-privilege on the server

**Example**:  
   

```cf3
access:

 "/home"

       admit => { "backup_host.example.org" },
 ifencrypted => "true",

     # Backup needs to have access to all users

     maproot => { "backup_host.example.org" };
```

**Notes**:  
   

Normally users authenticated by the server are granted access only to
files owned by them and no-one else. Even if the `cf-serverd` process
runs with root privileges on the server side of a client-server
connection, the client is not automatically granted access to download
files owned by non-privileged users. If `maproot` is true then remote
`root` users are granted access to all files.

A typical case where mapping is important is in making backups of many
user files. On Windows, `cf-serverd`, `maproot` is required to read
files if the connecting user does not own the file on the server.

#### `ifencrypted`

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

**Default value:** false

**Synopsis**: true/false whether the current file access promise is
conditional on the connection from the client being encrypted

**Example**:  
   

```cf3
access:

   "/path/file"

    admit     => { ".*\.example\.org" },
    ifencrypted => "true";
```

**Notes**:  
   

If this flag is true a client cannot access the file object unless its
connection is encrypted.

#### `resource_type`

**Type**: (menu option)

**Allowed input range**:   

```cf3
               path
               literal
               context
               query
               variable
```

**Synopsis**: The type of object being granted access (the default
grants access to files)

**Example**:  
   

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

**Notes**:  
   

By default, access to resources granted by the server are files.
However, sometimes it is useful to cache `literal` strings, hints and
data on the server for easy access (e.g. the contents of variables or
hashed passwords). In the case of literal data, the promise handle
serves as the reference identifier for queries. Queries are instigated
by function calls by any agent.

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
transmitted (See [Function
remoteclassesmatching](#Function-remoteclassesmatching)).

The term `query` may also be used in CFEngine Enterprise to query the server 
for data from embedded databases. This is currently for internal use only, and 
is used to grant access to report 'menus'. If the promiser of a query request 
is called `collect_calls`, this grants access to server peering collect-call 
tunneling.


#### `report_data_select` (body template)

**This body is only available in CFEngine Enterprise.**

**Type**: body

**Synopsis**: Restricts access to data for specified query type reported to 
the CFEngine Enterprise Database.

**Example**:


```cf3

body report_data_select
{
    variables_include => { "sys..*" };
    monitoring_exclude => { ".*" };
}
```

**Notes**:


This body template allow user to control content of reports collected by the 
Enterprise Database Server.
It can be used to differentiate content of delta and full reports as also 
allow user
to strip unwanted data e.g. temporary variables from reporting.
Report content can be differentiated between hosts which is controlled
by class expression on access promiser.

If more than one select statement apply to same host, all of them are applied.
Usage of this body in only allowed in conjunction with using
resource_type => "query" as this is the resource type that is being affected.

History: Introduced in Enterprise 3.5.0


`classes_include`

**Type**: `slist`

**Allowed input range**: (arbitrary string)

**Synopsis**: Scope down class report content to contain only classes matching
specified regular expression list.

**Example**:


```cf3

body report_data_select
{
    classes_include => { "report_only_my_classes_.*" };
}
```

**Notes**:


This attribute is used to filter content of class report collected by Enterprise Hub.
Classes matching specified regular expression list will only be send back in the report.
If attribute is not used, report content is not reduced.

History: Introduced in Enterprise 3.5.0


`classes_exclude`

**Type**: `slist`

**Allowed input range**: (arbitrary string)

**Synopsis**: Scope down class report content to exclude classes matching
specified regular expression list.

**Example**:


```cf3

body report_data_select
{
    classes_exclude => { "my_tmp_class.*" };
}
```

**Notes**:


This attribute is used to filter content of class report collected by Enterprise Hub.
Classes matching specified regular expression list will be excluded from report.
If attribute is used in conjunction with classes_include it will exclude entries from
subset selected by include expression.

History: Introduced in Enterprise 3.5.0


`variables_include`

**Type**: `slist`

**Allowed input range**: (arbitrary string)

**Synopsis**: Scope down variable report content to contain only variables matching
specified regular expression list.

**Example**:


```cf3

body report_data_select
{
    variables_include => { "my_bundle.my_variable_prefix_.*" };
}
```

**Notes**:


This attribute is used to filter content of variables report collected by Enterprise Hub.
Variables matching specified regular expression list will only be send back in the report.
Regular expression if matched agents variable name including scope: 

    <scope>.<variable_name>

If attribute is not used, report content is not reduced.

History: Introduced in Enterprise 3.5.0


`variables_exclude`

**Type**: `slist`

**Allowed input range**: (arbitrary string)

**Synopsis**: Scope down variable report content to exclude variables matching
specified regular expression list.

**Example**:


```cf3

body report_data_select
{
    variables_exclude => { "my_bundle.tmp_var_test.*" };
}
```

**Notes**:


This attribute is used to filter content of variable report collected by Enterprise Hub.
Variables matching specified regular expression list will be excluded from report.
Regular expression if matched agents variable name including scope: <scope>.<variable_name>
If attribute is used in conjunction with variables_include it will exclude entries from
subset selected by include expression.

History: Introduced in Enterprise 3.5.0


`promise_notkept_log_include`

**Type**: `slist`

**Allowed input range**: (arbitrary string)

**Synopsis**: Scope down promise not kept log report content to contain only promise
handles matching specified regular expression list.

**Example**:


```cf3

body report_data_select
{
    promise_notkept_log_include => { "my_none_important_promises_.*" };
}
```

**Notes**:


This attribute is used to filter content of not kept log report collected by Enterprise Hub.
Handles matching specified regular expression list will only be send back in the report.
If attribute is not used, report content is not reduced.

History: Introduced in Enterprise 3.5.0


`promise_notkept_log_exclude`

**Type**: `slist`

**Allowed input range**: (arbitrary string)

**Synopsis**: Scope down promise not kept log report content to exclude promise handles matching
specified regular expression list.

**Example**:


```cf3

body report_data_select
{
    promise_notkept_log_exclude => { "my_tmp_promise_handle.*" };
}
```

**Notes**:  


This attribute is used to filter content of not kept log report collected by Enterprise Hub.
Handles matching specified regular expression list will be excluded from report.
If attribute is used in conjunction with promise_notkept_log_include it will exclude entries from
subset selected by include expression.

History: Introduced in Enterprise 3.5.0


`promise_repaired_log_include`

**Type**: `slist`

**Allowed input range**: (arbitrary string)

**Synopsis**: Scope down promise repaired log report content to contain only promise
handles matching specified regular expression list.

**Example**:


```cf3

body report_data_select
{
    promise_repaired_log_include => { "my_none_important_promises_.*" };
}
```

**Notes**:


This attribute is used to filter content of repaired log report collected by Enterprise Hub.
Handles matching specified regular expression list will only be send back in the report.
If attribute is not used, report content is not reduced.

History: Introduced in Enterprise 3.5.0


`promise_repaired_log_exclude`

**Type**: `slist`

**Allowed input range**: (arbitrary string)

**Synopsis**: Scope down promise repaired log report content to exclude promise handles matching
specified regular expression list.

**Example**:


```cf3

body report_data_select
{
    promise_repaired_log_exclude => { "my_tmp_promise_handle.*" };
}
```

**Notes**:


This attribute is used to filter content of repaired log report collected by Enterprise Hub.
Handles matching specified regular expression list will be excluded from report.
If attribute is used in conjunction with promise_repaired_log_include it will exclude entries from
subset selected by include expression.

History: Introduced in Enterprise 3.5.0


`monitoring_include`

**Type**: `slist`

**Allowed input range**: (arbitrary string)

**Synopsis**: Scope down monitoring report content to contain only observed objects 
matching specified regular expression list.

**Example**:


```cf3

body report_data_select
{
    monitoring_include => { "mem_.*" };
}
```

**Notes**:


This attribute is used to filter content of monitoring report collected by Enterprise Hub.
Object names matching specified regular expression list will only be send back in the report.
If attribute is not used, report content is not reduced.

History: Introduced in Enterprise 3.5.0


`monitoring_exclude`

**Type**: `slist`

**Allowed input range**: (arbitrary string)

**Synopsis**: Scope down monitoring content to exclude observed objects matching
specified regular expression list.

**Example**:


```cf3

body report_data_select
{
    monitoring_exclude => { "mem_swap", "mem_freeswap" };
}
```

**Notes**:


This attribute is used to filter content of monitoring report collected by Enterprise Hub.
Object names matching specified regular expression list will be excluded from report.
If attribute is used in conjunction with monitoring_include it will exclude entries from
subset selected by include expression.

History: Introduced in Enterprise 3.5.0
