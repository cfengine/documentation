# `knowledge` control promises
         
         body knowledge control
         
         {
         query_output    => "html";
         }
         
Settings describing the details of the fixed behavioural promises
made by `cf-know`. These parameters control the way in which
knowledge data are stored and retrieved from a relational database
and the output format of the queries.





## `build_directory`

**Type**: string

**Allowed input range**: `.*`

**Default value:** Current working directory

**Synopsis**: The directory in which to generate output files

    body knowledge control
    
    {
    #..
    
    build_directory => "/tmp/builddir";
    }
    
    body reporter control
    
    {
    #..
    
    build_directory => "/tmp/builddir";
    }

**Notes**:

The directory where all auto-generated textual output is placed by
`cf-report`. This includes manual generation, ontology and topic
map data.





## `document_root`

**Type**: string

**Allowed input range**: `.*`

**Synopsis**: The directory in which the web root resides

    body knowledge control
    
    {
    document_root => "/srv/www/htdocs";
    }

**Notes**:

The local file path of the system's web document root.





## `generate_manual`

**Type**: (menu option)

**Allowed input range**:

                   true
                   false
                   yes
                   no
                   on
                   off

**Default value:** false

**Synopsis**: true/false generate texinfo manual page skeleton for
this version

    body knowledge control
    {
    generate_manual => "true";
    }

**Notes**:

Auto-creates a manual based on the self-documented code. As the
promise syntax is extended the manual self-heals. The resulting
manual is generated in Texinfo format, from which all other formats
can be generated.





## `graph_directory`

**Type**: string

**Allowed input range**: `"?(/.*)`

**Synopsis**: Path to directory where rendered .png files will be
created

    body knowledge control
    {
    graph_directory => "/tmp/output";
    }

**Notes**:

A separate location where the potentially large number of .png
visualizations of a knowledge representation are pre-compiled. This
feature only works if the necessary graphics libraries are
present.





## `graph_output`

**Type**: (menu option)

**Allowed input range**:

                   true
                   false
                   yes
                   no
                   on
                   off

**Synopsis**: true/false generate png visualization of topic map if
possible (requires lib)

    body knowledge control
    
    {
    # fix/override -g option
    
    graph_output => "true"; 
    }

**Notes**:

Equivalent to the use of the ‘-g’ option for `cf-know`.





## `html_banner`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: HTML code for a banner to be added to rendered in
html after the header

    body knowledge control
    {
    html_banner => "<img src=\"http://www.example.org/img/banner.png\">";
    }
    
    body reporter control
    {
    html_banner => "<img src=\"http://www.example.org/img/banner.png\">";
    }

**Notes**:

This content is cited when generating HTML output from the
knowledge agent.





## `html_footer`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: HTML code for a page footer to be added to rendered
in html before the end body tag

    body reporter control
    {
    html_footer => "
                   <div id=\"footer\">Bottom of the page</div>
                   ";
    }
    
    body knowledge control
    {
    html_footer => "
                   <div id=\"footer\">Bottom of the page</div>
                   ";
    }

**Notes**:

This allows us to cite HTML code for formatting reports generated
by the reporting and knowledge agents.





## `id_prefix`

**Type**: string

**Allowed input range**: `.*`

**Synopsis**: The LTM identifier prefix used to label topic maps
(used for disambiguation in merging)

    body knowledge control
    {
    id_prefix => "unique_prefix";
    }

**Notes**:

Use to disambiguate indentifiers for a successful merging of topic
maps, especially in Linear Topic Map (LTM) format using third party
tools such as Ontopia's Omnigator.





## `manual_source_directory`

**Type**: string

**Allowed input range**: `"?(/.*)`

**Synopsis**: Path to directory where raw text about manual topics
is found (defaults to build\_directory)

    body knowledge control
    {
    manual_source => "/path/cfengine_manual_commentary";
    }

**Notes**:

This is used in the self-healing documentation. The directory
points to a location where the Texinfo sources for per-section
commentary is maintained.





## `query_engine`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: Name of a dynamic web-page used to accept and drive
queries in a browser

    body knowledge control
    {
    query_engine => "http://www.example.org/script.php";
    }
    
    body reporter control
    {
    query_engine => "http://www.example.org/script.pl";
    }

**Notes**:

When displaying topic maps in HTML format, `cf-know` will render
each topic as a link to this URL with the new topic as an argument.
Thus it is possible to make a dynamic web query by embedding
CFEngine in the web page as system call and passing the argument to
it.





## `query_output`

**Type**: (menu option)

**Allowed input range**:

                   html
                   text

**Synopsis**: Menu option for generated output format

    body knowledge control
    {
    query_output => "html";
    }

**Notes**:





## `sql_type`

**Type**: (menu option)

**Allowed input range**:

                   mysql
                   postgres

**Synopsis**: Menu option for supported database type

    body knowledge control
    {
    sql_type => "mysql";
    }

**Notes**:





## `sql_database`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: Name of database used for the topic map

    body knowledge control
    {
    sql_database => "cfengine_knowledge_db";
    }

**Notes**:

The name of an SQL database for caching knowledge.





## `sql_owner`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: User id of sql database user

    body knowledge control
    {
    sql_owner => "db_owner";
    }

**Notes**:

Part of the credentials for opening the database. This depends on
the type of database.





## `sql_passwd`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: Embedded password for accessing sql database

    body knowledge control
    {
    sql_passwd => "";
    }

**Notes**:

Part of the credentials for connecting to the database server. This
is system dependent. If the server host is localhost a password
might not be required.





## `sql_server`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: Name or IP of database server (or localhost)

    body knowledge control
    {
    sql_server => "localhost";
    }

**Notes**:

The host name of IP address of the server. The default is to look
on the localhost.





## `sql_connection_db`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: The name of an existing database to connect to in
order to create/manage other databases

    body knowledge control
    {
    sql_connection_db => "mysql";
    }

**Notes**:

In order to create a database on a database server (all of which
practice voluntary cooperation), one has to be able to connect to
the server, however, without an existing database this is not
allowed. Thus, database servers provide a default database that can
be connected to in order to thereafter create new databases. These
are called `postgres` and `mysql` for their respective database
servers.

For the knowledge agent, this setting is made in the control body,
for database verification promises, it is made in the
`database_server` body.





## `style_sheet`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: Name of a style-sheet to be used in rendering html
output (added to headers)

    body knowledge control
    {
    style_sheet => "http://www.example.org/css/sheet.css";
    }
    
    body reporter control
    {
    style_sheet => "http://www.example.org/css/sheet.css";
    }

**Notes**:

For formatting the HTML generated output of `cf-know`.





## `view_projections`

**Type**: (menu option)

**Allowed input range**:

                   true
                   false
                   yes
                   no
                   on
                   off

**Default value:** false

**Synopsis**: Perform view-projection analytics in graph
generation

    body knowledge control
    {
    view_projections => "true";
    }

**Notes**:

If this is set to true, CFEngine Nova computes additional graphical
representations in its knowledge map, representing causal
dependencies between CFEngine promises.


