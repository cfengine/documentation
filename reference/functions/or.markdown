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
        if => or( "force_configs",
                  not(fileexists("/etc/config/$(config)"))
                );
```

**Notes:** Introduced primarily for use with `if` and `unless` promise attributes.

**See also:** `and()`, `not()`

**History:**

* Introduced in 3.2.0, Nova 2.1.0 (2011)
* Return type changed from `string` to `boolean` in 3.17.0 (2020) (CFE-3470)
