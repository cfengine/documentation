### 5.7 `knowledge` control promises





         
         body knowledge control
         
         {
         query_output    => "html";
         }
         



Settings describing the details of the fixed behavioural promises
made by `cf-know`. These parameters control the way in which
knowledge data are stored and retrieved from a relational database
and the output format of the queries.

-   [build\_directory in knowledge](/manuals/cf3-Reference#build_005fdirectory-in-knowledge)
-   [document\_root in knowledge](/manuals/cf3-Reference#document_005froot-in-knowledge)
-   [generate\_manual in knowledge](/manuals/cf3-Reference#generate_005fmanual-in-knowledge)
-   [graph\_directory in knowledge](/manuals/cf3-Reference#graph_005fdirectory-in-knowledge)
-   [graph\_output in knowledge](/manuals/cf3-Reference#graph_005foutput-in-knowledge)
-   [html\_banner in knowledge](/manuals/cf3-Reference#html_005fbanner-in-knowledge)
-   [html\_footer in knowledge](/manuals/cf3-Reference#html_005ffooter-in-knowledge)
-   [id\_prefix in knowledge](/manuals/cf3-Reference#id_005fprefix-in-knowledge)
-   [manual\_source\_directory in knowledge](/manuals/cf3-Reference#manual_005fsource_005fdirectory-in-knowledge)
-   [query\_engine in knowledge](/manuals/cf3-Reference#query_005fengine-in-knowledge)
-   [query\_output in knowledge](/manuals/cf3-Reference#query_005foutput-in-knowledge)
-   [sql\_type in knowledge](/manuals/cf3-Reference#sql_005ftype-in-knowledge)
-   [sql\_database in knowledge](/manuals/cf3-Reference#sql_005fdatabase-in-knowledge)
-   [sql\_owner in knowledge](/manuals/cf3-Reference#sql_005fowner-in-knowledge)
-   [sql\_passwd in knowledge](/manuals/cf3-Reference#sql_005fpasswd-in-knowledge)
-   [sql\_server in knowledge](/manuals/cf3-Reference#sql_005fserver-in-knowledge)
-   [sql\_connection\_db in knowledge](/manuals/cf3-Reference#sql_005fconnection_005fdb-in-knowledge)
-   [style\_sheet in knowledge](/manuals/cf3-Reference#style_005fsheet-in-knowledge)
-   [view\_projections in knowledge](/manuals/cf3-Reference#view_005fprojections-in-knowledge)




* * * * *

Next: [document\_root in knowledge](/manuals/cf3-Reference#document_005froot-in-knowledge),
Previous: [control knowledge](/manuals/cf3-Reference#control-knowledge),
Up: [control knowledge](/manuals/cf3-Reference#control-knowledge)
#### 5.7.1 `build_directory`

**Type**: string

**Allowed input range**: `.*`

**Default value:** Current working directory

**Synopsis**: The directory in which to generate output files

**Example**:

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




* * * * *

Next: [generate\_manual in knowledge](/manuals/cf3-Reference#generate_005fmanual-in-knowledge),
Previous: [build\_directory in knowledge](/manuals/cf3-Reference#build_005fdirectory-in-knowledge),
Up: [control knowledge](/manuals/cf3-Reference#control-knowledge)
#### 5.7.2 `document_root`

**Type**: string

**Allowed input range**: `.*`

**Synopsis**: The directory in which the web root resides

**Example**:

    body knowledge control
    
    {
    document_root => "/srv/www/htdocs";
    }

**Notes**:

The local file path of the system's web document root.




* * * * *

Next: [graph\_directory in knowledge](/manuals/cf3-Reference#graph_005fdirectory-in-knowledge),
Previous: [document\_root in knowledge](/manuals/cf3-Reference#document_005froot-in-knowledge),
Up: [control knowledge](/manuals/cf3-Reference#control-knowledge)
#### 5.7.3 `generate_manual`

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

**Example**:

    body knowledge control
    {
    generate_manual => "true";
    }

**Notes**:

Auto-creates a manual based on the self-documented code. As the
promise syntax is extended the manual self-heals. The resulting
manual is generated in Texinfo format, from which all other formats
can be generated.




* * * * *

Next: [graph\_output in knowledge](/manuals/cf3-Reference#graph_005foutput-in-knowledge),
Previous: [generate\_manual in knowledge](/manuals/cf3-Reference#generate_005fmanual-in-knowledge),
Up: [control knowledge](/manuals/cf3-Reference#control-knowledge)
#### 5.7.4 `graph_directory`

**Type**: string

**Allowed input range**: `"?(/.*)`

**Synopsis**: Path to directory where rendered .png files will be
created

**Example**:

    body knowledge control
    {
    graph_directory => "/tmp/output";
    }

**Notes**:

A separate location where the potentially large number of .png
visualizations of a knowledge representation are pre-compiled. This
feature only works if the necessary graphics libraries are
present.




* * * * *

Next: [html\_banner in knowledge](/manuals/cf3-Reference#html_005fbanner-in-knowledge),
Previous: [graph\_directory in knowledge](/manuals/cf3-Reference#graph_005fdirectory-in-knowledge),
Up: [control knowledge](/manuals/cf3-Reference#control-knowledge)
#### 5.7.5 `graph_output`

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

**Example**:

    body knowledge control
    
    {
    # fix/override -g option
    
    graph_output => "true"; 
    }

**Notes**:

Equivalent to the use of the ‘-g’ option for `cf-know`.




* * * * *

Next: [html\_footer in knowledge](/manuals/cf3-Reference#html_005ffooter-in-knowledge),
Previous: [graph\_output in knowledge](/manuals/cf3-Reference#graph_005foutput-in-knowledge),
Up: [control knowledge](/manuals/cf3-Reference#control-knowledge)
#### 5.7.6 `html_banner`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: HTML code for a banner to be added to rendered in
html after the header

**Example**:

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




* * * * *

Next: [id\_prefix in knowledge](/manuals/cf3-Reference#id_005fprefix-in-knowledge),
Previous: [html\_banner in knowledge](/manuals/cf3-Reference#html_005fbanner-in-knowledge),
Up: [control knowledge](/manuals/cf3-Reference#control-knowledge)
#### 5.7.7 `html_footer`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: HTML code for a page footer to be added to rendered
in html before the end body tag

**Example**:

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




* * * * *

Next: [manual\_source\_directory in knowledge](/manuals/cf3-Reference#manual_005fsource_005fdirectory-in-knowledge),
Previous: [html\_footer in knowledge](/manuals/cf3-Reference#html_005ffooter-in-knowledge),
Up: [control knowledge](/manuals/cf3-Reference#control-knowledge)
#### 5.7.8 `id_prefix`

**Type**: string

**Allowed input range**: `.*`

**Synopsis**: The LTM identifier prefix used to label topic maps
(used for disambiguation in merging)

**Example**:

    body knowledge control
    {
    id_prefix => "unique_prefix";
    }

**Notes**:

Use to disambiguate indentifiers for a successful merging of topic
maps, especially in Linear Topic Map (LTM) format using third party
tools such as Ontopia's Omnigator.




* * * * *

Next: [query\_engine in knowledge](/manuals/cf3-Reference#query_005fengine-in-knowledge),
Previous: [id\_prefix in knowledge](/manuals/cf3-Reference#id_005fprefix-in-knowledge),
Up: [control knowledge](/manuals/cf3-Reference#control-knowledge)
#### 5.7.9 `manual_source_directory`

**Type**: string

**Allowed input range**: `"?(/.*)`

**Synopsis**: Path to directory where raw text about manual topics
is found (defaults to build\_directory)

**Example**:

    body knowledge control
    {
    manual_source => "/path/cfengine_manual_commentary";
    }

**Notes**:

This is used in the self-healing documentation. The directory
points to a location where the Texinfo sources for per-section
commentary is maintained.




* * * * *

Next: [query\_output in knowledge](/manuals/cf3-Reference#query_005foutput-in-knowledge),
Previous: [manual\_source\_directory in knowledge](/manuals/cf3-Reference#manual_005fsource_005fdirectory-in-knowledge),
Up: [control knowledge](/manuals/cf3-Reference#control-knowledge)
#### 5.7.10 `query_engine`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: Name of a dynamic web-page used to accept and drive
queries in a browser

**Example**:

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




* * * * *

Next: [sql\_type in knowledge](/manuals/cf3-Reference#sql_005ftype-in-knowledge),
Previous: [query\_engine in knowledge](/manuals/cf3-Reference#query_005fengine-in-knowledge),
Up: [control knowledge](/manuals/cf3-Reference#control-knowledge)
#### 5.7.11 `query_output`

**Type**: (menu option)

**Allowed input range**:

                   html
                   text

**Synopsis**: Menu option for generated output format

**Example**:

    body knowledge control
    {
    query_output => "html";
    }

**Notes**:




* * * * *

Next: [sql\_database in knowledge](/manuals/cf3-Reference#sql_005fdatabase-in-knowledge),
Previous: [query\_output in knowledge](/manuals/cf3-Reference#query_005foutput-in-knowledge),
Up: [control knowledge](/manuals/cf3-Reference#control-knowledge)
#### 5.7.12 `sql_type`

**Type**: (menu option)

**Allowed input range**:

                   mysql
                   postgres

**Synopsis**: Menu option for supported database type

**Example**:

    body knowledge control
    {
    sql_type => "mysql";
    }

**Notes**:




* * * * *

Next: [sql\_owner in knowledge](/manuals/cf3-Reference#sql_005fowner-in-knowledge),
Previous: [sql\_type in knowledge](/manuals/cf3-Reference#sql_005ftype-in-knowledge),
Up: [control knowledge](/manuals/cf3-Reference#control-knowledge)
#### 5.7.13 `sql_database`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: Name of database used for the topic map

**Example**:

    body knowledge control
    {
    sql_database => "cfengine_knowledge_db";
    }

**Notes**:

The name of an SQL database for caching knowledge.




* * * * *

Next: [sql\_passwd in knowledge](/manuals/cf3-Reference#sql_005fpasswd-in-knowledge),
Previous: [sql\_database in knowledge](/manuals/cf3-Reference#sql_005fdatabase-in-knowledge),
Up: [control knowledge](/manuals/cf3-Reference#control-knowledge)
#### 5.7.14 `sql_owner`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: User id of sql database user

**Example**:

    body knowledge control
    {
    sql_owner => "db_owner";
    }

**Notes**:

Part of the credentials for opening the database. This depends on
the type of database.




* * * * *

Next: [sql\_server in knowledge](/manuals/cf3-Reference#sql_005fserver-in-knowledge),
Previous: [sql\_owner in knowledge](/manuals/cf3-Reference#sql_005fowner-in-knowledge),
Up: [control knowledge](/manuals/cf3-Reference#control-knowledge)
#### 5.7.15 `sql_passwd`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: Embedded password for accessing sql database

**Example**:

    body knowledge control
    {
    sql_passwd => "";
    }

**Notes**:

Part of the credentials for connecting to the database server. This
is system dependent. If the server host is localhost a password
might not be required.




* * * * *

Next: [sql\_connection\_db in knowledge](/manuals/cf3-Reference#sql_005fconnection_005fdb-in-knowledge),
Previous: [sql\_passwd in knowledge](/manuals/cf3-Reference#sql_005fpasswd-in-knowledge),
Up: [control knowledge](/manuals/cf3-Reference#control-knowledge)
#### 5.7.16 `sql_server`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: Name or IP of database server (or localhost)

**Example**:

    body knowledge control
    {
    sql_server => "localhost";
    }

**Notes**:

The host name of IP address of the server. The default is to look
on the localhost.




* * * * *

Next: [style\_sheet in knowledge](/manuals/cf3-Reference#style_005fsheet-in-knowledge),
Previous: [sql\_server in knowledge](/manuals/cf3-Reference#sql_005fserver-in-knowledge),
Up: [control knowledge](/manuals/cf3-Reference#control-knowledge)
#### 5.7.17 `sql_connection_db`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: The name of an existing database to connect to in
order to create/manage other databases

**Example**:

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




* * * * *

Next: [view\_projections in knowledge](/manuals/cf3-Reference#view_005fprojections-in-knowledge),
Previous: [sql\_connection\_db in knowledge](/manuals/cf3-Reference#sql_005fconnection_005fdb-in-knowledge),
Up: [control knowledge](/manuals/cf3-Reference#control-knowledge)
#### 5.7.18 `style_sheet`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: Name of a style-sheet to be used in rendering html
output (added to headers)

**Example**:

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




* * * * *

Previous: [style\_sheet in knowledge](/manuals/cf3-Reference#style_005fsheet-in-knowledge),
Up: [control knowledge](/manuals/cf3-Reference#control-knowledge)
#### 5.7.19 `view_projections`

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

**Example**:

    body knowledge control
    {
    view_projections => "true";
    }

**Notes**:

If this is set to true, CFEngine Nova computes additional graphical
representations in its knowledge map, representing causal
dependencies between CFEngine promises.




* * * * *

Next: [control hub](/manuals/cf3-Reference#control-hub),
Previous: [control knowledge](/manuals/cf3-Reference#control-knowledge),
Up: [Control Promises](/manuals/cf3-Reference#Control-Promises)
### 5.8 `reporter` control promises



    body reporter control
    {
    reports => { "performance", "last_seen", "monitor_history" };
    build_directory => "/tmp/nerves";
    report_output => "html";
    }



Determines a list of reports to write into the build directory. The
format may be in text, html or xml format. The reporter agent
`cf-report` replaces both `cfshow` and `cfenvgraph`. It no longer
produces output to the console.

Some reports are only available in enterprise level versions of
CFEngine.

-   [aggregation\_point in reporter](/manuals/cf3-Reference#aggregation_005fpoint-in-reporter)
-   [auto\_scaling in reporter](/manuals/cf3-Reference#auto_005fscaling-in-reporter)
-   [build\_directory in reporter](/manuals/cf3-Reference#build_005fdirectory-in-reporter)
-   [csv2xml in reporter](/manuals/cf3-Reference#csv2xml-in-reporter)
-   [error\_bars in reporter](/manuals/cf3-Reference#error_005fbars-in-reporter)
-   [html\_banner in reporter](/manuals/cf3-Reference#html_005fbanner-in-reporter)
-   [html\_embed in reporter](/manuals/cf3-Reference#html_005fembed-in-reporter)
-   [html\_footer in reporter](/manuals/cf3-Reference#html_005ffooter-in-reporter)
-   [query\_engine in reporter](/manuals/cf3-Reference#query_005fengine-in-reporter)
-   [reports in reporter](/manuals/cf3-Reference#reports-in-reporter)
-   [report\_output in reporter](/manuals/cf3-Reference#report_005foutput-in-reporter)
-   [style\_sheet in reporter](/manuals/cf3-Reference#style_005fsheet-in-reporter)
-   [time\_stamps in reporter](/manuals/cf3-Reference#time_005fstamps-in-reporter)




* * * * *

Next: [auto\_scaling in reporter](/manuals/cf3-Reference#auto_005fscaling-in-reporter),
Previous: [control reporter](/manuals/cf3-Reference#control-reporter),
Up: [control reporter](/manuals/cf3-Reference#control-reporter)
#### 5.8.1 `aggregation_point`

**Type**: string

**Allowed input range**: `"?(/.*)`

**Synopsis**: The root directory of the data cache for CMDB
aggregation

**Example**:

    body reporter control
    {
    aggregation_point => "/srv/www/htdocs/reports";
    }

**Notes**:

This feature is only used in enterprise level versions of CFEngine.
It specifies the directory where reports from multiple hosts are to
be aggregated in sub-directories. This should be somewhere under
the document root of the web server for the CFEngine knowledge base
in order to make the reports browsable.




* * * * *

Next: [build\_directory in reporter](/manuals/cf3-Reference#build_005fdirectory-in-reporter),
Previous: [aggregation\_point in reporter](/manuals/cf3-Reference#aggregation_005fpoint-in-reporter),
Up: [control reporter](/manuals/cf3-Reference#control-reporter)
#### 5.8.2 `auto_scaling`

**Type**: (menu option)

**Allowed input range**:

                   true
                   false
                   yes
                   no
                   on
                   off

**Default value:** true

**Synopsis**: true/false whether to auto-scale graph output to
optimize use of space

**Example**:

    body reporter control
    {
    auto_scaling => "true";
    }

**Notes**:

Automatic scaling is the default.




* * * * *

Next: [csv2xml in reporter](/manuals/cf3-Reference#csv2xml-in-reporter),
Previous: [auto\_scaling in reporter](/manuals/cf3-Reference#auto_005fscaling-in-reporter),
Up: [control reporter](/manuals/cf3-Reference#control-reporter)
#### 5.8.3 `build_directory`

**Type**: string

**Allowed input range**: `.*`

**Default value:** Current working directory

**Synopsis**: The directory in which to generate output files

**Example**:

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




* * * * *

Next: [error\_bars in reporter](/manuals/cf3-Reference#error_005fbars-in-reporter),
Previous: [build\_directory in reporter](/manuals/cf3-Reference#build_005fdirectory-in-reporter),
Up: [control reporter](/manuals/cf3-Reference#control-reporter)
#### 5.8.4 `csv2xml`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: A list of csv formatted files in the build directory
to convert to simple xml

**Example**:

    body reporter control
    {
    csv2xml => { "myreport.csv", "custom_report.csv"  };
    }

**Notes**:

CSV files are easy to generate in CFEngine from individual promise
logging functions. XML is not easily generated due to its
hierarchical structure. This function allows `cf-report` to convert
a CSV file into pidgin XML for convenience. The schema has the
general form:

    <output>
     <line> <one>...</one> <two>...</two> ... </line>
     <line> <one>...</one> <two>...</two> ... </line>
    </output>




* * * * *

Next: [html\_banner in reporter](/manuals/cf3-Reference#html_005fbanner-in-reporter),
Previous: [csv2xml in reporter](/manuals/cf3-Reference#csv2xml-in-reporter),
Up: [control reporter](/manuals/cf3-Reference#control-reporter)
#### 5.8.5 `error_bars`

**Type**: (menu option)

**Allowed input range**:

                   true
                   false
                   yes
                   no
                   on
                   off

**Default value:** true

**Synopsis**: true/false whether to generate error bars on graph
output

**Example**:

    body reporter control
    {
    error_bars => "true";
    }

**Notes**:

The default is to produce error bars. Without error bars from
CFEngine's machine learning data there is no way to assess the
significance of an observation about the system, i.e. whether it is
normal or anomalous.




* * * * *

Next: [html\_embed in reporter](/manuals/cf3-Reference#html_005fembed-in-reporter),
Previous: [error\_bars in reporter](/manuals/cf3-Reference#error_005fbars-in-reporter),
Up: [control reporter](/manuals/cf3-Reference#control-reporter)
#### 5.8.6 `html_banner`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: HTML code for a banner to be added to rendered in
html after the header

**Example**:

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




* * * * *

Next: [html\_footer in reporter](/manuals/cf3-Reference#html_005ffooter-in-reporter),
Previous: [html\_banner in reporter](/manuals/cf3-Reference#html_005fbanner-in-reporter),
Up: [control reporter](/manuals/cf3-Reference#control-reporter)
#### 5.8.7 `html_embed`

**Type**: (menu option)

**Allowed input range**:

                   true
                   false
                   yes
                   no
                   on
                   off

**Synopsis**: If true, no header and footer tags will be added to
html output

**Example**:

    body reporter control
    {
    html_embed => "true";
    }

**Notes**:

Embedded HTML means something that could be put into a frame or
table, without html or body tags, headers footers etc.




* * * * *

Next: [query\_engine in reporter](/manuals/cf3-Reference#query_005fengine-in-reporter),
Previous: [html\_embed in reporter](/manuals/cf3-Reference#html_005fembed-in-reporter),
Up: [control reporter](/manuals/cf3-Reference#control-reporter)
#### 5.8.8 `html_footer`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: HTML code for a page footer to be added to rendered
in html before the end body tag

**Example**:

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




* * * * *

Next: [reports in reporter](/manuals/cf3-Reference#reports-in-reporter),
Previous: [html\_footer in reporter](/manuals/cf3-Reference#html_005ffooter-in-reporter),
Up: [control reporter](/manuals/cf3-Reference#control-reporter)
#### 5.8.9 `query_engine`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: Name of a dynamic web-page used to accept and drive
queries in a browser

**Example**:

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




* * * * *

Next: [report\_output in reporter](/manuals/cf3-Reference#report_005foutput-in-reporter),
Previous: [query\_engine in reporter](/manuals/cf3-Reference#query_005fengine-in-reporter),
Up: [control reporter](/manuals/cf3-Reference#control-reporter)
#### 5.8.10 `reports`

**Type**: (option list)

**Allowed input range**:

                   all
                   audit
                   performance
                   all_locks
                   active_locks
                   hashes
                   classes
                   last_seen
                   monitor_now
                   monitor_history
                   monitor_summary
                   compliance
                   setuid
                   file_changes
                   installed_software
                   software_patches
                   value
                   variables

**Default value:** none

**Synopsis**: A list of reports that may be generated

**Example**:

    body reporter control
    {
    reports => { "performance", "classes"  };
    }

**Notes**:

A list of report types that can be generated by this agent. The
listed items from `compliance` onward are available only Enterprise
editions of CFEngine.

The keyword ‘all’ can be used to get all reports except the audit
and locking reports. The latter are large and unwieldy and need
specific confirmation.




* * * * *

Next: [style\_sheet in reporter](/manuals/cf3-Reference#style_005fsheet-in-reporter),
Previous: [reports in reporter](/manuals/cf3-Reference#reports-in-reporter),
Up: [control reporter](/manuals/cf3-Reference#control-reporter)
#### 5.8.11 `report_output`

**Type**: (menu option)

**Allowed input range**:

                   csv
                   html
                   text
                   xml

**Default value:** none

**Synopsis**: Menu option for generated output format. Applies only
to text reports, graph data remain in xydy format.

**Example**:

    body reporter control
    {
    report_output => "html";
    }

**Notes**:

Sets the output format of embedded database reports.




* * * * *

Next: [time\_stamps in reporter](/manuals/cf3-Reference#time_005fstamps-in-reporter),
Previous: [report\_output in reporter](/manuals/cf3-Reference#report_005foutput-in-reporter),
Up: [control reporter](/manuals/cf3-Reference#control-reporter)
#### 5.8.12 `style_sheet`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: Name of a style-sheet to be used in rendering html
output (added to headers)

**Example**:

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




* * * * *

Previous: [style\_sheet in reporter](/manuals/cf3-Reference#style_005fsheet-in-reporter),
Up: [control reporter](/manuals/cf3-Reference#control-reporter)
#### 5.8.13 `time_stamps`

**Type**: (menu option)

**Allowed input range**:

                   true
                   false
                   yes
                   no
                   on
                   off

**Default value:** false

**Synopsis**: true/false whether to generate timestamps in the
output directory name

**Example**:

    body reporter control
    {
    time_stamps => "true";
    }

**Notes**:

This option is only necessary with the default build directory.
This can be used to keep snapshots of the system but it will result
in a lot of storage be consumed. For most purposes CFEngine is
programmed to forget the past at a predictable rate and there is no
need to override this.




* * * * *

Next: [control file](/manuals/cf3-Reference#control-file),
Previous: [control reporter](/manuals/cf3-Reference#control-reporter),
Up: [Control Promises](/manuals/cf3-Reference#Control-Promises)


