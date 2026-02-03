---
layout: default
title: concat
aliases:
  - "/reference-functions-concat.html"
---

{{< CFEngine_function_prototype(...) >}}

**Description:** Concatenates all arguments into a string.

**Example:**

```cf3 {skip TODO}
commands:
  "/usr/bin/generate_config $(config)"
    if => concat("have_config_", canonify("$(config)"));
```

**History:** Was introduced in 3.2.0, Nova 2.1.0 (2011)
