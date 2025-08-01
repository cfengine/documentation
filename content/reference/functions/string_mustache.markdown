---
layout: default
title: string_mustache
---

[%CFEngine_function_prototype(template_string, optional_data_container)%]

**Description:** Formats a Mustache string template into a string, using either the system `datastate()` or an explicitly provided data container.

The usual Mustache facilities like conditional evaluation and loops are available, see the example below.

[%CFEngine_function_attributes(template_string, optional_data_container)%]

**Example:**

[%CFEngine_include_snippet(string_mustache.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(string_mustache.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**History:** Introduced in CFEngine 3.7

**See also:** `datastate()`, `readjson()`, `parsejson()`, `data`.
