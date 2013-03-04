# `cf-runagent`

Remote run agent - used to execute `cf-agent` on a remote machine
(in CFEngine 2 the remote run agent was called `cfrun`).
`cf-runagent` does not keep any promises, but instead is used to
ask another machine to do so.

The run agent connects to a list of running instances of the
`cf-serverd` service. The agent allows a user to forego the usual
scheduling interval for the agent and activate `cf-agent` on a remote
host. Additionally, a user can send additional classes to be
defined on the remote host. Two kinds of classes may be sent:
classes to decide on which hosts the agent will be started, and
classes that the user requests the agent should define on
execution. The latter type is regulated by `cf-serverd`'s role based
access control.

## Command reference

        '--help'
           (-h) - Print the help message
        '--background'
           (-b value) - Parallelize connections (50 by default)
        '--debug'
           (-d value) - Set debugging level 0,1,2,3
        '--verbose'
           (-v) - Output verbose information about the behaviour of the agent
        '--dry-run'
           (-n) - All talk and no action mode - make no changes, only
            inform of promises not kept
        '--version'
           (-V) - Output the version of the software
        '--file'
           (-f value) - Specify an alternative input file than the default
        '--define-class'
           (-D value) - Define a list of comma separated classes to be
            sent to a remote agent
        '--select-class'
           (-s value) - Define a list of comma separated classes to be
            used to select remote agents by constraint
        '--inform'
           (-I) - Print basic information about changes made to the
            system, i.e. promises repaired
        '--remote-options'
           (-o value) - Pass options to a remote server process
        '--diagnostic'
           (-x) - Activate internal diagnostics (developers only)
        '--hail'
           -H value - Hail the following comma-separated lists of hosts,
             overriding default list
        '--interactive'
           (-i) - Enable interactive mode for key trust
        '--query'
           (-q value) - Query a server for a knowledge menu (commercial
             editions only)
        '--timeout'
           (-t value) - Connection timeout, seconds

Debug levels: 1=parsing, 2=running, 3=summary, 4=expression eval

