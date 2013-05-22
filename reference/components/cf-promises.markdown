# `cf-promises`	

Promise validator - used to verify that the promises used by the
other components of CFEngine are syntactically valid. `cf-promises`
does not execute any promises, but can syntax-check all of them. 
Configurations that make changes must be approved by this validator
before being executed.

    '--help'
       (-h) - Print the help message
    '--bundlesequence'
       (-b value) - Use the specified bundlesequence for verification
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
       (-D) value - Define a list of comma separated classes to be
        defined at the start of execution
    '--negate'
       (-N) value - Define a list of comma separated classes to be
        undefined at the start of execution
    '--inform'
       (-I) - Print basic information about changes made to the
        system, i.e. promises repaired
    '--diagnostic'
       (-x) - Activate internal diagnostics (developers only)
    '--analysis'
       (-a) - Perform additional analysis of configuration
    '--reports'
       (-r) - Generate reports about configuration
    '--parse-tree'
       (-p) - Print a parse tree for the policy file in JSON format
    '--gcc-brief-format'
       (-g) - Use the GCC brief-format for output

Debug levels: 1=parsing, 2=running, 3=summary, 4=expression eval

