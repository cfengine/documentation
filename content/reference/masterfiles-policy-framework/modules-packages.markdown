---
layout: default
title: modules/packages/
aliases:
  - "/reference-masterfiles-policy-framework-modules-packages.html"
---

This directory tree is used for distributing package modules.

Files in this directory have an executable copy in `$(sys.workdir)/modules/packages/` and take precedence over modules in the vendored directory.

Package modules in the vendored sub-directory are rendered into `$(sys.workdir)/modules/packages` if no customized copy is found.
