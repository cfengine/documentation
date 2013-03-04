# `cf-know`

Knowledge modelling agent - responsible for building and analysing
a semantic knowledge network. It can configure a relational
database to contain a topic map and permit
regular-expression based searching of the map. Analysis of the
semantic network can be performed providing graphical output of the
data, and `cf-know` can assemble and converge the reference manual for
the current version of the CFEngine software.

`cf-know` keeps the promises made in `common`
and `knowledge` bundles, and is affected by
`common` and `knowledge` control bodies.

## Command reference

        '--help'
           (-h) - Print the help message
        '--build'
           (-b) - Build and store topic map in the CFDB
        '--debug'
           (-d value) - Set debugging level 0,1,2,3
        '--verbose'
           (-v) - Output verbose information about the behaviour of the agent
        '--version'
           (-V) - Output the version of the software
        '--file'
           (-f value) - Specify an alternative input file than the default
        '--goals'
           (-g) - Print basic information about changes made to the system, i.e. promises repaired
        '--inform'
           (-I) - Print JSON output about a possibly qualified context::topic
        '--lookup'
           (-l value) - lookup
        '--manpage'
           (-M) - Generate reference manpage from internal data
        '--tell-me-about'
           (-z value) - Look up stories for a given topic on the command line 
        '--search'
           (-s value) - Search the hub generically for results
        '--syntax'
           (-S value) - Print a syntax summary of the optional keyword or
            this CFEngine version
        '--topics'
           (-T) - Show all topic names in CFEngine
        '--test'
           (-t value) - Generate test data
        '--removetest'
           (-r) - Remove test data
        '--updatetest'
           (-u) - Update test data

Debug levels: 1=parsing, 2=running, 3=summary, 4

