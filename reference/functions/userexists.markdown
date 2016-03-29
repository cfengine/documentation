---
layout: default
title: userexists
published: true
tags: [reference, system functions, functions, userexists]
---

[%CFEngine_function_prototype(user)%]

**Description:** Return whether `user` name or numerical id exists on this
host.

Checks whether the user is in the password database for the current host. The
argument must be a user name or user id.

[%CFEngine_function_attributes(user)%]

**Example:**

[%CFEngine_include_snippet(userexists.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(userexists.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

