# `reporter` control promises

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




## `aggregation_point`

**Type**: string

**Allowed input range**: `"?(/.*)`

**Synopsis**: The root directory of the data cache for CMDB
aggregation

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





## `auto_scaling`

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

    body reporter control
    {
    auto_scaling => "true";
    }

**Notes**:

Automatic scaling is the default.





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





## `csv2xml`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: A list of csv formatted files in the build directory
to convert to simple xml

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





## `error_bars`

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

    body reporter control
    {
    error_bars => "true";
    }

**Notes**:

The default is to produce error bars. Without error bars from
CFEngine's machine learning data there is no way to assess the
significance of an observation about the system, i.e. whether it is
normal or anomalous.





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





## `html_embed`

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

    body reporter control
    {
    html_embed => "true";
    }

**Notes**:

Embedded HTML means something that could be put into a frame or
table, without html or body tags, headers footers etc.





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





## `reports`

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

    body reporter control
    {
    reports => { "performance", "classes"  };
    }

**Notes**:

A list of report types that can be generated by this agent. The
listed items from `compliance` onward are available only Enterprise
editions of CFEngine.

The keyword 'all' can be used to get all reports except the audit
and locking reports. The latter are large and unwieldy and need
specific confirmation.





## `report_output`

**Type**: (menu option)

**Allowed input range**:

                   csv
                   html
                   text
                   xml

**Default value:** none

**Synopsis**: Menu option for generated output format. Applies only
to text reports, graph data remain in xydy format.

    body reporter control
    {
    report_output => "html";
    }

**Notes**:

Sets the output format of embedded database reports.





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





## `time_stamps`

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

