---
layout: default
title: hash
published: true
---

[%CFEngine_function_prototype(input, algorithm)%]

**Description:** Return the hash of `input` using the hash `algorithm`.

Hash functions are extremely sensitive to input. You should not expect
to get the same answer from this function as you would from every other
tool, since it depends on how whitespace and end of file characters are
handled.

[%CFEngine_function_attributes(input, algorithm)%]

**Example:**

[%CFEngine_include_snippet(hash.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(hash.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**See also:** `file_hash()`
