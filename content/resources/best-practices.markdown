---
layout: default
title: Best practices
sorting: 100
aliases:
  - "/resources-best-practices.html"
---

## Policy style guide

When writing CFEngine policy using our [Policy style guide][Policy style guide] helps make your policy easily understood, debuggable and maintainable.

## Version control and configuration policy

CFEngine users version their policy. It's a reasonable, easy thing
to do: you just put `/var/cfengine/masterfiles` under version control
and... you're done?

What do you think? How do you version your own infrastructure?

### Problem statement

It turns out everyone likes convenience and writing the versioning
machinery is hard.
So we provide version control integration with Git out of the box, disabled
by default. This allows users to use branches for separate hubs
(which enables a policy release pipeline).

### Release pipeline

A build and release pipeline is how software is typically delivered to
production through testing stages. In the case of CFEngine, policy files
are the software. Users have at least two stages, development and
production, but typically the sequence has more stages including
various forms of testing/QA and pre-production.

### Policy changes

If you want to make manual changes to your policy, simply make those
changes in a checkout of your masterfiles repository, commit and push
the changes. The next time `update.cf` runs, your changes will be
checked out and in minutes distributed through your entire
infrastructure.

### Benefits

- easy to use compared to home-grown VCS integration
- supports Git out of the box and, with some work, can support others
  like Subversion, Mercurial, and CVS.
- tested, reliable, and built-in
- supports any repository and branch per hub
- your policy files are validated before deployment
- integration happens through shell scripts and `update.cf`, not C
  code or special policy files

### How to enable it

Follow detailed instructions in the [Policy deployment][Policy deployment] guide.

## Scalability

When running CFEngine Enterprise in a large-scale IT environment with many thousands of hosts, certain issues arise that require different approaches compared with smaller installations.

With CFEngine 3.6, significant testing was performed to identify the issues surrounding scalability and to determine best practices in large-scale installations of CFEngine.

### Moving PostgreSQL to separate hard drive

Moving the PostgreSQL database to another physical hard drive from the other CFEngine components can improve the stability of large-scale installations, particularly when using a solid-state drive (SSD) for hosting the PostgreSQL database.

The data access involves a huge number of random IO operations, with small chunks of data. SSD may give the best performance because it is designed for these types of scenarios.

_Important_: The PostgreSQL data files are in `/var/cfengine/state/pg/` by default. Before moving the mount point, please make sure that all CFEngine processes (including PostgreSQL) are stopped and the existing data files are copied to the new location.

### Setting the splaytime

The `splaytime` tells CFEngine hosts the base interval over which they will communicate with the `policy server`, which they then use to "splay" or hash their own runtimes.

Thus when `splaytime` is set to 4, 1000 hosts will hash their run attempts evenly over 4 minutes, and each minute will see about 250 hosts make a run attempt. In effect, the hosts will attempt to communicate with the policy server and run their own policies in predictable "waves." This limits the number of concurrent connections and overall system load at any given moment.
