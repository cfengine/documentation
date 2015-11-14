---
layout: default
title: string_mustache
published: true
tags: [reference, text functions, functions, text, mustache, string_mustache, json]
---

[%CFEngine_function_prototype(template_string, optional_data_container)%]

**Description:** Formats a Mustache string template into a string, using either the system `datastate()` or an explicitly provided data container.

The usual Mustache facilities like conditional evaluation and loops are available, see the example below.

[%CFEngine_function_attributes(template_string, optional_data_container)%]

**Example:**
{%raw%}
[%CFEngine_include_snippet(string_mustache.cf, #\+begin_src cfengine3, .*end_src)%]
{%endraw}

Output:

[%CFEngine_include_snippet(string_mustache.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**History:** Introduced in CFEngine 3.7

**See also:** `datastate()`, `readjson()`, `parsejson()`, `data`.
