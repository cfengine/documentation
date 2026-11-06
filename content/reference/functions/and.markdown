---
layout: default
title: and
aliases:
  - "/reference-functions-and.html"
---

{{< CFEngine_function_prototype(...) >}}

**Description:** Returns `any` if all arguments evaluate to true and `!any` if
any argument evaluates to false.

**Arguments**: A list of classes, class expressions, or functions that return
classes.

`and()` evaluates its arguments left to right and will return as soon as one is
false. See [short-circuit evaluation][Functions#short-circuit evaluation].

**Example:**

```cf3 {skip TODO}
commands:
  "/usr/bin/generate_config $(config)"
    if => and( "generating_configs",
               not(fileexists("/etc/config/$(config)"))
             );
```

**Notes:** Introduced primarily for use with `if` and `unless` promise attributes.

**See also:** `or()`, `not()`, [short-circuit evaluation][Functions#short-circuit evaluation]

**History:**

- Introduced in 3.2.0, Nova 2.1.0 (2011)
- Return type changed from `string` to `boolean` in 3.17.0 (2020) (CFE-3470)
- Stops evaluating arguments at the first false one in 3.29.0 (CFE-4272).
  Previously all arguments, including function calls in them, were evaluated.
