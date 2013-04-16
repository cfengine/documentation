# `cf-serverd`

Server - used to distribute policy and/or data files to clients
requesting them and used to respond to requests from `cf-runagent`
(in CFEngine 2 the remote run agent was called `cfservd`).

`cf-serverd` keeps the promises made in
`common` and `server` bundles, and is affected by `common` and
`server` control bodies.

## Command reference

        '--help'
           (-h) - Print the help message
        '--debug'
           (-d value) - Set debugging level 0,1,2,3
        '--verbose'
           (-v) - Output verbose information about the behaviour of the
            agent
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
        '--ld-library-path'
           (-L value) - Set the internal value of LD\_LIBRARY\_PATH for
            child processes

Debug levels: 1=parsing, 2=running, 3=summary, 4=expression eval

