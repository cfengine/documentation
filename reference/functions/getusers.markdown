---
layout: default
title: getusers
categories: [Reference, Functions, getusers]
published: true
alias: reference-functions-getusers.html
tags: [reference, system functions, functions, getusers]
---

[%CFEngine_function_prototype(exclude_names, exclude_ids)%]

**Description:** Returns a list of all users defined, except those names in `exclude_names` and uids in `exclude_ids`

[%CFEngine_function_attributes(exclude_names, exclude_ids)%]

**Example:**

[%CFEngine_include_snippet(getusers.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(getusers.cf, #\+begin_src\s+example_output\s*[ ,.0-9]+, .*end_src)%]

**Notes:**
This function is currently only available on Unix-like systems.

**History:** Was introduced in version 3.1.0b1,Nova 2.0.0b1 (2010).

