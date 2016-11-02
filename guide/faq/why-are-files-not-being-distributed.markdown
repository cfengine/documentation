---
layout: default
title: Why are some files inside masterfiles not being updated/distributed?
published: true
sorting: 90
tags: [getting started, installation, faq ]
---

During agent bootstrap all files found in `masterfiles` are copied to
`$(sys.inputdir)` (commonly `/var/cfengine/inputs`). However not all files are
considered for update in the default
[update policy][Masterfiles Policy Framework#update-policy-update-cf]
([`sys.update_policy_path`][sys#sys.update_policy_path]).

Verify the files you expect match
[`update_def.input_name_patterns`][Masterfiles Policy Framework].
