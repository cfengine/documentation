---
layout: default
title: Normal ordering
published: true
sorting: 40
---

CFEngine takes a pragmatic point of view to ordering. When promising `scalar`
attributes and properties, ordering is irrelevant and should not be considered.
More complex patterned data structures require ordering to be preserved, e.g.
editing in files. CFEngine solves this in a two-part strategy:

CFEngine maintains a default order of promise-types. This is based on a simple
logic of what needs to come first, e.g. it makes no sense to create something
and then delete it, but it could make sense to delete and then create (an
equilibrium). This is called normal ordering and is described below.  You can
override normal ordering in exceptional circumstances by making a promise in a
class context and defining that class based on the outcome of another promise,
or using the `depends_on` promise attribute.

## Agent normal ordering

CFEngine tries to keep variable and class promises before starting to consider
any other kind of promise. In this way, global variables and classes can be set.

If you set variables based on classes that are determined by other variables,
then you introduce an order dependence to the resolution that might be
non-unique. **Since CFEngine starts trying to converge values as soon as
possible, it is best to define variables in bundles before using them**, i.e.
as early as possible in your configuration. In order to make sure all global
variables and classes are available early enough policy pre-evaluation step was
introduced.

### Policy evaluation overview

CFEngine policy evaluation is done in several steps:

1. Classes provided as a command line argument (-D option) are read and set.
1. Environment detection and hard classes discovery is done.
1. Persistent classes are loaded.
1. Policy sanity check using cf-promises -c (full-check) is performed.
1. Pre-evaluation step is taking place.
1. Exact policy evaluation is done.


For more information regarding each step please see the detailed description
below.

### Policy evaluation details

Before exact evaluation of promises takes place first command line parameters
are read and all classes defined using `-D` parameter are set. Next,
environment detection takes place and hard classes are discovered.  When
environment detection is complete all the persistent classes are loaded and a
policy sanity check is performed using cf-promises.

#### cf-promises policy validation step

In this step policy is validated and `classes` and `vars` promises are
evaluated.  Note that cached functions are executed here, and then again during
the normal agent execution. Variables and classes resolved in this step do not
persist into the following evaluation step, so all functions will run again
during Agent pre-evaluation.

#### Agent pre-evaluation step

In order to support expansion of variables in body common control inputs and
make sure all needed classes and variables are determined before they are
needed in normal evaluation, pre-evaluation takes place immediately before
policy evaluation.

During pre-evaluation files are loaded based on ordering in body common control
(first) and body file control (after body common control). This means that
files included in body common control are loaded and parsed before files
placed in body file control. This is important from a common bundles
evaluation perspective as bundles placed in files included in body common
control inputs will be evaluated before bundles from file control inputs.

The following steps are executed per-bundle for each file parsed, in this order:

1. if it's a common bundle, evaluate **vars** promises
2. if it's a common bundle, evaluate **classes** promises
3. evaluate **vars** promises
(for details see `PolicyResolve()` in the C code)

This is done because classes placed in common bundles
are global whereas classes placed in agent bundles are local (by default) to
the bundle where those are defined. This means that common bundles
classes need these extra steps in order to be resolved for the next steps.

After all policy files are parsed and pre-evaluated, the above pre-evaluation
sequence runs once again in
order to help resolve dependencies between classes and vars placed in
different files.

#### Agent evaluation step

After pre-evaluation is complete normal evaluation begins.

In this step CFEngine executes agent promise bundles in the strict order
defined by the bundlesequence (possibly overridden by the `-b` or
`--bundlesequence` command line option). If the bundlesequence is not provided
via command line argument or is not present in body common control agent will
attempt to execute a bundle named `main`. If bundle `main` is not defined, the
agent will error and exit.

Within a bundle, the promise types are executed in a round-robin fashion
according to so-called `normal ordering` (essentially deletion first, followed
by creation). The actual sequence continues for up to three iterations of the
following, converging towards a final state:

1. [meta][meta]
2. [vars][vars]
3. [defaults][defaults]
4. [classes][classes]
5. [users][users]
6. [files][files]
7. [packages][packages]
8. [guest_environments][guest_environments]
9. [methods][methods]
10. [processes][processes]
11. [services][services]
12. [commands][commands]
13. [storage][storage]
14. [databases][databases]
15. [reports][reports]
16. [Custom promise types, in written order][custom]

Within [`edit_line` bundles in files promises][edit_line],
the normal ordering is:

1. [meta][meta]
2. [vars][vars]
3. [defaults][defaults]
4. [classes][classes]
5. [delete_lines][delete_lines]
6. [field_edits][field_edits]
7. [insert_lines][insert_lines]
8. [replace_patterns][replace_patterns]
9. [reports][reports]

The order of promises within one of the above types follows their top-down
ordering within the bundle itself. In vars this can be used to override the
value of a variable, if you have two vars promises with the same name, the
last one will override the first one. The order may be overridden by making a
promise depend on a class that is set by another promise, or by using the
`depends_on` attribute in the promise.

**Note:** The evaluation order of common bundles are `classes`, then
`variables` and finally `reports`. All common bundles are evaluated regardless
if they are placed in `bundlesequence` or not. Placing common bundles in
`bundlesequence` will cause classes and variables to be evaluated again, and is
generally good practice to make sure evaluation works properly.

## Server normal ordering

As with the agent, common bundles are executed before any server bundles;
following this all server bundles are executed (the `bundlesequence` is only
used for cf-agent). Within a server bundle, the promise types are unambiguous.
Variables and classes are resolved in the same way as the agent. On
connection, access control must be handled first, then a role request might be
made once access has been granted. Thus ordering is fully constrained by
process with no additional freedoms.

Within a server bundle, the normal ordering is:

1. [vars][vars]
2. [classes][classes]
3. [roles][roles]
4. [access][access]

## Monitor normal ordering

As with the agent, common bundles are executed before any monitor bundles;
following this all monitor bundles are executed (the `bundlesequence` is only
used for cf-agent). Variables and classes are resolved in the same way as the
agent.

Within a monitor bundle, the normal ordering is:

1. [vars][vars]
2. [classes][classes]
3. [measurements][measurements]
4. [reports][reports]

<!---
### Knowledge normal ordering

As with the agent, common bundles are executed before any knowledge bundles; following this all knowledge bundles are executed (the bundlesequence is only used for cf-agent). Variables and classes are resolved in the same way as the agent.

Within a knowledge bundle, the normal ordering is:

    vars
    classes
    topics
    occurrences
    inferences
    reports
-->
