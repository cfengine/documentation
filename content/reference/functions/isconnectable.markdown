---
layout: default
title: isconnectable
published: true
---

[%CFEngine_function_prototype(hostname, port, timeout)%]

**Description:** Checks whether a port is connectable

[%CFEngine_function_attributes(hostname, port, timeout)%]

This function checks whether a `hostname`:`port` is connectable within `timeout` in seconds, before it times out. If `timeout` is 0, the connection blocks forever. `timeout` defaults to 30 s.

**Example:**

[%CFEngine_include_example(isconnectable.cf)%]

**History:**

* Introduced in 3.26.0
