---
layout: default
title: read_module_protocol
published: true
tags: [reference, data functions, functions, "on"]
---

[%CFEngine_function_prototype(file_path)%]

**Description:** Interprets `file_path` as module protocol output.

This function is useful for reducing overhead by caching and then reading module protocol results from a file.

[%CFEngine_function_attributes(file_path)%]

**Example:**

[%CFEngine_include_example(read_module_protocol.cf)%]

**See also:** [usemodule()][usemodule], [Module Protocol][commands#module]

**History:**

- Introduced in 3.15.0


