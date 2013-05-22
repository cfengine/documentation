# `cf-execd`

Scheduler - responsible for running `cf-agent` on a regular (and
user-configurable) basis (in CFEngine 2 the scheduler was called
`cfexecd`). It collects the output of the agent and can email it to a
specified address. It can splay the start time of executions across
the network and work as a class-based clock for scheduling.

`cf-execd` keeps the promises made in
`common` bundles, and is affected by
`common` and `executor` control
bodies.


## Command reference

        '--help'
           (-h) - Print the help message
        '--debug'
           (-d value) - Set debugging level 0,1,2,3
        '--verbose'
           (-v) - Output verbose information about the behaviour of the
            agent
        '--dry-run'
           (-n) - All talk and no action mode - make no changes, only
            inform of promises not kept
        '--version'
           (-V) - Output the version of the software
        '--file'
           (-f value) - Specify an alternative input file than the default
        '--define'
           (-D value) - Define a list of comma separated classes to be
            defined at the start of execution
        '--negate'
           (-N value) - Define a list of comma separated classes to be
            undefined at the start of execution
        '--no-lock'
           (-K) - Ignore locking constraints during execution
            (ifelapsed/expireafter) if "too soon" to run
        '--inform'
           (-I) - Print basic information about changes made to the
            system, i.e. promises repaired
        '--diagnostic'
           (-x) - Activate internal diagnostics (developers only)
        '--no-fork'
           (-F) - Run as a foreground processes (do not fork)
        '--once'
           (-O) - Run once and then exit
        '--no-winsrv'
           (-W) - Do not run as a service on windows - use this when
            running from a command shell (commercial editions only)
        '--ld-library-path'
           (-L value) - Set the internal value of LD\_LIBRARY\_PATH for
            child processes

Debug levels: 1=parsing, 2=running, 3=summary, 4=expression eval

