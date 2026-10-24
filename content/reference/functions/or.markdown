---
layout: default
title: or
aliases:
  - "/reference-functions-or.html"
---

{{< CFEngine_function_prototype(...) >}}

**Description:** Returns `any` if any argument evaluates to true and `!any` if
all arguments evaluate to false.

**Arguments**: A list of classes, class expressions, or functions that return
classes.

`or()` evaluates its arguments left to right and will return as soon as one is
true. See [short-circuit evaluation][Functions#short-circuit evaluation].

**Example:**

```cf3 {skip TODO}
commands:
  "/usr/bin/generate_config $(config)"
    if => or( "force_configs",
              not(fileexists("/etc/config/$(config)"))
            );
```

**Notes:** Introduced primarily for use with `if` and `unless` promise attributes.

**See also:** `and()`, `not()`, [short-circuit evaluation][Functions#short-circuit evaluation]

**History:**

- Introduced in 3.2.0, Nova 2.1.0 (2011)
- Return type changed from `string` to `boolean` in 3.17.0 (2020) (CFE-3470)
- Stops evaluating arguments at the first true one in 3.29.0 (CFE-4272).
  Previously all arguments, including function calls in them, were evaluated.
