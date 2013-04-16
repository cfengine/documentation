# `cf-hub`

A data aggregator used as part of the commercial product.
This stub is not used in the community edition of CFEngine.

`cf-hub` keeps the promises made in `common`, and is affected by
`common` control bodies.

# Command reference

        '--cache'
           (-a) - Rebuild database caches used for efficient query handling (e.g. compliance graphs)
        '--continuous'
           (-c) - Continuous update mode of operation
        '--debug'
           (-d value) - Set debugging level 0,1,2,3
        '--no-fork'
           (-F) - Run as a foreground processes (do not fork)
        '--file'
           (-f value) - Specify an alternative input file than the default
        '--help'
           (-h) - Print the help message
        '--index'
           (-i) - Reindex all collections in the CFEngine report database
        '--no-lock'
           (-K) - Ignore locking constraints during execution (ifelapsed/expireafter) if "too soon" to run
        '--logging'
           (-l) - Enable logging of report collection and maintenance to hub_log in the working directory
        '--maintain'
           (-m) - Start database maintenance process. By default, entries older than 7 days (1 year for longterm reports) are purged.
        '--dry-run'
           (-n) - All talk and no action mode - make no changes, only inform of promises not kept
        '--splay_updates'
           (-s) - Splay/load balance full-updates, overriding bootstrap times, assuming a default 5 minute update schedule.
        '--version'
           (-V) - Output the version of the software
        '--verbose'
           (-v) - Output verbose information about the behaviour of the agent

