---
layout: default
title: Normal Ordering
categories: [Manuals, Language Concepts, Normal Ordering]
published: true
sorting: 60
alias: manuals-language-concepts-normal-ordering.html
tags: [manuals, language, syntax, concepts, ordering, depends_on]
---

CFEngine takes a pragmatic point of view to ordering. When promising `scalar` 
attributes and properties, ordering is irrelevant and needs not be considered. 
More complex patterned data structures require ordering to be preserved, e.g. 
editing in files. CFEngine solves this in a two-part strategy:

CFEngine maintains a default order of promise-types. This is based on a simple 
logic of what needs to come first, e.g. it makes no sense to create something 
and then delete it, but it could make sense to delete and then create (an 
equilibrium). This is called normal ordering and is described below.
You can override normal ordering in exceptional circumstances by making a 
promise in a class context and defining that class based on the outcome of 
another promise.

### Agent normal ordering

CFEngine tries to keep variable and class promises before starting to consider 
any other kind of promise. In this way, global variable and classes can be set.

If you set variables based on classes that are determined by other variables, 
then you introduce an order dependence to the resolution that might be 
non-unique. Since CFEngine starts trying to converge values as soon as 
possible, it is best to define variables in bundles before using them, i.e. as 
early as possible in your configuration. In general it is wise to avoid 
class-variable dependency as much as possible.

CFEngine executes agent promise bundles in the strict order defined by the 
`bundlesequence` (possibly overridden by the `-b` or `--bundlesequence` 
command line option).

Within a bundle, the promise types are executed in a round-robin fashion 
according to so-called `normal ordering` (essentially deletion first, followed 
by creation). The actual sequence continues for up to three iterations of the 
following, converging towards a final state:

    meta
    vars
    defaults
    classes
    users
    files
    packages
    guest_environments
    methods
    processes
    services
    commands
    storage
    databases
    reports

Within [`edit_line` bundles in files promises][bundle edit_line],
the normal ordering is:

    meta
    vars
    defaults
    classes
    delete_lines
    field_edits
    insert_lines
    replace_patterns
    reports

The order of promises within one of the above types follows their top-down 
ordering within the bundle itself. The order may be overridden by making a 
promise depend on a class that is set by another promise, or by using the
`depends_on` attribute in the promise.

### Server normal ordering

As with the agent, common bundles are executed before any server bundles; 
following this all server bundles are executed (the `bundlesequence` is only 
used for cf-agent). Within a server bundle, the promise types are unambiguous. 
Variables and classes are resolved in the same way as the agent. On 
connection, access control must be handled first, then a role request might be 
made once access has been granted. Thus ordering is fully constrained by 
process with no additional freedoms.

Within a server bundle, the normal ordering is:

    vars
    classes
    access
    roles

### Monitor normal ordering

As with the agent, common bundles are executed before any monitor bundles; 
following this all monitor bundles are executed (the `bundlesequence` is only 
used for cf-agent). Variables and classes are resolved in the same way as the 
agent.

Within a monitor bundle, the normal ordering is:

    vars
    classes
    measurements
    reports

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

