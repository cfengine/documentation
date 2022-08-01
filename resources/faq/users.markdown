---
layout: default
title: Users
published: true
sorting: 90
tags: [getting started, installation, enterprise, faq]
---

# How do I ensure that a local user is locked?

To ensure that a local user exists but is locked (for example a service
account) simply specify `policy => "locked"`.

[%CFEngine_include_snippet(users_type.cf, ### Locked User BEGIN ###, ### Locked User END ###)%]
