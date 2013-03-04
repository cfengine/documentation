# `cf-report`

Self-knowledge extractor - takes data stored in CFEngine's embedded
databases and converts them to human readable form

`cf-report` keeps the promises made in
`common` bundles, and is affected by
`common` and `reporter` control
bodies.

## Command reference

        '--help'
           '(-h) - Print the help message
        '--class-regex'
           '(-c value) - Specify a class regular expression to search for
        '--csv'
           '(-C) - Enable CSV output mode in hub queries
        '--debug'
           '(-d value) - Set debugging level 0,1,2,3
        '--verbose'
           '(-v) - Output verbose information about the behaviour of the agent
        '--inform'
           '(-I) - Output information about actions performed by the agent
        '--version'
           '(-V) - Output the version of the software
        '--no-lock'
           '(-K) - Ignore ifelapsed locks
        '--file'
           '(-f value) - Specify an alternative input file than the default
        '--hostkey'
           '(-k value) - Specify a hostkey to lookup
        '--html'
           '(-H) - Print output in HTML
        '--xml'
           '(-X) - Print output in XML
        '--version'
           '(-V) - Print version string for software
        '--purge'
           '(-P) - Purge data about peers not seen beyond the threshold
            horizon for assumed-dead
        '--erasehistory'
           '(-E value) - Erase historical data from the cf-monitord
            monitoring database
        '--filter'
           (-F value) - Specify a name regular expression for filtering results
        '--nova-export'
           '(-x value) - Export Nova reports to file - delta or full report
             (commercial editions only)
        '--nova-import'
           '(-i value) - Import Nova reports from file - specify the path
             (only on Nova/Enterprise policy hub)
        '--outputdir'
           '(-o value) - Set output directory for printing graph data
        '--promise-handle'
           '(-p value) - Specify a promise-handle to look up
        '--query-hub'
           '(-q value) - Query hub database interactively with optional
             regex search string
        '--titles'
           '(-t) - Add title data to generated graph files
        '--timestamps'
           '(-T) - Add a time stamp to directory name for graph file data
        '--resolution'
           '(-R) - Print graph data in high resolution
        '--show'
           '(-1 value) - Show data matching named criteria
             (software,variables,classes)
        '--syntax'
           '(-S) - Print a syntax summary for this CFEngine version
        '--syntax-export'
           '(-s) - Export a syntax tree in Javascript format
        '--no-error-bars'
           '(-e) - Do not add error bars to the printed graphs
        '--no-scaling'
           '(-n) - Do not automatically scale the axes
        '--remove-hosts,'
           '(-r value) - Remove comma separated list of IP address entries
             from the hosts-seen database

