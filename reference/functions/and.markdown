---
layout: default
title: and
published: true
tags: [reference, data functions, functions, and]
---

[%CFEngine_function_prototype(...)%]

**Description:** Returns `any` if all arguments evaluate to true and `!any` if
any argument evaluates to false.

**Arguments**: A list of classes, class expressions, or functions that return
classes.

**Example:**

```cf3
    commands:
      "/usr/bin/generate_config $(config)"
        if => and( "generating_configs",
                   not(fileexists("/etc/config/$(config)"))
                 );
```

**Notes:** Introduced primarily for use with `if` and `unless` promise attributes.

**See also:** `and`, `or`, `not`

**History:** Was introduced in 3.2.0, Nova 2.1.0 (2011)
