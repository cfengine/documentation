---
layout: default
title: databases
published: true
tags: [Reference, bundle agent, databases, promises, promise types]
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

* *LDAP - The Lightweight Directory Access Protocol*

A hierarchical network database primarily for reading simple schema
(Only CFEngine Enterprise).

* *SQL - Structured Query Language*

A number of relational databases (currently supported: MySQL, Postgres)
for reading and writing complex data.

* *Registry - Microsoft Registry*

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

      "cfengine.db/brand_new"

      # These are the defaults
      # database_type => "sql",
      # database_operation => "create",

      database_columns => {
                            "mighty varchar(50)",
                            "killer varchar(80)",
                            "batman varchar(20)",
                            "rating integer",
      },
      database_rows => {
                         "mighty='mouse', killer='cheeses', batman => 'yes', rating=>'5' ",
                         "mighty='gort', killer=>'raygun', batman => 'yes', rating=>'10' ",
                         "mighty='fred', killer='queen', batman => 'no', rating=>'10' ",
      },

      database_server => sqlite;
}


body database_server sqlite
{
      db_server_type => "sqlite";
      db_embedded_directory_path => "/tmp";
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
                            "topic_name varchar(256)",
                            "topic_comment varchar(1024)",
                            "topic_id varchar(256)",
                            "topic_type varchar(256)",
                            "topic_extra varchar(256)"
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

***

## Attributes ##

[%CFEngine_include_markdown(common-attributes-include.markdown)%]

### database_server

**Type:** `body database_server`

#### db_server_owner

**Description:** The `db_server_owner` string represents the user name
for a database connection.

**Type:** `string`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
     db_server_owner => "mark";
```

#### db_server_password

**Description:** The `db_server_password ` string represents the clear
text password for a database connection.

**Type:** `string`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
     db_server_password => "xyz.1234";
```

#### db_server_host

**Description:** The `db_server_host` string represents the hostname or
address for a database connection.

A blank value is equal to localhost.

**Type:** `string`

**Allowed input range:** (arbitrary string)

**Example:**
```cf3
     db_server_host => "sqlserv.example.org";
```

#### db_server_type

**Description:** The `db_server_type` string represents the type of
database server being used.

**Type:** (menu option)

**Allowed input range:**

```
    postgres
    mysql
```

**Default value:** none

**Example:**

```cf3
     db_server_type => "postgres";
```

#### db_server_connection_db

**Description:** The `db_server_connection_db` string is the name of an
existing database to connect to in order to create/manage other databases.

In order to create a database on a database server (all of which practice
voluntary cooperation), one has to be able to connect to the server.
However, without an existing database this is not allowed. Thus, database
servers provide a default database that can be connected to in order to
thereafter create new databases. These are called `postgres` and `mysql`
for their respective database servers.

**Type:** `string`

**Allowed input range:** (arbitrary string)

**Example:**

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

### database_type

**Description:** The `database_type` menu option is a type of database
that is to be manipulated.

**Type:** (menu option)

**Allowed input range:**

```
    sql
    ms_registry
```

**Default value:** none

**Example:**

```cf3
database_type => "ms_registry";
```

### database_operation

**Description:** The `database_operation` menu option represents the
nature of the promise.

**Type:** (menu option)

**Allowed input range:**

```
    create
    delete
    drop
    cache
    verify
    restore
```

**Example:**

```cf3
database_operation => "create";
```

### database_columns

**Description:** A `database_columns` slist defines column definitions
to be promised by SQL databases.

Columns are quoted SQL type statements, which may be database specific.

**Type:** `slist`

**Allowed input range:** `.*`

**Example:**

```cf3
  "cf_topic_maps/topics"

    database_operation => "create",
    database_type => "sql",
    database_columns => {
                        "topic_name varchar(256)",
                        "topic_comment varchar(1024)",
                        "topic_id varchar(256)",
                        "topic_type varchar(256)",
                        "topic_extra varchar(256)"
                        },

    database_server => myserver;
```

### database_rows

**Description:** `database_rows` is an ordered list of row values to be
promised by SQL databases.

This constraint is used only in adding data to database columns. Rows are
considered to be instances of individual columns.

If the database is  SQL database, the row elements may contain two kinds of
elements, those with `=' signs and those with attribute arrows `=>':
```cf3
 database_rows => { "mighty='mouse', killer='cheeses', batman => 'yes', rating=>'5' " }
```
The `=' symbols indicate `WHERE' clauses in SQL to match pre-existing conditions,
while the `=>' symbols indicate a convergent target to apply. Thus, in the example above,
one would read: set batman to yes, rating to 5, in rows where mighty is like mouse and
killer is like cheeses.

**Type:** `slist`

**Allowed input range:** `.*,.*`

**Example:**

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

 android:

  "cfengine.db/brand_new"

      database_columns => {
                          "mighty varchar(50)",
                          "killer varchar(80)",
                          "batman varchar(20)",
                          "rating integer",
                          },

      database_rows =>    {
                          "mighty='mouse', killer='cheeses', batman => 'yes', rating=>'5' ",
                          "mighty='gort', killer=>'raygun', batman => 'yes', rating=>'10' ",
                          "mighty='fred', killer='queen', batman => 'no', rating=>'10' ",
                          },

      database_server => sqlite;

}
```

**Notes:**

In the case of the system registry on Windows, the rows represent data on
data-value pairs. The currently supported types (the middle field) for the
Windows registry are `REG_SZ` (string), `REG_EXPAND_SZ` (expandable string)
and `REG_DWORD` (double word).

### registry_exclude

**Description:** An `registry_exclude` slist contains regular expressions
to ignore in key/value verification.

During recursive Windows registry scanning, this option allows us to ignore
keys of values matching a list of regular expressions. Some values in the
registry are ephemeral and some should not be considered. This provides a
convenient way of avoiding names. It is analogous to `exclude_dirs` for
files.

**Type:** `slist`

**Allowed input range:** (arbitrary string)

**Example:**

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
