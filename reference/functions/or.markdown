---
layout: default
title: or
published: true
tags: [reference, data functions, functions, or]
---

[%CFEngine_function_prototype(...)%]

**Description:** Returns `any` if any argument evaluates to true and `!any` if
any argument evaluates to false.

**Arguments**: A list of classes, class expressions, or functions that return
classes.

**Example:**

```cf3
    commands:
      "/usr/bin/generate_config $(config)"
        ifvarclass => or( "force_configs",
                          not(fileexists("/etc/config/$(config)"))
                        );
```

**Notes:** Introduced primarily for use with `ifvarclass`, `if`, and `unless`
promise attributes.

**See Also:** `and`, `or`, `not`

**History:** Was introduced in 3.2.0, Nova 2.1.0 (2011)
