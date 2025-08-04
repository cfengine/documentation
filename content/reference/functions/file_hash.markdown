---
layout: default
title: file_hash
---

{{< CFEngine_function_prototype(file, algorithm) >}}

**Description:** Return the hash of `file` using the hash `algorithm`.

This function is much more efficient that calling `hash()` on a string
with the contents of `file`.

Hash functions are extremely sensitive to input. You should not expect
to get the same answer from this function as you would from every other
tool, since it depends on how whitespace and end of file characters are
handled.

{{< CFEngine_function_attributes(file, algorithm) >}}

**Example:**

Prepare:

{{< CFEngine_include_snippet(filestat.cf, #\+begin_src prep, .*end_src) >}}

Run:

{{< CFEngine_include_snippet(file_hash.cf, #\+begin_src cfengine3, .*end_src) >}}

Output:

{{< CFEngine_include_snippet(file_hash.cf, #\+begin_src\s+example_output\s*, .*end_src) >}}

**History:** Introduced in CFEngine 3.7.0

**See also:** `hash()`
