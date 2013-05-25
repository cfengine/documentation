---
layout: default
title: The Work Directory
categories: [Manuals, Managing Environment, The Work Directory]
published: true
alias: manuals-managing-environments-work-directory.html
tags: [manuals, systems, configuration management, automation, directory, work directory]
---

In order to achieve the desired simplifications, it was decided to
reserve a private work area for the CFEngine tool-set.

_In CFEngine 1.x, the administrator could choose the locations of
configuration files, locks, and logging data independently. In
CFEngine 2.x, this diversity has been simplified to a single
directory which defaults to /var/cfengine (similar to /var/cron),
and in CFEngine 3.x this is preserved._

         /var/cfengine
         /var/cfengine/bin
         /var/cfengine/inputs
         /var/cfengine/outputs

A trusted cache of the input files must now be maintained in the
`inputs` subdirectory. When CFEngine is invoked by the scheduler, it
reads only from this directory. The default behavior of CFEngine will
copy policy from the default repository (`/var/cfengine/masterfiles`)
to the `inputs` subdirectory. For other architecural solutions (e.g.
pull from an external policy repository) it is up to the user to keep this
cache updated, on each host. This simplifies and consolidates the
CFEngine resources in a single place.

Unlike CFEngine 2, CFEngine 3 does not recognize the `CFINPUTS`
environment variable.

The outputs directory is now a record of spooled run-reports. These
are often mailed to the administrator by `cf-execd`, or can be
copied to another central location and viewed in an alternative
browser.

