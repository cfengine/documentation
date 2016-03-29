---
layout: default
title: cf-promises
published: true
sorting: 40
tags: [Components, cf-promises]
---

`cf-promises` is a  tool for checking CFEngine policy code. It operates by
first parsing policy code checking for syntax errors. Second, it validates the
integrity of policy consisting of multiple files. Third, it checks for
semantic errors, e.g. specific attribute set rules. Finally, `cf-promises`
attempts to expose errors by partially evaluating the policy, resolving as
many variable and classes promise statements as possible. At no point does
`cf-promises` make any changes to the system.

In 3.6.0 and later, `cf-promises` will not evaluate function calls
either.  This may affect customers who use `execresult` for instance.
Use the new `--eval-functions yes` command-line option (default is
`no`) to retain the old behavior from 3.5.x and earlier.

`cf-agent` calls `cf-promises` to validate the policy before running
it.  In that case `--eval-functions` is not specified, so functions
are not evaluated prematurely (as you would expect).

## Command reference ##

[%CFEngine_include_snippet(cf-promises.help, [\s]*--[a-z], ^$)%]
