---
layout: default
title: getusers
published: true
tags: [reference, system functions, functions, getusers]
---

[%CFEngine_function_prototype(exclude_names, exclude_ids)%]

**Description:** Returns a list of all users defined, except those names in `exclude_names` and uids in `exclude_ids`

[%CFEngine_function_attributes(exclude_names, exclude_ids)%]

**Example:**

[%CFEngine_include_snippet(getusers.cf, #\+begin_src cfengine3, .*end_src)%]

**Output:**

[%CFEngine_include_snippet(getusers.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**Notes:**

* This function is currently only available on Unix-like systems.
* This function will return both local and remote (for example, users defined in an external directory like LDAP) users on a system.

**History:**

* Introduced in CFEngine 3.1.0b1, CFEngine Nova/Enterprise 2.0.0b1 (2010).

**See also:** [`getuserinfo()`][getuserinfo], [`users`][users].
