---
layout: default
title: databases-in-agent-promises
categories: [Bundles-for-agent,databases-in-agent-promises]
published: true
alias: Bundles-for-agent-databases-in-agent-promises.html
tags: [Bundles-for-agent,databases-in-agent-promises]
---

### `databases` promises in agent

\

CFEngine Nova can interact with commonly used database servers to keep
promises about the structure and content of data within them.

There are two main cases of database management to address: small
embedded databases and large centralized databases.

Databases are often centralized entities that have a single point of
management. While large monolithic database can be more easily managed
with other tools, CFEngine can still monitor changes and discrepancies.
In addition, CFEngine can also manage smaller embedded databases that
are distributed in nature, whether they are SQL, registry or future
types.

For example, creating 100 new databases for test purposes is a task for
CFEngine; but adding a new item to an important production database is
not a recomended task for CFEngine.

There are three kinds of database supported by Nova:

*LDAP - The Lightweight Directory Access Protocol*

A hierarchical network database primarily for reading simple schema. \

*SQL - Structured Query Language*

A number of relational databases (currently supported: MySQL, Postgres)
for reading and writing complex data. \

*Registry - Microsoft Registry*

An embedded database for interfacing with system values in Microsoft
Windows (Only CFEngine Nova)

In addition, CFEngine uses a variety of embedded databases for its own
internals.

Embedded databases are directly part of the system and promises can be
made directly. However, databases running through a server process
(either on the same host or on a different host) are independent agents
and CFEngine cannot make promises on their behalf, unless they promise
(grant) permission for CFEngine to make the changes. Thus the
pre-requisite for making SQL database promises is to grant a point of
access on the server.

~~~~ {.smallexample}
     
      databases:
     
       "database/subkey or table"
     
         database_operation = "create/delete/drop",
         database_type = "sql/ms_registry",
         database_columns = {
                             "name,type,size",
                             "name,type",
                             },
     
         database_server = body;
     
     
      body database_server name
       {
       db_server_owner = "account name";
       db_server_password = "password";
       db_server_host = "hostname or omit for localhost";
       db_server_type = "mysql/posgres";
       db_server_connection_db = "database we can connect to";
       }
     
~~~~

\

~~~~ {.verbatim}
body common control
{
bundlesequence => { "databases" };
}

bundle agent databases

{
#commands:

#  "/usr/bin/createdb cf_topic_maps",

#        contain => as_user("mysql");

databases:

  "cf_topic_maps/topics"

    database_operation => "create",
    database_type => "sql",
    database_columns => { 
                        "topic_name,varchar,256",
                        "topic_comment,varchar,1024",
                        "topic_id,varchar,256",
                        "topic_type,varchar,256",
                        "topic_extra,varchar,26" 
                        },

    database_server => myserver;



}

################################################

body database_server myserver
{
any::
 db_server_owner => "postgres";
 db_server_password => "";
 db_server_host => "localhost";
 db_server_type => "postgres";
 db_server_connection_db => "postgres";
none::
 db_server_owner => "root";
 db_server_password => "";
 db_server_host => "localhost";
 db_server_type => "mysql";
 db_server_connection_db => "mysql";
}

body contain as_user(x)
{
exec_owner => "$(x)";
}
~~~~

\

The promiser in database promises is a concatenation of the database
name and underlying tables. This presents a simple hierarchical model
that looks like a file-system. This is the normal structure within the
Windows registry for instance. Entity-relation databases do not normally
present tables in this way, but no harm is done in representing them as
a hierarchy of depth 1.

-   [database\_server in databases](#database_005fserver-in-databases)
-   [database\_type in databases](#database_005ftype-in-databases)
-   [database\_operation in
    databases](#database_005foperation-in-databases)
-   [database\_columns in databases](#database_005fcolumns-in-databases)
-   [database\_rows in databases](#database_005frows-in-databases)
-   [registry\_exclude in databases](#registry_005fexclude-in-databases)

#### `database_server` (body template)

**Type**: (ext body)

`db_server_owner`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: User name for database connection

**Example**:\
 \

~~~~ {.verbatim}
     
     db_server_owner => "mark";
     
~~~~

**Notes**:\
 \
 \

`db_server_password`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: Clear text password for database connection

**Example**:\
 \

~~~~ {.verbatim}
     
     db_server_password => "xyz.1234";
     
~~~~

**Notes**:\
 \
 \

`db_server_host`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: Hostname or address for connection to database (blank
means localhost)

**Example**:\
 \

~~~~ {.verbatim}
     
     db_server_host => "sqlserv.example.org";
     
~~~~

**Notes**:\
 \

Hostname or IP address of the server. \

`db_server_type`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    postgres
                    mysql
~~~~

**Synopsis**: The dialect of the database server

**Default value:** none

**Example**:\
 \

~~~~ {.verbatim}
     
     db_server_type => "postgres";
     
~~~~

**Notes**:\
 \
 \

`db_server_connection_db`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: The name of an existing database to connect to in order to
create/manage other databases

**Example**:\
 \

~~~~ {.verbatim}
     
     body database_server myserver(x)
     {
     db_server_owner => "$(x)";
     db_server_password => "";
     db_server_host => "localhost";
     db_server_type => "$(mysql)";
     db_server_connection_db => "$(x)";
     }
     
~~~~

where x is currently `mysql` or `postgres`.

**Notes**:\
 \

In order to create a database on a database server (all of which
practice voluntary cooperation), one has to be able to connect to the
server, however, without an existing database this is not allowed. Thus,
database servers provide a default database that can be connected to in
order to thereafter create new databases. These are called `postgres`
and `mysql` for their respective database servers.

For the knowledge agent, this setting is made in the control body, for
database verification promises, it is made in the `database_server`
body.

#### `database_type`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
               sql
               ms_registry
~~~~

**Default value:** none

**Synopsis**: The type of database that is to be manipulated

**Example**:\
 \

~~~~ {.verbatim}
database_type => "ms_registry";
~~~~

**Notes**:\
 \

#### `database_operation`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
               create
               delete
               drop
               cache
               verify
               restore
~~~~

**Synopsis**: The nature of the promise - to be or not to be

**Example**:\
 \

~~~~ {.verbatim}
database_operation => "create";
~~~~

**Notes**:\
 \

#### `database_columns`

**Type**: slist

**Allowed input range**: `.*`

**Synopsis**: A list of column definitions to be promised by SQL
databases

**Example**:\
 \

~~~~ {.verbatim}
  "cf_topic_maps/topics"

    database_operation => "create",
    database_type => "sql",
    database_columns => { 
                        "topic_name,varchar,256",
                        "topic_comment,varchar,1024",
                        "topic_id,varchar,256",
                        "topic_type,varchar,256",
                        "topic_extra,varchar,26" 
                        },

    database_server => myserver;
~~~~

**Notes**:\
 \

Columns are a list of tuplets (Name,type,size). Array items are
triplets, and fixed size data elements are doublets.

#### `database_rows`

**Type**: slist

**Allowed input range**: `.*,.*`

**Synopsis**: An ordered list of row values to be promised by SQL
databases

**Example**:\
 \

~~~~ {.verbatim}
bundle agent databases

{
databases:

 windows::

  # Regsitry has (value,data) pairs in "keys" which are directories

  "HKEY_LOCAL_MACHINE\SOFTWARE\CFEngine AS\CFEngine"

    database_operation => "create",
    database_rows => { "value1,REG_SZ,new value 1", "value2,REG_DWORD,12345"} ,
    database_type     => "ms_registry";
}
~~~~

**Notes**:\
 \

This constraint is used only in adding data to database columns. Rows
are considered to be instances of individual columns.

In the case of the system registry on Windows, the rows represent data
on data-value pairs. The currently supported types (the middle field)
for the Windows registry are `REG_SZ` (string), `REG_EXPAND_SZ`
(expandable string) and `REG_DWORD` (double word).

#### `registry_exclude`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: A list of regular expressions to ignore in key/value
verification

**Example**:\
 \

~~~~ {.verbatim}
databases:

 "HKEY_LOCAL_MACHINE\SOFTWARE"

    database_operation => "cache",

    registry_exclude => { ".*Windows.*CurrentVersion.*", 
                          ".*Touchpad.*",
                          ".*Capabilities.FileAssociations.*", 
                          ".*Rfc1766.*" , 
                          ".*Synaptics.SynTP.*", 
                          ".*SupportedDevices.*8086", 
                          ".*Microsoft.*ErrorThresholds" 
                        },

    database_type     => "ms_registry";
~~~~

**Notes**:\
 \

During recursive Windows registry scanning, this option allows us to
ignore keys of values matching a list of regular expressions. Some
values in the registry are ephemeral and some should not be considered.
This provides a convenient way of avoiding names. It is analogous to
`exclude_dirs` for files.
