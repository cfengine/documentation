---
layout: default
title: databases
categories: [Reference, Promise Types, databases]
published: true
alias: reference-promise-types-databases.html
tags: [Reference, Bundles, agent, databases, promises, promise types]
---

CFEngine can interact with commonly used database servers to keep
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
not a recommended task for CFEngine.

There are three kinds of database supported by CFEngine:

*LDAP - The Lightweight Directory Access Protocol*

A hierarchical network database primarily for reading simple schema.   

*SQL - Structured Query Language*

A number of relational databases (currently supported: MySQL, Postgres)
for reading and writing complex data.   

*Registry - Microsoft Registry*

An embedded database for interfacing with system values in Microsoft
Windows (Only CFEngine Enterprise)

In addition, CFEngine uses a variety of embedded databases for its own
internals.

Embedded databases are directly part of the system and promises can be
made directly. However, databases running through a server process
(either on the same host or on a different host) are independent agents
and CFEngine cannot make promises on their behalf, unless they promise
(grant) permission for CFEngine to make the changes. Thus the
pre-requisite for making SQL database promises is to grant a point of
access on the server.

```cf3
     
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
     
```

  

```cf3
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
```

The promiser in database promises is a concatenation of the database
name and underlying tables. This presents a simple hierarchical model
that looks like a file-system. This is the normal structure within the
Windows registry for instance. Entity-relation databases do not normally
present tables in this way, but no harm is done in representing them as
a hierarchy of depth 1.

### database_server

**Type**: `body database_server`

#### db_server_owner

**Type**: `string`

**Allowed input range**: (arbitrary string)

**Description**: The `db_server_owner` string represents the user name 
for a database connection.

**Example**:

```cf3
     
     db_server_owner => "mark";
     
```  
   

#### db_server_password

**Type**: `string`

**Allowed input range**: (arbitrary string)

**Description**: The `db_server_password ` string represents the clear 
text password for a database connection.

**Example**:

```cf3
     
     db_server_password => "xyz.1234";
     
```

#### db_server_host

**Type**: `string`

**Allowed input range**: (arbitrary string)

**Description**: The `db_server_host` string represents the hostname or 
address for a database connection. 

A blank value is equal to localhost.

```cf3
     
     db_server_host => "sqlserv.example.org";
     
```

#### db_server_type

**Type**: (menu option)

**Allowed input range**:   

```cf3
                    postgres
                    mysql
```

**Default value:** none

**Description**: The `db_server_type` string represents the type of 
database server being used.

**Example**:

```cf3
     
     db_server_type => "postgres";
     
```

#### db_server_connection_db

**Type**: `string`

**Allowed input range**: (arbitrary string)

**Description**: The `db_server_connection_db` string is the name of an 
existing database to connect to in order to create/manage other databases.

In order to create a database on a database server (all of which practice 
voluntary cooperation), one has to be able to connect to the server. 
However, without an existing database this is not allowed. Thus, database 
servers provide a default database that can be connected to in order to 
thereafter create new databases. These are called `postgres` and `mysql` 
for their respective database servers.

**Example**:

```cf3
     
     body database_server myserver(x)
     {
     db_server_owner => "$(x)";
     db_server_password => "";
     db_server_host => "localhost";
     db_server_type => "$(mysql)";
     db_server_connection_db => "$(x)";
     }
     
```

where x is currently `mysql` or `postgres`.

**Notes**:

For the knowledge agent, this setting is made in the control body. For 
database verification promises, it is made in the `database_server` body.


### database_type

**Type**: (menu option)

**Allowed input range**:   

```cf3
               sql
               ms_registry
```

**Default value:** none

**Description**: The `database_type` menu option is a type of database 
that is to be manipulated.

**Example**:

```cf3
database_type => "ms_registry";
```

### database_operation

**Type**: (menu option)

**Allowed input range**:   

```cf3
               create
               delete
               drop
               cache
               verify
               restore
```

**Description**: The `database_operation` menu option represents the 
nature of the promise.

**Example**:

```cf3
database_operation => "create";
```

### database_columns

**Type**: `slist`

**Allowed input range**: `.*`

**Description**: A `database_columns` slist defines column definitions 
to be promised by SQL databases.

Columns are a list of tuplets (Name,type,size). Array items are triplets, 
and fixed size data elements are doublets.

**Example**:

```cf3
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
```

### database_rows

**Type**: `slist`

**Allowed input range**: `.*,.*`

**Description**: `database_rows` is an ordered list of row values to be 
promised by SQL databases.

This constraint is used only in adding data to database columns. Rows are 
considered to be instances of individual columns.

**Example**:

```cf3
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
```

**Notes**:

In the case of the system registry on Windows, the rows represent data on 
data-value pairs. The currently supported types (the middle field) for the 
Windows registry are `REG_SZ` (string), `REG_EXPAND_SZ` (expandable string) 
and `REG_DWORD` (double word).

### registry_exclude

**Type**: `slist`

**Allowed input range**: (arbitrary string)

**Description**: An `registry_exclude` slist contains regular expressions 
to ignore in key/value verification.

During recursive Windows registry scanning, this option allows us to ignore 
keys of values matching a list of regular expressions. Some values in the 
registry are ephemeral and some should not be considered. This provides a 
convenient way of avoiding names. It is analogous to `exclude_dirs` for 
files.

**Example**:

```cf3
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
```




