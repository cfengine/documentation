---
layout: default
title: cf-support
published: true
sorting: 10
keywords: [cf-support]
---

`cf-support` gathers various details about the system and creates a tarball in the current directory to submit to support.
If the system is an enterprise hub then additional details will be gathered and included.
The utility will prompt for an optional support ticket number as well as prompt whether to include masterfiles in the tarball.

## Command reference

[%CFEngine_include_snippet(cf-support.help, [\s]*--[a-z], ^$)%]

## History

* Introduced in 3.21.0, 3.18.3
