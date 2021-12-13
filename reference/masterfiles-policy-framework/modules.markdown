---
layout: default
title: modules/
published: true
tags: [reference, modules, MPF]
---
This directory tree is used for distributing Modules. The [packages subtree][modules/packages/] is used for vendoring packages modules and the [promises sub-directory][modules/promises/] is used for promise modules, including the libraries used by promise modules.

Distribute custom package modules by placing them in the packages directory. Modules placed in the root of the packages directory are copied into `$(sys.workdir)/modules/`.
