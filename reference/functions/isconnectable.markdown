---
layout: default
title: isconnectable
published: true
---

[%CFEngine_function_prototype(hostname, port, time_limit)%]

**Description:** Checks whether a port is connectable

[%CFEngine_function_attributes(hostname, port, time_limit)%]

This function checks whether a `hostname`:`port` is connectable within a time limit `time_limit`, before it times out. If `time_limit` is 0, the connection blocks forever.

**Example:**

[%CFEngine_include_snippet(isconnectable.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(isconnectable.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**History:**

* Introduced in 3.26.0
