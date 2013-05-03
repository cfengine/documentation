---
layout: default
title: access-in-server-promises
categories: [Bundles-for-server,access-in-server-promises]
published: true
alias: Bundles-for-server-access-in-server-promises.html
tags: [Bundles-for-server,access-in-server-promises]
---

### `access` promises in server

\

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

~~~~ {.smallexample}
     
      access:
     
         "/path/file_object"
     
           admit   = { "hostname", "ipv4_address", "ipv6_address"  };
     
     
~~~~

\

Example:

~~~~ {.verbatim}
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
          admit   => { "127.0.0.1"  };
  "full"
          comment => "Grant access to cfengine hub to collect full report dump",
    resource_type => "query",
          admit   => { "127.0.0.1"  };

  policy_hub::

  "collect call"
          comment => "Grant access to cfengine client to request the collection of its reports",
    resource_type => "query",
          admit   => { "10.1.2.*" };


}
~~~~

\

Entries may be literal addresses of IPv4 or IPv6, or any name registered
in the POSIX `gethostbyname` service.

-   [admit in access](#admit-in-access)
-   [deny in access](#deny-in-access)
-   [maproot in access](#maproot-in-access)
-   [ifencrypted in access](#ifencrypted-in-access)
-   [resource\_type in access](#resource_005ftype-in-access)

#### `admit`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: List of host names or IP addresses to grant access to file
objects

**Example**:\
 \

~~~~ {.verbatim}
access:

  "/home/mark/LapTop"

    admit   => { "127.0.0.1", "192.168.0.1/24", ".*\.domain\.tld"  };
~~~~

**Notes**:\
 \

Admit promises grant access to file objects on the server. Arguments may
be IP addresses or hostnames, provided DNS name resolution is active. In
order to reach this stage, a client must first have passed all of the
standard connection tests in the control body.

The lists may contain network addresses in CIDR notation or regular
expressions to match the IP address or name of the connecting host.

#### `deny`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: List of host names or IP addresses to deny access to file
objects

**Example**:\
 \

~~~~ {.verbatim}
bundle server access_rules()

{
access:

  "/path"

    admit   => { ".*\.example\.org" },
    deny    => { "badhost_1\.example\.org", "badhost_1\.example\.org" };
}
~~~~

**Notes**:\
 \

Denial is for special exceptions. A better strategy is always to grant
on a need to know basis. A security policy based on exceptions is a weak
one.

Note that only regular expressions or exact matches are allowed in this
list, as non-specific matches are too greedy for denial.

#### `maproot`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: List of host names or IP addresses to grant full
read-privilege on the server

**Example**:\
 \

~~~~ {.verbatim}
access:

 "/home"

       admit => { "backup_host.example.org" },
 ifencrypted => "true",

     # Backup needs to have access to all users

     maproot => { "backup_host.example.org" };
~~~~

**Notes**:\
 \

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

**Allowed input range**: \

~~~~ {.example}
               true
               false
               yes
               no
               on
               off
~~~~

**Default value:** false

**Synopsis**: true/false whether the current file access promise is
conditional on the connection from the client being encrypted

**Example**:\
 \

~~~~ {.verbatim}
access:

   "/path/file"

    admit     => { ".*\.example\.org" },
    ifencrypted => "true";
~~~~

**Notes**:\
 \

If this flag is true a client cannot access the file object unless its
connection is encrypted.

#### `resource_type`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
               path
               literal
               context
               query
               variable
~~~~

**Synopsis**: The type of object being granted access (the default
grants access to files)

**Example**:\
 \

~~~~ {.verbatim}

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
~~~~

**Notes**:\
 \

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

~~~~ {.verbatim}
access:

  "$(variable_name)"

         handle => "variable_name",
  resource_type => "literal";
~~~~

If the resource type is `context`, the promiser is treated as a regular
expression to match persistent classes defined on the server host. If
these are matched by the request from the client, they will be
transmitted (See [Function
remoteclassesmatching](#Function-remoteclassesmatching)).

The term `query` may also be used in commercial versions of CFEngine to
query the server for data from embedded databases. This is currently for
internal use only, and is used to grant access to report \`menus'. If
the promiser of a query request is called collect\_calls, this grants
access to server peering collect-call tunneling (See
[call\_collect\_interval in
server](#call_005fcollect_005finterval-in-server)).
