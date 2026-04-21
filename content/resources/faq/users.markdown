---
layout: default
title: Users
sorting: 90
---

Frequently asked questions about managing users from policy.

## How do I ensure that a local user is locked?

To ensure that a local user exists but is locked (for example a service
account) simply specify `policy => "locked"`.

[%CFEngine_include_snippet(users_type.cf, ### Locked User BEGIN ###, ### Locked User END ###)%]
