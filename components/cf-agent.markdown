# `cf-agent`

Active agent - responsible for maintaining promises about the state
of your system (in CFEngine 2 the agent was called `cfagent`). You
can run `cf-agent` manually, but if you want to have it run on a
regular basis, you should use `cf-execd` (instead of
using `cron`).

`cf-agent` keeps the promises made in `common`
and `agent` bundles, and is affected by
`common` and `agent` control bodies.

## Command reference

        '--bootstrap'
           (-B) - Bootstrap/repair a CFEngine configuration from failsafe file in the current directory
        '--bundlsequence'
           (-b) - Set or override bundlesequence from command line
        '--debug'
           (-d value) - Set debugging level 0,1,2,3
        '--define'
           (-D value) - Define a list of comma separated classes to be defined at the start of execution
        '--diagnostic'
           (-x) - Activate internal diagnostics (developers only)
        '--dry-run'
           (-n) - All talk and no action mode - make no changes, only inform of promises not kept
        '--file'
           (-f value) - Specify an alternative input file than the default
        '--help'
           (-h) - Print the help message
        '--inform'
           (-I) - Print basic information about changes made to the system, i.e. promises repaired
        '--negate'
           (-N value) - Define a list of comma separated classes to be undefined at the start of execution
        '--no-lock'
           (-K) - Ignore locking constraints during execution (ifelapsed/expireafter) if "too soon" to run
        '--policy-server'
           (-B) - Define the server name or IP address of the a policy server (for use with bootstrap).
        '--verbose'
           (-v) - Output verbose information about the behaviour of the agent
        '--version'
           (-V) - Output the version of the software

Debug levels: 1=parsing, 2=running, 3=summary, 4=expression eval


