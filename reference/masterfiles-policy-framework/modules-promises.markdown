---
layout: default
title: modules/promises/
published: true
tags: [reference, promise modules, MPF]
---
This directory tree is used for distributing promise modules and supporting libraries.

Files in this directory have an executable copy in `$(sys.workdir)/modules/packages/` and take precedence over modules in the vendored directory.

Package modules in the vendored sub-directory are rendered into `$(sys.workdir)/modules/packages` if no customized copy is found.
