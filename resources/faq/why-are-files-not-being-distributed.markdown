---
layout: default
title: Why are some files inside masterfiles not being updated/distributed?
published: true
sorting: 90
tags: [getting started, installation, faq ]
---

During agent bootstrap all files found in `masterfiles` are copied to
`$(sys.inputdir)` (commonly `/var/cfengine/inputs`).

However not all files are
considered for update in the default update policy.

The default update policy in the MPF only copies files matching a list of
regular expressions defined in [update_def.input_name_patterns][Masterfiles Policy Framework#files considered for copy during policy updates]
